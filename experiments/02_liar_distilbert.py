# experiments/02_liar_distilbert.py
"""
Day 7 — Detection arm, transformer.
LIAR (binary collapse) + DistilBERT fine-tune, same split as Day 6.

Why this experiment exists:
- Second row of the Experiments table. Same paradigm as Day 6 (detection,
  text-only, binary labels), different model family.
- Tests whether the detection plateau Day 6 hit near the majority class is a
  TF-IDF limitation or a deeper signature of surface-pattern learning.
  Thesis-relevant: if a strong pretrained encoder also plateaus, the
  bottleneck is the paradigm, not the features.
- Reuses the Day 6 loader code byte-for-byte so the within-paradigm
  comparison is on identical splits.

Runs in Google Colab on a free T4 GPU.

Setup cell (run once in Colab before this script):
    !pip -q install "transformers>=4.40,<5" "datasets>=2.18,<5" \
                    "accelerate>=0.30" "scikit-learn>=1.3"
"""

import io
import json
import zipfile
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    get_linear_schedule_with_warmup,
)
from torch.optim import AdamW
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    classification_report,
    confusion_matrix,
)
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

# Primary + fallback URLs for LIAR. UCSB's server has been intermittently
# flaky; HF mirror is a backup that ships the same zip contents.
LIAR_URLS = [
    "https://www.cs.ucsb.edu/~william/data/liar_dataset.zip",
    # If the line above 403s in Colab, uncomment and use the HF mirror:
    # "https://huggingface.co/datasets/chengxuphd/liar2/resolve/main/liar_dataset.zip",
]
LIAR_LOCAL_ZIP = DATA_DIR / "liar_dataset.zip"

RANDOM_STATE = 42
MODEL_NAME = "distilbert-base-uncased"
MAX_LEN = 128            # set after distribution check, see Methodology note
BATCH_SIZE = 16
LR = 2e-5
EPOCHS = 3
WARMUP_RATIO = 0.1

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# --- Same as 01_liar_svm.py: do not diverge --------------------------------
LIAR_COLUMNS = [
    "id", "label", "statement", "subject", "speaker", "job_title",
    "state_info", "party_affiliation",
    "barely_true_counts", "false_counts", "half_true_counts",
    "mostly_true_counts", "pants_on_fire_counts",
    "context",
]
LABEL_TO_BINARY = {
    "pants-fire": 0, "false": 0, "barely-true": 0,
    "half-true": 1, "mostly-true": 1, "true": 1,
}
BINARY_NAMES = ["False", "True"]


# ---------------------------------------------------------------------------
# Data loading (mirror of 01_liar_svm.py — keep identical)
# ---------------------------------------------------------------------------
def download_liar_if_needed():
    if LIAR_LOCAL_ZIP.exists():
        return
    last_err = None
    for url in LIAR_URLS:
        try:
            print(f"Downloading LIAR from {url} ...")
            urllib.request.urlretrieve(url, LIAR_LOCAL_ZIP)
            print(f"Saved to {LIAR_LOCAL_ZIP}")
            return
        except Exception as e:
            print(f"  failed: {e}")
            last_err = e
    raise RuntimeError(f"All LIAR mirrors failed; last error: {last_err}")


def load_split(zip_handle, filename):
    with zip_handle.open(filename) as f:
        df = pd.read_csv(
            f, sep="\t", header=None, names=LIAR_COLUMNS,
            quoting=3, on_bad_lines="skip",
        )
    df = df[df["label"].isin(LABEL_TO_BINARY)].copy()
    texts = df["statement"].astype(str).tolist()
    labels = df["label"].map(LABEL_TO_BINARY).to_numpy(dtype=int)
    return texts, labels


def load_liar_binary():
    download_liar_if_needed()
    with zipfile.ZipFile(LIAR_LOCAL_ZIP) as z:
        train = load_split(z, "train.tsv")
        dev = load_split(z, "valid.tsv")
        test = load_split(z, "test.tsv")
    return train, dev, test


