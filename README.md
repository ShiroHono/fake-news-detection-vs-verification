# Fake News Detection vs Verification

Comparative NLP study for [course name]. Two paradigms compared on aligned data:
detection (LIAR + classical/transformer) vs verification (FEVER + off-the-shelf MNLI).

## Setup

    python -m venv .venv
    source .venv/bin/activate   # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

## Layout

- `experiments/` — one script per experiment
- `notes/` — paper drafts and project state
- `results/` — small output files (numbers, confusion matrices)
