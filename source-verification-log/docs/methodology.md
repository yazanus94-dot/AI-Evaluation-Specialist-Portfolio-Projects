# Verification Methodology

## Goal
For each claim an AI model might state, decide whether it is true, find the authoritative evidence, and write a rationale that another reviewer can follow and check.

## Workflow
1. **Split the claim** into checkable parts: names, dates, numbers, section references, causal statements.
2. **Find the primary source** (standard, RFC, official documentation, the issuing organization). Prefer the original page over summaries.
3. **Check each part** against the source. Check the **date and version**: many errors are facts that used to be true.
4. **Run it** when the claim is about code behavior or arithmetic. Keep the reproduction in `tests/test_executable_claims.py`.
5. **Check the citation itself** if the claim names a section, RFC, PEP or page. A real document with the wrong section is still a citation error.
6. **Choose the verdict**, error type and severity, then write the rationale.

## Verdicts
| Verdict | Use when |
|---|---|
| supported | Every part of the claim matches the primary source |
| partially_supported | Part is right and part is wrong, imprecise or missing context |
| contradicted | A primary source or a reproduction shows the claim is false |
| unverifiable | No authoritative source settles it (for example a prediction or an invented statistic) |

## Error types
| Type | Meaning |
|---|---|
| factual_error | States something false |
| outdated_fact | Was true earlier; no longer true |
| wrong_citation | The idea may be right but the section, number or source is wrong |
| overstatement | Stretches a source ("must" instead of "may", "removed" instead of "optional") |
| unsupported_prediction | Presents a future outcome as fact |

## Severity (impact if a user relied on the claim)
| Severity | Example |
|---|---|
| high | Security exposure or compliance failure (SHA-1 signatures, unsupported OS) |
| medium | Wrong behavior in code or wrong standard cited |
| low | Minor date or section slip |

## Verification methods recorded for each claim
| Method | Meaning |
|---|---|
| online_primary | The primary source text was read on the stated date |
| online_secondary_quote | The wording was confirmed through quotations of the primary source; **open the primary page to confirm** |
| executed_locally | Reproduced by a passing test in this repository |

## Writing the rationale
State **what is wrong**, **what the source says**, and **why it matters**. Summarise evidence in your own words; the validator rejects evidence longer than 70 words so that nothing is copied wholesale.

| Weak | Strong |
|---|---|
| "Wrong." | "The date is off by one year. For a planning question this matters, because the system is already unsupported. The Microsoft lifecycle page gives 14 October 2025." |
| "Hallucinated source." | "The section number belongs to a different status code, so a reader who opens it finds the wrong definition." |

## Red flags
- A precise section number with no quotation or link
- A statistic with no named survey
- A confident claim about a version without a date
- "Always" and "never" in technical statements
- A source that exists but does not say what is claimed
