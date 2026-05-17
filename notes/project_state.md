# Project State — Fake News Detection vs Verification

**Source of truth for what's locked, what's open, and what the lit review pre-flagged for later sections.**

---

## Phase

**Lit review and Related Work drafting: complete.** All 25 papers read; Related Work drafted as 10 stitched paragraphs in `paper_draft.md` (minor stitching deferred to final polish).

**Current phase: experiments / coding.** Methodology decisions are locked (subject to revision if code phase reveals problems — see "if things go south" notes per decision). No experiments run yet.

---

## Thesis (anchor for every section)

Detection learns surface patterns of "fakeness."
Verification checks claims against evidence.
Every experiment should illuminate that contrast.

---

## Locked methodology decisions

Each one is justified by lit-review evidence. Flag in Methodology, restate in Limitations where the lit review pre-flagged the trade-off.

**Binary labels for detection.** Collapse LIAR's 6-way to binary, following Rashkin [#9]'s precedent. Trades graded sensitivity for cross-paradigm comparability with FEVER's binary-friendly verification labels. _If things go south:_ ISOT or WELFake as drop-in replacement (also binary, also Colab-clean).

**Text-only detection features.** No metadata, no source credibility, no engagement signals. Keeps the comparison cleanly text-vs-text. Reis [#12] and Wang [#13] both show non-textual features carry signal — note in Limitations as a known way to do better that's out of scope.

**Two detection arms.** TF-IDF + Linear SVM (classical baseline, Ahmed [#10] precedent). Fine-tuned transformer — DistilBERT or BERT-base — on the same LIAR-binary split (Devlin [#11] foundation, Reis [#12] comparison framing). Two arms = two data-points within the same paradigm, which the lit review already justifies. _If things go south on transformer fine-tuning:_ drop to feature-extraction-only (frozen BERT + linear head) before dropping the arm entirely.

**Oracle (gold) evidence for verification arm.** Four independent results converge: retrieval, not entailment, eats most of the headroom.

- Hanselowski [#16]: 93.55 × 87.10 × 68.49 → 64.74 (ESIM, FEVER)
- Nie [#19]: dNSMN 92.34 + sNSMN 91.19 + vNSMN 66.14 (NSMN, FEVER)
- Thorne [#21]'s own baseline: DA oracle 80.82 vs full-pipeline 52.09; manual error analysis 58.27% retrieval failures vs 13.84% RTE failures given correct evidence
- Wadden [#23]: 46.5 open / 72.7 oracle-abstract / 83.3 oracle-rationale F1 (RoBERTa-large, SciFact) — different corpus, different model family, same gap shape

To study verification _reasoning_, treat retrieval as solved. Hanselowski as primary citation in P8 S3; Thorne / Nie / Wadden as corroboration. MultiFC [#22] + SciFact [#23] are the external-validity citations in Limitations.

**Claim-selection idealization (companion to above).** From Hassan [#20]: FEVER's pre-written claims also abstract away the upstream claim-selection stage. Flag both idealizations (retrieval + claim-selection) together in Limitations — this is what "external validity" means for this setup.

**Off-the-shelf MNLI checkpoint for verification.** No FEVER fine-tuning. Tests how far generic NLI capability transfers, not how well a model can be tuned to one benchmark. NLI→FEVER label mapping is approximate (entailment≈Supported, contradiction≈Refuted, neutral≈NEI) — flag in Methodology. Concrete framing: Wadden [#23]'s label predictor gains ~6 points from FEVER pretraining (81.9 vs 75.7 dev acc), and FEVER→SciFact zero-shot reaches 51.8 oracle F1 vs SciFact-fine-tuned 72.7 — both show "small in-domain fine-tuning beats generic pretraining"; our no-fine-tune setup is the weaker version consciously accepted for cleanliness of comparison. **Framing must read as pragmatic scope, not principled rigour — otherwise P10 S4 closing ("makes no claim to escape") becomes inconsistent.**

**LIWC concat for classical baseline — DEFERRED.** Only add if classical-vs-transformer gap is too wide to discuss meaningfully. Don't add proactively.

---

## Dataset plan (FEVER-first, SciFact fallback)

**Detection:** LIAR (binary collapse). Backup: ISOT or WELFake.

**Verification (primary):** FEVER with gold evidence. Off-the-shelf MNLI checkpoint.

**Verification (fallback):** SciFact. 1,409 claims, 5,183 abstracts. Loads cleanly, same 3-way structure (SUPPORTS/REFUTES/NOINFO ≈ Supported/Refuted/NEI). Already cited in Related Work P9; the pivot is one paragraph of Methodology, not a paper-level rewrite.

**Why FEVER may fight us:** the canonical loader expects a 5M-page Wikipedia dump. With oracle evidence we don't need it (gold evidence sentences are in the claim file), but HuggingFace `fever` dataset versions have been unstable. Acceptable proxies: `pietrolesci/fever`, FEVER-symmetric subsets, or pre-extracted oracle-evidence pairs from a paper repo. If none load in a session, pivot to SciFact rather than burn a week fighting loaders.

---

## Carry-forward caveats — pre-scripts the Limitations / Discussion / Error Analysis sections

Every bullet here is a sentence (or paragraph) waiting to be written into one of the later sections. Tagged with target section.

**[Limitations + Methodology] FEVER class imbalance in training set.** Train set is S 80,035 / R 29,775 / NEI 35,639 (~55/20/25). Dev/test are balanced 1:1:1. Doesn't matter for off-the-shelf MNLI (we're not fine-tuning). If we ever drop NEI for binary cross-paradigm comparison, note we're using FEVER's balanced dev split, S+R subset, ~6,666 claims. Honest framing.

**[Limitations] FEVER's NEI training is synthetic.** Thorne [#21]'s NEARESTP vs RANDOMS comparison shows synthetic-negative choice matters — RANDOMS inflates oracle accuracy (88.00% DA) but harms pipeline NEI recall; NEARESTP yields realistic but lower numbers (80.82% DA). Off-the-shelf MNLI inherits whichever NEI semantics its training assumed (MNLI "neutral" = "premise underdetermines hypothesis"), yet another reason the NLI→FEVER label mapping is approximate. Compounds with NEI confusion (below).

**[Limitations] LIAR credit-history leakage.** Vector includes current statement's label. Text-only so doesn't bite us — flag as known dataset quirk.

**[Limitations] Potthast publisher-holdout vs LIAR vanilla splits.** Our setup doesn't isolate speaker style. Flag: "Unlike Potthast et al.'s publisher-holdout design, our LIAR splits do not isolate speaker style; reported detection accuracy may include speaker-recognition signal." Don't switch — would break comparability with Wang [#13].

**[Error Analysis — expected failure mode #1] NEI handling.** Hanselowski [#16]'s error analysis: models confuse "evidence doesn't support" with "evidence refutes." Nie [#19]: NEI F1 drops 3 points without retrieval-confidence features (model leans on retrieval weakness as NEI proxy). MNLI's "neutral" was trained on "premise underdetermines hypothesis," not FEVER's NEI definition. **Expect this as the primary failure mode of the verification arm.**

**[Error Analysis — expected failure mode #2] Numerical reasoning.** GloVe/FastText don't distinguish numbers; pretrained MNLI inherits the bias via similar embeddings. Nie [#19]'s 5-d number embedding was a partial fix (0.77 FEVER gain). Modern wordpiece transformers help but don't solve. Hassan [#20] corroboration: top discriminative feature is CD (cardinal number); 45% of check-worthy sentences contain numbers vs 6% of non-factual. Wadden [#23] corroboration: SciFact lists numerical reasoning (hazard ratios, confidence intervals, p-values) as one of five capabilities biomedical verification demands — same failure type, new corpus, RoBERTa-large doesn't fix it. **Discussion framing: "the same property that makes claims worth checking — numerical specificity — makes them hard to verify off the shelf."**

**[Error Analysis — expected failure mode #3] Directionality.** Hanselowski [#16] flags SUPPORT↔REFUTE confusion on direction-flipped claims ("increases" vs "decreases"). Wadden [#23] confirms directionality as a distinct failure capability on biomedical claims ("protects against severe anemia" → "raises vulnerability"). Two independent corpora, same flip-failure mode.

**[Error Analysis — expected failure mode #4] Coreference and cause-and-effect.** From Wadden [#23]: "the intervention group" → "the low-fat diet group" (coreference); gene knockouts as evidence for gene function (cause-and-effect). General reasoning failures, not biomedicine-specific — expect even when running on FEVER.

**[Limitations] Joint-training trade-off.** Nie [#19]'s verifier benefits from upstream retrieval-confidence scores (removing the 2-d relatedness feature drops FEVER 1.24, NEI F1 ~3). Decoupled off-the-shelf pipeline gives this up. Limitation, not a change of design.

**[P10 setup — already cited] NLI hypothesis-only artifacts.** SNLI and MNLI both have known post-hoc hypothesis-only artifacts (Gururangan 2018 — contextual, not cited in our paper). Mirrors FEVER claim-only artifacts [#24]. P10 already handles this.

**[Limitations] MultiFC reproducibility caveat.** Augenstein [#22]'s evidence is whatever Google Search returned in 2019 — results drift, dataset is not re-fetchable. Doesn't affect us (we cite, don't run) but flag: "real-world verification has a moving-target evidence problem that benchmark verification does not."

**[Discussion] MultiFC topic-prior shortcut.** Augenstein [#22]'s error analysis: specific topic tags ("hong-kong", "brisbane-4000") co-occur with correct predictions; generic tags co-occur with errors. The model learns topic-veracity priors when evidence is ambiguous — real-world analogue of FEVER's claim-only artifacts [#24]. Useful Discussion line: "even with evidence, models lean on topic priors when evidence is ambiguous."

**[Discussion + Limitations] Any FEVER accuracy is an upper bound.** Schuster [#24]'s symmetric-test-set result quantifies it: NSMN drops 81.8% → 58.7% (−23.1 pts) from FEVER dev to a test where claim-only shortcuts are neutralised. Same drop almost certainly affects our off-the-shelf MNLI+FEVER pipeline, but we can't easily measure it (no symmetric version of our setup exists). Useful Discussion framing: "Schuster et al. [#24] show that ~23 points of FEVER-dev accuracy on this class of architecture is recoverable from the claim alone; we expect our verifier inherits some fraction of this bias."

**[Discussion] Artifact problem generalises beyond FEVER.** Three independent lines: NLI hypothesis-only artifacts in SNLI/MNLI; MultiFC topic-prior shortcut [#22]; FEVER claim-only n-gram artifacts [#24]. **Artifact phenomenon is a property of how text-classification benchmarks get built when one side of the input is human-authored under task constraints**, not a property of any specific dataset.

**[Methodology + Error Analysis] Label-vs-evidence dissociation.** Thorne 2019 [#25]'s Paraphrase attack: 43.06% label accuracy but 0.00% FEVER score across all systems — systems pick the right verdict without picking the right evidence. **If the verification arm reports anything, it should report both label accuracy and joint label-and-evidence score whenever the dataset supports it.** Discussion framing: "a verifier can be correct for the wrong reason."

**[Limitations] Adversarial-fragility universality.** Across seven leading FEVER systems spanning BERT-NLI, pointer-network+RL, and OpenIE-triple semantic similarity, no system exceeded 37.31% resilience [#25] against ~500 hand-constructed adversarial pairs vs standard FEVER scores of 57.4–68.5%. The ~30-point gap is shared across architectural families. Any verification system trained on FEVER inherits this fragility envelope, including off-the-shelf pipelines.

**[Error Analysis + Limitations] Compositional reasoning as fragility frontier.** Multi-hop, temporal arithmetic, transitive numerical reasoning are where FEVER 2.0 systems collapse (Multi-Hop Temporal 8.33% FEVER, SubsetNum 0.00%). Aligns with the numerical-reasoning failure mode tracked across [#9, #16, #19, #20, #23] and adds **multi-hop / compositional reasoning** as a related but distinct failure axis. Limitations line: "our verification arm is not designed for multi-hop claims; FEVER itself documents ~16.82% of its claims as multi-hop, and FEVER 2.0 shows even targeted systems collapse on this subset."

**[Future Scope] CUNLP fixer's modest gain bounds the cost of targeted defence.** [#25]'s only fixer submission added document-pointer-network multi-hop retrieval + OpenIE-arithmetic temporal-reasoning rules and recovered +1.72 FEVER score, +3.69 resilience — small, attack-specific. **A serious robustness story is not a one-component fix; it is a per-failure-mode architecture.** Frame Future Scope: targeted defence helps incrementally; fundamental robustness improvement is open.

**[Discussion] SciFact's claim-only baseline as positive-example contrast [#23 vs #24].** SciFact's claim-only baseline reaches only 44.5% (vs 33% chance) on 3-way — barely above floor. Compare to Schuster [#24]'s measured 61.7% claim-only BERT on FEVER. **Careful claim construction (citance-derived + hand-negation without "not" cues) resists the artifact problem.** Artifacts are not inevitable.

**[Limitations] Field-acknowledgement framing.** Guo [#5] (flagship survey) explicitly cites Schuster 2020 [#14] and Schuster 2019 [#24] as acknowledged limitations of both paradigms. Frame our argument as "operationalising critiques the field's standard survey already accepts" — stronger than presenting as our own observations.

---

## Pending paper-side polish (do near final draft)

- P9 stitching pass.
- P10 stitching pass — see `paper_draft.md` deferred-polish section.
- Optional P6↔P8 Potthast/Hassan callback.
- Whole-Related-Work read-through, length-balance trim, `[#N]` → final citation style.
- Citation style (APA / IEEE / ACL) — flag to professor.
