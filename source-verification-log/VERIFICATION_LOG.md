# Verification Log

Each entry: the claim as an AI might state it, the verdict, the correct statement, a short evidence summary, the sources and the reviewer's written rationale.

## VL-001: CONTRADICTED (web_protocols)

> RFC 9110 defines status code 418 "I'm a teapot" as a standard response that servers can use.

**Error type:** factual_error | **Severity:** medium

**Correct statement:** RFC 9110 reserves 418 and lists it as (Unused) in section 15.5.19. The teapot response comes from the April Fools' RFC 2324.

**Evidence:** The IANA registry lists 418 as (Unused) and points to RFC 9110 section 15.5.19; HTTP libraries such as Go's net/http annotate it the same way.

**Sources:**

- [IANA HTTP Status Code Registry](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml), Entry for 418 (primary)
- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110), Sections 15.5.x (client error codes) (primary)
- [Go net/http status table (cites RFC 9110 section numbers)](https://go.googlesource.com/go/+/e46e861/src/net/http/status.go), StatusUnauthorized, StatusForbidden, StatusTeapot (secondary)

**Verification:** online_primary on 2026-10-22

**Rationale:** The claim reverses the registry state: 418 is reserved, not defined. A developer relying on it would ship a non-standard response. A correct answer cites section 15.5.19 and names RFC 2324 as the origin.

---

## VL-002: CONTRADICTED (web_protocols)

> RFC 9110 section 15.5.7 is where status code 418 is marked as unused.

**Error type:** wrong_citation | **Severity:** low

**Correct statement:** 418 (Unused) is in section 15.5.19. Section 15.5.7 defines 406 Not Acceptable.

**Evidence:** The IANA registry gives 418 as RFC 9110 section 15.5.19; Go's status table maps 406 to 15.5.7.

**Sources:**

- [IANA HTTP Status Code Registry](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml), Entry for 418 (primary)
- [Go net/http status table (cites RFC 9110 section numbers)](https://go.googlesource.com/go/+/e46e861/src/net/http/status.go), StatusUnauthorized, StatusForbidden, StatusTeapot (secondary)

**Verification:** online_primary on 2026-10-22

**Rationale:** The idea (418 is unused) is right but the section number is wrong, which makes the citation useless for anyone checking it. Wrong section numbers are a common sign of fabricated references and should be marked as citation errors even when the topic is correct.

---

## VL-003: CONTRADICTED (web_protocols)

> 401 Unauthorized is defined in RFC 9110 section 15.5.4.

**Error type:** wrong_citation | **Severity:** low

**Correct statement:** 401 Unauthorized is defined in section 15.5.2. Section 15.5.4 defines 403 Forbidden.

**Evidence:** Go's status table, which cites RFC 9110 numbering, maps 401 to 15.5.2 and 403 to 15.5.4.

**Sources:**

- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110), Sections 15.5.x (client error codes) (primary)
- [Go net/http status table (cites RFC 9110 section numbers)](https://go.googlesource.com/go/+/e46e861/src/net/http/status.go), StatusUnauthorized, StatusForbidden, StatusTeapot (secondary)

**Verification:** online_secondary_quote on 2026-10-22

**Rationale:** The section number belongs to a different status code (403), so a reader who opens it finds the wrong definition. The correct reference is 15.5.2. Open RFC 9110 directly to confirm before relying on a secondary mapping.

---

## VL-004: CONTRADICTED (web_protocols)

> RFC 7231 is the current standard for HTTP/1.1 semantics.

**Error type:** outdated_fact | **Severity:** medium

**Correct statement:** RFC 9110 (June 2022) obsoletes RFC 7231 and now defines HTTP semantics for HTTP/1.1, HTTP/2 and HTTP/3.

**Evidence:** The header of RFC 9110 lists RFC 7231 among the documents it obsoletes and is dated June 2022.

**Sources:**

- [RFC 9110: HTTP Semantics](https://datatracker.ietf.org/doc/html/rfc9110), Header: Obsoletes (primary)

**Verification:** online_primary on 2026-10-22

**Rationale:** The claim was true before June 2022 and is now outdated. Citing an obsoleted RFC sends readers to a superseded document. A correct answer names RFC 9110 and states the date.

---

## VL-005: CONTRADICTED (python)

> Python 3.14 removed the GIL completely.

**Error type:** overstatement | **Severity:** medium

**Correct statement:** Python 3.14 officially supports an optional free-threaded build (PEP 779, phase II). The default build still has the GIL.

**Evidence:** PEP 779 defines phase I as experimental, phase II as officially supported but optional, and phase III as making free-threading the default; 3.14 is phase II.

**Sources:**

- [PEP 779: Criteria for supported status for free-threaded Python](https://peps.python.org/pep-0779/), Phases I to III (primary)

**Verification:** online_primary on 2026-10-22

**Rationale:** The claim jumps from 'optional and supported' to 'removed'. Someone acting on it could assume default CPython runs threads in parallel. The correct statement separates the optional free-threaded build from the default build.

---

## VL-006: SUPPORTED (python)

> PEP 703 was accepted for Python 3.13 as an explicitly experimental feature.

**Error type:** none | **Severity:** none

**Correct statement:** PEP 703 was accepted for Python 3.13 as an experimental feature; PEP 779 later set criteria for supported status.

**Evidence:** The Python core developer discussion that introduced PEP 779 states that PEP 703 was accepted for 3.13 as an explicitly experimental feature.

**Sources:**

- [discuss.python.org: PEP 779 criteria thread](https://discuss.python.org/t/pep-779-criteria-for-supported-status-for-free-threaded-python/84319), Opening post (primary)
- [PEP 779: Criteria for supported status for free-threaded Python](https://peps.python.org/pep-0779/), Phases I to III (primary)

**Verification:** online_primary on 2026-10-22

**Rationale:** Checked against the core developers' own discussion and the PEP. The statement is accurate, dated correctly and does not overreach, so it passes.

---

## VL-007: CONTRADICTED (tech_history)

> CERN put the World Wide Web software into the public domain in 1991.

**Error type:** factual_error | **Severity:** medium

**Correct statement:** CERN issued the public-domain statement on 30 April 1993.

**Evidence:** CERN's licensing history states that on 30 April 1993 it put the line-mode client, the basic server and the common code library into the public domain.

**Sources:**

- [CERN: Licensing the Web](https://home.cern/science/computing/the-birth-of-the-web/licensing-web/), Public releases of Web software (primary)
- [CERN Timeline: CERN puts the World Wide Web in the public domain](https://timeline.web.cern.ch/node/794), Entry (primary)

**Verification:** online_primary on 2026-10-22

**Rationale:** 1991 is when the Web spread to other labs, not the licensing decision. The error confuses two events and misdates the one that mattered legally. A correct answer gives the exact date and names the three components.

---

## VL-008: CONTRADICTED (security)

> RFC 6151 says HMAC-MD5 is broken and must be removed from all existing protocols immediately.

**Error type:** overstatement | **Severity:** medium

**Correct statement:** RFC 6151 says attacks on HMAC-MD5 do not indicate a practical vulnerability as a MAC, that stopping existing use is not urgent, and that new designs should not employ it.

**Evidence:** RFC 6151 (March 2011) separates MD5 for signatures (unacceptable) from HMAC-MD5 (no practical vulnerability known; avoid in new designs).

**Sources:**

- [RFC 6151: Updated Security Considerations for MD5 and HMAC-MD5](https://www.rfc-editor.org/rfc/rfc6151), Sections 1-3 (March 2011) (primary)

**Verification:** online_primary on 2026-10-22

**Rationale:** The claim exaggerates the RFC. It could trigger needless emergency changes, or make readers dismiss the real point that MD5 must not be used for signatures. A correct answer keeps both parts of the RFC's position.

---

## VL-009: SUPPORTED (security)

> RFC 6151 states that MD5 is no longer acceptable for digital signatures.

**Error type:** none | **Severity:** none

**Correct statement:** RFC 6151 says MD5 is no longer acceptable where collision resistance is required, such as digital signatures.

**Evidence:** The RFC text states that MD5 is no longer acceptable where collision resistance is required, such as digital signatures.

**Sources:**

- [RFC 6151: Updated Security Considerations for MD5 and HMAC-MD5](https://www.rfc-editor.org/rfc/rfc6151), Sections 1-3 (March 2011) (primary)

**Verification:** online_primary on 2026-10-22

**Rationale:** The claim is accurate, attributed to the right document and date, and does not overstate what the RFC says about MD5, so it passes verification.

---

## VL-010: CONTRADICTED (security)

> NIST still allows SHA-1 for generating new digital signatures.

**Error type:** outdated_fact | **Severity:** high

**Correct statement:** NIST deprecated SHA-1 for generating new digital signatures in SP 800-131A (2011) and plans to complete its transition away from SHA-1 by 31 December 2030.

**Evidence:** NIST's 2022 announcement says SP 800-131A deprecated SHA-1 for new digital signatures in 2011 and that the transition away from SHA-1 will be completed by the end of 2030.

**Sources:**

- [NIST: Transitioning Away from SHA-1 for All Applications](https://csrc.nist.gov/news/2022/nist-transitioning-away-from-sha-1-for-all-apps), Announcement of 15 December 2022 (primary)

**Verification:** online_primary on 2026-10-22

**Rationale:** A security-relevant claim that is wrong: relying on it could lead to non-compliant or weak signature schemes. Severity is high because users act on cryptographic guidance. The correct answer names the 2011 deprecation and the 2030 deadline.

---

## VL-011: SUPPORTED (security)

> NIST plans to complete its transition away from SHA-1 by 31 December 2030.

**Error type:** none | **Severity:** none

**Correct statement:** NIST announced on 15 December 2022 that its transition away from SHA-1 will be completed by 31 December 2030.

**Evidence:** The NIST announcement gives 31 December 2030 as the completion date for the transition.

**Sources:**

- [NIST: Transitioning Away from SHA-1 for All Applications](https://csrc.nist.gov/news/2022/nist-transitioning-away-from-sha-1-for-all-apps), Announcement of 15 December 2022 (primary)

**Verification:** online_primary on 2026-10-22

**Rationale:** The date, the organization and the scope of the claim all match the primary NIST announcement exactly, so the claim passes verification.

---

## VL-012: CONTRADICTED (tech_industry)

> Windows 10 reaches end of support in October 2026.

**Error type:** outdated_fact | **Severity:** medium

**Correct statement:** Windows 10 Home and Pro reached end of support on 14 October 2025.

**Evidence:** Microsoft's lifecycle page for Windows 10 Home and Pro lists 14 October 2025 as the retirement date.

**Sources:**

- [Microsoft Lifecycle: Windows 10 Home and Pro](https://learn.microsoft.com/en-us/lifecycle/products/windows-10-home-and-pro), Support dates (primary)

**Verification:** online_primary on 2026-10-22

**Rationale:** The date is off by one year. For a planning or compliance question this error matters, because the system is already unsupported. The correct answer cites the Microsoft lifecycle page.

---

## VL-013: CONTRADICTED (tech_industry)

> As of October 2026, Windows 10 Home and Pro still receive free monthly security updates.

**Error type:** outdated_fact | **Severity:** high

**Correct statement:** Free security updates for Windows 10 Home and Pro ended on 14 October 2025 when support retired.

**Evidence:** Microsoft's lifecycle page gives 14 October 2025 as the end of support for Windows 10 Home and Pro, with 22H2 as the final version.

**Sources:**

- [Microsoft Lifecycle: Windows 10 Home and Pro](https://learn.microsoft.com/en-us/lifecycle/products/windows-10-home-and-pro), Support dates (primary)

**Verification:** online_primary on 2026-10-22

**Rationale:** A user relying on this would keep unsupported systems online believing they are patched. Severity is high because the consequence is a security exposure. Any paid extended-update programs are separate and should be named explicitly.

---

## VL-014: PARTIALLY SUPPORTED (python)

> Python 2.7 support ended in April 2020 with the release of 2.7.18.

**Error type:** factual_error | **Severity:** low

**Correct statement:** Support officially ended on 1 January 2020. Python 2.7.18, released on 20 April 2020, bundled the last fixes made before that date.

**Evidence:** Python.org says support ended on 1 January 2020 and that 2.7.18 was released in April 2020 for convenience; PEP 373 lists the 2.7.18 release date as 2020-04-20.

**Sources:**

- [Python.org: Sunsetting Python 2](https://python.org/doc/sunset-python-2/), Whole page (primary)
- [PEP 373: Python 2.7 Release Schedule](https://peps.python.org/pep-0373/), Maintenance releases (primary)

**Verification:** online_primary on 2026-10-22

**Rationale:** The release date is right but the claim treats the last release as the end of support, which blurs the official sunset date. Mark as partially supported and ask for the January 2020 date.

---

## VL-015: CONTRADICTED (data_formats)

> Under the current JSON standard, JSON sent between systems can be encoded in UTF-8, UTF-16 or UTF-32 with equal validity.

**Error type:** outdated_fact | **Severity:** medium

**Correct statement:** RFC 8259 section 8.1 requires UTF-8 for JSON exchanged between systems that are not part of a closed ecosystem. Older RFC 7159 was looser.

**Evidence:** RFC 8259 section 8.1, as quoted in several public discussions, says JSON text exchanged outside a closed ecosystem MUST be encoded using UTF-8.

**Sources:**

- [RFC 8259: The JSON Data Interchange Format](https://datatracker.ietf.org/doc/html/rfc8259#section-8.1), Section 8.1 Character Encoding (primary)
- [Public quotations of RFC 8259 section 8.1 (httpx project discussion)](https://github.com/encode/httpx/pull/2911), RFC 8259 section 8.1 text as quoted (secondary)

**Verification:** online_secondary_quote on 2026-10-22

**Rationale:** The claim describes the older, looser rule. The primary RFC page should be opened to confirm the wording before this entry is relied on, because here the wording was confirmed through quotations.

---

## VL-016: CONTRADICTED (data_formats)

> RFC 8259 says JSON parsers must reject any text that starts with a byte order mark.

**Error type:** overstatement | **Severity:** low

**Correct statement:** RFC 8259 says implementations MUST NOT add a byte order mark to networked JSON text; parsers MAY ignore a BOM instead of treating it as an error.

**Evidence:** Quoted text of RFC 8259 section 8.1 forbids generators from adding a BOM and allows parsers to ignore one.

**Sources:**

- [RFC 8259: The JSON Data Interchange Format](https://datatracker.ietf.org/doc/html/rfc8259#section-8.1), Section 8.1 Character Encoding (primary)
- [Public quotations of RFC 8259 section 8.1 (httpx project discussion)](https://github.com/encode/httpx/pull/2911), RFC 8259 section 8.1 text as quoted (secondary)

**Verification:** online_secondary_quote on 2026-10-22

**Rationale:** The rule applies to generators; the parser rule is permissive. Reversing MUST NOT and MAY changes what a conforming implementation does. Open the primary text to confirm before relying on this entry.

---

## VL-017: CONTRADICTED (python)

> Python's sorted() is not stable, so equal elements can change their relative order.

**Error type:** factual_error | **Severity:** medium

**Correct statement:** Python's sort is guaranteed stable: equal elements keep their original relative order.

**Evidence:** A run with records that share a key shows the original order preserved among equal keys.

**Sources:**

- [Python HOWTO: Sorting](https://docs.python.org/3/howto/sorting.html#sort-stability-and-complex-sorts), Sort stability and complex sorts (primary)

**Verification:** executed_locally on 2026-10-22 (test: `test_sorted_is_stable`)

**Rationale:** Stability is documented and testable. Believing the claim would lead developers to add unnecessary workarounds or to distrust multi-key sorting. Reproduced with a short test.

---

## VL-018: CONTRADICTED (python)

> In Python, a is b is True whenever a == b.

**Error type:** factual_error | **Severity:** medium

**Correct statement:** The is operator tests object identity; == tests equality. Two equal lists are different objects.

**Evidence:** Two lists with the same contents compare equal but are not the same object.

**Sources:**

- [Python Language Reference: Comparisons](https://docs.python.org/3/reference/expressions.html#is-not), Identity comparisons (primary)

**Verification:** executed_locally on 2026-10-22 (test: `test_is_compares_identity_not_equality`)

**Rationale:** Confusing identity and equality causes real bugs, such as comparing strings or lists with is. The claim is easy to disprove with a two-line test.

---

## VL-019: CONTRADICTED (python)

> In Python, -7 // 2 equals -3 because integer division truncates toward zero.

**Error type:** factual_error | **Severity:** medium

**Correct statement:** Python's // floors toward negative infinity, so -7 // 2 equals -4.

**Evidence:** Evaluating -7 // 2 returns -4, and divmod(-7, 2) returns (-4, 1).

**Sources:**

- [Python Language Reference: Binary arithmetic operations](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations), Floor division (primary)

**Verification:** executed_locally on 2026-10-22 (test: `test_floor_division_rounds_down`)

**Rationale:** Truncation toward zero is how C and Java behave, so the claim imports another language's rule. The result affects any code that handles negative numbers.

---

## VL-020: CONTRADICTED (python)

> bool('False') evaluates to False in Python.

**Error type:** factual_error | **Severity:** low

**Correct statement:** Any non-empty string is truthy, so bool('False') is True.

**Evidence:** Evaluating bool('False') returns True, while bool('') returns False.

**Sources:**

- [Python Standard Library: Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing), Built-in truthiness rules (primary)

**Verification:** executed_locally on 2026-10-22 (test: `test_non_empty_string_is_truthy`)

**Rationale:** The claim treats the text of the string as its meaning. This is a classic bug when parsing configuration values, and it is easy to reproduce.

---

## VL-021: CONTRADICTED (python)

> Because tuples are immutable, nothing inside a tuple can ever change.

**Error type:** overstatement | **Severity:** medium

**Correct statement:** A tuple cannot rebind its items, but a mutable object inside a tuple, such as a list, can still change.

**Evidence:** A tuple holding a list shows the changed list after an append, without any change to the tuple's own items.

**Sources:**

- [Python Language Reference: Data model](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types), Objects, values and types (primary)

**Verification:** executed_locally on 2026-10-22 (test: `test_tuple_can_hold_mutable_objects`)

**Rationale:** The claim is true of the tuple's structure but false of its contents, which makes it an overgeneralization. It matters for hashing and shared state.

---

## VL-022: CONTRADICTED (python)

> round(2.5) returns 3 in Python 3.

**Error type:** factual_error | **Severity:** low

**Correct statement:** Python 3 rounds half to even, so round(2.5) returns 2 and round(3.5) returns 4.

**Evidence:** Evaluating round(2.5) returns 2 and round(3.5) returns 4.

**Sources:**

- [Python Standard Library: Built-in Functions](https://docs.python.org/3/library/functions.html#round), round() (primary)

**Verification:** executed_locally on 2026-10-22 (test: `test_round_half_to_even`)

**Rationale:** School-style rounding is assumed instead of the documented rule. The difference shows up in financial and statistical code.

---

## VL-023: CONTRADICTED (databases)

> SQLite cannot drop a column; ALTER TABLE ... DROP COLUMN is not supported.

**Error type:** outdated_fact | **Severity:** medium

**Correct statement:** SQLite supports ALTER TABLE ... DROP COLUMN since version 3.35.0 (March 2021).

**Evidence:** On the SQLite version used for the check (3.35.0 or later), ALTER TABLE DROP COLUMN succeeds and the column is removed.

**Sources:**

- [SQLite Documentation: ALTER TABLE](https://www.sqlite.org/lang_altertable.html), DROP COLUMN (primary)

**Verification:** executed_locally on 2026-10-22 (test: `test_sqlite_supports_drop_column`)

**Rationale:** The claim was true for older versions and is now outdated. The behavior was reproduced locally; open the SQLite page to confirm the exact version number before publishing.

---

## VL-024: SUPPORTED (python)

> In Python, 0.1 + 0.2 == 0.3 evaluates to False.

**Error type:** none | **Severity:** none

**Correct statement:** The comparison is False because the binary floating-point sum is 0.30000000000000004.

**Evidence:** Evaluating the expression returns False and the sum prints as 0.30000000000000004.

**Sources:**

- [Python Tutorial: Floating-Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html), Whole page (primary)

**Verification:** executed_locally on 2026-10-22 (test: `test_float_sum_is_not_exact`)

**Rationale:** Correct and reproducible. The statement does not blame Python, which is the usual error in explanations, so it passes.

---

## VL-025: SUPPORTED (python)

> Python's list.sort() is stable.

**Error type:** none | **Severity:** none

**Correct statement:** Python's sort is stable: equal elements keep their original relative order.

**Evidence:** A run with records sharing a key keeps the original order among equal keys.

**Sources:**

- [Python HOWTO: Sorting](https://docs.python.org/3/howto/sorting.html#sort-stability-and-complex-sorts), Sort stability and complex sorts (primary)

**Verification:** executed_locally on 2026-10-22 (test: `test_list_sort_is_stable`)

**Rationale:** Matches the documentation and the local test. This is the counterpart of the earlier false claim about sorted(), included to show that correct claims must also be confirmed, not assumed.

---

## VL-026: SUPPORTED (python)

> In Python, bool is a subclass of int, so True + True equals 2.

**Error type:** none | **Severity:** none

**Correct statement:** bool is a subclass of int; True behaves as 1 and False as 0, so True + True is 2.

**Evidence:** issubclass(bool, int) returns True and True + True returns 2.

**Sources:**

- [Python Standard Library: Built-in Functions](https://docs.python.org/3/library/functions.html#bool), class bool (primary)

**Verification:** executed_locally on 2026-10-22 (test: `test_bool_is_int_subclass`)

**Rationale:** The claim is correct and reproducible, and it gives the right reasoning (the subclass relationship) behind the result, so it passes verification.

---

## VL-027: UNVERIFIABLE (python)

> Python 3.16 will make the free-threaded build the default.

**Error type:** unsupported_prediction | **Severity:** low

**Correct statement:** No accepted proposal makes the free-threaded build the default in any named Python version. PEP 779 treats that step (phase III) as a future decision.

**Evidence:** PEP 779 describes phase III, making the free-threaded build the default, as a later step that would need a future proposal.

**Sources:**

- [PEP 779: Criteria for supported status for free-threaded Python](https://peps.python.org/pep-0779/), Phases I to III (primary)

**Verification:** online_primary on 2026-10-22

**Rationale:** A specific version and outcome are stated as fact, but the primary source leaves the decision open. The claim cannot be verified today. It would be resolved by an accepted PEP or a Steering Council decision naming the version.

---
