# Literature Review — 25 Papers

**Project:** Fake News Detection vs Verification: A Comparative NLP Study
**Function:** Citation source-of-truth. Only cite papers from this file. If one feels missing, flag it; never invent.

---

## Theme 1 — Foundations and Problem Definition

_Sets up the two paradigms in the introduction._

### 1. Shu et al. 2017 — Fake News Detection on Social Media: A Data Mining Perspective

- **Venue:** SIGKDD Explorations Newsletter
- **Status:** ✅ Read
- **Definition:** Fake news = "intentionally and verifiably false" — authenticity + intent. Excludes satire, rumour, conspiracy theories, hoaxes-for-fun.
- **Taxonomy (cite this):** Two feature families — News Content (Linguistic + Visual) and Social Context (User + Post + Network). Models split into News Content Models (Knowledge-based, Style-based) and Social Context Models (Stance-based, Propagation-based).
- **Why it matters for our paper:** Their **Knowledge-based** branch ≈ the verification paradigm; their **Style-based** branch ≈ what we critique in Paragraph 6. Shu already acknowledges both exist — we sharpen the comparison they sketched.
- **Datasets listed:** BuzzFeedNews, LIAR, BS Detector, CREDBANK. Notes that no single dataset has all features.
- **What they don't do:** No empirical head-to-head between paradigms — that's our gap.
- **Honest weakness:** Pre-BERT survey; files verification under detection rather than as a parallel paradigm.

---

### 2. Vlachos & Riedel 2014 — Fact Checking: Task Definition and Dataset Construction

