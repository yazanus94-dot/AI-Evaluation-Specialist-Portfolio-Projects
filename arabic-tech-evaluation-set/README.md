# Arabic Technology Evaluation Set

A framework and a set of **30 evaluated Arabic and English responses about technology**, built the way an evaluation specialist reviews AI output in a non-English language: a weighted rubric with gates, an error taxonomy for Arabic, a terminology glossary, an automatic lint for Arabic text, and a written rationale with a corrected version for every flawed response.

> The prompts and responses are **synthetic examples** written for this demonstration, with deliberate errors in the flawed ones. Every entry is marked `needs_native_review`; see `docs/native-review-checklist.md`.

## What is evaluated
| Area | Examples of what the set tests |
|---|---|
| Technical accuracy | Hashing is not reversible; DNS maps names to addresses; a byte has 8 bits; an invented RFC |
| Terminology | Standard terms (قاعدة بيانات, متصفح, كلمة المرور) instead of transliterations (داتابيز, براوزر, باسوورد) |
| Language quality | Hamza and spelling mistakes, agreement, colloquial answers to a Modern Standard Arabic request |
| Instruction following | Wrong count, a missing negative test case, ignoring "in one sentence" |
| Formatting and right-to-left text | Latin commas and question marks inside Arabic sentences, mixed-direction text |
| Translation | A wrong unit (months became days), an unnatural word-for-word rendering |

## Results (from `docs/summary.md`)
- 30 responses: 12 rated 5, 2 rated 4, 7 rated 3, 8 rated 2, 1 rated 1; mean score 71.2 out of 100
- 13 responses were capped by a rubric gate (wrong core fact, ignored instruction, serious language problems)
- Most frequent error tag: factual errors (7), then instruction violations (4) and terminology errors (3)
- The automatic lint matched the reviewer's tags for all 5 terminology and punctuation cases, with no false alarms; grammar, dialect and meaning still need a human

## How scoring works
Five criteria (accuracy 35%, terminology 20%, language 20%, instructions 15%, formatting 10%) are scored 1 to 5 and combined into a 0 to 100 score. **Gates** cap the score for serious problems: a wrong core fact caps it at 40, an ignored instruction or serious language problems at 60, and a fabricated source at 20. The reviewer's overall rating must stay within one point of the score band.

## Example entry
> **Prompt:** كم بتًا في البايت الواحد؟ (How many bits are in one byte?)
> **Response:** البايت الواحد يتكون من 16 بتًا.
> **Scores:** accuracy 1, other criteria 5 | **Rating:** 2 | **Tag:** factual_error
> **Rationale:** A byte has 8 bits, not 16. A simple verifiable fact stated confidently and wrongly.
> **Correction:** يتكون البايت الواحد من 8 بتّات.

## Project contents
| Path | Purpose |
|---|---|
| `data/evaluations.json` | The 30 evaluated responses with scores, tags, rationales and corrections |
| `data/rubric.json` | Criteria, weights, gates, scale guide |
| `data/glossary.csv` | 19 technical terms: preferred, accepted and discouraged Arabic forms |
| `EVALUATIONS.md` | Readable catalogue (Arabic shown right-to-left) |
| `docs/evaluation-guidelines.md` | Process, Modern Standard Arabic versus dialect, terminology, formatting, rationale writing |
| `docs/rubric-and-error-tags.md` | Weights, gates, rating bands, 11 error tags, validator rules |
| `docs/native-review-checklist.md` | What a native reviewer must confirm before publishing |
| `docs/summary.md` | Statistics by rating, criterion, tag and topic |
| `arabic_eval/` | Scoring, validator, Arabic lint and report builder (Python) |
| `tests/` | 18 automated tests |

## The Arabic lint
`arabic_eval/lint.py` flags discouraged transliterated terms (even with prefixes such as ال and ب, and with hamza variants), Latin punctuation in Arabic sentences and mixed numeral styles. It is an aid, not a replacement for a reviewer.

## Use it
```bash
python -m arabic_eval data --catalogue EVALUATIONS.md --summary docs/summary.md
pytest -q
```

## Skills demonstrated
Non-English (Arabic) AI output evaluation, rubric and gate design, error taxonomy, terminology management, right-to-left text checks, written rationales, Python, test automation.

## Author
Yazan Aljabari - QA Engineer
