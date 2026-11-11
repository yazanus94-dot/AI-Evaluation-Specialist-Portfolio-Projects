# AI Evaluation Specialist Portfolio

[![Tests](https://github.com/yazanus94-dot/AI-Evaluation-Specialist-Portfolio-Projects/actions/workflows/ci.yml/badge.svg)](https://github.com/yazanus94-dot/AI-Evaluation-Specialist-Portfolio-Projects/actions/workflows/ci.yml)
![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Three projects showing the **core craft of an AI evaluation specialist**:
designing questions that expose model weaknesses, reviewing model output in a
non-English language with a defensible rubric, and verifying confident claims
against primary sources. Every artifact here is **machine-validated**: the
schemas, rubrics and even the reference answers are checked by tests and CLI
validators on every push.

| # | Project | What it contains | Validation |
|---|---------|------------------|------------|
| 1 | [adversarial-question-set-technology](adversarial-question-set-technology/) | **29 expert-level questions** across networking, security, databases, programming and Unicode/time — each with trap type (misconception, subtle_distinction, edge_case, false_premise, outdated_fact…), gradable key points, the likely wrong answer, and an authoritative source | 18 tests incl. **executable facts**: the reference answers themselves are re-derived in Python (subnet math, SQL NULL logic, Unicode NFC/NFD, Y2038 boundary) |
| 2 | [arabic-tech-evaluation-set](arabic-tech-evaluation-set/) | **30 evaluated Arabic/English responses** about technology: weighted rubric with gates, an Arabic error taxonomy (hamza/terminology/RTL punctuation/translation units), terminology glossary, and a corrected version for every flawed response | 18 tests + automatic **Arabic lint** (Latin commas/question marks in Arabic sentences, transliterations vs. standard terms, mixed-direction text) |
| 3 | [source-verification-log](source-verification-log/) | **27 AI-style claims checked against primary sources**: verdict, corrected statement, evidence summary, source links, rationale — 19 contradicted, 6 supported, 1 partial, 1 unverifiable | 19 tests incl. **executable claims** (hash/encoding facts re-verified in code) + link/verdict schema validation |

## The method, not just the artifacts

- **Design first.** Every adversarial question documents *why* it works: the trap,
  the misconception it targets, the answer a model is likely to produce.
- **Rubrics with gates.** The Arabic review uses weighted criteria plus hard gates
  (a factual error can never be outweighed by fluent prose), so scores are defensible.
- **Verify, don't trust.** The verification log treats model confidence as a claim
  to check, never as evidence — with the difference explained in writing.
- **Self-checking datasets.** Wherever a fact can be computed, it is: the tests
  re-derive reference answers and claims, so the ground truth cannot silently rot.

## Quick start

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

## Scope

Portfolio projects by Yazan Aljabari. The Arabic evaluation set's prompts and
responses are synthetic examples with deliberate errors, and every entry is marked
`needs_native_review` per the native-review checklist. Sources are linked for
orientation; check current primary sources before relying on any fact.

## License

MIT, see [LICENSE](LICENSE).