# ---------------------------------------------------------------------------
# Length distribution check (Methodology note: justify MAX_LEN choice)
# ---------------------------------------------------------------------------
def report_token_length_distribution(texts, tokenizer):
    lengths = [len(tokenizer.encode(t, add_special_tokens=True)) for t in texts]
    lengths = np.array(lengths)
    pcts = {p: int(np.percentile(lengths, p)) for p in [50, 90, 95, 99, 100]}
    print("Token length percentiles (train):")
    for p, v in pcts.items():
        print(f"  p{p:>3}: {v}")
    return pcts


# ---------------------------------------------------------------------------
# Torch dataset
# ---------------------------------------------------------------------------
class LiarDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_len):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        enc = self.tokenizer(
            self.texts[idx],
            truncation=True,
            padding="max_length",
            max_length=self.max_len,
            return_tensors="pt",
        )
        return {
            "input_ids": enc["input_ids"].squeeze(0),
            "attention_mask": enc["attention_mask"].squeeze(0),
            "labels": torch.tensor(self.labels[idx], dtype=torch.long),
        }


# ---------------------------------------------------------------------------
# Train / eval loops
# ---------------------------------------------------------------------------
def run_epoch_train(model, loader, optimizer, scheduler):
    model.train()
    total_loss, n = 0.0, 0
    for batch in loader:
        batch = {k: v.to(DEVICE) for k, v in batch.items()}
        optimizer.zero_grad()
        out = model(**batch)
        out.loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()
        scheduler.step()
        total_loss += out.loss.item() * batch["labels"].size(0)
        n += batch["labels"].size(0)
    return total_loss / n


@torch.no_grad()
def predict(model, loader):
    model.eval()
    all_pred, all_true = [], []
    for batch in loader:
        batch = {k: v.to(DEVICE) for k, v in batch.items()}
        out = model(input_ids=batch["input_ids"],
                    attention_mask=batch["attention_mask"])
        pred = out.logits.argmax(dim=-1).cpu().numpy()
        all_pred.append(pred)
        all_true.append(batch["labels"].cpu().numpy())
    return np.concatenate(all_pred), np.concatenate(all_true)


