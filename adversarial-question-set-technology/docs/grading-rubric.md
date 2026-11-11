# Grading Rubric for Model Answers

Use `advqs.grade_answer()` or apply the same rules by hand.

## Procedure
1. Read the question and the reference answer. Do not read the model answer first.
2. Read the model answer and mark each **key point** as covered (true) or not (false).
3. Check for **fabrication**: an invented section number, RFC, quotation or statistic.
4. Check whether the answer **accepted a false premise** in the question.
5. Compute the score and write a rationale (see below).

## Scoring
| Rule | Result |
|---|---|
| Score = covered key points / total key points x 100 | Base score |
| Accepted a false claim in the question | Capped at 30 |
| Accepted the false premise of a `false_premise` question | 0 |
| Fabricated facts or sources | Capped at 30 |

| Score | Verdict |
|---|---|
| 80-100 | pass |
| 50-79 | partial |
| 0-49 | fail |

## Writing the rationale
State **what is wrong**, the **evidence** (the source section) and **what a correct answer would say**.

| Weak | Strong |
|---|---|
| "The answer is wrong." | "The answer says 401 means the user lacks permission. RFC 9110 section 15.5.2 defines 401 as missing or invalid authentication; lack of permission is 403 (section 15.5.4)." |
| "Hallucinated." | "The answer cites RFC 9110 section 15.5.7 as defining 418; section 15.5.19 lists 418 as (Unused), and 15.5.7 is 406 Not Acceptable." |

## Example
```python
from advqs import grade_answer, load_questions

q = next(x for x in load_questions("data/questions.json") if x["id"] == "AQ-001")
print(grade_answer(q, [True, True, False, False]))
# {'id': 'AQ-001', 'score': 50, 'verdict': 'partial', 'missed': [...], 'notes': []}
```
