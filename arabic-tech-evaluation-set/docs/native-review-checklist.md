# Native Review Checklist

All 30 entries have `review_status: needs_native_review`. The Arabic prompts, answers and corrections were drafted for this project, including deliberate errors in the flawed responses. A native speaker must read everything before the project is published.

For each entry:
- [ ] The prompt reads naturally and is unambiguous
- [ ] Good responses (rating 5) contain no grammar, spelling or terminology problems
- [ ] The deliberate error in each flawed response is the error described in the tags, and no accidental extra error changes the verdict
- [ ] The corrected version is natural Modern Standard Arabic
- [ ] Terms in the glossary are the ones you would use or accept; add accepted alternatives to `accepted_ar`
- [ ] Punctuation and numerals follow the guideline

After checking an entry, change `review_status` to `native_reviewed` in `data/evaluations.json` and run `python -m arabic_eval data` to confirm that the file is still valid.

Known judgement calls to check first: the memory-types answer (AR-029), the wording of AR-024's corrected answer, and whether you prefer التعلم الآلي to تعلّم الآلة as the term for machine learning.
