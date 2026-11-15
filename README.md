# AI Evaluation Specialist Portfolio

**AI Evaluation Specialist Portfolio** — Three projects showing the core craft of an AI evaluation specialist: designing questions that expose model weaknesses, reviewing model output in a non-English language with a defensible rubric, and verifying confident claims against primary sources. Every artifact is machine-validated in CI.

**Author:** [Yazan Aljabari](https://www.linkedin.com/in/yazan-aljabari-878202139/)  
**License:** [MIT](LICENSE)  
**Branch:** `main`

[![Tests](https://github.com/yazanus94-dot/AI-Evaluation-Specialist-Portfolio-Projects/actions/workflows/ci.yml/badge.svg)](https://github.com/yazanus94-dot/AI-Evaluation-Specialist-Portfolio-Projects/actions/workflows/ci.yml)
![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)## Overview

Three projects showing the **core craft of an AI evaluation specialist**: designing questions that expose model weaknesses, reviewing model output in a non-English language with a defensible rubric, and verifying confident claims against primary sources. Every artifact here is **machine-validated**: the schemas, rubrics and even the reference answers are checked by tests and CLI validators on every push.

| # | Project | What it contains | Validation |
|---|---------|------------------|------------|
| 1 | [adversarial-question-set-technology](adversarial-question-set-technology/) | **29 expert-level questions** across networking, security, databases, programming and Unicode/time — each with trap type (misconception, subtle_distinction, edge_case, false_premise, outdated_fact…), gradable key points, the likely wrong answer, and an authoritative source | 18 tests incl. **executable facts**: the reference answers themselves are re-derived in Python (subnet math, SQL NULL logic, Unicode NFC/NFD, Y2038 boundary) |
| 2 | [arabic-tech-evaluation-set](arabic-tech-evaluation-set/) | **30 evaluated Arabic/English responses** about technology: weighted rubric with gates, an Arabic error taxonomy (hamza/terminology/RTL punctuation/translation units), terminology glossary, and a corrected version for every flawed response | 18 tests + automatic **Arabic lint** (Latin commas/question marks in Arabic sentences, transliterations vs. standard terms, mixed-direction text) |
| 3 | [source-verification-log](source-verification-log/) | **27 AI-style claims checked against primary sources**: verdict, corrected statement, evidence summary, source links, rationale — 19 contradicted, 6 supported, 1 partial, 1 unverifiable | 19 tests incl. **executable claims** (hash/encoding facts re-verified in code) + link/verdict schema validation |

## Problem statement

AI evaluation often rewards confident-sounding answers over correct ones. Models produce plausible-but-wrong technical claims, evaluation rubrics reward fluent prose over factual accuracy, and "ground truth" itself is frequently asserted without verification. This portfolio addresses those gaps: questions are designed to expose specific weaknesses, reviews use weighted rubrics with hard gates so factual errors cannot be outweighed by fluency, and every confident claim is checked against primary sources rather than trusted.

## Objectives

- Design adversarial questions that discriminate genuine understanding from memorization and convention errors.
- Build a defensible, gate-protected rubric for non-English (Arabic) technology response review.
- Verify AI-style claims against primary sources with explicit verdicts and corrected statements.
- Make every artifact machine-validated so ground truth cannot silently rot.
- Document the methodology, not just the artifacts, for reviewer and recruiter transparency.## Features

- **29 expert-level adversarial questions** with trap type, gradable key points, likely wrong answer, and authoritative source per item.
- **Executable reference facts**: where a fact can be computed, it is — tests re-derive reference answers in Python (subnet math, SQL NULL logic, Unicode NFC/NFD, Y2038 boundary).
- **30 Arabic/English technology evaluations** with a weighted rubric, hard gates (a factual error can never be outweighed by fluent prose), an Arabic error taxonomy, a terminology glossary, and corrected versions for every flawed response.
- **Automatic Arabic lint**: detects Latin commas/question marks in Arabic sentences, transliterations vs. standard terms, and mixed-direction text.
- **27-claim source-verification log** with verdict, corrected statement, evidence summary, source links, and rationale (19 contradicted, 6 supported, 1 partial, 1 unverifiable).
- **Executable claim verification**: hash/encoding facts are re-verified in code, plus link/verdict schema validation.
- **CLI validators and stats generators** for each project (`advqs --stats`, `arabic_eval --summary`, `claimlog --summary`).
- **CI on Python 3.11 / 3.12 / 3.13** running all three suites and validators on every push.

## Technologies

- **Language:** Python 3.11+
- **Standard library:** `json`, `re`, `hashlib`, `unicodedata`, `argparse`, `pathlib`
- **Testing:** pytest
- **CI/CD:** GitHub Actions
- **Data formats:** JSON, Markdown, CSV, text

## Project structure

```text
.
├── adversarial-question-set-technology/   # 29 expert-level questions with traps + sources
├── arabic-tech-evaluation-set/            # 30 Arabic/English evaluations with gated rubric
├── source-verification-log/               # 27 claims checked against primary sources
├── archive/                               # Original upload archives, kept for provenance
├── .github/workflows/ci.yml               # Continuous integration
├── LICENSE                                # MIT license
└── README.md                              # This file
```

Each project directory contains its source, tests, data files, and per-project `README.md`.## Installation

### Prerequisites
- **Python 3.11+** (3.12/3.13 recommended; CI tests on all three)
- `pip` and virtual environment tooling

### Setup

```bash
# Clone the repository
git clone https://github.com/yazanus94-dot/AI-Evaluation-Specialist-Portfolio-Projects.git
cd AI-Evaluation-Specialist-Portfolio-Projects

# Create and activate a virtual environment
python -m venv .venv
# Windows (PowerShell): .venv\Scripts\Activate.ps1
# macOS/Linux:         source .venv/bin/activate

pip install --upgrade pip
pip install pytest
```

> **Note:** All three projects are dependency-free at runtime (standard library only); `pytest` is required only for running the test suites.## Usage

```bash
# 1. Adversarial question set (validate + generate catalogue/stats)
cd adversarial-question-set-technology
python -m pytest -q
python -m advqs --stats output/stats.md        # OK: 29 questions valid

# 2. Arabic evaluation set (validate + score + lint)
cd ../arabic-tech-evaluation-set
python -m pytest -q
python -m arabic_eval --summary output/summary.md   # OK: 30 evaluations valid

# 3. Source verification log
cd ../source-verification-log
python -m pytest -q
python -m claimlog --summary output/summary.md      # OK: 27 claims valid
```

CI runs all three suites and validators on Python 3.11 / 3.12 / 3.13.

## Methodology

- **Design first.** Every adversarial question documents *why* it works: the trap, the misconception it targets, and the answer a model is likely to produce.
- **Rubrics with gates.** The Arabic review uses weighted criteria plus hard gates (a factual error can never be outweighed by fluent prose), so scores are defensible.
- **Verify, don't trust.** The verification log treats model confidence as a claim to check, never as evidence — with the difference explained in writing.
- **Self-checking datasets.** Wherever a fact can be computed, it is: the tests re-derive reference answers and claims, so the ground truth cannot silently rot.

## Results

**Machine-validated artifact counts (repository state):**
- **Adversarial question set:** 29 questions valid (schema, trap presence, source presence, executable-fact checks).
- **Arabic evaluation set:** 30 evaluations valid (rubric schema, gate logic, Arabic lint clean).
- **Source verification log:** 27 claims valid (verdict schema, link presence, executable-claim re-derivation).

These are **authoring and validation results** — counts of artifacts that pass the repository's own machine checks. They demonstrate the quality-control machinery, not measurements of any AI model. No model outputs or benchmark scores are claimed.## Testing

```bash
# Run all three suites
cd adversarial-question-set-technology && python -m pytest -q
cd ../arabic-tech-evaluation-set          && python -m pytest -q
cd ../source-verification-log             && python -m pytest -q
```

- **18 tests** for the adversarial question set, including executable facts (subnet math, SQL NULL logic, Unicode NFC/NFD, Y2038 boundary).
- **18 tests + Arabic lint** for the Arabic evaluation set.
- **19 tests** for the source verification log, including executable claims (hash/encoding facts re-verified in code) and link/verdict schema validation.
- **CI:** `.github/workflows/ci.yml` runs all suites and CLI validators on Python 3.11 / 3.12 / 3.13 on every push.

## Limitations

- **Synthetic Arabic content:** the Arabic evaluation set's prompts and responses are synthetic examples with deliberate errors, and every entry is marked `needs_native_review` per the native-review checklist.
- **Sources are orientation links:** sources are linked for orientation; check current primary sources before relying on any fact.
- **Executable facts are limited in scope:** only facts that can be computed in pure Python are re-derived in code; the rest rely on cited sources.
- **No model evaluation:** this portfolio tests artifacts and methodology, not model behavior; no model outputs or benchmark scores are claimed.## Future improvements

- Expand the adversarial question bank with additional domains and difficulty calibration.
- Add a native-Arabic reviewer pass for the Arabic evaluation set.
- Extend executable-fact coverage to more standards (RFCs, protocol specs, algorithm complexity).
- Add trend tracking and per-item revision history for question quality.
- Publish a hosted question-bank explorer (e.g. GitHub Pages).

## References

- Project-local documentation and source files within each numbered directory.
- RFC series (networking/security references in the adversarial question set).
- Unicode standard (NFC/NFD references).
- Official documentation for tools and standards cited in the verification log.