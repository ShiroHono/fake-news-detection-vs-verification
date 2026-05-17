# experiments/01_liar_svm.py
"""
Day 6 — Detection arm, classical baseline.
LIAR (binary collapse) + TF-IDF + LinearSVC, vs majority-class floor.

Why this experiment exists:
- Gives the first row of the Experiments table.
- Anchors the "detection learns surface patterns" half of the thesis.
- Provides a floor (majority class) so the SVM number is interpretable.

Data note:
- HuggingFace `datasets` >=4.0 removed support for loader scripts, so the
  `liar` and `ucsbnlp/liar` dataset repos no longer load. We bypass that by
  downloading the original UCSB zip directly and parsing the TSVs.
"""

import io
import json
import zipfile
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.dummy import DummyClassifier
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
LIAR_ZIP_URL = "https://www.cs.ucsb.edu/~william/data/liar_dataset.zip"
LIAR_LOCAL_ZIP = DATA_DIR / "liar_dataset.zip"

RANDOM_STATE = 42

# LIAR columns (no header row in the TSVs):
LIAR_COLUMNS = [
    "id", "label", "statement", "subject", "speaker", "job_title",
    "state_info", "party_affiliation",
    "barely_true_counts", "false_counts", "half_true_counts",
    "mostly_true_counts", "pants_on_fire_counts",
    "context",
]

# Binary collapse: False (0) = {pants-fire, false, barely-true}
#                  True  (1) = {half-true, mostly-true, true}
LABEL_TO_BINARY = {
    "pants-fire": 0, "false": 0, "barely-true": 0,
    "half-true": 1, "mostly-true": 1, "true": 1,
}
BINARY_NAMES = ["False", "True"]


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------
def download_liar_if_needed():
    """Fetch the UCSB zip on first run; reuse cached copy after that."""
    if LIAR_LOCAL_ZIP.exists():
        return
    print(f"Downloading LIAR from {LIAR_ZIP_URL} ...")
    urllib.request.urlretrieve(LIAR_ZIP_URL, LIAR_LOCAL_ZIP)
    print(f"Saved to {LIAR_LOCAL_ZIP}")


def load_split(zip_handle, filename):
    """Read one TSV split out of the zip and return (texts, binary_labels)."""
    with zip_handle.open(filename) as f:
        df = pd.read_csv(
            f, sep="\t", header=None, names=LIAR_COLUMNS,
            quoting=3,           # csv.QUOTE_NONE — LIAR has stray quotes
            on_bad_lines="skip",
        )
    df = df[df["label"].isin(LABEL_TO_BINARY)].copy()  # drop any malformed rows
    texts = df["statement"].astype(str).tolist()
    labels = df["label"].map(LABEL_TO_BINARY).to_numpy(dtype=int)
    return texts, labels


def load_liar_binary():
    """Return (train, dev, test) as tuples of (texts, labels)."""
    download_liar_if_needed()
    with zipfile.ZipFile(LIAR_LOCAL_ZIP) as z:
        train = load_split(z, "train.tsv")
        dev = load_split(z, "valid.tsv")
        test = load_split(z, "test.tsv")
    return train, dev, test


# ---------------------------------------------------------------------------
# Evaluation helpers
# ---------------------------------------------------------------------------
def evaluate(name, y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    macro_f1 = f1_score(y_true, y_pred, average="macro", zero_division=0)   # <- changed
    print(f"\n=== {name} ===")
    print(f"accuracy  : {acc:.4f}")
    print(f"macro-F1  : {macro_f1:.4f}")
    print(classification_report(y_true, y_pred, target_names=BINARY_NAMES,
                                digits=4, zero_division=0))                  # <- changed
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
    print("Loading LIAR...")
    (X_train, y_train), (X_dev, y_dev), (X_test, y_test) = load_liar_binary()
    print(f"sizes: train={len(X_train)}, dev={len(X_dev)}, test={len(X_test)}")
    print(f"train class balance: True={y_train.mean():.3f}  "
          f"False={1 - y_train.mean():.3f}")

    results = {}

    # --- Majority-class floor ---
    dummy = DummyClassifier(strategy="most_frequent")
    dummy.fit(X_train, y_train)
    results["majority_dev"] = evaluate("Majority class — dev",
                                       y_dev, dummy.predict(X_dev))
    results["majority_test"] = evaluate("Majority class — test",
                                        y_test, dummy.predict(X_test))

    # --- TF-IDF + LinearSVC ---
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        min_df=2,
        max_df=0.95,
        sublinear_tf=True,
    )
    Xtr = vectorizer.fit_transform(X_train)
    Xdv = vectorizer.transform(X_dev)
    Xte = vectorizer.transform(X_test)
    print(f"\nTF-IDF feature count: {Xtr.shape[1]}")

    svm = LinearSVC(C=1.0, random_state=RANDOM_STATE)
    svm.fit(Xtr, y_train)

    pred_dev = svm.predict(Xdv)
    pred_test = svm.predict(Xte)

    results["svm_dev"] = evaluate("TF-IDF + LinearSVC — dev", y_dev, pred_dev)
    results["svm_test"] = evaluate("TF-IDF + LinearSVC — test", y_test, pred_test)

    # --- Confusion matrix on test ---
    results["svm_confusion_test"] = save_confusion_matrix(
        y_test, pred_test,
        title="TF-IDF + LinearSVC (LIAR-binary, test)",
        filename="01_liar_svm_confusion_test.png",
    )

    # --- Save metrics JSON ---
    with open(RESULTS_DIR / "01_liar_svm_metrics.json", "w") as f:
        json.dump(results, f, indent=2)

    # --- Save up to 20 misclassified test examples for later error analysis ---
    misclassified = []
    for stmt, true, pred in zip(X_test, y_test, pred_test):
        if true != pred:
            misclassified.append((stmt, BINARY_NAMES[true], BINARY_NAMES[pred]))
        if len(misclassified) >= 20:
            break
    with open(RESULTS_DIR / "01_liar_svm_misclassified.tsv", "w",
              encoding="utf-8") as f:
        f.write("statement\ttrue\tpredicted\n")
        for stmt, t, p in misclassified:
            stmt_clean = stmt.replace("\t", " ").replace("\n", " ")
            f.write(f"{stmt_clean}\t{t}\t{p}\n")

    print("\nSaved:")
    print("  results/01_liar_svm_metrics.json")
    print("  results/01_liar_svm_confusion_test.png")
    print("  results/01_liar_svm_misclassified.tsv")


if __name__ == "__main__":
    main()