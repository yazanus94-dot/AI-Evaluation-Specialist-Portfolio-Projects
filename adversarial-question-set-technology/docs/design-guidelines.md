# Design Guidelines for Adversarial Evaluation Questions

The aim is a question that a capable model is **likely to get wrong for a reason that can be explained and verified**. A good question exposes a reasoning flaw, a stale fact or a hidden assumption, not just obscure trivia.

## The eight trap types
| Trap type | What it tests | Example in this set |
|---|---|---|
| `false_premise` | Does the model challenge a wrong assumption inside the question? | AQ-002 (RFC 9110 "defines" 418) |
| `outdated_fact` | Does the model know the current state, not an old one? | AQ-019 (Python GIL as of 3.14) |
| `multi_step_reasoning` | Can it chain several steps without slipping? | AQ-014 (shared mutable default) |
| `subtle_distinction` | Can it separate two similar concepts? | AQ-004 (idempotent vs identical response) |
| `edge_case` | Does it handle boundary or unusual inputs? | AQ-011 (SQL NULL logic) |
| `numerical` | Is the arithmetic and unit handling exact? | AQ-007 (subnet math) |
| `misconception` | Does it repeat a popular half-truth? | AQ-005 (what HTTPS hides) |
| `over_generalization` | Does it apply a rule where it does not hold? | AQ-008 (CNAME at the zone apex) |

## Quality checklist (every question must pass)
1. **One defensible answer.** Two experts reading the sources would agree on the reference answer.
2. **Verifiable.** A primary source (standard, RFC, official documentation, specification) is cited with the exact section, or the answer is reproduced by running code.
3. **Self-contained.** No hidden context is needed; all inputs are in the question.
4. **A named failure mode.** `expected_model_failure` states the wrong answer a model is likely to give, and `why_hard` explains why.
5. **Gradable.** At least two `key_points` that a reviewer can mark true or false.
6. **Not a lookup.** The question needs reasoning or a distinction, not only recall of one string.
7. **Stable or dated.** Volatile facts are dated in the reference answer (for example "as of Python 3.14").
8. **No opinion.** Avoid "best" or "should" questions unless the source states a rule.

## Difficulty scale
| Level | Meaning |
|---|---|
| 1 | Common knowledge |
| 2 | One concept, easy to slip on |
| 3 | Two concepts or one exact rule |
| 4 | Multi-step reasoning or a rule most practitioners forget |
| 5 | Specialist knowledge plus reasoning |

## Process
1. Pick a topic where you hold real expertise.
2. Find a real misconception or an exact rule in a primary source.
3. Write the question so that the tempting answer is wrong.
4. Write the reference answer, key points and the source section.
5. Verify (see `source-verification-protocol.md`), then run `python -m advqs` to validate the record.
