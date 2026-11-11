# Evaluation Guidelines: Arabic Technology Responses

## Process for each response
1. Read the prompt and list every explicit requirement: language, register, count, length, format.
2. **Verify the facts first.** Fluent Arabic can carry a wrong fact; check numbers, definitions and sources.
3. Check the **terminology** against `data/glossary.csv`, then check grammar, spelling and register by reading closely.
4. Check the **formatting** of mixed text: Arabic punctuation, consistent numerals, Latin terms placed correctly.
5. Score each criterion 1 to 5 using the rubric, tag every error, choose an overall rating and write the rationale.
6. Write a corrected version for any response rated below 5.

## Modern Standard Arabic and dialects
- Use Modern Standard Arabic (MSA) unless the prompt asks for a dialect.
- A colloquial answer to an MSA request is an **instruction violation** and a **dialect mix**, even if the content is right.
- If the prompt asks for a dialect, judge naturalness within that dialect and do not penalise MSA-incompatible forms.

## Technical terminology
- Prefer the standard Arabic term; give the English term in brackets the first time when it helps (for example الحوسبة السحابية (Cloud Computing)).
- Latin abbreviations such as RAM, SQL, DNS and HTTP are normal. Transliterating a term into Arabic letters when a standard term exists (باسوورد, براوزر) is a `terminology_error`.
- Where several accepted terms exist, any accepted term is fine; use `accepted_ar` in the glossary.

## Formatting and right-to-left text
- Use Arabic punctuation in Arabic sentences: the Arabic comma ، the Arabic semicolon ؛ and the Arabic question mark ؟.
- Pick one numeral style (Western 0-9 or Arabic-Indic ٠-٩) and use it throughout one text.
- Keep Latin words and numbers inside the sentence they belong to; a Latin question mark after a Latin word will display on the wrong side.

## Translation
- Check meaning first (numbers, units, negation), then naturalness. A word-for-word rendering that sounds colloquial or foreign is an `unnatural_literal_translation`.

## Written rationale
State **what is wrong**, **why it matters** and **what correct looks like**.

| Weak | Strong |
|---|---|
| "Wrong." | "A byte has 8 bits, not 16. A simple, verifiable fact stated confidently and wrongly." |
| "Bad Arabic." | "The answer uses colloquial verbs although Modern Standard Arabic was requested explicitly; the content is otherwise correct." |
