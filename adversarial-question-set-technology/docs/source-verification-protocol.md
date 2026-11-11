# Source Verification Protocol

Every reference answer must be backed by an authoritative source or reproduced by code.

## Source hierarchy
1. **Primary:** standards and specifications (IETF RFCs, W3C/WHATWG, ECMAScript, ISO/POSIX), official project documentation (Python, PostgreSQL, Git), the originating institution (CERN), original papers.
2. **Secondary (only to find the primary):** reputable technical references such as MDN Web Docs and OWASP cheat sheets.
3. **Never sufficient alone:** blogs, forums, social media and AI-generated summaries.

## Steps
1. Locate the exact section or page that states the fact; record `title`, `reference` and `url`.
2. Check the **date and version** of the source. Facts about versions or standards status must be dated.
3. For anything executable (code behavior, arithmetic, SQL), **run it** and keep the check in `tests/test_executable_facts.py`.
4. For volatile facts (software versions, deprecations), confirm with at least two independent sources or the project's own release notes.
5. Record the result in the question's `verification` field.

## Verification statuses
| Status | Meaning |
|---|---|
| `primary_source_checked_online` | Section numbers or dates were confirmed against the cited source on the stated date |
| `executed_locally` | The answer was reproduced by running code that is part of the test suite |
| `needs_manual_check` | Drafted from known documentation; confirm the section before publishing (see `verification-checklist.md`) |
| `verified_by_author` | The author opened the source and confirmed the wording on the stated date |

## Red flags when checking a model answer
- A confident quote with no section number
- A source that exists but does not say what is claimed
- An RFC, PEP or section number that is close to the right one but wrong
- Facts that were true for an older version