def evaluate(name, y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    macro_f1 = f1_score(y_true, y_pred, average="macro", zero_division=0)
    print(f"\n=== {name} ===")
    print(f"accuracy  : {acc:.4f}")
    print(f"macro-F1  : {macro_f1:.4f}")
    print(classification_report(y_true, y_pred, target_names=BINARY_NAMES,
                                digits=4, zero_division=0))
    return {"accuracy": acc, "macro_f1": macro_f1}


def save_confusion_matrix(y_true, y_pred, title, filename):
    cm = confusion_matrix(y_true, y_pred)
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.imshow(cm, cmap="Blues")
    ax.set_xticks([0, 1], BINARY_NAMES)
    ax.set_yticks([0, 1], BINARY_NAMES)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("True")
    ax.set_title(title)
    for i in range(2):
        for j in range(2):
            ax.text(j, i, cm[i, j], ha="center", va="center",
                    color="white" if cm[i, j] > cm.max() / 2 else "black")
    fig.tight_layout()
    fig.savefig(RESULTS_DIR / filename, dpi=120)
    plt.close(fig)
    return cm.tolist()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    # Reproducibility
    torch.manual_seed(RANDOM_STATE)
    np.random.seed(RANDOM_STATE)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(RANDOM_STATE)

    print(f"Device: {DEVICE}")
    if DEVICE == "cuda":
        print(f"GPU: {torch.cuda.get_device_name(0)}")

    print("Loading LIAR...")
    (X_train, y_train), (X_dev, y_dev), (X_test, y_test) = load_liar_binary()
    print(f"sizes: train={len(X_train)}, dev={len(X_dev)}, test={len(X_test)}")
    print(f"train class balance: True={y_train.mean():.3f}  "
          f"False={1 - y_train.mean():.3f}")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    # Length distribution (for Methodology — justify MAX_LEN)
    length_pcts = report_token_length_distribution(X_train, tokenizer)
    if length_pcts[99] > MAX_LEN:
        print(f"WARNING: p99 length {length_pcts[99]} > MAX_LEN {MAX_LEN}; "
              f"consider raising MAX_LEN.")

    # Datasets / loaders
    train_ds = LiarDataset(X_train, y_train, tokenizer, MAX_LEN)
    dev_ds   = LiarDataset(X_dev,   y_dev,   tokenizer, MAX_LEN)
    test_ds  = LiarDataset(X_test,  y_test,  tokenizer, MAX_LEN)

    train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True)
    dev_loader   = DataLoader(dev_ds,   batch_size=BATCH_SIZE * 2)
    test_loader  = DataLoader(test_ds,  batch_size=BATCH_SIZE * 2)

    # Model
    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_NAME, num_labels=2,
    ).to(DEVICE)

    # Optimizer + scheduler
    total_steps = len(train_loader) * EPOCHS
    warmup_steps = int(WARMUP_RATIO * total_steps)
    optimizer = AdamW(model.parameters(), lr=LR, weight_decay=0.01)
    scheduler = get_linear_schedule_with_warmup(
        optimizer, num_warmup_steps=warmup_steps,
        num_training_steps=total_steps,
    )

    # --- Train, track best dev macro-F1 ---
    best_dev_f1 = -1.0
    best_epoch = -1
    best_state = None
    per_epoch = []

    for epoch in range(1, EPOCHS + 1):
        train_loss = run_epoch_train(model, train_loader, optimizer, scheduler)
        pred_dev, true_dev = predict(model, dev_loader)
        dev_metrics = evaluate(f"epoch {epoch} — dev", true_dev, pred_dev)
        per_epoch.append({"epoch": epoch, "train_loss": train_loss,
                          **{f"dev_{k}": v for k, v in dev_metrics.items()}})

        if dev_metrics["macro_f1"] > best_dev_f1:
            best_dev_f1 = dev_metrics["macro_f1"]
            best_epoch = epoch
            best_state = {k: v.detach().cpu().clone()
                          for k, v in model.state_dict().items()}
            print(f"  -> new best dev macro-F1: {best_dev_f1:.4f} (epoch {epoch})")

    # --- Restore best, evaluate test ---
    print(f"\nRestoring best checkpoint from epoch {best_epoch} "
          f"(dev macro-F1 {best_dev_f1:.4f})")
    model.load_state_dict(best_state)
    pred_test, true_test = predict(model, test_loader)

    results = {
        "config": {
            "model": MODEL_NAME, "max_len": MAX_LEN, "batch_size": BATCH_SIZE,
            "lr": LR, "epochs": EPOCHS, "warmup_ratio": WARMUP_RATIO,
            "random_state": RANDOM_STATE,
        },
        "train_length_percentiles": length_pcts,
        "per_epoch_dev": per_epoch,
        "best_epoch": best_epoch,
        "distilbert_dev": evaluate("DistilBERT (best) — dev",
                                   true_dev, pred_dev),
        "distilbert_test": evaluate("DistilBERT (best) — test",
                                    true_test, pred_test),
    }
    results["distilbert_confusion_test"] = save_confusion_matrix(
        true_test, pred_test,
        title="DistilBERT (LIAR-binary, test)",
        filename="02_liar_distilbert_confusion_test.png",
    )

    # --- Save metrics ---
    with open(RESULTS_DIR / "02_liar_distilbert_metrics.json", "w") as f:
        json.dump(results, f, indent=2)

    # --- Misclassified: shuffle then take 20 (more representative than
    # taking the first 20 in test-file order, which is what Day 6 did)
    rng = np.random.default_rng(RANDOM_STATE)
    mis_idx = np.where(true_test != pred_test)[0]
    rng.shuffle(mis_idx)
    mis_idx = mis_idx[:20]

    with open(RESULTS_DIR / "02_liar_distilbert_misclassified.tsv", "w",
              encoding="utf-8") as f:
        f.write("statement\ttrue\tpredicted\n")
        for i in mis_idx:
            stmt = X_test[i].replace("\t", " ").replace("\n", " ")
            f.write(f"{stmt}\t{BINARY_NAMES[true_test[i]]}\t"
                    f"{BINARY_NAMES[pred_test[i]]}\n")

    print("\nSaved:")
    print("  results/02_liar_distilbert_metrics.json")
    print("  results/02_liar_distilbert_confusion_test.png")
    print("  results/02_liar_distilbert_misclassified.tsv")


if __name__ == "__main__":
    main()