- **Venue:** ACL Workshop on Language Technologies and Computational Social Science
- **Status:** ✅ Read
- **Big move:** First formal definition of computational fact-checking as an NLP task. Turns "fact-checking" from journalism into a research problem with defined input, output, evaluation.
- **Task definition (cite this):** "Assignment of a truth value to a claim made in a particular context." Argues against pure binary classification; proposes 5-point ordinal scale (TRUE / MOSTLYTRUE / HALFTRUE / MOSTLYFALSE / FALSE) because real claims are often partly true. Context (time, speaker) is essential.
- **Four-stage pipeline they propose** (conceptual ancestor of FEVER):
  1. Extract statements to be fact-checked
  2. Construct appropriate questions
  3. Obtain answers from relevant sources
  4. Reach a verdict
     → Stages 1, 3, 4 map directly to claim detection (Hassan #20), evidence retrieval (Nie #19), entailment (Hanselowski #16).
- **Dataset:** 106 statements from PolitiFact + Channel 4 FactCheck. Too small to train on; seminal as task formulation.
- **Why it matters for our paper:** Origin citation for the verification paradigm. Pairs with Shu (#1) in the opening — Shu defines detection's scope, V&R define verification's scope. Guo et al. (#5) is the modern refinement; cite together for lineage.
- **Honest weakness:** Pipeline never implemented; proposed kNN-on-prior-claims baseline can't handle novel claims; Wikipedia-as-truth fails for claims requiring calculations.

---

### 3. Conroy, Rubin & Chen 2015 — Automatic Deception Detection: Methods for Finding Fake News

- **Venue:** ASIST
- **Status:** ✅ Read
- **Taxonomy (cite this):** Two method families:
  1. **Linguistic approaches** — analyze message content for "predictive deception cues."
  2. **Network approaches** — use external network info (knowledge graphs, social-network behavior, metadata).
     → Early precursor to our detection-vs-verification framing: linguistic ≈ style-based detection; the "linked data / knowledge networks" branch of network approaches ≈ verification.
- **Key inside knowledge-network branch:** Fact-checking reduced to shortest-path computation on a knowledge graph (DBpedia, GREC). Cites Ciampaglia 2015. Reports 61-95% accuracy across subject areas. **This is the verification paradigm in early form.**
- **Their argument:** No single method is sufficient — advocate hybrid linguistic + network/behavioral.
- **Why it matters for our paper:** Historical precedent for the two-paradigm split (cite in introduction). Their "limited generalizability towards real-time veracity detection of news" line is useful for our error analysis.
- **Honest weakness:** Very short (4 pp.), no original experiments. Conflates knowledge-graph fact-checking with social-network behavior under "network" — our paper sharpens that.

---

### 4. Zhou & Zafarani 2020 — A Survey of Fake News

- **Venue:** ACM Computing Surveys
- **Status:** ✅ Read
- **Taxonomy (cite this):** Four-perspective framework mapped to news life cycle (creation → publication → propagation):
  1. **Knowledge-based** — verify claims against facts. **= verification paradigm.**
  2. **Style-based** — analyze writing style, emotion, complexity. **= detection paradigm.**
  3. **Propagation-based** — analyze how news spreads.
  4. **Source-based** — assess credibility of authors/publishers/users.
     → For our paper, perspectives 1 and 2 are central; 3 and 4 are social-context detection we mention but don't experiment on.
- **Style-based details (feeds Paragraphs 3-4):** Four language levels — lexicon (BOW, TF-IDF, n-grams), syntax (PCFG parse trees), discourse (RST), semantic (10 dimensions). Table 6: TF-IDF + classical ML hits 80-87% on PolitiFact/BuzzFeed. Non-latent features outperform word2vec/doc2vec.
- **Section 3.4 — limit of detection (cite for Paragraph 6):** "style-based fake news detection sometimes can be a cat-and-mouse game; any success at detection, in turn, will inspire future countermeasures by fake news writers." Pre-figures our thesis hinge.
- **Why it matters for our paper:** Best single citation for the detection paradigm's 2020 landscape, paired with Shu (#1) for 2017. Their 4-perspective framework is cleaner than Shu's because it carves out knowledge-based (verification) as its own perspective.
- **Honest weakness:** Survey only. Table 6 numbers come from one source (Zhou 2019a), not a fair cross-field benchmark. Acknowledges but doesn't resolve the cat-and-mouse problem we centre.

---

### 5. Guo, Schlichtkrull & Vlachos 2022 — A Survey on Automated Fact-Checking

- **Venue:** TACL
- **Status:** ⏳ In progress
- **Framework (cite this):** Three-stage NLP framework for automated fact-checking:
  1. **Claim detection** — check-worthiness (subjective) vs. checkability (objective).
  2. **Evidence retrieval** — supporting/refuting sources.
  3. **Claim verification** — verdict prediction + justification production.
     → Modern refinement of Vlachos & Riedel (#2). Cite together for lineage.
- **Verification = NLI (cite for Paragraph 7):** They explicitly frame claim verification as Recognizing Textual Entailment, citing Dagan 2010 and Bowman 2015 (our #17). Direct justification for our NLI pipeline.
- **Cross-refs that strengthen our argument (load-bearing for Paragraphs 6 + 10):** Guo et al. cite Schuster 2020 (#14) for "claim-only models fail on machine-generated text" and Schuster 2019 (#24) for FEVER claim-only artifacts. **This means our thesis-hinge critiques are field-acknowledged limitations in the flagship 2022 survey, not contrarian claims.** Frame our argument as "operationalizing critiques the field's standard survey already accepts."
- **Other challenges they call out (for Limitations + Future Scope):** dataset artifacts; single-source-of-truth assumption (Wikipedia); multilinguality/multimodality; faithfulness of generated justifications; debunking vs. prebunking.
- **Why it matters for our paper:** Best single citation for the verification paradigm landscape, parallel to Zhou & Zafarani (#4) for detection. Paragraph 1 now has both anchor surveys.
- **Honest weakness:** Survey only; no head-to-head detection-vs-verification benchmark (our gap). Feb 2022 — predates LLM-generated misinformation; multimodal/LLM sections are dated.

---

## Theme 2 — Bridging the Two Paradigms

_Prior work that has connected the two paradigms; sets up the gap._

### 6. Karadzhov et al. 2017 — Fully Automated Fact Checking Using External Sources

- **Venue:** RANLP
- **Status:** ✅ Read
- **Big move:** First end-to-end fact-checking system using the **open Web** as evidence source (not Wikipedia, not a curated KG). Operationalizes the detection→verification bridge: takes a claim (detection's input) through evidence retrieval + matching (verification's machinery) in a single system.
- **3-stage pipeline (maps onto Guo et al. #5):**
  1. Retrieval: tf-idf-weighted 5-10-token query (nouns/verbs/adjectives + NER) → Google + Bing → snippets + full pages → manually-curated unreliable-domain filter.
  2. Representation: three similarities (cosine-tf-idf, GloVe-cosine, containment) between claim and (a) snippets and (b) best-matching rolling triplet from each page. Plus LSTM encodings of claim, best snippet, best triplet learned end-to-end.
  3. Prediction: NN, RBF-SVM, or SVM+NN hybrid.
- **Datasets:** (1) Snopes rumor set — 761 claims (Ma et al. 2016), split 509/132/120. (2) **New cQA factuality** — 249 Q-A pairs from SemEval-2016 Task 3 Qatar Living, 128 positive / 121 negative, split 185/31/32.
- **Results:** Snopes — SVM+NN = 80.0% acc / 77.2 macro-F1 (majority 66.7%, 39.9% relative error reduction, matches Popat 2017 with much less data). cQA — SVM+NN = 72.7% acc. Snippets ≈ full pages once NN embeddings added; Google ≈ Bing.
- **Why it matters for our paper:** Theme 2 anchor for Paragraph 2 Sentence 1. Justifies our similarity-based verification arm (cosine-tf-idf + embedding cosine + containment between claim and retrieved evidence) — published precedent rather than invention. Useful for external-validity caveat (Wikipedia-grounded FEVER is controlled; real world looks more like Snopes-on-open-web).
- **Honest weakness:** Small datasets; relies on **defunct IBM AlchemyAPI** for NER and on live Google/Bing rankings (non-reproducible today — for our methodology, use spaCy/HuggingFace NER + static evidence corpus); unreliable-domain blocklist is unablated hidden supervision; no explanations of which snippet swung the verdict.

---

### 7. Bondielli & Marcelloni 2019 — A Survey on Fake News and Rumour Detection Techniques

- **Venue:** Information Sciences
- **Status:** ✅ Read
- **Big move:** First survey to treat fake news detection AND rumour detection as two faces of the same problem ("false information on the web") rather than separate literatures.
- **Their taxonomy:** Content-based (lexical, syntactic, semantic) vs. context-based (user-based, network-based) features. Methods catalog: SVM, DT, RF, LR, CRF, HMM, RNN/LSTM, CNN, plus "other approaches" (Hawkes process, crowdsourcing, anomaly detection, **computational fact-checking**).
- **KEY POINT for our framing:** Computational fact-checking is NOT given its own top-level category — it appears at the end of Section 5.2 as one item in "Other Approaches" alongside Hawkes process and anomaly detection. They acknowledge it as "definitely akin" but treat it as a minor sub-branch, not a parallel paradigm. **The asymmetry our paper inverts is visible exactly here.**
- **Supporting citation for Paragraph 6 (thesis hinge):** Section 4.1 explicitly notes "fake news are becoming more and more similar to proper news for what concerns the writing style" and that content-based features have "limited generalization capability in a real word application system." Pair with Schuster 2020 (#14): B&M for "field has noticed in passing"; Schuster 2020 for "field has measured it." Also flags concept drift for streaming social media (Section 6).
- **Methodological honesty they admit:** "since there do not exist benchmark datasets, it is practically impossible to compare the different approaches" — aligns with our methodological choice to use multiple datasets / aligned-subset evaluation.
- **Why it matters for our paper:** Theme 2 anchor #2 (with Karadzhov #6). Paragraph 2 Sentence 2: best citation for "prior surveys treat detection and verification asymmetrically." One-line callout option for Para 2 or Intro: "even surveys that treat fake news and rumour detection as a unified field still treat verification as a side technique."
- **Honest weakness:** Pure survey; every accuracy number borrowed. Conflates fake news and rumour methodology despite distinguishing them definitionally. Pre-BERT in spirit (BERT was out, but not integrated). Future-directions section never calls out the detection-vs-verification split as a research direction — which is exactly what our paper argues for.

---

## Theme 3 — Detection via Linguistic & Stylistic Features

_Justifies the classical ML baseline (TF-IDF + Logistic Regression / SVM)._

### 8. Pérez-Rosas et al. 2018 — Automatic Detection of Fake News

- **Venue:** COLING
- **Status:** ✅ Read
- **Big move:** First fake-news detection paper to build two **purpose-built, domain-controlled datasets** specifically for studying deception — avoiding the satire/politics confounds of prior datasets.
- **Two datasets they release:**
  1. **FakeNewsAMT** — 240 real + 240 crowdsourced-fake across 6 domains (sports, business, entertainment, politics, technology, education). Real from mainstream US outlets; fake from AMT workers writing fake versions in journalistic style.
  2. **Celebrity** — 250 real + 250 fake celebrity news, scraped from web (entertainment magazines, tabloids), veracity from GossipCop. Naturally occurring, not crowdsourced.
- **Features:** n-grams (uni+bi tf-idf), punctuation (12 LIWC types), psycholinguistic (LIWC), readability (Flesch-Kincaid, Gunning Fog, ARI), syntax (CFG production rules with parent+grandparent context). Linear SVM, 5-fold CV, **default parameters / no tuning**.
- **Within-domain results:** FakeNewsAMT best = Readability 0.78 acc; all features 0.74. Celebrity best = LIWC 0.74; all features 0.76 (best overall). Human baseline = 0.70-0.71 / 0.77-0.80 (Kappa 0.38-0.45 — moderate). System beats humans on FakeNewsAMT, loses on Celebrity.
- **THE KEY RESULT (empirical pre-evidence for Paragraph 6 thesis hinge):** Cross-domain transfer **COLLAPSES**. Train FakeNewsAMT → test Celebrity = **0.48-0.52 acc (random)**. Reverse = 0.60-0.65. Within FakeNewsAMT leave-one-domain-out: Politics/Tech generalize at 0.90-0.91 (Readability), Sports/Business at 0.51-0.53 (random). **Linguistic features are domain-fragile.**
- **Authors' own recommendation (gift for Paragraph 6 and Intro):** Section 8 explicitly states linguistic features alone are insufficient and recommends integrating "computational approaches to fact verification (Thorne et al., 2018)" — i.e., FEVER (our #21). The authors themselves point at verification.
- **Why it matters for our paper:** Theme 3 anchor for Paragraph 3 S1. Justifies our classical TF-IDF + LR/SVM baseline (~74-78% within-domain). Cross-domain table = empirical demonstration of style-doesn't-transfer; pair with Rashkin (#9) for cross-source corroboration.
- **Confound to flag for our experimental design:** FakeNewsAMT fake = AMT-generated. Authors observed "verbal mirroring" — workers unconsciously matched journalistic style. Classifier may pick up "AMT-worker style vs journalist style." If we use LIAR (#13) or ISOT (real political fake vs real political real), we sidestep this — note in Methodology / Limitations.
- **Honest weakness:** Tiny datasets (480, 500); pre-BERT; default hyperparams; human baseline = 2 annotators with moderate Kappa; cross-domain claim from 40-example folds.

---

### 9. Rashkin et al. 2017 — Truth of Varying Shades

- **Venue:** EMNLP
- **Status:** ✅ Read
- **Big move:** First paper to do quantitative linguistic analysis of fake news across BOTH a graded-truthfulness setting (6-point PolitiFact) AND coarse news-type (trusted/satire/hoax/propaganda). Argues truthfulness is a spectrum — only 20% of PolitiFact claims rated True, 7% Pants-on-Fire; 73% sit in between.
- **Two datasets:** (1) **News-type corpus** — trusted (Gigaword 13,995) + satire (Onion/Borowitz/Clickhole ~15k) + hoax (American News/DC Gazette ~12k) + propaganda (Natural News/Activist Report ~33k). Train/test split uses **different sources within each category** (cross-source generalization). (2) **PolitiFact** — 10,483 statements; analyze 4,366 direct quotes, split 2575/712/1074, speakers confined to single set (no speaker leakage).
- **Lexical features:** LIWC, subjective words (Wilson 2005), hedging (Hyland 2015), and **5 new intensifying lexicons** crawled from Wiktionary (comparatives, superlatives, action/manner/modal adverbs).
- **Specific markers for our error analysis (Table 2, statistically significant, Bonferroni-corrected):**
  - **More in fake:** swear words (7.0×), 2nd-person "you" (6.73×, propaganda), modal adverbs (2.63×), action adverbs (2.18×), 1st-person "I" (2.06×), manner adverbs (1.87×), strong subjectives (1.51×), hedging (1.19×), superlatives (1.17×).
  - **More in trusted:** numbers (2.3×), money words (1.75×), assertive verbs (1.19×), comparatives (1.16×).
  - Interpretation: fake exaggerates; trusted gives concrete figures and is less vague.
- **Results — cross-source generalization (more evidence for Paragraph 6):** 4-way news-type F1 = 0.91 in-domain dev → **0.65 out-of-domain test** (different sources, same category). PolitiFact best 2-class macro-F1 = 0.56 (NB+LIWC, vs 0.39 baseline); **6-class = 0.22 (MaxEnt+LIWC) vs 0.06 baseline** — graded truthfulness from text alone is HARD.
- **Methodological observations:** (a) LIWC substantially helps classical models (NB 0.16 → 0.21 on 6-class); (b) LIWC does NOT help LSTM (and slightly hurts) — neural model already learns lexical info from raw text. Implication: if we use a transformer, LIWC concat is unnecessary; for classical baseline it's a published, beginner-friendly extension.
- **Methodology decision needed (graded vs binary):** Rashkin argues truthfulness is genuinely a spectrum. Our project assumes binary for clean comparison. Justify in Methodology: "collapse LIAR's 6-way using top-3/bottom-3 split as Rashkin et al., trading graded sensitivity for cross-paradigm comparability." Flag in Limitations.
- **Why it matters for our paper:** Paragraph 3 S2 anchor (specific markers); empirical reinforcement of Pérez-Rosas's cross-domain finding (two independent collapses); thesis-hinge support for Paragraph 6.
- **Honest weakness:** PolitiFact US-centric; 4-way labels conflate intent (deceive) with content (true/false) — tangled label; "out-of-domain" is cross-source within same category (weaker than Pérez-Rosas's cross-domain); pre-BERT.

---

### 10. Ahmed, Traore & Saad 2018 — Detecting Opinion Spams and Fake News Using Text Classification

- **Venue:** Security and Privacy
- **Status:** ✅ Read
- **Big move:** Direct head-to-head benchmark of six classical classifiers × two feature schemes × four n-gram orders × four feature dimensionalities on three datasets. Releases the **ISOT Fake News Dataset** (12,600 fake + 12,600 real 2016 political articles).
- **Three datasets:** (1) Ott 2011 hotel reviews (800+800); (2) Horne & Adali news; (3) **ISOT** — fake from Kaggle PolitiFact-flagged unreliable sites, real from Reuters.com, all 2016, >200 chars. Main experiment uses 2,000-article subset focused on 2016 US elections.
- **Pipeline:** Porter stem + stop-word removal + sklearn CountVectorizer/TfidfVectorizer + top-p feature selection (1k/5k/10k/50k) + 5-fold CV (80/20 split). No DL.
- **Results:** Ott reviews — **Linear SVM + TF-IDF + bigram + 10k = 90% acc** (beats Ott's own 89%). ISOT subset — **Linear SVM + TF-IDF + unigram + 50k = 92% acc**. Horne & Adali — Linear SVM + unigram = 87% (vs their 71%). Worst: KNN + 4-gram + 50k = 45-47% (below chance).
- **Empirical patterns (concrete recipe for our classical baseline):**
  - **Linear classifiers (LSVM, SGD, LR) consistently beat non-linear** (KNN, DT, RBF-SVM) on sparse TF-IDF.
  - **TF-IDF beats raw TF** consistently.
  - **Unigrams/bigrams win**; trigrams/4-grams degrade (sparse).
  - **10k-50k features** > 1k; diminishing returns past 10k.
    → Our recipe: TF-IDF + unigrams (or +bigrams) + Linear SVM or LR + 10k-50k features + 5-fold CV. No need to sweep — Ahmed already did it.
- **Implicit cautionary tale (for Paragraph 6):** Original broader-time-window experiment hit 98% acc; restricting to 2016 political articles only dropped it to 92%. They restricted on temporal confound but didn't control for the publisher-style confound (Reuters vs Kaggle blogs). Same artifact phenomenon as Pérez-Rosas cross-domain collapse and Schuster 2020 — surface classifiers are fragile to underlying-confound shifts.
- **Why it matters for our paper:** Paragraph 3 S3 anchor — cleanest published "classical ML head-to-head" justifying TF-IDF + Linear SVM/LR as a hard-to-beat baseline (90-92%). **ISOT is our drop-in backup** if LIAR fights us in Colab; available on Kaggle/HuggingFace.
- **Publisher-style confound to flag if we use ISOT:** Real = Reuters, fake = Kaggle blogs. Classifier may learn publisher style, not truth. Methodology note: "ISOT splits on publisher provenance, which may inflate measured accuracy vs within-source detection." Useful error-analysis angle — train a publisher-classifier on the same features; if accuracy matches, that's evidence the signal is publisher-style.
- **Honest weakness:** Publisher confound (above); no cross-domain test (unlike #8, #9); pre-BERT; no significance tests on accuracy differences; stylistic side-observations (Figs 2, 5) descriptive only, weaker than Rashkin Table 2.

---

## Theme 4 — Detection via Transformers

### 11. Devlin et al. 2019 — BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

### 11. Devlin et al. 2019 — BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

- **Venue:** NAACL-HLT
- **Status:** ✅ Read
- **Big move:** Introduces BERT — a deeply bidirectional Transformer encoder pre-trained on unlabeled text and fine-tuned end-to-end on downstream tasks with only a single added output layer. Replaces the prior split between (a) shallow bidirectionality via concatenated independently-trained LMs (ELMo) and (b) deep unidirectionality (OpenAI GPT, left-to-right only) with deep bidirectionality in a single model.
- **Architecture (cite for Paragraph 4 S1):** Multi-layer bidirectional Transformer encoder (Vaswani et al. 2017). Two sizes reported: BERT_BASE (L=12, H=768, A=12, 110M params) — matched to GPT for comparison — and BERT_LARGE (L=24, H=1024, A=16, 340M params). WordPiece tokenizer, 30k vocab. Every sequence prefixed with a special `[CLS]` token whose final hidden state is used as the aggregate representation for classification tasks (the mechanism fake-news detection inherits).
- **Two pre-training objectives:**
  1. **Masked Language Model (MLM):** mask 15% of WordPiece tokens at random (of those: 80% `[MASK]`, 10% random token, 10% unchanged — mitigates pre-train/fine-tune mismatch since `[MASK]` doesn't appear at fine-tuning). Bidirectional conditioning becomes possible because the model isn't asked to predict tokens it has already seen.
  2. **Next Sentence Prediction (NSP):** binary classification on whether sentence B follows sentence A in the corpus (50/50 actual-next vs random). Section 5.1 ablation shows removing NSP hurts QNLI/MNLI/SQuAD; LTR-without-NSP is worse than MLM-without-NSP on every task — bidirectionality is the larger of the two gains.
- **Pre-training data:** BooksCorpus (800M words) + English Wikipedia (2,500M words), 1M steps, batch size 256.
- **Key results (just enough to support Paragraph 4):** New SOTA on 11 NLP tasks. GLUE average pushed to 80.5 (+7.7 absolute); MultiNLI 86.7 (+4.6); SQuAD v1.1 Test F1 93.2; SQuAD v2.0 Test F1 83.1. BERT_LARGE beats BERT_BASE across all GLUE tasks, including those with very small training sets (e.g., MRPC at 3.6k examples) — first convincing demonstration that extreme pre-training scale helps even very-small-data downstream tasks.
- **Fine-tuning recipe (relevant to our Methodology when we get there):** All parameters fine-tuned end-to-end. Recommended hyperparameter ranges — batch size 16 or 32, learning rate 2e-5 / 3e-5 / 5e-5, 2-4 epochs. Replicable in ~1 hour on a single Cloud TPU or a few hours on a GPU. **Important for our Colab plan:** large datasets (100k+ labels) are robust to hyperparameter choice; small datasets (LIAR at 12.8k is borderline) are sensitive — Devlin himself observed BERT_LARGE was sometimes unstable on small datasets and used random restarts.
- **Why it matters for our paper:** Paragraph 4 Sentence 1 anchor — the citation that establishes the transformer fine-tuning paradigm fake news detection inherits. Specifically supports the claim "a pre-trained transformer + one classification layer + fine-tune all parameters" as a generic recipe for text classification. The `[CLS]`-token-into-linear-layer setup (Figure 4, panel b: "Single Sentence Classification Tasks") is exactly what our transformer detection model will use on LIAR.
- **Honest weakness:** Not a fake news paper — generic NLP foundation, so the relevance is methodological, not empirical. No results on misinformation tasks. NSP was later shown (RoBERTa, Liu et al. 2019) to be unnecessary or harmful, but that's outside our reading list and doesn't affect our use of BERT as a citation. Pre-LLM era; doesn't engage with the style-vs-content question our thesis hinges on — BERT learns whatever the fine-tuning labels signal, which makes it just as vulnerable to the Schuster 2020 critique (#14) as any other detection model. Worth flagging when we get to Paragraph 6: our transformer baseline doesn't escape the "style ≠ truth" problem — it inherits it.

### 12. Reis, Correia, Murai, Veloso & Benevenuto 2019 — Supervised Learning for Fake News Detection

- **Venue:** IEEE Intelligent Systems (Affective Computing and Sentiment Analysis dept., March/April 2019) — short 6-page department piece, not a full research paper.
- **Status:** ✅ Read
- **Big move:** Head-to-head benchmark of five classical classifiers (KNN, NB, RF, RBF-SVM, XGBoost) over a feature set consolidated from prior fake news work, on a single recently-released labeled dataset. Adds a new feature family — **domain localization** (IP/geo of news outlet) — and a credibility/trustworthiness bundle pulled from Facebook + Alexa APIs.
- **Dataset:** BuzzFace (Santia & Williams 2018) — 2,282 BuzzFeed news articles on the 2016 US election, journalist-labeled, enriched with Facebook comments/shares/reactions. Drops "non-factual" stories (12%), merges "mostly false" (4%) + "mixture of true and false" (11%) into one **fake** class; remaining 73% = **true**. Binary task. **Class imbalance is ~3:1 true:fake** — they don't say how they handle this, and report AUC + Macro-F1 (Macro-F1 partly controls for it).
- **Features (3 families, 170 features total):**
  1. **Textual (141 features):** language/syntax (POS, n-grams, readability — 31 features), lexical (counts, pronouns, punctuation), psycholinguistic (LIWC 2015 — 44 features), semantic (Google Perspective API toxicity score), subjectivity/sentiment (TextBlob).
  2. **News source (13 features):** political bias label from BuzzFeed dataset; **credibility/trust** — Facebook page-fan count, page-talking-about count, Alexa rank, dissimilarity-to-top-500-newspapers (edit distance, on the theory that fake sites mimic real ones), low-credibility-domain indicators from Shao et al. 2017; **domain location** (5 new features: IP, lat, lon, city, country via trace route + ipstack API).
  3. **Environment (21 features):** Facebook engagement (likes, shares, comments), and **comment-rate temporal patterns** in 9 time windows (15 min → 24 hr post-publication).
- **Method:** Hand-crafted features fed to classical classifiers. No DL. Five-fold CV × 10 shuffles = 50 runs, 95% CIs. Authors explicitly skip neural networks: "since we used hand-crafted features, there was no need to include a neural network model… it would only associate weights with the features, rather than find new ones." (Defensible for the comparison but means this paper does NOT speak to the question "does BERT beat TF-IDF on fake news.")
- **Results (Table 1):** AUC — KNN 0.80, NB 0.72, RF 0.85, SVM 0.79, **XGB 0.86**. Macro-F1 — KNN 0.75, NB 0.75, **RF 0.81**, SVM 0.76, **XGB 0.81**. RF and XGB statistically tied at the top.
- **ROC operating point (their headline practical finding):** On XGB, choose a threshold that catches ~100% of fake news at the cost of ~40% false-positive rate on true news. They frame this as "useful for fact-checkers" — the system flags candidates, humans verify.
- **Feature-importance ranking (Fig. 2, Chi-Square):** Most discriminative families are **credibility/trustworthiness of source**, **domain localization**, and **news engagement** — i.e., **non-textual** features dominate. Textual feature families (language, lexical, LIWC, semantic) rank lower. **This is the result worth flagging for our thesis.**
- **Why it matters for our paper:**
  - **Paragraph 4 Sentence 2:** modern empirical comparison of supervised methods on fake news (the slot Reis fills). Concrete numbers: tree ensembles (RF, XGB) at 0.85-0.86 AUC / 0.81 Macro-F1 beat linear SVM (0.79) and KNN/NB on a moderate-sized real-world dataset.
  - **Useful side-implication for Paragraph 6 (thesis hinge):** Reis's own feature-importance result shows that on a real dataset where source/engagement metadata is available, **non-textual features carry more signal than textual ones.** This is a quieter version of the style-≠-truth argument — even within the detection paradigm, the most discriminative cues are not about _what the article says_ but _who published it and how it spread_. Worth a single sentence in Para 6 if it fits.
- **Confound to flag (matches Ahmed's publisher-style problem from #10):** Source credibility features include things like "is this domain in Alexa's top 500 newspapers" and "edit-distance similarity to top-500 newspaper domains." On a dataset where real news comes from mainstream outlets and fake news comes from fringe sites, these features effectively encode **publisher provenance**, not factuality. Same conceptual problem as ISOT (Reuters vs Kaggle blogs).
- **Honest weakness:**
  1. **Short department piece**, not a full research paper — 6 pages, light methodology section, no error analysis, no ablations beyond Chi-Square ranking.
  2. **Single dataset** (BuzzFace, 2,282 articles, US politics, 2016) — narrower than Ahmed #10 (three datasets) or Pérez-Rosas #8 (two datasets + cross-domain).
  3. **No cross-domain / cross-source test** — they don't probe generalization at all.
  4. **No neural baseline** — authors explicitly skip; this paper doesn't actually settle "classical vs transformer" for our Paragraph 4.
  5. **Reproducibility is broken in 2026:** Alexa Internet ranking shut down in 2022; Facebook Graph API has locked down most engagement metrics; Google Perspective API still exists but has changed; ipstack still works but their pipeline isn't documented enough to reproduce. Don't propose to replicate Reis's source/environment features in our experiments.
  6. **Class imbalance not addressed.** ~3:1 true:fake split; they don't report how (or whether) they balance for training.
  7. **Pre-BERT in spirit.** 2019 publication but no contextual embeddings, no fine-tuning, no comparison to neural baselines that were already standard by then.

---

## Theme 5 — Detection Benchmarks

### 13. Wang 2017 — "Liar, Liar Pants on Fire": A New Benchmark Dataset for Fake News Detection

- **Venue:** ACL (short paper, 5 pp.)
- **Status:** ✅ Read
- **Big move:** Releases **LIAR**, a 12,836-statement fake news dataset that is "an order of magnitude larger" than the prior PolitiFact-derived sets (Vlachos & Riedel #2's 221 statements; Ferreira & Vlachos 2016's 300 rumors). First fake news dataset large enough to actually train and evaluate machine learning models on short-statement classification.
- **Dataset specifics (cite this):**
  - 12,836 short statements from PolitiFact's API, 2007–2016.
  - **6-way labels:** pants-fire, false, barely-true, half-true, mostly-true, true.
  - **Label distribution is roughly balanced:** all classes 2,063–2,638 except pants-fire (1,050). Important — no need for class-balancing tricks on the 6-way task.
  - **Splits:** train 10,269 / valid 1,284 / test 1,283.
  - **Avg. statement length: 17.9 tokens** — these are _short_ (one sentence), unlike article-length datasets (ISOT, FakeNewsAMT). Has consequences for modelling.
  - **Inter-annotator agreement:** Cohen's κ = 0.82 on a 200-sample second-pass — high, but only against the _PolitiFact reporter's verdict_, not against independent annotators.
  - **Metadata included per statement:** subject, speaker, speaker's job, state, party affiliation, context/venue, and a **credit history vector** = counts of the speaker's prior labels across the 5 truthfulness levels. (NB: the current statement's label is included in this vector — must be subtracted before use, or it leaks the target.)
  - **Contexts sampled:** news releases, TV/radio interviews, campaign speeches, TV ads, tweets, debates, Facebook posts. **Top subjects:** economy, healthcare, taxes, federal-budget, education, jobs, state-budget, candidates-biography, elections, immigration. US-centric and politically focused.
- **Models & results (6-way classification, accuracy on test set):**
  - Majority baseline: **0.208**
  - SVM: 0.255
  - Logistic Regression: 0.247
  - Bi-LSTM: 0.233 (overfits)
  - **CNN (text only): 0.270** — best text-only model, significantly beats SVM (p < .0001, paired t-test)
  - **Hybrid CNN (text + all metadata): 0.274** — best overall
  - Best single-metadata hybrid: Text + Speaker (valid 0.277, test 0.248)
- **What the numbers actually say (for Paragraph 5):**
  - 0.27 accuracy is **only ~6 points above the 0.21 majority baseline** on 6-way classification. **Short-statement truthfulness classification from text alone is very hard.**
  - Adding all metadata moves the test number from 0.270 → 0.274 — **0.4 absolute points.** Wang frames this as "significant improvements"; honestly, it's marginal.
  - This is one of the strongest empirical signals in our reading list that **content alone has a low ceiling for fake news detection** — feeds directly into the Paragraph 6 thesis hinge.
- **Why it matters for our paper:**
  - **Paragraph 5 anchor (all 3 sentences).** Wang gives us: what LIAR is (S1), how hard the task is (S2), and our methodological choice (S3: binary collapse).
  - **Provides the empirical floor for Paragraph 6.** Wang's 0.27 on 6-way + 0.274 with all metadata is a quieter, larger-sample version of the same "content ≠ truth" story Schuster (#14) makes formally. Worth a one-clause callback in P6 if it fits.
  - **Decides our primary detection dataset.** LIAR is the canonical choice: most-cited fake news benchmark, clean splits, available on HuggingFace (`liar` dataset), loads in Colab in seconds. ISOT remains the backup if LIAR causes us trouble.
- **Honest weakness:**
  1. **US-centric and political-only.** PolitiFact's focus is US politics 2007–2016 — no general-news, no international, no science. Our cross-paradigm comparison inherits this scope.
  2. **Single-rater ground truth.** Each statement labeled by _one_ PolitiFact editor; Wang's κ = 0.82 is between Wang's 200-sample re-check and the original rating — not multi-annotator agreement on the full set.
  3. **Statements are decontextualized.** The "claim" is one sentence; the surrounding analysis report (which the rater used) is _not_ in the dataset. So the task is effectively "judge truth from a sentence with some metadata" — an arguably impossible setup for the harder cases, which inflates the difficulty and depresses ceilings.
  4. **6-way labels conflate intent with content** (same critique as Rashkin #9 makes of his own 4-way news-type labels). Pants-fire vs false is a journalistic distinction about _how wrong_, not a clean ML target.
  5. **Pre-BERT.** Best model is a CNN on word2vec; no transformer baseline. The reported 0.27 ceiling is not the state of the art today, but the _gap_ (small metadata gain, low absolute number) is what survives.
  6. **Metadata leakage risk.** Credit history vector includes the current statement's label — easy to miss when loading, would inflate results.
- **Cross-refs:**
  - Vlachos & Riedel #2 — LIAR is the dataset-scale answer to V&R's 221-statement seed.
  - Rashkin #9 — also uses PolitiFact (4,366 quotes); Rashkin reports 0.22 macro-F1 on 6-class with classical models. Same dataset family, same difficulty signal.
  - Schuster 2020 #14 — Wang's 0.4-point metadata gain is the empirical hint; Schuster will be the theoretical statement.
  - Ahmed #10 — contrast point: Ahmed reaches 92% on full articles, Wang gets 27% on single sentences. The difference _is the statement length and the publisher-style confound_, not the underlying task being easier. Worth flagging in our Methodology when we justify dataset choice.

## Theme 6 — The Limit of Detection: Style ≠ Truth ⭐ THESIS HINGE

### 14. Schuster et al. 2020 — The Limitations of Stylometry for Detecting Machine-Generated Fake News

- **Venue:** TACL (Computational Linguistics, Vol. 46, No. 2)
- **Status:** ✅ Read
- **Big move:** Surgically separates **provenance detection** (machine-vs-human authorship) from **veracity detection** (true-vs-false content) and shows that the same state-of-the-art stylometry-based classifier — Grover-Mega's discriminator — does the first well and the second barely above chance, when both classes are LM-generated. The argument's grounding (Section 1, citing Mazar, Amir & Ariely 2008): **humans diverge stylistically when lying; LMs do not** — they generate stylistically consistent text regardless of underlying intent. So style cues that work on human deception don't transfer to LM-mediated misinformation.
- **Adversarial framing (Section 3):** Attacker uses an LM to mass-produce text containing false claims; verifier (Grover-Mega discriminator) sees the attacker's outputs and trains adaptively to flag them against real text from reputable sources (NYT, CNN). "Fake news" is defined narrowly — true article with small false additions/edits — matching how humans actually lie (smallest possible deviation from truth, also matching LIAR-style short-statement datasets).
- **Two veracity datasets they build (Section 4):**
  1. **QA extension (newsQA + Grover):** Take a CNN article, remove the gold-answer sentence, append `We attempt to answer: <question>\nAnswer:`, and let Grover generate. Human-label the generation: real if true, fake if at least one false statement. Inter-annotator κ = 0.78. Both classes are LM-generated; only veracity differs.
  2. **Article modification (NYT + GPT-2 Medium):** Take an NYT article; randomly delete m/2 occurrences of "not"/"no" and add m/2 negations at the highest-probability locations under GPT-2 Medium. Total negation count unchanged (avoids that confound). Original = real, modified = fake. Tested at m=2, 6, 10.
- **Two provenance datasets for the mirror experiment (Section 5):** Full-article GPT-2 XL generations vs WebText; "vanilla extension" — articles where the last g% (g ∈ {1%, 20%}) is GPT-2 Medium continuation, vs human-only truncations of the same length; QA extension reframed as machine-vs-human (gold newsQA answers as real, Grover answers as fake).
- **Headline results — VERACITY (Table 1):**
  - QA extension: **0.71 F1, 71% accuracy.** But length-only baseline reaches 56%, and restricting to short (≤10-word) answers drops accuracy to 62% — most of the gain is a length artifact, not stylometric signal.
  - Modification m=2: **0.53 F1, 53% accuracy — at chance.** m=6: 0.65 F1. m=10: 0.63 F1 (precision 0.73, recall 0.47 — the classifier hedges).
  - Zero-shot: "very low in all cases."
- **Headline results — PROVENANCE (Table 2):**
  - Full article (zero-shot, GPT-2 XL vs WebText): **0.90 F1, 90% accuracy.**
  - Adaptive, full article: 0.94 F1, 94% acc.
  - Adaptive, vanilla extension at g=1% (a single machine-generated sentence in a wall of human text): **0.94 F1, 95% accuracy.**
  - QA extension as machine-vs-human: 0.83 F1, 83% accuracy.
- **THE LOAD-BEARING JUXTAPOSITION (this is what we cite):** Same Grover-Mega classifier, same family of LM outputs.
  - Detecting a **single machine-generated sentence** inside human text → **0.94 F1.**
  - Detecting whether **fully machine-generated text is false vs true** → **0.53 F1** (m=2) or **0.71 F1** with length confound (QA).
  - The classifier is sensitive enough to flag one synthetic sentence in a wall of human writing — and yet, on text that's entirely LM-generated, it cannot separate truth from falsehood. **This is the cleanest published demonstration that stylometric detectors are picking up provenance, not veracity.**
- **Human evaluation (Section 4.1) — bridges directly to Paragraph 7:**
  - QA-veracity, no external info: human F1 = 0.68 (about the same as the classifier's 0.71).
  - QA-veracity, **with access to external sources for fact-checking**: human F1 = 0.84.
  - Modification m=2: human F1 = 0.74.
  - **The 0.16 F1 gain comes from external evidence access, not better stylistic intuition.** Schuster's own framing: "verifying against other resources can drastically improve results." This is the authors of the most-cited "limits of detection" paper pointing directly at the verification paradigm as the answer.
- **Authors' own recommendations (Section 6):** (1) Extend veracity-based benchmarks (current ones assume no legitimate LM use); (2) Improve non-stylometry methods — they explicitly highlight fact-checking, citing Thorne et al. 2018 (our #21), Hanselowski et al. 2018 (our #16), Wang 2017 (our #13), Augenstein et al. 2019 (our #22), and **Schuster et al. 2019 (our #24)**. The paper's own roadmap is exactly the architecture of our reading list.
- **Why it matters for our paper:**
  - **Paragraph 6 anchor — Sentence 2.** The single load-bearing citation in Related Work. The juxtaposition (0.94 F1 provenance vs 0.53 F1 veracity, same classifier) is the punchline.
  - **Seeds Para 6 S4 (synthesis, no citation).** The synthesis sentence — "detection systems learn the style of fakeness, not its factual content" — rests on Schuster's specific finding generalized via the convergent evidence chain in our reading list (Pérez-Rosas #8 cross-domain collapse, Rashkin #9 cross-source drop, Wang #13 0.27 ceiling on short statements, Bondielli & Marcelloni #7 style-convergence remark, Potthast #15 upcoming).
  - **Seeds Para 6 S5 (bridge to verification).** Schuster's own human-eval finding (external sources → +0.16 F1) is the in-paper bridge.
  - **Frames as field-acknowledged, not contrarian (per our cross-paper observation on Guo #5).** Guo et al. 2022 already cite Schuster 2020 as an accepted limitation of detection; we're operationalizing a critique the field's flagship survey accepts.
  - **Cross-paper symmetry note:** Schuster 2020 cites Schuster 2019 (our #24) in Section 2 as the verification-side parallel. The P6 ↔ P10 mirror in our paper structure is field-grounded, not invented.
- **Honest weakness / scope of the claim:**
  1. **Scope is machine-generated misinformation only.** Schuster 2020 does _not_ show stylometry fails on human-written true-vs-false (Pérez-Rosas, Rashkin, Wang carry that load in our reading list). When framing P6 S2 we must say "for LM-generated misinformation" — overclaiming would be inaccurate.
  2. **Single detector tested.** Grover-Mega is the SOTA stylometric detector circa 2019-2020, but it's one model. The conclusion would be stronger with multiple detectors; the paper doesn't ablate.
  3. **QA-extension veracity result has a length confound** the authors themselves flag (56% length-only baseline, 71% → 62% on short answers). The modification result (m=2 at chance) is the cleaner finding.
  4. **Modification dataset is narrow.** Negation-flip is a single edit type; doesn't cover paraphrase, entity substitution, number-swap, etc. The result is "stylometry can't catch negation-flip"; it generalizes by intuition, not by demonstration.
  5. **Pre-LLM-scale era.** GPT-2 Medium/XL and Grover-Mega; modern LLMs (GPT-3.5+, Claude, Llama) are stylistically more sophisticated, which strengthens Schuster's conclusion in spirit but is outside the paper's tested scope.
  6. **Adaptive setting is generous to the detector.** Verifier sees attacker examples and fine-tunes against them; real-world detectors usually don't have this. Even with this generous setting, veracity classification collapses to 0.53 F1 — strengthens the conclusion, but worth being explicit about.
- **Cross-refs (already lined up in earlier notes):**
  - #5 (Guo 2022) — cites Schuster 2020 directly as a limitation of detection.
  - #7 (Bondielli & Marcelloni 2019) — style-convergence remark ("fake news are becoming more and more similar to proper news for what concerns the writing style").
  - #8 (Pérez-Rosas 2018) — cross-domain collapse 0.78 → 0.48 acc.
  - #9 (Rashkin 2017) — cross-source drop 0.91 → 0.65 F1; 0.22 macro-F1 on 6-class graded.
  - #10 (Ahmed 2018) — 98% → 92% on temporal confound restriction (publisher-style confound implicit).
  - #12 (Reis 2019) — Chi-Square ranks source/engagement above textual features (already in P4 S3, do NOT repeat in P6).
  - #13 (Wang 2017) — 0.27 ceiling on 6-way short-statement detection; 0.4-point metadata gain.
  - #15 (Potthast 2018) — upcoming, reinforces with stylometric "hyperpartisan ≠ false."
  - #24 (Schuster 2019) — mirror paper for verification (Theme 10).

---

### 15. Potthast et al. 2018 — A Stylometric Inquiry into Hyperpartisan and Fake News

- **Venue:** ACL (long paper)
- **Status:** ✅ Read
- **Big move:** Tests a clean version of the question "does style separate truth from falsehood?" on a professionally fact-checked corpus of human-written political news, and answers no. The headline result is a juxtaposition of three tasks run on the same feature set: style discriminates hyperpartisan from mainstream (F1 = 0.78), satire from real (F1 = 0.81), but **fake from real fails (F1 = 0.46)** — at or below the all-real naive baseline.
- **Corpus they release — BuzzFeed-Webis Fake News Corpus 2016:** 1,627 articles from 9 Facebook-verified publishers (3 mainstream — ABC, CNN, Politico; 3 hyperpartisan left — Addicting Info, Occupy Democrats, The Other 98%; 3 hyperpartisan right — Eagle Rising, Freedom Daily, Right Wing News), collected over 7 workdays around the 2016 US election. Each article fact-checked by 1 of 4 BuzzFeed journalists into 4 labels: mostly true / mixture of true and false / mostly false / no factual content. Operationalisation for fake-news experiments: mostly-true = real, (mostly-false ∪ mixture) = fake, no-factual-content dropped, satire compared separately on Rubin et al.'s corpus. **Striking fact for our intro / motivation:** 97% of the 299 articles labelled fake are also hyperpartisan; mainstream publishers produced 0 mostly-false articles and 8 mixtures across 826 articles.
- **Feature set:** char/stop-word/POS n-grams (n ∈ [1,3]), 10 readability scores, General Inquirer dictionary features, plus domain-specific news features (quote ratio, external-link ratio, paragraph count, average paragraph length). Random forest classifier (WEKA defaults).
- **Critical methodological choice (cite this — strengthens our use of their result):** 3-fold cross-validation where **each fold holds out one publisher per orientation**, so the classifier cannot win by learning publisher style. This is the publisher-holdout design that Ahmed #10 and Reis #12 _don't_ have, and it's exactly what controls for the Reuters-vs-Kaggle-blogs confound flagged in their notes. When Potthast's classifier fails at fake-vs-real (F1 0.46), the failure is not a publisher-style artefact — it's the style-≠-truth finding in its cleanest form.
- **Three results (Tables 2, 3, 5, 6):**
  - **Hyperpartisan vs mainstream (binary):** Style F1 = 0.78, accuracy 0.75, hyperpartisan-class recall 0.89. Beats the topic baseline.
  - **Predicting orientation (left vs right vs mainstream, 3-way):** Style accuracy 0.60 (vs majority 0.51). Confusion matrix: 66% of misclassified left articles → right. Triggers their hypothesis that left and right share a hyperpartisan style.
  - **Fake vs real, restricted to hyperpartisan articles only (since mainstream has ~0 fakes):** Generic classifier Style F1 = 0.41 (fake) / 0.63 (real); orientation-specific Style F1 = 0.46 (fake) / 0.61 (real). **None of these beats the all-real naive baseline of F1 = 0.76.** Topic baseline (BOW) does no better. They state plainly: "style-based fake news classification simply does not work in general."
  - **Satire vs real (Rubin et al.'s S-n-L corpus):** Style F1 = 0.81. Confirms style works for genre-level distinctions but not within-genre veracity.
- **Why this is the cleanest "style ≠ truth" demonstration for human-written misinformation:** Three things stack favourably. (1) The labels are professional journalist fact-checks, not crowd-sourced (no AMT-mirroring confound like Pérez-Rosas #8) and not source-as-label (no publisher confound like Ahmed #10 / ISOT). (2) The cross-validation explicitly holds out publishers, so the classifier can't shortcut on outlet style. (3) The same feature set on the same corpus _does_ succeed at hyperpartisan-vs-mainstream and satire-vs-real, so the failure on fake-vs-real cannot be blamed on weak features. The remaining hypothesis the data supports is that within a single posture (hyperpartisan political writing), true and false articles are written the same way.
- **Authors' own bridge to verification (gift for our P6 → P7 transition):** Conclusion explicitly recommends style-based hyperpartisan detection as **pre-filtering for human fact-checkers** — "Employed as pre-filtering technologies to separate hyperpartisan news from mainstream news, our approach allows for directing the attention of human fact checkers to the most likely sources of fake news." Mirror of Schuster 2020's "external sources → +0.16 F1" bridge — both Theme 6 papers point at verification as the next step.
- **Side-finding worth a sentence in cross-paper observations (not in P6):** Three independent methods (random forest on style features; leave-out classification; Unmasking adapted to genre styles) converge: hyperpartisan-left and hyperpartisan-right are stylistically _more similar to each other_ than either is to the mainstream. Orthogonal to our thesis but a useful corroboration that style tracks posture, not content.
- **Why it matters for our paper:**
  - **Paragraph 6 S3 anchor.** Pairs with Schuster #14 in S2. Schuster covers the LM-generated case; Potthast covers the human-written-political case. Between them, S2 and S3 cover the two regimes of fake news that matter for our project.
  - **Strengthens Para 6 S4 synthesis.** Two independent demonstrations of the same structural limit — one on machine-generated text (Schuster), one on human-written political news (Potthast) — make the synthesis claim ("structural rather than a matter of more data or larger models") substantially more defensible than either alone would.
  - **Strengthens the P6 → P7 bridge in S5.** Two thesis-hinge papers (Schuster, Potthast) both end by pointing at verification / external evidence as the answer. The bridge is no longer just our framing — it's the convergent recommendation of the field's load-bearing critiques.
  - **Methodological precedent.** Their publisher-holdout 3-fold CV is the right design for our detection arm on LIAR — though LIAR is statement-level not article-level, so the analogue is speaker-holdout (which we are deliberately _not_ doing, since we're using LIAR vanilla splits for comparability with Wang #13). Note in Limitations: our LIAR setup does not control for speaker-style confounds the way Potthast controls for publisher style.
- **Honest weakness / scope of the claim:**
  1. **Single corpus, single time window, single country.** 1,627 articles, US politics, 7 days around the 2016 election, English only. Same scope critique as LIAR #13. The failure of style on this dataset doesn't formally prove style fails everywhere, but the design controls strengthen the inference.
  2. **Article-level labels.** Many "fake" articles are mixture-of-true-and-false rather than entirely fabricated — Potthast acknowledges this; it's realistic but means the task is "detect partially-fake," not "detect outright fabrication."
  3. **Single random forest, WEKA defaults.** No transformer baseline. A modern fine-tuned BERT might do better; the paper predates that as a standard. The convergent failure of style features + topic BOW + Unmasking is still a meaningful negative result, but a strict-falsifier would want a contemporary neural baseline rerun on the same corpus.
  4. **Round-robin single-annotator labels.** Each article reviewed by one journalist (with second/third opinions only for non-true ratings). No inter-annotator agreement reported on a held-out re-rating set. Comparable to LIAR's single-rater protocol.
  5. **Fake-vs-real classifier is trained on hyperpartisan articles only.** Mainstream is excluded because it has ~0 fakes. This is honest (you can't classify what isn't there) but means the result is "style doesn't separate fake from real _within hyperpartisan political news_" — narrower than "style doesn't separate fake from real anywhere." Worth flagging when we draft S3 to avoid overclaim.
- **Cross-refs (lined up with earlier notes):**
  - #1, #4 — Potthast's three-paradigm taxonomy (knowledge / context / style) in Figure 1 matches Shu's and Zhou & Zafarani's; explicit confirmation of the framing our Paragraph 1 uses.
  - #8 (Pérez-Rosas) — Potthast cites P-R explicitly in related work and flags the AMT-mirroring confound; Potthast's professional-journalist labels are the answer to that confound.
  - #10 (Ahmed) — Potthast's publisher-holdout CV is the methodological answer to Ahmed's Reuters-vs-Kaggle publisher confound.
  - #9 (Rashkin) — Potthast adopts Rashkin's best-performing style features. Stylistic-feature lineage is direct.
  - #13 (Wang) — Potthast cites Wang/LIAR in related work; the two are complementary scope (Wang: statement-level political; Potthast: article-level political).
  - #14 (Schuster 2020) — Theme 6 partner. Schuster covers LM-generated; Potthast covers human-written. P6 S2 and S3 respectively.
  - #20 (Hassan, ClaimBuster) — Potthast's "pre-filter for fact-checkers" framing is exactly the role check-worthy claim detection plays upstream of verification. Note for when we reach Theme 8.

---

## Theme 7 — Verification via NLI / Textual Entailment

### 16. Hanselowski et al. 2018 — UKP-Athene: Multi-Sentence Textual Entailment for Claim Verification

- **Venue:** EMNLP FEVER Shared Task Workshop (2018)
- **Status:** ✅ Read
- **Big move:** Third-place system (out of 23) in the inaugural FEVER shared task. Operationalizes the four-stage Vlachos & Riedel (#2) / Guo et al. (#5) pipeline as a concrete three-module neural system, and — most importantly for our paper — frames the final verdict step as **multi-sentence textual entailment**: the claim is the hypothesis, the five retrieved evidence sentences are the (combined) premise, and the verdict is one of {Supported, Refuted, NotEnoughInfo}. This is the citation that anchors "verification = NLI" in our reading list.
- **Three-module pipeline (maps cleanly onto Guo et al. #5):**
  1. **Document retrieval (entity-linking-style):** Constituency-parse the claim, take every noun phrase + all tokens before the main verb + the whole claim as candidate mentions, query the MediaWiki API for the top-7 Wikipedia titles per mention, run an exact-title search over the 2017 dump (since MediaWiki uses live Wikipedia), then filter out titles whose stemmed form isn't fully contained in the stemmed claim.
  2. **Sentence selection (modified ESIM as a ranker):** Feed (claim, candidate sentence) into ESIM, project the last hidden state through a hidden layer + one neuron to produce a scalar ranking score. Trained with a **hinge loss with negative sampling** — positive = ground-truth evidence concatenated; negative = five randomly sampled sentences from the same Wikipedia articles. Test-time = ensemble of 10 ESIMs with different seeds, mean-score-rank the (claim, sentence) pairs, keep top 5.
  3. **Recognizing textual entailment (multi-sentence ESIM):** This is the methodological contribution. Standard ESIM takes one premise + one hypothesis; FEVER needs five evidence sentences + one claim. Their fix: run ESIM five times in parallel (claim paired with each evidence sentence individually), then use a **claim-conditioned attention mechanism** to weight and pool the five ESIM outputs into a single representation, fed through a 3-layer MLP for the 3-way verdict.
- **Word representations:** Concatenated GloVe + FastText embeddings, both pretrained on Wikipedia (domain-matched to the FEVER source corpus).
- **Results on FEVER dev (Table 3):**
  - Document retrieval accuracy: **93.55%** (baseline 70.20%)
  - Sentence selection recall: **87.10%** (baseline 44.22%)
  - Textual entailment label accuracy: **68.49%** (baseline 52.09%)
  - **Full-pipeline FEVER score: 64.74%** (baseline 32.27%) — roughly a 100% relative improvement over the organizers' baseline pipeline.
- **Sentence-count ablation (Table 2):** 1 sentence → 63.64 FEVER; 5 sentences → 64.74. The multi-sentence machinery matters but the absolute gain is modest (~1 point) — most of the verdict signal is in the top-ranked evidence sentence, with the remaining four sentences providing marginal additional context.
- **Error analysis (Section 5.3) — useful for our Discussion / error-analysis section:**
  - **Numerical reasoning failures.** Claim "The heart beats at a resting rate close to 22 beats per minute" not refuted by evidence "...close to 72 beats per minute" — GloVe/FastText embeddings don't distinguish numbers distinctly enough. Direct parallel to the kind of error we expect from our NLI-based verifier; flag in Discussion.
  - **NotEnoughInfo confusion.** Claim "Terry Crews played on the Los Angeles Chargers" labeled NEI but classified as Refuted given evidence listing teams he played for that doesn't include the Chargers. The model can't distinguish "evidence doesn't support" from "evidence refutes" — this is a recurring failure mode of NLI-based verifiers.
- **Why it matters for our paper:**
  - **Paragraph 7 S1 anchor.** The citation that lands the claim "verification can be framed as multi-sentence entailment between a claim and retrieved evidence." Hanselowski operationalizes exactly this framing in a competition-grade system.
  - **Paragraph 8 S1 anchor (carry-forward).** The three-module pipeline (retrieval → sentence selection → entailment) is the canonical FEVER architecture; Hanselowski is one of three systems (with Nie #19 and Yoneda et al.) that defined this shape. Either #16 or #19 can anchor P8 S1 — #19 is the AAAI long-paper version with more depth, #16 is the closer methodological match to what we'll build.
  - **Methodological reference for our verification arm.** Our planned verification arm = "off-the-shelf NLI model on FEVER claim-evidence pairs." Hanselowski's setup is the same shape but trained from scratch with ESIM; we get to swap in a pretrained MNLI model (Williams #18) and skip the from-scratch training. The architectural lineage is intact.
  - **Justifies the oracle-evidence simplification.** Hanselowski's full-pipeline FEVER score is 64.74, but their textual-entailment label accuracy on the selected sentences is 68.49 — and the entailment step is what we actually want to study. By using **oracle (gold) evidence** for our verification arm, we isolate the entailment step from retrieval errors, which lets the comparison with detection be about reasoning, not retrieval engineering. Mention in Methodology.
- **Honest weakness:**
  1. **ESIM is pre-BERT.** The full pipeline predates large-scale pretrained transformers; later FEVER systems using BERT/RoBERTa exceed Hanselowski's numbers substantially. We cite #16 for the framing, not for SOTA.
  2. **Pipeline error compounds.** 93.55% doc retrieval × 87.10% sentence recall × 68.49% entailment = the 64.74 full-pipeline score reflects multiplicative degradation. This is exactly why our oracle-evidence design is defensible — we want to study verification, not retrieval cascades.
  3. **Numerical-reasoning failures are unsolved.** Our pretrained MNLI verifier inherits this weakness — MNLI is also general-domain and doesn't teach numerical comparison. Flag in Limitations.
  4. **NEI handling is fragile.** Hanselowski's own error analysis shows the model can't cleanly separate "evidence doesn't support" from "evidence refutes." A pretrained 3-way NLI model has the same three labels (entailment / contradiction / neutral) but those labels weren't trained on retrieval-grounded NEI — the mapping NLI→FEVER labels is approximate. Important methodological caveat for our verification arm.
  5. **2017 Wikipedia dump dependency.** Reproducibility issue for re-running their retrieval module today; doesn't affect our use since we'll use HuggingFace's `fever` dataset with prepackaged evidence.
- **Cross-refs:**
  - #2 (Vlachos & Riedel) — Hanselowski's three modules instantiate stages 1, 3, 4 of V&R's four-stage pipeline (stage 2, "question construction," is absorbed into evidence retrieval).
  - #5 (Guo et al.) — Hanselowski is the worked example of the three-stage automated fact-checking framework Guo et al. survey.
  - #17 (Bowman, SNLI) — ESIM was originally built for SNLI; the move from "single-premise NLI on SNLI" to "multi-sentence NLI on FEVER" is the methodological bridge between #17 and #16.
  - #18 (Williams, MNLI) — Our planned upgrade: replace Hanselowski's from-scratch ESIM with a pretrained MNLI model. P7 S3 will make this case.
  - #19 (Nie, NSMN) — Sibling top-FEVER system; will anchor P8 S1 with the same three-module architecture. We won't cite both for the same claim — split #16 to P7, #19 to P8.
  - #21 (Thorne, FEVER) — Hanselowski's dataset; our P9 will introduce FEVER properly.
  - #24 (Schuster 2019) — Direct relevance to Hanselowski's NEI confusion: claim-only artifacts in FEVER mean models can sometimes guess the label without reading the evidence at all. The "evidence doesn't refute" error in §5.3 looks like reasoning failure; some of it may be artifact-driven. Note in P10 setup.

---

### 17. Bowman et al. 2015 — A Large Annotated Corpus for Learning Natural Language Inference (SNLI)

- **Venue:** EMNLP
- **Status:** ✅ Read
- **Big move:** Releases SNLI — 570,152 sentence pairs labelled entailment / contradiction / neutral — two orders of magnitude larger than prior NLI resources (RTE challenges had <1k examples each; SICK had 4,500). First NLI corpus large enough to train modern data-intensive models. Until SNLI, distributed-representation models couldn't be competitive at NLI for lack of data.
- **Construction (cite for "why this corpus is trustworthy"):** Crowdsourced on Mechanical Turk. Premises = captions from Flickr30k (literal scene descriptions, not personal-photo style). Workers wrote three hypotheses per premise — one definitely true, one possibly true, one definitely false — yielding balanced 3-way labels by construction. Critically, premises and hypotheses describe the same grounded scenario from the same perspective, which mitigates (though doesn't eliminate) the event/entity coreference indeterminacies that plague prior NLI corpora. ~2,500 workers contributed.
- **Validation:** ~10% of pairs (56,941) re-annotated by 4 additional workers → 5 labels per pair. 98% had 3-of-5 consensus; 58% unanimous. Fleiss κ = 0.70 overall (0.77 contradiction, 0.72 entailment, 0.60 neutral). Test and dev sets (10k each) are fully validated; the 2% with no consensus get a placeholder "-" label and are excluded from train/eval.
- **Splits:** 550,152 train / 10,000 dev / 10,000 test. Premise mean 14.1 tokens; hypothesis mean 8.3 tokens.
- **Models reported (just enough to know what SNLI can train):** A lexicalised classifier (BLEU, length-diff, word overlap, unigrams/bigrams, cross-unigrams, cross-bigrams) reaches 78.2% test accuracy 3-way. A 100d LSTM sentence-embedding model reaches 77.6% — first time a neural model is competitive with a strong feature classifier on NLI. Transfer learning: LSTM pretrained on SNLI, fine-tuned on SICK → 80.8% on SICK (vs 71.3% SICK-only), approaching the 84% inter-annotator ceiling. **The transfer result is what foreshadows our usage**: an NLI model trained on SNLI carries enough semantic signal to transfer to other entailment tasks — but Bowman's own RTE-3 transfer attempt failed because of genre mismatch, which is exactly the gap MultiNLI (#18) later addressed.
- **Why it matters for our paper:**
  - **Paragraph 7 S2 anchor.** Cite for the claim "large-scale supervised NLI is a well-studied task," which is the precondition for "you can grab a pretrained NLI model off the shelf and apply it to FEVER claim-evidence pairs." Don't oversell — SNLI alone is single-genre (image captions); the cross-domain transfer claim belongs to MNLI (#18) in S3.
  - **Methodological lineage check.** Hanselowski's ESIM (#16) is built on the SNLI-era NLI architecture. Pretrained MNLI checkpoints we'll use as our verifier inherit SNLI's label scheme (entailment / contradiction / neutral). Worth flagging when describing the NLI→FEVER label mapping (Supported ≈ entailment, Refuted ≈ contradiction, NEI ≈ neutral — approximate, per Hanselowski's error analysis).
- **Honest weakness:**
  1. **Single genre.** Premises are all Flickr30k image captions — concrete, present-tense scene descriptions. SNLI-trained models do not transfer cleanly to other genres (Bowman's own RTE-3 attempt failed). The "cross-domain NLI works" claim must be sourced to MNLI, not SNLI.
  2. **Hypothesis artifacts (known post-publication, not in this paper).** Gururangan et al. 2018 / Poliak et al. 2018 later showed that ~67% of SNLI labels can be predicted from the hypothesis alone — annotators developed predictable patterns (negation → contradiction, generalisation → entailment). Direct parallel to the FEVER claim-only artifact Schuster 2019 (#24) flags. Worth mentioning in P10 setup if it fits, but don't redirect Theme 7 to talk about it — Theme 10 carries that argument.
  3. **Coreference indeterminacy mitigated, not solved.** Same-scenario grounding helps but doesn't eliminate edge cases.
- **Cross-refs:**
  - #2 (Vlachos & Riedel), #5 (Guo et al.) — Guo et al. explicitly cite Bowman 2015 when framing verification as RTE.
  - #16 (Hanselowski) — ESIM trained on SNLI is the architectural ancestor of his FEVER entailment module.
  - #18 (Williams, MNLI) — MNLI extends SNLI to multiple genres; cite together for the SNLI→MNLI lineage.
  - #24 (Schuster 2019) — claim-only artifacts in FEVER mirror Gururangan et al.'s hypothesis-only artifacts in SNLI. Note for P10.

---

### 18. Williams, Nangia & Bowman 2018 — A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference (MultiNLI)

- **Venue:** NAACL-HLT
- **Status:** ✅ Read
- **Big move:** Releases MultiNLI — 433k premise-hypothesis pairs labelled entailment / neutral / contradiction across **ten genres** of written and spoken English, designed explicitly to remedy SNLI's single-genre limitation. Pairs are constructed by the same crowdsourcing recipe as SNLI (Bowman #17) — one premise → three hypotheses (one entailing, one neutral, one contradicting), 3-way balanced by construction. Validation: 5 labels per dev/test pair, gold by majority; agreement statistics (58.2% unanimous, 88.7% individual=gold, Table 2) are essentially identical to SNLI's despite the wider genre coverage.
- **Ten genres (cite this for the diversity claim):** Five appear in train + dev + test (FICTION, GOVERNMENT, SLATE, TELEPHONE, TRAVEL — the **matched** sets, 77k–83k train each); five appear only in dev + test (9/11, FACE-TO-FACE, LETTERS, OUP, VERBATIM — the **mismatched** sets, 0 train). Total: 392,702 train / 20,000 dev / 20,000 test. **The matched/mismatched split is the load-bearing design choice** — it builds cross-domain transfer evaluation directly into the corpus.
- **Premise sources:** Nine genres from the Open American National Corpus (transcribed conversations, government documents, philanthropic letters, the 9/11 Commission report, Oxford UP non-fiction, Slate articles, Switchboard telephone transcripts, Berlitz travel guides, Verbatim linguistics posts); the tenth, FICTION, compiled from freely available novels 1912–2010. Mean premise length 22.3 tokens vs SNLI's 14.1 — premises are **longer and more syntactically complete** (91% parsed as full sentences vs SNLI's 74%).
- **Baseline results (Table 4) — the difficulty claim:**
  - SNLI test (trained on SNLI): CBOW 80.6, BiLSTM 81.5, **ESIM 86.7**.
  - MultiNLI test (trained on MultiNLI): CBOW 64.8 / 64.5, BiLSTM 66.9 / 66.9, **ESIM 72.3 / 72.1** (matched / mismatched).
  - **~15 point gap** between SNLI and MultiNLI performance with the same models — MultiNLI is dramatically harder.
- **Matched ≈ mismatched (the cross-genre transfer headline):** ESIM scores 72.3 on matched genres and 72.1 on mismatched — essentially identical. Williams et al. read this as evidence that current models aren't yet fitting the training genres tightly enough for genre mismatch to bite; the design anticipates that future stronger models will show a wider matched/mismatched gap, at which point the corpus serves as a genuine domain-adaptation benchmark.
- **Single-genre transfer experiment (Section 3, the genre-similarity finding):** A CBOW model trained on TELEPHONE achieves its best accuracy (63%) on FACE-TO-FACE — _better than on its own genre_. SLATE trains the broadest model: highest accuracy of any single-genre model on 9/11, VERBATIM, TRAVEL, and GOVERNMENT. A model trained only on SNLI performs **worse on every MultiNLI genre than any model trained on any MultiNLI genre** — concrete evidence that SNLI's image-caption distribution does not generalise.
- **Linguistic-phenomenon coverage (Table 5):** MultiNLI dramatically increases the rate of phenomena rare or absent in SNLI: pronouns (34% → 68%), quantifiers (33% → 63%), modals (<1% → 28%), negation (5% → 31%), WH-terms (5% → 30%), belief verbs (<1% → 19%), discourse markers (<1% → 14%), presupposition triggers (8% → 22%), conditionals (4% → 15%). These are the phenomena that matter for verification — claims often involve quantification ("all," "some"), negation, modality ("might," "should"), and temporal reasoning. SNLI-trained models simply don't see enough of these.
- **Mixed-training result (Table 4, MNLI+SNLI row):** Training on MultiNLI + downsampled SNLI improves SNLI test accuracy substantially (e.g., ESIM 60.7 → 79.7 on SNLI) but yields **no significant gain on MultiNLI itself** — adding SNLI does not help cover MultiNLI's phenomena, while adding MultiNLI rescues SNLI performance. Asymmetric.
- **Side-result the paper anticipates (Conneau et al. 2017, cited in §5):** MultiNLI + SNLI is an effective source corpus for transfer learning to other sentence-understanding tasks via pre-trained sentence encoders — the precedent that justifies the modern recipe of "pretrained NLI checkpoint as off-the-shelf entailment classifier." This is the practical consequence for our pipeline.
- **Why it matters for our paper:**
  - **Paragraph 7 S3 anchor.** The citation that lands the claim "MultiNLI extends NLI to multiple genres, producing models that transfer better across domains than SNLI-only models." Specific numerical support: SNLI-trained models lose on every MultiNLI genre; ESIM trained on MultiNLI reaches 72.1 on **unseen** genres (mismatched) vs 72.3 on seen genres.
  - **Justifies our verifier choice (P7 S4).** Our verification arm will use a pretrained MNLI checkpoint applied to FEVER claim-evidence pairs. The justification chain: SNLI (#17) establishes the task at scale → MultiNLI (#18) extends it to heterogeneous text genres → therefore an MNLI-trained NLI model is the appropriate off-the-shelf verifier when evidence comes from heterogeneous sources (FEVER's Wikipedia sentences, distinct genre from SNLI's image captions).
  - **Genre alignment with FEVER.** FEVER's evidence sentences are Wikipedia text — closer to MultiNLI's GOVERNMENT, TRAVEL, and OUP genres than to SNLI's image captions. An MNLI-trained model has at least seen prose like this; an SNLI-trained model has not.
- **Honest weakness:**
  1. **Matched ≈ mismatched gap is suspiciously small.** ESIM scores 72.3 vs 72.1 — Williams et al. acknowledge this means the genre-mismatch benchmark hasn't yet exposed real generalisation failure at the ESIM model scale. The corpus's value as a cross-domain benchmark depends on stronger future models actually showing a gap. For our purposes (citing MNLI as cross-genre training data), this caveat doesn't bite — we want training-side diversity, not a clean test-side benchmark.
  2. **Pre-BERT baselines only.** The reported 72.3 ESIM accuracy is the 2018 state of the play; modern BERT/RoBERTa fine-tuned on MNLI reach mid-80s. Our use of off-the-shelf MNLI checkpoints will rely on these later results, not on the Williams et al. numbers themselves.
  3. **English-only.** Same scope critique as SNLI and LIAR.
  4. **Hypothesis-only artifacts.** Gururangan et al. 2018 / Poliak et al. 2018 (not in our reading list, contextual note from #17) showed MultiNLI also has hypothesis-only artifacts — though somewhat less severe than SNLI's. Parallel to the FEVER claim-only artifact Schuster 2019 (#24) flags. Carry to P10 setup, not P7.
  5. **No fact-verification baseline.** MultiNLI is general-domain NLI; it does not train models on the specific challenge of verifying retrieved evidence against a claim (FEVER's actual task). The transfer from MNLI labels (entailment / contradiction / neutral) to FEVER labels (Supported / Refuted / NEI) is approximate — same caveat as flagged in #16's NEI confusion. Important methodological note for the verification arm.
- **Cross-refs:**
  - #5 (Guo et al. 2022) — cites both Bowman 2015 and Williams 2018 when framing verification as RTE; lineage is field-standard.
  - #16 (Hanselowski) — uses ESIM, the same architecture Williams et al. evaluate. Hanselowski trains ESIM from scratch on FEVER; our planned pipeline swaps in an MNLI-pretrained transformer.
  - #17 (Bowman, SNLI) — direct predecessor. Cite together for the SNLI → MNLI scale-and-diversity lineage. Bowman's RTE-3 transfer failure (genre mismatch) is exactly what MNLI is designed to fix.
  - #24 (Schuster 2019) — MNLI's hypothesis-only artifacts mirror FEVER's claim-only artifacts; both feed into the P10 setup.

---

## Theme 8 — Verification Pipelines and Architectures

### 19. Nie, Chen & Bansal 2019 — Combining Fact Extraction and Verification with Neural Semantic Matching Networks (NSMN)

- **Venue:** AAAI 2019
- **Status:** ✅ Read
- **Big move:** Top-ranked FEVER 1.0 shared task system (UNC-NLP). Builds the canonical three-stage FEVER pipeline — document retrieval → sentence selection → claim verification — using a **single homogeneous neural architecture (NSMN)** at every stage. Sibling to Hanselowski #16; the architectural difference is that Hanselowski runs ESIM per (claim, evidence) pair and pools, while Nie concatenates all retrieved evidence into a single premise and runs one verification pass. Both achieve roughly the same top-3 leaderboard performance with different design philosophies.

- **NSMN architecture (4 layers, ESIM-derived):**
  1. **Encoding:** BiLSTM over GloVe + ELMo token embeddings.
  2. **Alignment:** soft attention matrix between the two sequences; each token gets an attended representation from the other side.
  3. **Matching:** BiLSTM over [encoded, aligned, difference, element-wise product] — plus a shortcut connection from the raw input to the matching layer (their modification over vanilla ESIM).
  4. **Output:** max-pool → affine layers. Different head shape per task — 2-way for retrieval ranking, 3-way for verification.
  - **Difference vs vanilla ESIM:** shortcut input→matching connection + simplified output layer. Ablation in Table 4 shows vNSMN beats vanilla ESIM by ~1 FEVER point (66.14 vs 65.07) — modest, architecture isn't the load-bearing contribution.

- **Three-stage pipeline:**
  1. **Document retrieval.** Keyword matching (constituency parse → NPs + named entities, MediaWiki API → titles) narrows the search space to ~8 candidate pages per claim. Non-"disambiguative" pages auto-included; "disambiguative" pages (~10% of dataset, titles like "Savages (band)") ranked by dNSMN over (claim, [title + first sentence]). Optionally augmented with Wikipedia Pageview frequency as a popularity prior.
  2. **Sentence selection.** sNSMN over (claim, candidate sentence) pairs from retrieved pages. Trained with **annealed negative sampling** — start at p_e=0.5 of including each negative, decrement 0.1 per epoch, reset to 0.02. Annealing trades precision for recall (F1 drops 74.33 → 51.38, recall jumps 79.98 → 86.79); the recall is what matters downstream.
  3. **Claim verification (vNSMN).** All retrieved evidence concatenated into one premise; claim is the hypothesis. **Three add-on token features stacked on GloVe + ELMo:**
     - **WordNet features (30-d):** 10 binary indicators × 3-element position encoding [in-evidence, in-claim, fired]. Indicators cover lemma match, antonymy, hypernymy/hyponymy at distances {0, 1, 2, >2} in the WordNet topological graph.
     - **Number embedding (5-d):** learned per-unique-number embedding — partial fix for the GloVe-numbers-not-distinguished failure that Hanselowski #16 explicitly flagged.
     - **Normalized semantic relatedness scores (2-d):** the p(x=1) values from the upstream dNSMN and sNSMN, broadcast to every evidence token. This is the "joint" part — verification sees retrieval's confidence.

- **Results on FEVER (Table 4 + Table 7):**
  - **Document retrieval (k=5):** KM alone OFEVER 88.86 → KM + dNSMN 92.34 → KM + Pageview + dNSMN 92.42. On the **difficult subset** (claims whose evidence is in a disambiguative document), dNSMN moves OFEVER from 60.15 (KM alone) to 87.93 — the semantic-matching step matters where keyword matching is ambiguous.
  - **Sentence selection (Table 3):** sNSMN with annealed sampling OFEVER 91.19 (vs 86.65 without annealing, 84.08 max-pool sentence encoder, 83.77 TF-IDF). The annealing trade is visible: recall 86.79, precision/F1 collapses to 36.49/51.38.
  - **Verification ablation (Table 4):** Final vNSMN FEVER 66.14, label accuracy 69.60 (S/R/NEI F1 = 75.7/69.4/63.3). Dropping WordNet+Number = −0.77 FEVER. Dropping sentence-level relatedness score = −1.24 FEVER (also drops NEI F1 from 63.3 to 60.7 — relatedness scores help the model recognize "evidence is weak" = NEI).
  - **Blind test (Table 7):** **UNC-NLP final 64.23 FEVER, label accuracy 68.16, evidence F1 52.81** — first place on the FEVER 1.0 leaderboard, just ahead of UCL/UKP-Athene (#16, 64.74 FEVER reported in Hanselowski's paper / 61.58 on this leaderboard table).

- **Why it matters for our paper:**
  - **Paragraph 8 S1 anchor.** This is the citation that lands the claim "the dominant FEVER architecture is a three-stage pipeline: document retrieval, sentence selection, then entailment-based verification." Nie's framing — three subtasks as one homogeneous semantic-matching problem — is the cleanest published statement of the canonical pipeline shape. Pair with Hanselowski #16 for redundancy of evidence but do NOT double-cite: progress_log split is firm. #16 = P7 NLI framing, #19 = P8 architecture.
  - **Reinforces the oracle-evidence methodology decision.** Nie's pipeline scores ~92 doc retrieval, ~91 sentence retrieval (OFEVER), but only 66 FEVER and 69 label accuracy — same multiplicative-degradation pattern as Hanselowski. Using oracle FEVER evidence for our verification arm continues to be justified: real pipelines lose most of their headroom at the entailment step, which is what we want to isolate. Either #16 or #19 can be the citation; #16 has cleaner numerical decomposition (93.55 × 87.10 × 68.49), use that.
  - **Direct number-handling precedent (small but worth flagging).** Nie's 5-d number embedding is one of the first published attempts to address the numerical-reasoning weakness Hanselowski #16 flagged. Doesn't change our methodology (we're using off-the-shelf MNLI, won't add custom features) but useful in Discussion / error analysis as "this is a known problem — published systems have tried specific embeddings to partly address it; we expect to inherit the failure."
  - **Optional Discussion point:** Nie shows the verifier benefits from seeing retrieval confidence scores (the 2-d relatedness feature). This is a small architectural commitment to joint training that our off-the-shelf pipeline gives up — flag in Limitations as a known way to do better that's out of scope.

- **Honest weakness:**
  1. **Pre-BERT (GloVe + ELMo).** Same era as Hanselowski; modern FEVER systems with fine-tuned RoBERTa/DeBERTa cross 80 FEVER score. Cite Nie for the architecture, not for SOTA.
  2. **NSMN ≈ ESIM + shortcut.** The architectural novelty is small (1 FEVER point). The paper's real contributions are (a) the unified three-stage framing and (b) the joint training via relatedness-score passing. Don't oversell the architecture in our Related Work.
  3. **Pageview is a popularity prior.** Combining Pageview with dNSMN gives the headline blind-test number, but Pageview is essentially "Wikipedia tells us what's famous" — extra-textual signal that doesn't generalize off-Wikipedia. Worth noting as why FEVER results don't transfer to real-world fact-checking (Augenstein #22 will carry this argument).
  4. **Verification reads concatenated evidence as a single premise.** Architecturally different from Hanselowski's per-pair-then-pool design. Neither is obviously better; the field hasn't settled. Worth a one-line acknowledgement in P8 that two designs exist.
  5. **Annealed sampling is a recall-tuning hack.** Effective but model-specific; doesn't speak to the underlying task. Skip in P8 unless we need to fill a sentence.
  6. **Inherits Hanselowski's NEI confusion.** Same 3-way label structure, same approximate NLI→FEVER mapping, same problem distinguishing "evidence absent" from "evidence refutes." Nie's relatedness-score feature _helps_ (NEI F1 drops 3 points without it) but doesn't solve. Confirms our error-analysis prediction.

- **Cross-refs:**
  - **#16 (Hanselowski).** Sibling top-3 FEVER system, same year, same task. **Architectural split:** Hanselowski = per-pair ESIM + claim-conditioned attention pool; Nie = concatenate-then-match. **Citation split in our paper:** #16 → P7 S1 (NLI framing of verification); #19 → P8 S1 (three-stage pipeline architecture). Both anchor different paragraphs; do not double-cite.
  - **#5 (Guo et al.).** Nie's three-stage pipeline is the worked example of Guo's claim-detection → evidence-retrieval → claim-verification framework. Different from Hanselowski only in which stage gets emphasized.
  - **#11 (Devlin/BERT).** Nie predates BERT's adoption in FEVER systems. The shortcut-connection + max-pool head Nie uses is one of the last competitive pre-BERT FEVER architectures.
  - **#17 (Bowman/SNLI), #18 (Williams/MNLI).** NSMN's verification head is "ESIM-style NLI applied to retrieved evidence." The lineage runs SNLI ESIM (#17 era) → MNLI ESIM (#18) → FEVER NSMN (#19) — same architectural family, three different tasks.
  - **#20 (Hassan/ClaimBuster).** Upstream of Nie's pipeline: Hassan does check-worthy claim detection (deciding _whether_ to verify); Nie assumes the claim is already given and handles retrieval + entailment. P8 S2 separation.
  - **#21 (Thorne/FEVER).** Nie's dataset; their 2-times-baseline framing is relative to Thorne's TF-IDF baseline.
  - **#24 (Schuster 2019).** Nie's vNSMN, like all FEVER systems of this era, was trained and evaluated on a dataset Schuster later shows has claim-only artifacts. Some of Nie's headline 64.23 FEVER score may be artifact-driven rather than reasoning-driven. Carry to P10.

### 20. Hassan et al. 2017 — Toward Automated Fact-Checking: Detecting Check-worthy Factual Claims by ClaimBuster

- **Venue:** KDD (Applied Data Science track)
- **Status:** ✅ Read
- **Big move:** First paper to formalize **check-worthy claim detection** as a supervised NLP task — a dedicated stage _upstream_ of evidence retrieval and verification, designed to decide _which_ sentences in a stream of discourse are worth fact-checking at all. Operationalizes stage 1 of Vlachos & Riedel's (#2) four-stage pipeline and the "claim detection" stage of Guo et al.'s (#5) three-stage framework as a concrete classifier with a released dataset, scoring API, and live deployment.
- **Task formulation (cite this):** 3-way sentence classification over US presidential debate transcripts.
  - **NFS (Non-Factual Sentence):** opinions, beliefs, declarations, most questions — no factual claim. (66% of dataset.)
  - **UFS (Unimportant Factual Sentence):** factual but the public wouldn't care to verify (e.g., "Next Tuesday is Election day"). (10%.)
  - **CFS (Check-worthy Factual Sentence):** factual + the public would want to know if it's true (e.g., "Over a million and a quarter Americans are HIV-positive"). (24%.)
  - Output is a probability score P(class=CFS|sentence) used as a ranking; the system delivers a priority list rather than a binary decision.
- **Dataset (released, valuable on its own):** 30 US presidential debate transcripts 1960–2012; 20,788 candidate-spoken sentences ≥ 5 words. Crowdsourced labels from 374 paid participants (mostly US-politics-aware students, professors, journalists — explicitly _not_ MTurk, after a CrowdFlower pilot gave poor quality). Quality control via 1,032 expert-labeled screening sentences mixed into each participant's stream at ~1-in-10 rate; participants with positive weighted error score (LQ_p ≤ 0) are flagged as "top-quality" (86 of 374). Stopping rule: a sentence is finalized once it has ≥ 2 top-quality labels and a majority. Final dataset: 76,552 labels (68% from top-quality participants) covering 20,617 sentences (99.17% of candidate sentences hit the stopping criterion). Experiments in the paper use an earlier 8,231-sentence slice (because dataset size showed diminishing returns past 4-8k for SVM — see Fig. 4).
- **Features (5 categories, 6,615 total):** sentiment score (AlchemyAPI, -1 to +1), length (word count), tf-idf over 6,549 stemmed tokens, 43 POS-tag counts (NLTK), 26 entity-type counts (AlchemyAPI). Random-forest GINI feature importance: top features are **VBD** (past-tense verb) and **CD** (cardinal number) — quietly aligned with Rashkin #9's finding that trusted news uses concrete figures, and confirming that numeric content is a strong claim-worthiness signal (45% of CFSs contain numbers vs 6% of NFSs).
- **Results:**
  - **3-way classification (4-fold CV, Table 2):** Best = SVM + words + POS + entity types. On the CFS class: **precision 0.72, recall 0.67, F1 0.70**. UFS is the hardest class (precision 0.43, recall 0.24) — unsurprising, since it sits between the other two. SVM beats NBC and RFC across feature combinations; RFC barely classifies anything as UFS (recall ≈ 0).
  - **Ranking accuracy (Table 3) against top-quality human coders:** **P@10 = 1.00, P@100 = 0.96, P@500 = 0.68**. Strong agreement at the top of the ranking — exactly the operating regime fact-checkers care about.
  - **Failed-hypothesis baseline:** Two off-the-shelf subjectivity classifiers (Riloff & Wiebe 2003/2005, via OpinionFinder) fail to filter NFS from {UFS, CFS}: 574 of 731 NFSs are labeled "objective"; 44 of 238 CFSs are labeled "subjective" (Tables 4, 5). **Check-worthiness is not the same as objectivity** — a dedicated supervised task is needed, not a repurposing of subjectivity tools.
  - **External validation against professional fact-checkers (Section 4, the load-bearing case-study finding):** Across all 21 2016 primary debate transcripts (30,737 sentences), ClaimBuster scores were compared to claims actually fact-checked by CNN (224 verdicts) and PolitiFact (118 verdicts).
    - CNN-checked sentences: **avg score 0.433** vs **0.258** for unchecked sentences (t = 21.1, p ≈ 1.8 × 10⁻⁹⁸).
    - PolitiFact-checked sentences: **avg score 0.438** vs **0.258** for unchecked (t = 16.4, p ≈ 6.3 × 10⁻⁶⁰).
    - This is the cleanest published evidence that automated check-worthiness scoring agrees with what professional fact-checkers actually choose to check — i.e., that a claim-selection stage is _learnable_ and not just a definitional convenience.
  - **Transfer beyond debates (Section 5, Twitter, Table 7):** Same model applied zero-shot to 1,000 political tweets: P@10 = 0.50, P@25 = 0.48, P@100 = 0.19, nDCG@100 = 0.81. Domain shift hurts precision sharply but the ranking is still meaningful — useful caveat for our limitations.
- **Why it matters for our paper:**
  - **Paragraph 8 S2 anchor.** This is the citation that lands the claim that an upstream stage — deciding _which_ sentences in a text are worth checking at all — is handled separately and _before_ the document retrieval / sentence selection / entailment cascade described in Nie #19 and Hanselowski #16. In Nie's framing of the FEVER pipeline, the claim is _given_; in real-world fact-checking, the claim has to be picked first, and Hassan's ClaimBuster is the canonical published system for that pick. P8 S2 should make this stage-zero-vs-three-stage relationship explicit.
  - **Sharpens the "verification is well-defined" framing.** Without Hassan, our verification arm reads as if claims arrive pre-packaged. With Hassan, we can be honest that real-world verification needs an extra upstream stage that we are _not_ studying — our project takes FEVER claims as given (they are already pre-selected by the FEVER annotators) and verifies them, which mirrors Nie/Hanselowski's experimental setup but not real-world deployment.
  - **Reinforces P6 → P8 architectural narrative.** Potthast et al. (#15) close their conclusion by recommending style-based detection as a **pre-filter directing human fact-checkers to articles worth checking**. Hassan operationalizes exactly that role — but with a model trained on what fact-checkers actually pick, not on stylistic hyperpartisanship. Worth a single-clause forward-reference in P6 S5 or a single-clause callback in P8 S2: "what Potthast et al. recommend as a role for style-based classifiers, Hassan et al. operationalize directly with a model trained on check-worthiness judgments."
  - **Useful in Discussion / error analysis later.** Hassan's top feature being CD (cardinal number) and 45% of CFSs containing numbers maps directly to our predicted numerical-reasoning failure mode in the verification arm (carried over from #16 + #19 notes). Check-worthy claims disproportionately contain numbers; pretrained NLI models handle numbers poorly. The same property that makes claims worth checking makes them hard to verify off the shelf.
- **Honest weakness:**
  1. **US-political-debate scope.** Single discourse type, single country, single 50-year window. The model and the dataset are both shaped to this domain; the Twitter zero-shot result (P@100 drops 0.96 → 0.19) makes the scope limit concrete.
  2. **CFS is defined by "the general public will be interested,"** which is a journalistic, not linguistic, criterion. The label is reasonable but inherently subjective — what's check-worthy in 2016 may not be in 2024, and "the public" is implicitly the US news-consuming public.
  3. **External validation has selection bias.** CNN and PolitiFact don't fact-check uniformly — they pick claims that are interesting, newsworthy, or politically charged. The 0.433-vs-0.258 score gap shows the system agrees with editorial selection, which is partly truth-tracking and partly attention-tracking. The paper acknowledges this implicitly when it notes a 9% topic mismatch on Social Issues between CNN/PolitiFact and ClaimBuster.
  4. **No transformer baseline.** SVM + tf-idf + POS + entity types is a 2017 classical pipeline; modern check-worthy claim detection (e.g., the CheckThat! shared tasks from 2018 onward) uses fine-tuned BERT and gets substantially better numbers. Hassan is the foundational citation, not the SOTA reference.
  5. **AlchemyAPI is defunct** (IBM shut it down in 2017). Reproducing the sentiment and entity-type features today requires substitutes (spaCy NER, VADER or transformer-based sentiment). Doesn't affect our use of the citation — we're not re-implementing the system.
  6. **UFS class is poorly modelled** (precision 0.43, recall 0.24). The 3-way distinction matters conceptually but the middle class is hard; in practice the system is mostly a binary CFS-vs-rest ranker.
- **Cross-refs:**
  - **#2 (Vlachos & Riedel 2014).** Hassan operationalizes V&R's stage 1 ("extract statements to be fact-checked"). The lineage is explicit — Hassan cites V&R in related work as the only prior attempt to analyze the tasks in fact-checking.
  - **#5 (Guo et al. 2022).** Hassan's check-worthiness detection IS Guo's "claim detection" stage. Guo cites the ClaimBuster line of work as the canonical example.
  - **#9 (Rashkin 2017).** Hassan's top-feature finding (CD / cardinal numbers, 45% of CFSs contain numbers) corroborates Rashkin's table-2 finding that trusted news uses concrete figures. Two independent signals that numeric content is a strong marker.
  - **#15 (Potthast 2018).** Potthast closes by recommending style-based detection as a pre-filter for fact-checkers; Hassan operationalizes exactly that role with a _non-style-based_ claim-worthiness model. Useful comparative framing for the P6 → P8 bridge.
  - **#16 (Hanselowski 2018), #19 (Nie 2019).** Both treat the claim as given and start their pipelines at document retrieval. Hassan supplies the implicit stage-zero. In our P8: Hassan = upstream selection, Nie = three-stage retrieval-and-verification cascade.
  - **#21 (Thorne 2018, FEVER).** FEVER assumes claims are pre-given (the annotators wrote them); this mirrors Hassan-style claim selection done by humans rather than a classifier. Our methodology will inherit this — flag in P8 S3 that FEVER's pre-selected-claims setup is also why our oracle-evidence design works.

## Theme 9 — Verification Benchmarks

### 21. Thorne et al. 2018 — FEVER: A Large-Scale Dataset for Fact Extraction and VERification

- **Venue:** NAACL-HLT
- **Status:** ✅ Read
- **Big move:** Releases FEVER, the first verification benchmark large enough to actually train modern data-intensive models (185,445 claims) — three orders of magnitude larger than Vlachos & Riedel #2's 106 claims and the Fake News Challenge's 300 claims. Pairs each claim with sentence-level Wikipedia evidence and a 3-way label (SUPPORTED / REFUTED / NOTENOUGHINFO), turning verification from a task definition (#2) into a learnable problem with held-out evaluation. Becomes the canonical verification benchmark every subsequent system in our reading list (#16, #19) is built on.

- **Dataset construction (two-stage annotation, cite this for design quality):**
  1. **Claim generation.** Annotators given a sentence sampled from ~50,000 popular Wikipedia pages (June 2017 dump, processed with Stanford CoreNLP) and asked to extract a single-fact claim. Given a **dictionary** of hyperlinked entities + their first-sentence Wikipedia summaries, allowing controlled complexity beyond pure paraphrase but bounded so claims remain Wikipedia-verifiable. Annotators then generate **mutations** along six axes from Natural Logic Inference (Angeli & Manning 2014): paraphrase, negation, substitution with similar/dissimilar entity/relation, generalisation, specification. Interface explicitly discourages trivial "not" insertions and shows all mutation types simultaneously. Mean claim length 9.4 tokens (comparable to SNLI hypotheses at 8.3, per Bowman #17).
  2. **Claim labeling.** A separate set of annotators — crucially, **aware of the originating page but not the originating sentence** — label each claim SUPPORTED / REFUTED / NOTENOUGHINFO and select the supporting evidence sentences. Default evidence pool is the introductory section of the main entity's page plus every linked entity's page; annotators can also add arbitrary Wikipedia pages via URL. NEI is reserved for claims that can be neither supported nor refuted from any Wikipedia content.

- **Dataset statistics (Table 1):** Train 145,449 (S 80,035 / R 29,775 / NEI 35,639 — **note the training-set class imbalance**); dev 9,999 (balanced 3,333 each); test 9,999 (balanced 3,333 each); reserved 19,998 (balanced 6,666 each). Total 185,445. **31.75% of claims have multiple valid evidence sets**; **16.82% require composition of evidence from multiple sentences**; **12.15% require evidence from multiple Wikipedia pages.** Multi-hop reasoning is built into the benchmark, not optional.

- **Annotation quality (the trustworthiness case):**
  - **5-way inter-annotator agreement** on 4% (n=7,506) of claims: **Fleiss κ = 0.6841** for the 3-way label — Thorne argues this compares favorably to Bowman #17's κ = 0.7 on the easier SNLI task (premise given, no evidence retrieval needed).
  - **Super-annotator agreement** (1% of data re-annotated by experts with no time limit, searching over all Wikipedia): regular annotations achieve **95.42% precision** but only **72.36% recall** on evidence selection. The recall gap is mostly long-tail listings (e.g., the Akshay Kumar filmography example, where the super-annotator listed 34 valid evidence sentences). **This is the main reason FEVER evaluation penalizes precision but allows multiple valid evidence sets.**
  - **Author validation** on 227 claims: 91.2% correctly annotated; of incorrect cases, most are evidence-coverage rather than label errors (only 4 of 227 had wrong labels per guidelines).

- **Baseline pipeline (three stages — direct ancestor of Hanselowski #16 and Nie #19):**
  1. **Document retrieval:** DrQA (Chen et al. 2017) — binned unigram + bigram TF-IDF cosine, k nearest documents.
  2. **Sentence selection:** Top-l sentences ranked by TF-IDF similarity to the claim (DrQA modified, or NLTK unigram TF-IDF).
  3. **RTE:** Two models compared — MLP (Riedel et al. 2017's Fake News Challenge submission, term frequencies + TF-IDF cosine features) and Decomposable Attention (Parikh et al. 2016, SOTA on SNLI at the time, no parsing required). NEI training problem solved by sampling negatives via NEARESTP (sentence from highest-ranked retrieved page) or RANDOMS (uniform random Wikipedia sentence).

- **Headline results — the load-bearing numbers (Tables 2, 3, 4):**
  - **Document retrieval (Table 2):** With k=5, **55.30% of evidence is recoverable** (excluding NEI); oracle accuracy 70.20%. With k=100, fully-supported rate rises to 86.59%, oracle accuracy 91.06%. The plateau is at k=50.
  - **After sentence selection at l=5:** Fully-supported rate **drops to 44.22% with DrQA, 34.03% with NLTK** — sentence selection discards correct evidence. Oracle accuracies fall correspondingly to 62.81% and 56.02%.
  - **Oracle entailment (Table 3, gold evidence, dev set):** DA + NEARESTP **80.82%**, DA + RANDOMS **88.00%**, MLP + NEARESTP 65.13%, MLP + RANDOMS 73.81%. **The pretrained SNLI model (zero-shot) collapses to 38.54%** — direct empirical demonstration that SNLI's image-caption training doesn't transfer to Wikipedia-grounded verification, which is exactly the gap MNLI (#18) was built to close.
  - **Full pipeline (Table 4, dev set):** Best is DA + NEARESTP at **52.09% NoScoreEv / 32.57% ScoreEv** — i.e., ~52% if you ignore the evidence-correctness requirement, ~33% if you enforce it.
  - **Test set (the headline number, Section 5.7):** **31.87% with evidence; 50.91% without.** Evidence retrieval (combined document + sentence retrieval) on test set: recall 45.89%, precision 10.79%, **F1 = 17.47%.**

- **The oracle-vs-pipeline gap is the load-bearing finding for our methodology:** DA with gold evidence reaches 80.82% (NEARESTP) on dev; the same model in the full pipeline drops to 52.09% NoScoreEv. **The ~30-point gap between oracle-evidence and full-pipeline performance is retrieval cost, not entailment cost.** This is the single cleanest published argument for our oracle-evidence design choice — directly parallel to (and stronger than) the Hanselowski #16 multiplicative decomposition (93.55 × 87.10 × 68.49 → 64.74) and the Nie #19 stage-level scores (dNSMN 92.34, sNSMN 91.19, vNSMN 66.14). Three independent FEVER systems converge on the same finding: retrieval is what eats the headroom.

- **Manual error analysis (Section 5.8, useful for our Discussion):** Of 961 incorrect predictions on the test set, **58.27% (n=560) were retrieval failures** — the pipeline failed to identify any correct evidence. Where suitable evidence was retrieved, RTE misclassified only **13.84% (n=133)**. Restated: **even on a relatively weak 2018 pipeline, when evidence retrieval succeeds, entailment classification is the smaller problem.** Reinforces the oracle-evidence design.

- **NEI training is non-trivial (Section 4, methodological note):** Because NEI-labeled claims have no annotated evidence, training requires synthesizing negative examples. RANDOMS (uniform Wikipedia sentence) yields semantically unrelated negatives that inflate oracle accuracy (88.00% DA) but harm pipeline NEI recall (the model misclassifies related-but-uninformative retrieved evidence as SUPPORTED/REFUTED). NEARESTP (sentence from highest-ranked retrieved page) yields more realistic negatives, lower oracle accuracy (80.82% DA), but better pipeline behavior. This is the same NEI difficulty Hanselowski #16 and Nie #19 both report — Thorne is where it's first measured.

- **Why it matters for our paper:**
  - **Paragraph 9 S1 anchor.** The citation that lands "FEVER provides ~185k claims against Wikipedia evidence with three-way labels (SUPPORTED / REFUTED / NEI)." Plus the specific figures we'll use: 185,445 claims, three balanced 9,999-claim eval sets, Fleiss κ = 0.6841.
  - **Reinforces P8 S3 (oracle-evidence bridge — still pending).** Thorne's own oracle vs. full-pipeline gap (80.82% vs. 52.09% DA on dev; 88.00% oracle accuracy on RANDOMS) is the most direct empirical argument for treating retrieval as solved when studying verification reasoning. Use Hanselowski #16's multiplicative decomposition as the primary citation for P8 S3 (we already decided this) but **mention Thorne's oracle results as corroborating evidence** in a sub-clause.
  - **Foreshadows P10 (claim-only artifacts, Schuster #24).** Thorne's annotation protocol — claim generation by mutating Wikipedia sentences, with labelers aware of the originating page — is exactly the protocol Schuster 2019 (#24) later shows leaves systematic claim-only artifacts. Don't preempt P10 in our writing of P9; just note the connection.
  - **Justifies the binary-collapse decision (P5 S3, already filled).** FEVER's three-way labels (S/R/NEI) are at the same structural level as LIAR's binary collapse — both reduce graded truthfulness to a small label set. Our cross-paradigm comparison uses LIAR's binary split for detection and FEVER's S/R subset (dropping NEI) for verification to maintain comparability. Flag in Methodology.

- **Honest weakness / scope of the claim:**
  1. **Wikipedia-as-truth is a strong simplification.** Claims that depend on time-varying facts (population counts, current officeholders) or on common-sense world knowledge not present in Wikipedia introduce label noise. Thorne explicitly acknowledges this (Section 6, "we do not consider Wikipedia to be the only source of information worth considering in verification, hence not using TRUE or FALSE in our classification scheme"). MultiFC (#22) is the contrast point — real-world claims with messier evidence sources.
  2. **Claim generation is artificial.** Mutating Wikipedia sentences produces claims that — by construction — are likely either supported by their source page (paraphrase, generalisation/specification) or refuted by it (negation, substitution). This is the structural reason claim-only artifacts exist (Schuster 2019 / #24 forthcoming): annotators are working in a small mutation space and develop predictable patterns, which a model can pick up from the claim alone.
  3. **NEI is the hardest class to annotate and train.** Thorne's NEI claims have no evidence (by definition); the synthetic-negative methods (NEARESTP, RANDOMS) are workarounds, not solutions. Both Hanselowski #16 and Nie #19 report NEI as the weakest verdict class. Our verification arm will inherit this — flag in Limitations as "FEVER's NEI category does not cleanly map to MNLI's 'neutral' label, and pipeline systems and off-the-shelf NLI models both underperform on it."
  4. **Multi-hop reasoning (16.82% of claims) is the long tail.** Most pipeline systems (including ours) concatenate retrieved evidence and run single-pass entailment; this works for single-sentence-evidence claims but not for multi-hop ones. Hanselowski #16's claim-conditioned pooling is a partial fix; Nie #19's concatenation is not. Worth noting in Discussion if our error analysis shows multi-hop failures.
  5. **Single Wikipedia snapshot (June 2017).** Reproducibility issue for retrieval but not for our oracle-evidence setup since the HuggingFace `fever` dataset bundles the corresponding evidence sentences. Doesn't affect our use.
  6. **English-only.** Same scope critique as every other dataset in our reading list (LIAR #13, SNLI #17, MNLI #18, Potthast #15).
  7. **Test-set blind in original release; HuggingFace `fever` exposes dev only.** Our verification experiments will report dev-set numbers — fine for our comparative analysis, but worth flagging that the original Thorne et al. headline (31.87% / 50.91%) is the **test** set, not directly comparable to dev numbers.

- **Cross-refs:**
  - **#2 (Vlachos & Riedel 2014).** FEVER is the dataset-scale answer to V&R's 106-statement task definition. The Vlachos pipeline (extract → question → retrieve → verdict) is operationalized in FEVER's three-stage baseline (retrieval → selection → RTE). Direct lineage.
  - **#5 (Guo et al. 2022).** FEVER is the worked example of Guo's three-stage automated fact-checking framework. Their "claim detection" stage is implicit in FEVER (annotators wrote the claims); evidence retrieval and claim verification are the FEVER pipeline.
  - **#16 (Hanselowski 2018).** Uses FEVER directly. Hanselowski's 93.55 / 87.10 / 68.49 stage scores correspond to Thorne's 70.20 / 62.81 / oracle accuracy at k=5 — Hanselowski's pipeline is the substantially-improved successor.
  - **#17 (Bowman/SNLI), #18 (Williams/MNLI).** Thorne's Table 3 shows the pretrained SNLI DA model at 38.54% on FEVER oracle — direct empirical demonstration that SNLI alone doesn't transfer. Strengthens our P7 S3 case for MNLI as the appropriate training corpus.
  - **#19 (Nie 2019).** Uses FEVER directly; his 64.23 blind-test FEVER score is the next year's leaderboard improvement over Thorne's 31.87% baseline.
  - **#20 (Hassan/ClaimBuster).** Thorne's annotators do claim generation (writing claims from Wikipedia sentences) rather than claim selection (picking sentences worth checking). FEVER's stage-zero is humans-as-claim-writers, the upstream analogue Hassan would automate.
  - **#22 (Augenstein/MultiFC).** The external-validity contrast — Wikipedia-grounded FEVER vs. real-world fact-checking-site claims. P9 S2 anchor when we get there.
  - **#23 (Wadden/SciFact).** The domain-specific contrast — Wikipedia general-domain FEVER vs. scientific-abstract SciFact. P9 S3 anchor when we get there.
  - **#24 (Schuster 2019).** Directly examines FEVER's claim-only artifacts. The mutation-based claim generation protocol Thorne describes in Section 3.1 is what Schuster shows leaves exploitable patterns. P10 setup.
  - **#25 (Thorne 2019).** Same author; adversarial follow-up to this paper. P10 anchor.

---

### 22. Augenstein et al. 2019 — MultiFC: A Real-World Multi-Domain Dataset for Evidence-Based Fact Checking

- **Venue:** EMNLP-IJCNLP 2019
- **Status:** ✅ Read
- **Big move:** Releases the largest dataset of **naturally occurring** claims for evidence-based verification — 34,918 claims crawled from **26 English fact-checking websites** (PolitiFact, Snopes, FactCheck.org, AfricaCheck, etc.), each paired with **rich metadata** (speaker, checker, topic tags, claim/publish dates, linked Wikipedia entities) and **10 evidence pages** retrieved via Google Search. This is the deliberate external-validity counter to FEVER (#21): instead of Wikipedia-sentence-mutation claims with curated evidence, MultiFC has actual public claims fact-checked by journalists, with evidence that is whatever the web returns.

- **Dataset construction (Section 3):**
  1. **Source selection.** Crawled all 38 active English fact-checking sites listed by Duke Reporters' Lab and Wikipedia; 10 unusable (no labels, no crawl pattern, encoding issues — Table 9), 28 usable, of which 26 were retained after removing duplicates and labels appearing fewer than 5 times. Each website becomes a **domain**; each is treated as its own task in MTL.
  2. **Evidence retrieval.** Claim text submitted verbatim (without quotes) to Google Search API; top 10 results saved per claim — title, rank, URL, timestamp, snippet, full HTML. Most frequent URL domains: Wikipedia 4.4%, Snopes 4.0%, Washington Post 3.0%, NY Times 2.5% (Table 3) — i.e., authoritative sites dominate but the long tail is heterogeneous and noisy.
  3. **Entity linking.** All claims passed through Kolitsas et al. 2018 neural entity linker; 25,763 entity mentions linked to Wikipedia in 42% of claims. Top entities US-political (Table 4: United States 2810, Obama 1598, Texas 665, Trump 556) — confirming US-centric skew typical of English FC sites.

- **Dataset statistics (the load-bearing numbers):**
  - **34,918 claims** total, split 80/10/10 train/dev/test, **label-stratified per domain**.
  - **165 unique labels** across all domains. Number of labels per domain ranges **from 2 to 27** (Table 6): bove and ranz have 2 (fact/fiction); tron has 27 (fiction!, truth!, unproven!, mostly truth!, satire!, scam!, ...); snes has 12; pomt (PolitiFact statements) has 9 (the canonical Truth-O-Meter scale). **No mapping onto a unified veracity scale is attempted** — instead, each domain is treated as its own task.
  - Domain sizes vary by ~3 orders of magnitude: pomt 15,390 → snes 6,455 → tron 3,423 → goop 2,943 → ... → fani 20, ranz 21. This is unbalanced multi-task learning by construction.

- **Models (Section 4, all BiLSTM-based, pre-BERT):**
  - **Base architecture:** MTL with Label Embedding Layer (LEL) from Augenstein et al. 2018 — each domain is a task with its own softmax mask, but labels from all domains are projected into a **shared label embedding space**, letting the model learn semantic relationships between labels like "mostly true" (pomt) ≈ "mostly correct" (afck) without manual mapping. This handles the 165-label-space heterogeneity end-to-end.
  - **Claim-only baselines:** `claim-only` (BiLSTM over claim text); `claim-only_embavg` (mean-pooled word embeddings).
  - **Claim + evidence:** `crawled_docavg` (mean-pool BiLSTM embeddings of all 10 evidence snippets, concatenate with claim); `crawled_ranked` (their proposed model — see below).
  - **Joint evidence ranking + verdict (Section 4.2, the novel contribution).** Each evidence snippet is jointly encoded with the claim using the Mou et al. 2016 matching-feature concatenation `[h_a; h_e; h_a−h_e; h_a·h_e]`. These 10 claim-evidence pair encodings are passed through a fully connected layer to produce a 10-d **soft ranking** of evidence utility. Final prediction = dot product of label-compatibility scores with the ranking weights, so the model learns end-to-end which evidence pages matter for verdict — **without any direct supervision on evidence relevance** (labels exist only for verdict). This is the methodological novelty: a learned attention-over-evidence trained purely from veracity labels.
  - **Metadata encoding (Section 4.3):** Speaker, category, topic tags, linked entities encoded as one-hot, passed through a CNN + max-pool, concatenated with the instance representation. Reason and checker excluded (reason leaks the label; checker too sparse).

- **Headline results (Tables 5, 6, 7, 8 — the load-bearing numbers):**
  - **Best model `crawled_ranked + meta`: Macro F1 = 49.2%, Micro F1 = 62.5%** averaged across 26 domains.
  - **Evidence helps a lot.** `claim-only` Macro F1 = 25.3% → `crawled_ranked` Macro F1 = 44.1% (an 18.8-point gap from adding evidence). `crawled_ranked` also beats `crawled_docavg` Macro F1 = 24.8% by 19.3 points, showing the **learned ranking** matters more than the mere presence of evidence.
  - **Metadata helps a bit.** `crawled_ranked` Macro 44.1% → `crawled_ranked + meta` Macro 49.2% (+5.1 points). Ablation (Table 7): topic tags alone contribute most; metadata hurts on domains where it's missing — suggests an ensemble.
  - **MTL with LEL beats single-task (Table 8):** STL Macro 38.8 → MTL Macro 44.8 → MTL + LEL Macro 49.2.
  - **Per-domain variance is enormous (Table 6).** Some small domains hit 100% Micro/Macro F1 (ranz, bove, fani, thal, huca) — the verdict leaks into the claim phrasing. Domains with many labels collapse: tron (27 labels) Macro F1 = 4.6%, snes (12 labels) Macro 9.7%, farg (11 labels) Macro 14.0%, pomt (9 labels) Macro 27.6%. **The most realistic domains are the hardest.**

- **Error analysis (Section 6) — useful for our Discussion:**
  - Confusion matrix on pomt (Figure 3): model confuses adjacent labels along the truth scale (half-true ↔ mostly true, mostly false ↔ false). Asymmetry: "true" claims are harder to identify than "false" claims.
  - **Longer claims are harder to classify.** Claims with high direct token overlap with evidence get higher evidence ranks (i.e., the ranker leans on lexical overlap).
  - **Tag-correlation effect:** generic tags like "government-and-politics" or "tax" co-occur with wrong predictions; specific tags ("hong-kong", "brisbane-4000") co-occur with correct ones. The model succeeds when "specific topics co-occur with certain veracities" — i.e., it learns topic-veracity priors, not pure verification reasoning. **This is the real-world analogue of FEVER's claim-only artifacts (Schuster #24).**

- **Why it matters for our paper:**
  - **Paragraph 9 S2 anchor.** The citation that lands "Real-world claims drawn from fact-checking sites are noisier and harder than FEVER's controlled, Wikipedia-grounded ones." Specific figures we'll use: 34,918 claims from 26 sites, 2–40 labels per domain, best Macro F1 only **49.2%** with evidence + metadata — compared to FEVER's three-way 64-68% (Nie #19, Hanselowski #16). The gap is the external-validity tax.
  - **Companion to Thorne #21 (P9 S1).** Direct paired contrast: Thorne's Wikipedia-mutation claims with curated single-source evidence vs. Augenstein's real journalistic claims with Google-snippet evidence. P9 S2 should explicitly position MultiFC as the external-validity foil, not just as another benchmark.
  - **Strengthens the Limitations section.** Our oracle-evidence + FEVER design choice (P8 S3) abstracts away two real-world difficulties: (a) evidence retrieval from heterogeneous web sources, (b) label-space heterogeneity (165 labels, no unified scale). Augenstein's 49.2% is the empirical reminder that "verification works" is an in-distribution claim, not a domain-general one.
  - **Foreshadows the topic-prior failure mode.** Their error analysis (specific tags → correct predictions, generic tags → errors) is the real-world version of the artifact problem Schuster #24 documents for FEVER. We can cite this in Discussion as "even with evidence, models lean on topic-veracity priors when evidence is ambiguous" — same failure pattern, different dataset.
  - **NOT a Methodology citation.** MultiFC is too big, too messy, and too multi-label for our Colab-scale comparative experiments. We're not running on it. It's purely a Related Work / Limitations citation.

- **Honest weakness / scope of the claim:**
  1. **Pre-BERT architectures.** All baselines are BiLSTM with randomly initialised embeddings; authors explicitly note ELMo/BERT/ULMFit would offer "complementary performance gains." The 49.2% Macro F1 is a 2019 floor, not a ceiling. Modern models would do better — but the gap relative to FEVER would likely persist.
  2. **Macro F1 across domains with 2–40 labels is barely interpretable.** A model getting 100% on a 2-label domain (ranz, bove) and 5% on a 27-label domain (tron) averages to a middling number that masks both successes and catastrophes. The per-domain Table 6 numbers are more honest than the headline 49.2%.
  3. **Google Search evidence is non-reproducible.** Search results change over time; authors acknowledge "studying temporal effects is outside the scope." Anyone running the dataset post-2019 gets different evidence pages — this is exactly the "noisier real-world evidence" property that makes MultiFC interesting, but it's also a reproducibility problem we wouldn't want to inherit.
  4. **US-centric.** Top entities are overwhelmingly US-political (United States, Obama, Trump, Republican/Democratic parties, US states). Even though 26 sites are crawled, English FC infrastructure is US-skewed. Same critique applies to LIAR #13.
  5. **Verdict-leakage in some domains.** The 100% Micro/Macro F1 on ranz/bove/fani/thal/huca is because "the verdict is often already revealed as part of the claim using explicit wording" — i.e., the claim text contains the answer. This is a data-quality issue specific to certain FC sites and not a general property of real-world claims.
  6. **No NEI-equivalent class.** Unlike FEVER's three-way S/R/NEI, MultiFC's labels are domain-specific verdicts; "unverified" exists in some domains but not others. Doesn't matter for our use (we cite, don't experiment), but worth knowing.

- **Cross-refs:**
  - **#21 (Thorne/FEVER).** Direct contrast. FEVER = 185k synthetic Wikipedia claims, curated evidence, ~65% three-way accuracy; MultiFC = 35k real claims, web evidence, **49.2%** macro F1. Together they bound the verification problem: clean Wikipedia floor (FEVER) vs. messy real-world ceiling (MultiFC). P9 S1 + S2 pair.
  - **#13 (Wang/LIAR).** Wang's PolitiFact-only dataset (12,836 claims, 6-way) is essentially **one domain (pomt)** of MultiFC. Augenstein's pomt at 9 labels and 15,390 claims is the slightly-expanded, multi-domain-trained version of Wang's setup. Direct lineage.
  - **#2 (Vlachos & Riedel 2014).** Their 106-statement seed dataset comes from PolitiFact + Channel 4 News — Augenstein scales the same idea to 35k claims and 26 sites.
  - **#19 (Nie 2019), #16 (Hanselowski 2018).** FEVER-system FEVER scores (Nie 64.23 blind test, Hanselowski 64.74 full pipeline) vs. MultiFC's 49.2 best Macro F1 — different metrics, different tasks, but the rough difficulty gap (~15 points) is real and load-bearing for our P9 framing.
  - **#24 (Schuster 2019).** MultiFC's tag-correlation error pattern (generic tags → wrong, specific tags → right) is the real-world analogue of FEVER's claim-only artifacts. Both papers say: models learn shortcuts. P10 echo.
  - **#5 (Guo 2022).** MultiFC is one of the example real-world verification benchmarks Guo's survey covers; useful cross-ref in P9 stitching.

---

### 23. Wadden et al. 2020 — Fact or Fiction: Verifying Scientific Claims (SciFact)

- **Venue:** EMNLP 2020
- **Status:** ✅ Read
- **Big move:** Releases **SciFact**, a small but high-quality expert-annotated dataset for **scientific claim verification** — 1,409 atomic scientific claims verified against a curated corpus of 5,183 biomedical abstracts, with three-way labels (SUPPORTS / REFUTES / NOINFO) and sentence-level **rationales** for each supports/refutes pair. Positioned as the **scientific-domain counterpart to FEVER #21**: same claim-evidence-verdict shape, but the evidence is research abstracts (not Wikipedia) and the labels require domain expertise (not crowd workers). Three orders of magnitude smaller than FEVER by design — expert biomedical annotation does not scale.

- **Dataset construction (Section 3) — three structural choices that matter:**
  1. **Claims are derived from citances (citation sentences), not invented.** Annotators see a sentence in a paper that cites another paper, and re-write it into up to three atomic claims about a single scientific finding (e.g., the citance "IL-6 signaling plays a major role in atherosclerotic CVD" becomes the claim "IL-6 signaling plays a major role in atherosclerotic cardiovascular disease"). This is the **structural opposite of FEVER's mutation-based generation** (#21 → #24 artifacts): claims are _naturally occurring_, taken from things scientists actually wrote, while the cited abstract is the obvious place to look for evidence.
  2. **Annotators don't see the cited abstract while writing claims.** This guarantees claims aren't paraphrases of the evidence — a baked-in defence against the lexical-overlap shortcut.
  3. **REFUTES claims are hand-negated by an NLP expert.** Without obvious cues like "not." Mostly direction reversal (e.g., "protects against severe anemia" → "raises vulnerability to severe anemia"). Their claim-only baseline at **44.5% accuracy** (Table 3) — barely above the 33% three-class chance floor — empirically validates that this negation procedure didn't seed obvious artifacts. **Contrast with FEVER, where the equivalent claim-only baseline reaches ~60% (Schuster #24).**

- **Dataset statistics (load-bearing for our citation):**
  - **1,409 claims** total: train 809 (S 332 / NEI 304 / R 173), dev 300, test 300 — dev/test fully balanced 1:1:1 across S/NEI/R. (Compare FEVER's 145k train / 9,999 balanced dev/test.)
  - **5,183 abstracts** in the corpus: 601 seed abstracts (from journals like Cell, Nature, JAMA, BMJ, NEJM — ten citations minimum), 140 co-cited, 4,259 distractor (added to make retrieval harder without false negatives — distractors are abstracts the citance authors knew about but didn't cite).
  - Annotation quality: **Cohen's κ = 0.75** label agreement, **κ = 0.71** rationale-sentence agreement — comparable to FEVER's 0.68 Fleiss κ (#21) and UKP Snopes's 0.70 (#16).
  - **63% of cited abstracts contain evidence** (annotators found evidence; rest are NEI). Rationales are short: 1542 single-sentence rationales, 92 two-sentence, 11 three-sentence.

- **Task formulation (Section 4) — two settings, four metrics:**
  - **Open setting:** model must retrieve evidence abstracts from the full 5,183-abstract corpus, then select rationales, then label.
  - **Oracle-abstract setting:** gold evidence abstracts provided; model still does rationale selection + labelling.
  - **Oracle-rationale setting** (sanity check): gold abstract AND gold rationale provided; model only labels.
  - **Metrics:** Abstract-level Label-Only F1, Abstract-level Label+Rationale F1 (rationale must contain a gold rationale), Sentence-level Selection-Only F1, Sentence-level Selection+Label F1. **The Label+Rationale metric is the strict one** — analogous to FEVER score.

- **Baseline VERISCI (Section 5) — structurally identical to Nie's #19 NSMN three-stage pipeline:**
  1. **ABSTRACTRETRIEVAL:** TF-IDF (unigram+bigram) over the claim, top **k=3** abstracts.
  2. **RATIONALESELECTION:** BERT-style encoder on `[sentence_i; SEP; claim]`, sigmoid score per sentence, threshold tuned on dev set.
  3. **LABELPREDICTION:** Same encoder on `[selected_rationales; SEP; claim]`, 3-way softmax (S/R/NEI). NEI predicted if no rationales selected.
  - **Best encoder configuration:** RoBERTa-large for both selector and predictor. Predictor pretrained on FEVER (~145k claims) **then fine-tuned** on SciFact (~800 claims) — the FEVER→SciFact transfer adds ~6 points label accuracy (75.7 → 81.9 on dev, Table 3). Selector trained on SciFact alone (FEVER pretraining hurts here — science-specific vocabulary).

- **Headline results (Table 4 — load-bearing numbers):**
  - **Oracle-rationale (just label): 83.3 F1** Label+Rationale. The ceiling when retrieval and rationale selection are perfect.
  - **Oracle-abstract (gold abstract, model selects rationale + labels): 72.7 F1** Label+Rationale, 74.7 Label-Only.
  - **Open (full pipeline): 46.5 F1** Label+Rationale, 47.4 Label-Only.
  - **The retrieval-vs-reasoning gap: 46.5 → 72.7 → 83.3** — same shape as FEVER (Hanselowski full pipeline 64.74, Nie blind test 64.23, Thorne DA oracle 80.82). **Independent corroboration on a completely different corpus** that most headroom is lost in retrieval/selection, not in reasoning over correct evidence.
  - **FEVER pretraining helps the label predictor** (81.9 vs 75.7 dev accuracy) — out-of-domain entailment pretraining transfers, even from political news to biomedicine. Useful precedent for our off-the-shelf MNLI choice.
  - **Zero-shot FEVER→SciFact: 51.8 F1 Label+Rationale oracle-abstract** (vs SciFact-trained 72.7) — FEVER alone is _not_ enough, but is a strong starting point.
  - **Claim-only baseline: 44.5% label accuracy** (3-way; chance = 33%) — much weaker than the analogous FEVER claim-only baseline (Schuster #24 will document ~60%). The citance-based + hand-negated construction successfully resists shortcut learning.

- **Error analysis (Section 6.4, Table 5) — five capabilities needed for scientific verification:**
  1. **Science background** (Drosophila = fruit fly; troponin = cardiac marker).
  2. **Directionality** (increase vs decrease — same property that flips REFUTE↔SUPPORT).
  3. **Numerical reasoning** (hazard ratios with confidence intervals, p-values, effect sizes).
  4. **Cause and effect** (knocking out a gene → counterfactual about its function).
  5. **Coreference** (resolving "the intervention group" to "the low-fat diet group" stated elsewhere in the abstract).
  - **Directionality and numerical reasoning are the same compound failure modes already flagged across #9 / #16 / #19 / #20 in our progress log** — SciFact provides a third independent corpus showing the same pattern.

- **COVID-19 case study (Section 6.3) — vibe-check, not clinical evaluation:**
  - 36 COVID-related claims hand-written by a medical student; VERISCI ran against CORD-19 corpus.
  - **23 / 36 claims judged "plausible"** by the same annotator (≥half retrieved abstracts had reasonable rationales+labels).
  - Authors **explicitly warn:** "we emphasize that our model is a research prototype and should not be used to make any medical decisions whatsoever" (footnote 1).
  - For our paper this is a useful "verification has real-world relevance" anchor without overclaiming.

- **Why it matters for our paper:**
  - **Paragraph 9 S3 anchor.** The citation that lands "Domain-specific verification — e.g., scientific claims with abstract evidence — introduces additional challenges." Specific figures: 1,409 expert-annotated claims, 5,183-abstract corpus, **VERISCI 46.5% F1 open vs 72.7% F1 oracle-abstract** — the same retrieval-vs-reasoning gap as FEVER, on a corpus that requires domain expertise no transformer was pretrained for. Pairs with #21 (Wikipedia/common knowledge) and #22 (journalistic web evidence) to triangulate the **three axes of verification difficulty: claim source, evidence source, knowledge required**.
  - **Independent corroboration of oracle-evidence methodology (P8 S3).** SciFact's 46.5 → 72.7 → 83.3 cascade is a third independent confirmation (after Hanselowski #16's 64.74 full pipeline / 93.55 × 87.10 × 68.49 decomposition and Thorne #21's 80.82% DA oracle / 52.09% NoScoreEv pipeline) that **retrieval, not entailment, eats most of the headroom**. Different corpus (biomedicine), different model (RoBERTa-large vs ESIM vs Decomposable Attention), same pattern. Robustness check.
  - **Precedent for FEVER pretraining + in-domain fine-tuning.** Wadden's label predictor gains ~6 points from FEVER pretraining. Our off-the-shelf MNLI choice (no FEVER fine-tune) is a weaker version of the same idea — generic entailment capability transfers, but in-domain training would beat us. **Useful Limitations framing:** "we do not fine-tune; Wadden et al. show that even small in-domain fine-tuning sets (~800 SciFact claims) substantially improve over FEVER-pretrained baselines."
  - **Error-type taxonomy for our Discussion.** Table 5's five failure types (background / direction / number / cause / coreference) overlap heavily with the failure modes already collected in our carry-forward caveats (numerical reasoning #9+#16+#19+#20, directionality #16). SciFact contributes **coreference** and **cause-and-effect** as new failure types we haven't yet anchored. Useful for the Discussion error-categorisation section.
  - **NOT a Methodology dataset for us.** SciFact requires biomedical expertise we don't have for error analysis, and the corpus is small enough that off-the-shelf MNLI without fine-tuning will likely underperform meaningfully. We cite it; we don't run on it. (Same posture as MultiFC #22.)

- **Honest weakness / scope of the claim:**
  1. **Small.** 1,409 claims, 800-claim train set. The authors acknowledge SciFact is "comparable in size to recent scientific datasets" (PubMedQA: 1k; SciERC: 500 abstracts) — but three orders of magnitude smaller than FEVER. Generalisation claims should be cautious.
  2. **Biomedicine-only.** Source journals are biomedical (Cell, Nature, JAMA, BMJ, NEJM). No physics, chemistry, social science, computer science. "Scientific verification" claims should really read "biomedical verification" in our wording.
  3. **Evidence is abstracts, not full papers.** Authors chose abstracts for annotation scalability + inter-annotator agreement. ~37% of cited abstracts are NEI (evidence isn't actually in the abstract — it's in the full paper). This is a known dataset limitation, acknowledged in Section 7.
  4. **No global truth labels.** Unlike FEVER's "Barack Obama was the 44th President" (verifiable against Wikipedia at a single point in time), SciFact labels are **claim-abstract pairs**, not global truth. A claim may be SUPPORTS-ed by one abstract and REFUTES-d by another (this happens in COVID claims). Realistic, but means SciFact verdicts are _evidence-relative_, not absolute.
  5. **COVID demo evaluated by a single annotator.** The 23/36 "plausible" number is by the same medical student who wrote the claims; no inter-annotator agreement on the demo. Headline-grabbing but methodologically thin.
  6. **Pre-large-LLM.** RoBERTa-large baselines; modern domain-specific LLMs (PubMedBERT, SciBERT-large, BioBERT, GPT-4 in medical contexts) would substantially shift the numbers. The 46.5 F1 is a 2020 floor, not a current ceiling.

- **Cross-refs:**
  - **#21 (Thorne/FEVER).** Direct contrast. FEVER = 185k synthetic Wikipedia claims / common-knowledge evidence / ~65% three-way pipeline accuracy. SciFact = 1.4k expert-written biomedical claims / specialist abstract evidence / 46.5% F1 open pipeline. The retrieval-vs-reasoning gap pattern replicates: SciFact's 46.5 → 72.7 → 83.3 echoes FEVER's 64.74 full vs 80.82 oracle. P9 S1 + S3 pair.
  - **#22 (Augenstein/MultiFC).** Companion external-validity citation. MultiFC = real-world journalistic claims with noisy web evidence (49.2% Macro F1). SciFact = expert-written scientific claims with curated abstract evidence (46.5% open F1, 72.7% oracle). Together with FEVER, the three benchmarks triangulate verification difficulty along claim source, evidence source, and knowledge requirements. P9 S1+S2+S3 form a deliberate progression.
  - **#19 (Nie 2019), #16 (Hanselowski 2018).** VERISCI is _structurally_ the same three-stage retrieve-select-label pipeline as NSMN (#19) and the Hanselowski FEVER ensemble (#16). Same pipeline shape, different corpus, same retrieval-as-bottleneck finding. The fact that **three independent pipelines on two corpora produce the same gap** is the empirical basis for our oracle-evidence methodology.
  - **#11 (Devlin/BERT).** VERISCI is a "BERT-to-BERT" architecture, citing DeYoung et al. 2020 (ERASER) as the template. Confirms the BERT-encoder-everywhere pattern as standard for verification by 2020.
  - **#24 (Schuster 2019).** Schuster reveals FEVER claim-only artifacts (~60% accuracy without evidence). SciFact's analogue: claim-only baseline only 44.5%, barely above 33% chance. **SciFact's construction process (citance-based + hand-negation without obvious cues) is the methodological response Schuster's critique implicitly calls for.** Cite as positive-example contrast in P10 stitching.
  - **#9 (Rashkin), #16 (Hanselowski), #19 (Nie), #20 (Hassan).** Numerical-reasoning compound failure mode. Wadden's Table 5 adds biomedicine-specific numerical-reasoning examples (hazard ratios, confidence intervals, p-values) — same failure type, new corpus.
  - **#5 (Guo 2022).** Guo's survey covers SciFact as an example domain-specific verification benchmark; useful in P9 stitching.

---

## Theme 10 — The Limit of Verification: Artifacts & Adversarial Fragility ⭐ MIRRORS THEME 6

### 24. Schuster et al. 2019 — Towards Debiasing Fact Verification Models

- **Venue:** EMNLP 2019 (short paper)
- **Status:** ✅ Read
- **Big move:** The **verification-side parallel to Schuster 2020 (#14)** — same lead author, same surgical methodology (build a controlled test set where a known shortcut becomes impossible), applied to the other paradigm. Shows that on FEVER, a **claim-only BERT classifier — never shown any evidence — reaches 61.7% three-way accuracy**, against a 33.3% majority baseline and only 8 percentage points behind NSMN (#19), the evidence-aware FEVER state-of-the-art. The diagnosis: crowdworker mutation habits during FEVER's claim-generation pipeline (#21 protocol) leave systematic n-gram-to-label correlations that a model can exploit without ever consulting the supporting Wikipedia sentence. The paper's structural twin to #14's provenance-vs-veracity juxtaposition is the **81.8% → 58.7% drop** for the same NSMN classifier moving from FEVER dev to a symmetric test set where claim-only shortcuts are designed to fail.

- **Diagnosis (Section 2) — what the artifacts actually are:**
  - **Local Mutual Information (LMI) ranking of claim bigrams.** LMI(w, l) = p(w, l) · log(p(l|w)/p(l)) — weighted "how surprising is label l given n-gram w." Top 10 LMI bigrams correlated with REFUTES in the FEVER training set: _did not_ (p(l|w) = 0.83), _yet to_ (0.90), _does not_ (0.78), _refused to_ (0.87), _failed to_ (0.88), _only ever_ (0.86), _incapable being_ (0.89), _to be_ (0.50), _unable to_ (0.88), _not have_ (0.78). Same correlations replicate in the dev set, often stronger. **Almost all are negations or near-negations** — the structural fingerprint of how annotators turned a sentence into a REFUTES claim.
  - **World-knowledge ablation rules out the easy counter-explanation.** Maybe the claim-only model is using GloVe's world knowledge ("Magic Johnson" + "Lakers" → true). They retrain InferSent (Conneau 2017) on FEVER claims with random embeddings → 54.1% accuracy. With GloVe → 57.3%. **World knowledge contributes ~3 points; the remaining ~21 points above chance is dataset artifacts.** (Note they use InferSent rather than BERT for this ablation specifically because BERT is pretrained on Wikipedia and carries world knowledge in its weights — they can't disable that.)

- **The Symmetric Test Set (Section 3) — what's actually constructed:**
  - **956 claim-evidence pairs**, derived from 99 SUPPORTS + 140 REFUTES original FEVER pairs that NSMN initially predicted correctly (so the drop they report is _not_ an artifact of starting from hard cases — they start from easy ones).
  - For each original pair, the authors **manually generate a contradicting twin**: a new claim that asserts the opposite fact, paired with new evidence that supports the original claim. Crossed with the original pair, this produces **four pairs total per original** with a specific symmetry — see paper's Figure 1.
  - **By construction, p(label | any claim n-gram) = 0.5** for the two-class subset. Claim-only models are now reduced to chance on this test set.
  - **Quality check:** 30% of pairs re-annotated by two subjects; 94% agreement with authors' labels; Cohen κ = 0.88; 2% flagged for typos/minor grammar. Honest about being small — used only as test, not training.

- **Headline results (Table 3) — the load-bearing numbers:**

  | Model          | FEVER Dev (S+R) | Symmetric Test | Drop  |
  | -------------- | --------------- | -------------- | ----- |
  | NSMN (Nie #19) | 81.8%           | **58.7%**      | −23.1 |
  | ESIM (GloVe)   | 80.8%           | 55.9%          | −24.9 |
  | BERT           | 86.2%           | 58.3%          | −27.9 |
  - **The 23-point gap on identical vocabulary is the measurement.** Models trained on FEVER perform substantially worse on a test set where claim-only shortcuts are neutralized — even though every word in the symmetric test set appears in FEVER's vocabulary. The drop is the artifact-driven margin.
  - **Same shape as #14's measurement on the detection side:** Schuster 2020 reports 0.94 F1 provenance vs 0.53 F1 veracity on the same Grover-Mega classifier. Schuster 2019 reports 81.8% FEVER-dev vs 58.7% symmetric on the same NSMN classifier. Two paradigms, two artifact takedowns, same evidential shape.

- **Re-weighting mitigation (Section 4) — modest, included for completeness:**
  - Pre-processing step: solve min(Σⱼ maxᶜ bᶜⱼ + λ‖α⃗‖₂) for instance weights α⁽ⁱ⁾ that flatten claim-n-gram-to-label correlations, then train the verifier with reweighted cross-entropy (1+α⁽ⁱ⁾)L(x⁽ⁱ⁾, y⁽ⁱ⁾).
  - **Effect (Table 3):** ESIM gains 3.4 pts on symmetric (55.9 → 59.3), BERT gains 3.3 pts (58.3 → 61.6). Both lose 1–4.8 pts on FEVER dev.
  - **Effect on the bigrams (Table 4):** _did not_ goes from p(REFUTES | _did not_) = 0.83 to 0.35. The give-away effectively neutralised in the reweighted training distribution.
  - **Authors are honest about scope:** "Creating a large symmetric dataset for training is outside the scope of this paper as it would be too expensive." The reweighting is a partial fix, not a solution. Their forward-looking recommendation is to use the symmetric test set _alongside_ FEVER for evaluation, not to replace FEVER.

- **Why it matters for our paper:**
  - **Paragraph 10 anchor — Sentence 1.** The single load-bearing citation. The specific numbers: 61.7% claim-only BERT (Section 2); 81.8 → 58.7 NSMN drop (Table 3); top LMI bigrams almost all negations (Table 1); 54.1% claim-only with random embeddings rules out world knowledge as the explanation (Section 2). These are what go into P10 S1.
  - **Structural mirror of P6 anchor (#14).** Schuster 2020 measured 0.94 → 0.53 provenance-vs-veracity F1 on the same classifier (#14 → P6 S2). Schuster 2019 measures 81.8 → 58.7 FEVER-dev-vs-symmetric on the same classifier (#24 → P10 S1). **Same author, same surgical methodology, same shape of evidence, applied to the two paradigms our paper compares.** This is what makes the P6 ↔ P10 mirror in our Related Work structure not just rhetorically symmetric but evidentially symmetric.
  - **Seeds P10 S2 (own words, no citation).** The synthesis line — "a verifier that performs well by exploiting claim-only artifacts is not genuinely verifying; the gap between FEVER-style benchmark performance and what verification _is_ has to be accounted for in evaluation" — rests on #24's specific finding generalized via the convergent evidence chain: #17 + #18 (SNLI/MNLI hypothesis-only artifacts, known post-publication), #22 (MultiFC topic-prior shortcut, the real-world analogue), #23 (SciFact's 44.5% claim-only baseline as positive-example contrast — careful construction can resist this).
  - **Frames as field-acknowledged, not contrarian (mirror of #14's framing).** Guo 2022 (#5) cites both Schuster 2020 (#14) and Schuster 2019 (#24) as accepted limitations of the two paradigms. We're operationalising critiques the field's flagship survey accepts.
  - **Direct relevance to our error analysis.** Some fraction of our FEVER+MNLI verifier's _correct_ predictions on FEVER dev will be claim-only-artifact-driven rather than evidence-driven. We can't easily measure this in our own run (we don't have a symmetric test set for our setup), but we can flag it in Discussion as a known confound for any FEVER-reported number — including ours.

- **Honest weakness / scope of the claim:**
  1. **Symmetric test set is small (956 pairs) and single-team annotated.** All twins were generated by the paper's authors; inter-annotator validation was on 30% of pairs by two subjects, but the _generation_ step had no diversity check. A larger or independently-generated symmetric set might show different effect sizes.
  2. **The reweighting fix is modest.** 3–3.4 points on symmetric, 1–4.8 point cost on FEVER dev. This is a diagnosis paper with a small mitigation, not a "we've solved FEVER artifacts" paper. Worth being honest that #24's contribution is mostly the measurement.
  3. **Only the SUPPORTS / REFUTES subset is tested symmetrically.** NEI cases are excluded from the symmetric test set construction (Section 3 footnote: "NOT ENOUGH INFO cases are easy to generate so we focus on the two other labels"). Strictly speaking, the 58.7% drop is on two-class evaluation, not three-class; this is comparable across rows in Table 3 but doesn't directly translate to three-class FEVER score.
  4. **Pre-fine-tuning era.** BERT-base, ESIM with GloVe, NSMN — all 2018–early-2019 systems. Modern transformers (RoBERTa-large, DeBERTa) likely still exhibit the artifact effect (the artifact is in the data, not the model), but the absolute numbers would shift.
  5. **The bias-correction algorithm is general (not FEVER-specific)** — Eq. 3 in Section 4 — but the authors don't ablate on other artifact-prone datasets. Generalisation claim about the method is by analogy to Jiang & Nachum 2019, not by demonstration.
  6. **Doesn't address evidence-side artifacts.** #24 measures and mitigates _claim-side_ shortcuts only. Whether FEVER's _evidence_ retrieval has analogous artifacts (e.g., systematic correlations between evidence text and labels independent of the claim) is not investigated. Plausibly a smaller effect, but unmeasured.

- **Cross-refs:**
  - **#14 (Schuster 2020).** Twin paper — same lead author, same methodology applied to the detection side. The P6 ↔ P10 structural mirror in our Related Work derives directly from this pair. Schuster 2020's Section 2 explicitly cites #24 as the verification analogue; the symmetry is field-stated, not invented.
  - **#21 (Thorne/FEVER).** #24 is a direct critique of FEVER's claim-generation protocol. Thorne's mutation-based pipeline (annotators alter Wikipedia sentences along six NLI-inspired axes) is the structural reason the artifacts exist: annotators given a small mutation space develop predictable habits. Don't preempt this in P9 (already noted as "carry to P10" in the #21 entry).
  - **#19 (Nie/NSMN).** #24 tests NSMN as one of its three classifiers. Some fraction of Nie's 64.23 FEVER blind-test score is artifact-driven rather than reasoning-driven — exact fraction unmeasured but bounded above by the 23-point dev-to-symmetric drop. Carry to P10.
  - **#17 (Bowman/SNLI), #18 (Williams/MNLI).** Field analogues — Gururangan 2018 / Poliak 2018 (contextual, not cited) showed SNLI and MNLI have hypothesis-only artifacts. #24 is the FEVER version of the same phenomenon. **Reinforces P10 S2's own-words generalization:** crowd-sourced NLP datasets routinely contain claim/hypothesis-side artifacts; FEVER is not anomalous in this respect.
  - **#22 (Augenstein/MultiFC).** Real-world analogue — MultiFC's topic-tag-correlation effect (specific tags co-occur with correct predictions, generic tags with errors) is what FEVER's claim-only n-grams look like when the dataset is naturalistic rather than crowd-mutated. Same shortcut phenomenon, different surface form. P10 framing: artifacts are not FEVER-specific, they're a property of how verification benchmarks get built.
  - **#23 (Wadden/SciFact).** Positive-example contrast — SciFact's claim-only baseline reaches only 44.5% three-way (vs FEVER's 61.7%), barely above the 33% three-class floor. **SciFact's citance-based + hand-negated construction is the methodological response Schuster's critique implicitly calls for**, and the small claim-only margin is evidence it works. Cite as the constructive contrast in P10 stitching.
  - **#5 (Guo 2022).** Flagship survey cites #24 as an acknowledged limitation of verification benchmarking. Field-acknowledgement framing for P10, mirror of how #5 framed #14 for P6.
  - **#16 (Hanselowski).** Hanselowski's NEI-vs-REFUTES confusion in error analysis may be partly artifact-driven; the "evidence doesn't refute" failure mode looks like a reasoning error but is consistent with claim-only-negation shortcuts the model has learned. Note for Discussion error analysis.
  - **#25 (Thorne 2019, upcoming).** Sequel — FEVER 2.0 adversarial extension. #24 shows claim-only artifacts; #25 will show adversarial-rephrasing fragility. Together they fill P10 S1 (artifact) and S3 (adversarial).

---

### 25. Thorne et al. 2019 — The FEVER 2.0 Shared Task

- **Venue:** EMNLP FEVER 2.0 Workshop (Hong Kong, November 2019)
- **Status:** ✅ Read
- **Big move:** The **adversarial-fragility complement to Schuster #24's artifact diagnosis.** Where #24 shows FEVER systems exploit claim-only shortcuts (a _data_ problem), #25 shows the same generation of systems collapses under deliberately-constructed adversarial claims (a _model robustness_ problem). Together they form P10's evidence pair: the same paradigm that has artifact-driven margins on the standard test set also fragments under inputs designed to require genuine compositional reasoning. The shared task adopted a **build-it / break-it / fix-it** protocol on the FEVER 1.0 dataset (#21): builders submitted systems; breakers submitted up to 1,000 novel adversarial claim-evidence-label instances (balanced across SUPPORT / REFUTE / NOTENOUGHINFO); fixers attempted to recover. Three qualifying builders, three qualifying breakers, one fixer.

- **The headline numbers — every single builder lost FEVER score under adversarial evaluation.** Builder FEVER score (standard FEVER 1.0 test) vs Resilience (weighted FEVER score on the adversarial test set, weighted by per-attack correctness rate):

  | System | FEVER Score (%) | Resilience (%) |
  | ------ | --------------- | -------------- |
  | Papelo | 57.36           | **37.31**      |
  | UCLMR  | 62.52           | 35.83          |
  | DOMLIN | 68.46           | 35.82          |
  | CUNLP  | 67.08           | 32.92          |
  | UNC    | 64.21           | 30.47          |
  | Athene | 61.58           | 25.35          |
  | GPLSI  | 58.07           | 19.63          |
  - **No system above 37.31% resilience.** A ~30-point gap between standard-test FEVER score and adversarial-test resilience is the headline finding. The architectural details vary (BERT-based NLI in DOMLIN; pointer-network + RL in CUNLP; OpenIE-triple semantic similarity in GPLSI) but the gap shape is the same across all of them.

- **The attack taxonomy (Table 4) — where the breaks happen:**

  | Breaker    | Attack                       | FEVER Score (%) | Label Acc (%) | n   |
  | ---------- | ---------------------------- | --------------- | ------------- | --- |
  | CUNLP      | Multi-Hop Reasoning          | 31.54 ± 13.19   | 51.64 ± 7.18  | 130 |
  | CUNLP      | Multi-Hop Temporal Reasoning | **8.33 ± 2.08** | 24.48 ± 16.98 | 24  |
  | CUNLP      | Date Manipulation            | 27.53 ± 6.07    | 34.18 ± 4.50  | 94  |
  | CUNLP      | Word Replacement             | 28.87 ± 6.79    | 29.08 ± 9.28  | 71  |
  | CUNLP      | Conjunction                  | 38.25 ± 18.01   | 42.50 ± 15.93 | 50  |
  | TMLab      | AI Generated (GPT-2/GEM)     | 38.07 ± 13.29   | 40.63 ± 11.04 | 44  |
  | TMLab      | **Paraphrase**               | **0.00 ± 0.00** | 43.06 ± 19.59 | 9   |
  | NbAuzDrLqg | **SubsetNum** (transitivity) | **0.00 ± 0.00** | 16.12 ± 17.08 | 38  |
  - **Two attacks drive FEVER score to zero across all systems:** TMLab's Paraphrase attack and NbAuzDrLqg's SubsetNum attack. Critically, the Paraphrase attack shows 43.06% label accuracy — **systems sometimes assign the correct verdict, but never identify the correct evidence sentence.** This separates the two halves of verification: label prediction can survive, evidence retrieval cannot. **The FEVER score (which jointly requires label + evidence) is the metric that exposes the gap; raw label accuracy hides it.**
  - **The compositional-reasoning attacks (Multi-Hop, Multi-Hop Temporal, Date Manipulation, SubsetNum) are systematically the worst.** Where the attack requires combining evidence from two Wikipedia pages, or transitive numerical reasoning about geographic areas, or arithmetic on dates, accuracy collapses near or to chance.

- **The fixer phase (CUNLP, only submission):** Added a document-pointer network on top-4 layers of a BERT title-to-document classifier, modeled the sequence of evidence-sentence selections via a pointer network, and added OpenIE-extracted predicate arguments + arithmetic rules for temporal reasoning. **Result: +1.72 FEVER score, +3.69 resilience.** This is what targeted defence looks like — the gap narrows, but only by a few points on resilience, and only for the attack types the fixer specifically anticipated. Multi-hop and paraphrase remain hard.

- **Attack-generation methodology (matters for our framing):**
  - **CUNLP:** Multi-hop claims generated by augmenting existing FEVER claims with conjunctions or relative clauses sourced from linked Wikipedia articles. Temporal-reasoning claims generated by hand-written rules manipulating date expressions ("in 2001" → "4 years before 2005"). Noisy variants generated using disambiguation pages and the lexical-substitution method of Alzantot et al. 2018.
  - **TMLab:** Built **Generative Enhanced Model (GEM)** — a fine-tuned GPT-2 conditioned on two hyperlinked Wikipedia pages + keywords — to generate claim text automatically; annotators then labelled the generated claims and manually added evidence sentences. Paraphrase attack: rewrite Wikipedia sentences using vocabulary borrowed from texts outside the evidence set, then label the rewrite as SUPPORTS.
  - **NbAuzDrLqg:** Mostly manual. Retrieval-side attacks: claims without entity terms usable as retrieval queries. NLI-side attacks: arithmetic operations, logical inconsistencies, hedged statements, SubsetNum (transitive reasoning about geographic area).

- **Why it matters for our paper:**
  - **Paragraph 10 anchor — Sentence 3.** The adversarial-fragility complement to #24's artifact diagnosis. The load-bearing numbers for P10 S3: **best resilience 37.31% vs builder FEVER scores 57–68%** (the universal-gap finding); **Paraphrase and SubsetNum attacks drove FEVER score to 0.00% across all systems** (the strongest single-attack-type results); **the Paraphrase attack reaches 43% label accuracy but 0% FEVER score** (the label-vs-evidence dissociation — best single result for the thesis); the **+3.69 resilience gain from CUNLP's targeted fixer** (small, attack-specific improvement is what a fix looks like).
  - **Same evidential shape as the P6 ↔ P10 mirror.** #14 + #15 are the detection-side pair: one "data is broken" finding (Schuster 2020: provenance ≠ veracity), one "model is brittle" finding (Potthast: hyperpartisan style swamps fake/real). #24 + #25 are the verification-side pair: one "data is broken" finding (Schuster 2019: claim-only artifacts), one "model is brittle" finding (Thorne 2019: adversarial collapse). **P10's S3 is the structural twin of P6's brittleness finding.** This is what makes both paragraphs of the thesis-hinge run on the same architecture rather than relying on different argumentative shapes.
  - **The label-vs-evidence dissociation is conceptually load-bearing.** Verification is a two-step task: pick the evidence, then judge the claim against it. The Paraphrase attack shows the second step can succeed (43% label accuracy) while the first fails (0% evidence F1, hence 0% FEVER score). For our paper: when reporting any FEVER number, we should distinguish label accuracy from full FEVER score; the gap between them is informative. **Useful Discussion / error-analysis line:** systems can be correct for the wrong reason — picking the right label without picking the right evidence — and this is the failure mode adversarial evaluation surfaces that standard test-set accuracy hides.
  - **Compositional reasoning as the fragility frontier.** Multi-hop, temporal arithmetic, and transitive numerical reasoning are systematically where systems break. This aligns with the numerical-reasoning failure mode we've been tracking across #9 + #16 + #19 + #20 + #23, and adds compositional / multi-hop reasoning as a related failure axis. Useful Limitations framing for our off-the-shelf MNLI verifier: we should expect it to fail on the same composition / arithmetic axes documented here — these are not just MNLI-NLI artifacts, they are a property of the verification task itself when claims require evidence from more than one source.
  - **Honest framing for the universality of the finding.** Every architectural family in the shared task — BERT-NLI, pointer-network-RL, OpenIE-triple — exhibits the same gap. This is not a "weak baselines fall over" story; it is "all the strong systems fall over." That universality is what we should lean on in P10 S3, not any individual system's number.

- **Honest weakness / scope of the claim:**
  1. **Small per-attack-type n.** Paraphrase n=9, SubsetNum n=38, Multi-Hop Temporal n=24. The 0%-FEVER-score findings are dramatic but rest on tens of instances; standard errors are reported alongside means (Table 4) and are large for the small-n attacks. The aggregate resilience numbers are over the full ~500-instance adversarial test set and are tighter.
  2. **Adversaries were not generated independently of the systems being attacked.** Breakers had sandbox access — they could test attacks against the hosted builder systems with twice-daily 50-instance probes before final submission. The attacks are therefore _calibrated_ against the specific systems, not blind. This is intentional (the point of build-it / break-it) but means the resilience numbers are an in-the-wild adversarial worst case, not an estimate of natural-distribution robustness.
  3. **Only three qualifying builders.** DOMLIN, CUNLP, GPLSI. The other four systems in Table 1 (Papelo, UCLMR, UNC, Athene) are reference systems carried over from FEVER 1.0. The "all systems fall" finding holds across this combined set of seven, but the diversity is constrained by what FEVER 1.0 produced.
  4. **One fixer submission.** CUNLP's +3.69 resilience gain is the only data point on how much targeted defence helps. We can't generalize from n=1 fixer to claims about how fixable the problem is in general.
  5. **Pre-large-LM era.** All systems are BERT-base / ESIM / ELMo / OpenIE. Modern systems (RoBERTa-large, DeBERTa, large pre-trained LMs) almost certainly have higher absolute FEVER scores _and_ higher resilience, but whether the proportional gap (~30 pts) closes is empirically untested in this paper. The adversarial-fragility _phenomenon_ has been replicated for larger models in subsequent literature; the specific 2019 numbers should not be over-generalized.
  6. **Composite-metric interpretation.** "Resilience" is a weighted average of FEVER scores weighted by per-attack correctness rate, which is itself an annotator-quality estimate. The metric is well-defined (Section 2.2 equations) but compresses several distinct phenomena (per-attack difficulty, attack correctness, system FEVER score) into one number. The per-attack-type breakdown in Table 4 is more interpretable than the headline resilience column.

- **Cross-refs:**
  - **#24 (Schuster 2019).** Direct pair. Same FEVER paradigm, complementary failure mode (artifacts vs adversarial fragility). Both papers underlie P10's two halves.
  - **#21 (Thorne 2018, FEVER 1.0).** Direct predecessor. FEVER 2.0 uses the same dataset, same task definition, same scoring metric (FEVER score) — adversarial extension only. Same lead author; the sequel.
  - **#19 (Nie/NSMN).** UNC system in Table 1 is Nie et al.'s NSMN, which is the FEVER 1.0 leaderboard winner (64.23 blind test → 30.47% resilience in FEVER 2.0). The same system that anchored "verification works at 64% FEVER score" in our P8 S1 anchors "verification collapses to 30% resilience" in P10 S3. Different sentence, different paper — both true, same system.
  - **#14 (Schuster 2020), #15 (Potthast 2018).** P6 ↔ P10 structural mirror. #14 + #15 form the detection-side data-broken / model-brittle pair; #24 + #25 form the verification-side equivalent. Cross-paragraph symmetry is what makes the thesis-hinge architecture work.
  - **#16 (Hanselowski/UKP-Athene).** Athene system in Table 1 → 25.35% resilience. Hanselowski's NEI-confusion failure mode (P7 / oracle-evidence carry-forward) is one of the failure modes the adversarial attacks systematically exploit, in particular the compositional-reasoning attacks where Hanselowski's claim-attention pooling cannot synthesize evidence across multiple sentences.
  - **#5 (Guo 2022).** Flagship survey covers adversarial-robustness work on FEVER systems. Field-acknowledgement framing again: our P10 S3 critique is what the standard survey says.
  - **#23 (Wadden/SciFact).** Wadden's five-axis SciFact failure taxonomy (science background, directionality, numerical reasoning, cause-and-effect, coreference) overlaps with the FEVER 2.0 attack types (multi-hop = composition, date manipulation = temporal reasoning, SubsetNum = numerical/transitive reasoning, paraphrase = lexical generalization). Two corpora, similar fragility surface — useful cross-corpus convergence for Discussion.

---

## Themes Summary Table

| Theme                                     | Papers        | Function in paper                |
| ----------------------------------------- | ------------- | -------------------------------- |
| 1. Foundations                            | 1, 2, 3, 4, 5 | Intro / Related Work setup       |
| 2. Bridging                               | 6, 7          | Comparative framing              |
| 3. Linguistic detection                   | 8, 9, 10      | Classical baseline justification |
| 4. Transformer detection                  | 11, 12        | Transformer model justification  |
| 5. Detection benchmarks                   | 13            | Detection data section           |
| 6. **Limit of detection (style ≠ truth)** | 14, 15        | **Thesis hinge**                 |
| 7. NLI verification                       | 16, 17, 18    | NLI pipeline justification       |
| 8. Verification pipelines                 | 19, 20        | Architectural reference          |
| 9. Verification benchmarks                | 21, 22, 23    | Verification data section        |
| 10. **Limit of verification**             | 24, 25        | **Mirrors Theme 6**              |

---

## Cross-paper observations

**Thesis-hinge citation chain (load-bearing for Paragraph 6):** Bondielli & Marcelloni 2019 (#7, noticed in passing — style convergence) → Pérez-Rosas 2018 (#8, cross-domain collapse 0.78 → 0.48) → Rashkin 2017 (#9, cross-source drop 0.91 → 0.65; graded ceiling 0.22 F1) → Ahmed 2018 (#10, 98% → 92% on temporal confound) → Schuster 2020 (#14, formalized for machine-generated text) → Potthast 2018 (#15, formalized for hyperpartisan style). Six converging citations on one hinge.

**Field-acknowledgement framing (Paragraphs 6 + 10):** Guo et al. 2022 (#5, flagship survey) explicitly cites Schuster 2020 (#14) and Schuster 2019 (#24) as acknowledged limitations of both paradigms. Frame our argument as "operationalizing critiques the field's standard survey already accepts" — stronger than presenting them as our own observations.
