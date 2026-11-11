# Source Verification Log

A log of **27 claims written the way an AI model might state them**, each checked against authoritative sources, with a verdict, the correct statement, a short evidence summary, source links and a written rationale. It shows the core evaluation skill: **do not trust a confident answer; verify it against the primary source and explain the difference.**

## Results
| Result | Claims |
|---|---|
| Fully supported | 6 |
| Contradicted | 19 |
| Partially supported | 1 |
| Unverifiable | 1 |

The claims were chosen because their errors are instructive, so the high error rate is **not** a measurement of any model's accuracy.

Error types found: 8 factual errors, 6 outdated facts, 4 overstatements, 2 wrong citations, 1 unsupported prediction. Two findings are high severity: treating SHA-1 as acceptable for new signatures, and treating Windows 10 as still receiving free security updates.

## Example entry
> **VL-013:** "As of October 2026, Windows 10 Home and Pro still receive free monthly security updates."
>
> **Verdict:** contradicted (outdated_fact, high). **Correct:** free security updates ended on 14 October 2025. **Source:** Microsoft Lifecycle page for Windows 10 Home and Pro.
>
> **Rationale:** a user relying on this would keep unsupported systems online believing they are patched; severity is high because the consequence is a security exposure.

## How each claim was verified
| Method | Claims | Meaning |
|---|---|---|
| online_primary | 14 | Primary source read online on 22 October 2026 (RFCs, PEPs, NIST, Microsoft, CERN, Python.org, IANA) |
| executed_locally | 10 | Reproduced by passing tests (Python behavior, SQLite) |
| online_secondary_quote | 3 | Wording confirmed through quotations; **open the primary page to confirm** (VL-003, VL-015, VL-016) |

## Project contents
| Path | Purpose |
|---|---|
| `data/claims.json` | The 27 verified claims |
| `VERIFICATION_LOG.md` | Readable log generated from the data |
| `docs/methodology.md` | Workflow, verdicts, error types, severity, rationale writing, red flags |
| `docs/research-notes.md` | What was checked, where and when |
| `docs/summary.md` | Statistics by verdict, error type, severity, domain, method |
| `claimlog/` | Validator and report builder (Python) |
| `tests/` | 19 automated tests, including the code that reproduces each executable claim |

## Quality rules enforced by the validator
- A supported claim cannot have an error type; any other verdict needs an error type and a severity
- At least one **primary** source with an https link, and a verification date
- Evidence limited to 70 words so it is summarised, not copied
- A rationale of at least 15 words
- Every `executed_locally` claim must name a test that exists and passes

## Use it
```bash
python -m claimlog data/claims.json --log VERIFICATION_LOG.md --summary docs/summary.md
pytest -q
```

## Skills demonstrated
Source verification against primary sources, citation checking, reasoning rationales, error classification, rubric discipline, Python, test automation, documentation.

## Author
Yazan Aljabari - QA Engineer
