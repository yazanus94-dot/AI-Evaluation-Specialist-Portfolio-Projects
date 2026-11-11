# Adversarial Question Set: Technology Domain

A set of **29 expert-level questions designed to expose weaknesses in AI language models**, covering web protocols, networking, security, databases, Python, JavaScript, Java, software testing, Unicode and time handling, tooling and technology history. Each question comes with a verified reference answer, gradable key points, the trap it uses, the wrong answer a model is likely to give and an authoritative source.

This is the kind of work an evaluation specialist does: write tasks that probe model limits, verify answers against primary sources, and document clear rationales.

## What makes the questions adversarial
| Trap type | Count | Example |
|---|---|---|
| misconception | 7 | "Does HTTPS hide the hostname?" (AQ-005) |
| subtle_distinction | 7 | Idempotent does not mean identical responses (AQ-004) |
| edge_case | 4 | SQL NULL logic (AQ-011) |
| numerical | 4 | Subnet and boundary-value arithmetic (AQ-007) |
| false_premise | 2 | "RFC 9110 defines 418..." (AQ-002) |
| outdated_fact | 2 | Python's GIL as of 3.14 (AQ-019) |
| multi_step_reasoning | 2 | Mutable default argument trace (AQ-014) |
| over_generalization | 1 | CNAME at the zone apex (AQ-008) |

Average difficulty is 2.9 out of 5; 21 of 29 questions are rated 3 or higher.

## Example record
```json
{
  "id": "AQ-002", "topic": "web_protocols", "difficulty": 3, "trap_type": "false_premise",
  "question": "RFC 9110 defines status code 418 'I'm a teapot' as a standard HTTP response ... In which section does it define the behavior of 418?",
  "reference_answer": "The premise is false. RFC 9110 lists 418 as '(Unused)' in section 15.5.19 ...",
  "key_points": ["Rejects the premise", "418 is marked (Unused) in RFC 9110 section 15.5.19", "..."],
  "expected_model_failure": "Accepts the premise and invents a section describing 418 behavior.",
  "source": {"title": "RFC 9110: HTTP Semantics", "reference": "Section 15.5.19", "url": "https://www.rfc-editor.org/rfc/rfc9110"},
  "verification": {"status": "primary_source_checked_online", "date": "2026-10-22"}
}
```

## Source verification (honest status)
| Status | Questions | Meaning |
|---|---|---|
| `executed_locally` | 8 | Reproduced by running code in `tests/test_executable_facts.py` (SQL, Python, subnet math, ISO weeks, Unicode, Unix time) |
| `primary_source_checked_online` | 5 | Section numbers or dates confirmed against the source (RFC 9110, RFC 6151, PEP 779, CERN) |
| `needs_manual_check` | 16 | Drafted from known documentation; confirm each against its source using `docs/verification-checklist.md` |

## Project contents
| Path | Purpose |
|---|---|
| `data/questions.json` | The 29 questions |
| `QUESTIONS.md` | Readable catalogue generated from the data |
| `docs/design-guidelines.md` | Trap types, quality checklist, difficulty scale, process |
| `docs/source-verification-protocol.md` | Source hierarchy, steps, verification statuses |
| `docs/grading-rubric.md` | How to score a model answer and write a rationale |
| `docs/verification-checklist.md` | Items to confirm before publishing |
| `docs/dataset-summary.md` | Counts by topic, trap, difficulty and verification status |
| `advqs/` | Validator, grader and catalogue builder (Python) |
| `tests/` | 18 automated tests |

## Use it
```bash
python -m advqs data/questions.json --catalog QUESTIONS.md --stats docs/dataset-summary.md
pytest -q
```
The validator enforces required fields, an allowed topic and trap type, at least two key points, an https source URL, a verification date for verified items, an explicit "premise is false" statement for false-premise questions and dated facts for outdated-fact questions.

## Skills demonstrated
Adversarial task design, domain depth in technology, source verification against primary sources, reasoning rationales, rubric-based evaluation, Python, test automation, documentation.

## Author
Yazan Aljabari - QA Engineer
