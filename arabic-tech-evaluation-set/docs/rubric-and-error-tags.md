# Rubric and Error Tags

## Criteria and weights
| Criterion | Weight | What it covers |
|---|---|---|
| technical_accuracy | 35% | Facts, definitions, numbers, sources |
| terminology | 20% | Standard Arabic technical terms |
| language_quality | 20% | Grammar, spelling, fluency, register |
| instruction_following | 15% | Language, count, length, format |
| formatting | 10% | Arabic punctuation, numerals, mixed-direction text |

Each criterion is scored 1 to 5. The weighted result is a score from 0 to 100.

## Gates (caps for serious problems)
| Condition | Maximum score | Why |
|---|---|---|
| technical_accuracy 2 or lower | 40 | A wrong core fact cannot be offset by good language |
| instruction_following 2 or lower | 60 | An explicit instruction was ignored |
| language_quality 2 or lower | 60 | Serious language problems |
| fabricated source | 20 | An invented source is the most damaging error |

## Overall rating
The overall rating (1-5) must stay within one point of the score band: 0-20 is 1, 20-40 is 2, 40-60 is 3, 60-80 is 4 and 80-100 is 5. The validator rejects larger gaps, which catches rating mistakes.

## Error tags
| Tag | Meaning |
|---|---|
| factual_error | A statement is false |
| fabricated_source | A cited document or reference does not exist or does not say that |
| terminology_error | Wrong term or unnecessary transliteration |
| grammar_error | Agreement, case or syntax mistakes |
| spelling_error | Hamza, letter or word spelling mistakes |
| dialect_mix | Colloquial forms where Modern Standard Arabic is expected |
| mistranslation | The meaning changed in translation |
| unnatural_literal_translation | Word-for-word rendering that sounds unnatural |
| rtl_formatting_issue | Latin punctuation or misplaced mixed-direction text |
| instruction_violation | An explicit instruction was not followed |
| omission | A required part is missing |

## Consistency rules enforced by the validator
- Low scores need an explaining error tag, and error tags cannot go with all-5 scores
- A response below 5 must come with a corrected version
- A fabricated source must be rated 1
- Rationales have at least 15 words
