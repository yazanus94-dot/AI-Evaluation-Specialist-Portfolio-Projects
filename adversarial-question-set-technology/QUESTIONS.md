# Question Catalogue

Each entry has the question, the reference answer, the gradable key points, the trap and the source.

## AQ-001: web_protocols | difficulty 2 | trap: subtle_distinction

**Question**

> A REST API receives a request carrying a valid access token for user Sam, but Sam's role does not allow deleting invoices. A second request arrives with no token at all. Which HTTP status code should the server return for each request, and which of the two code names is misleading?

**Reference answer:** Return 403 Forbidden for Sam (the server understood the request and the identity but refuses to authorize it). Return 401 Unauthorized for the request with no token, together with a WWW-Authenticate header. The misleading name is 401: despite 'Unauthorized', it means the request lacks valid authentication credentials.

**Key points to grade:**

1. Sam's request gets 403 Forbidden
2. The tokenless request gets 401
3. 401 means unauthenticated, not unauthorized
4. 401 responses include a WWW-Authenticate header

**Expected model failure:** Swaps the two codes or returns 401 for both, trusting the name 'Unauthorized'.

**Why it is hard:** The code names conflict with their meanings, so a model must recall the specification rather than the label.

**Source:** [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110), Sections 15.5.2 (401) and 15.5.4 (403)

**Verification:** primary_source_checked_online (2026-10-22)

---

## AQ-002: web_protocols | difficulty 3 | trap: false_premise

**Question**

> RFC 9110 defines status code 418 'I'm a teapot' as a standard HTTP response that servers may use to reject requests. In which section does it define the behavior of 418?

**Reference answer:** The premise is false. RFC 9110 does not define behavior for 418: it lists 418 as '(Unused)' in section 15.5.19 and reserves it. The 'I'm a teapot' response comes from RFC 2324 (HTCPCP), an April Fools' RFC published on 1 April 1998.

**Key points to grade:**

1. Rejects the premise
2. 418 is marked (Unused) in RFC 9110 section 15.5.19
3. Origin is RFC 2324 (HTCPCP), an April Fools' RFC
4. Should not be used as a normal application error

**Expected model failure:** Accepts the premise and invents a section describing 418 behavior.

**Why it is hard:** The question presupposes something false and sounds plausible; a model has to know both the joke RFC and the current registry state.

**Source:** [RFC 9110: HTTP Semantics (and IANA HTTP Status Code Registry)](https://www.rfc-editor.org/rfc/rfc9110), Section 15.5.19; RFC 2324

**Verification:** primary_source_checked_online (2026-10-22)

---

## AQ-003: security | difficulty 2 | trap: outdated_fact

**Question**

> A scanner flags a server that still accepts TLS 1.1. A colleague says this is fine because only TLS 1.0 was deprecated and TLS 1.1 is newer. Evaluate this claim and name the document that applies.

**Reference answer:** The claim is wrong. RFC 8996 (March 2021), 'Deprecating TLS 1.0 and TLS 1.1', deprecates both versions (and DTLS 1.0): they must not be negotiated. Servers should require at least TLS 1.2, and TLS 1.3 (RFC 8446) is preferred.

**Key points to grade:**

1. Claim is incorrect
2. RFC 8996 deprecates both TLS 1.0 and TLS 1.1
3. Published March 2021
4. Minimum should be TLS 1.2, ideally TLS 1.3

**Expected model failure:** Says only TLS 1.0 is deprecated, or cites an older date or the wrong RFC.

**Why it is hard:** Requires current standards status, and 'newer therefore safe' sounds reasonable.

**Source:** [RFC 8996: Deprecating TLS 1.0 and TLS 1.1](https://www.rfc-editor.org/rfc/rfc8996), Abstract and Section 1

**Verification:** needs_manual_check

---

## AQ-004: web_protocols | difficulty 3 | trap: subtle_distinction

**Question**

> A client sends DELETE /orders/42 twice. The first response is 204 No Content and the second is 404 Not Found. A teammate says this proves DELETE is not idempotent. Is the teammate correct? Also state whether PUT and POST are defined as idempotent methods.

**Reference answer:** The teammate is incorrect. Idempotent means that the intended effect on the server of several identical requests is the same as for one request; the responses do not have to be identical. After the first DELETE the order is gone and the second changes nothing. PUT and DELETE are idempotent; POST is not defined as idempotent.

**Key points to grade:**

1. Teammate is wrong
2. Idempotency concerns server state, not identical responses
3. PUT and DELETE are idempotent
4. POST is not defined as idempotent

**Expected model failure:** Agrees with the teammate because the status codes differ, or says POST is idempotent.

**Why it is hard:** Confuses 'same effect' with 'same response', a common reasoning slip.

**Source:** [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110), Section 9.2.2 (Idempotent Methods)

**Verification:** needs_manual_check

---

## AQ-005: security | difficulty 3 | trap: misconception

**Question**

> Assuming TLS 1.3 with no additional privacy extension, which of these can a network observer between you and the website see: the hostname you connect to, the URL path and query string, and the request headers? Answer each separately.

**Reference answer:** The hostname is visible, because the Server Name Indication (SNI) in the ClientHello is sent in plaintext, and the destination IP address is also visible. The URL path, query string and request headers are encrypted. DNS lookups are also visible unless DNS over HTTPS/TLS is used. Encrypted Client Hello (ECH) can hide the SNI where supported.

**Key points to grade:**

1. Hostname visible via SNI
2. Destination IP visible
3. Path, query and headers are encrypted
4. DNS queries leak unless encrypted

**Expected model failure:** Says 'HTTPS hides everything except the IP' or claims the hostname is encrypted by TLS 1.3 alone.

**Why it is hard:** A popular half-truth: models over-generalize the privacy of HTTPS.

**Source:** [RFC 6066: TLS Extensions (Server Name Indication); RFC 8446: TLS 1.3](https://www.rfc-editor.org/rfc/rfc6066), RFC 6066 Section 3; RFC 8446 Section 4.1.2

**Verification:** needs_manual_check

---

## AQ-006: security | difficulty 3 | trap: misconception

**Question**

> A developer writes: 'We configured CORS on our API, so scripts from other websites and tools like curl can no longer send requests to it.' What is wrong with this statement?

**Reference answer:** CORS is enforced by browsers: it controls whether JavaScript from another origin may read a response. It does not stop curl, servers or other non-browser clients, and a browser may still send a cross-origin 'simple' request (the side effects happen) even when the page cannot read the answer. CORS is not authentication or authorization; use proper auth and CSRF protection.

**Key points to grade:**

1. CORS is browser-enforced
2. Does not block curl or non-browser clients
3. Simple requests can still be sent and have effects
4. Not a substitute for authentication or CSRF protection

**Expected model failure:** Treats CORS as a server-side access control or firewall.

**Why it is hard:** The model must separate what is enforced by the browser from what the server enforces.

**Source:** [Fetch Standard: CORS protocol](https://fetch.spec.whatwg.org/#http-cors-protocol), Section 'HTTP extensions' / CORS protocol

**Verification:** needs_manual_check

---

## AQ-007: networking | difficulty 3 | trap: numerical

**Question**

> For the IPv4 address 192.168.10.100/26, give the network address, the broadcast address and the number of usable host addresses under the conventional rules for a normal subnet.

**Reference answer:** Network 192.168.10.64, broadcast 192.168.10.127, 62 usable hosts (192.168.10.65 to 192.168.10.126). A /26 has 64 addresses in blocks of 64: .0, .64, .128, .192; .100 falls in the .64 block.

**Key points to grade:**

1. Network address 192.168.10.64
2. Broadcast address 192.168.10.127
3. 62 usable hosts
4. Block size is 64

**Expected model failure:** Gives 192.168.10.0 as the network, or counts 64 or 63 usable hosts.

**Why it is hard:** Needs block-size arithmetic, not memorized subnet masks.

**Source:** [RFC 4632: Classless Inter-domain Routing (CIDR)](https://www.rfc-editor.org/rfc/rfc4632), Section 3 (address prefix notation)

**Verification:** executed_locally (2026-10-22)

---

## AQ-008: networking | difficulty 4 | trap: over_generalization

**Question**

> A company wants example.com (the zone apex) to point to a hosting provider using a CNAME record, while keeping the existing MX and NS records at example.com. Will this work under the DNS specifications? Explain why and name the common workaround.

**Reference answer:** It will not work. A CNAME record cannot coexist with other record types at the same owner name (RFC 1034 section 3.6.2; RFC 2181 section 10.1), and the apex must hold SOA and NS records (and here MX). The usual workaround is a provider feature such as ALIAS/ANAME or CNAME flattening, which answers with A/AAAA records, or publishing A/AAAA records directly. (DNSSEC records such as RRSIG and NSEC are the exception.)

**Key points to grade:**

1. CNAME cannot coexist with other records at the same name
2. Apex always has SOA and NS
3. Workaround: ALIAS/ANAME/CNAME flattening or A/AAAA records

**Expected model failure:** Says it works, or says CNAME at the apex is only 'discouraged'.

**Why it is hard:** Real-world practice (flattening) hides a hard protocol rule; models blur the two.

**Source:** [RFC 1034: Domain Names - Concepts and Facilities; RFC 2181](https://www.rfc-editor.org/rfc/rfc1034), RFC 1034 Section 3.6.2; RFC 2181 Section 10.1

**Verification:** needs_manual_check

---

## AQ-009: security | difficulty 4 | trap: misconception

**Question**

> MD5 is considered cryptographically broken. Does that mean HMAC-MD5 is broken in the same way, and is MD5 acceptable for digital signatures?

**Reference answer:** MD5 must not be used for digital signatures or anywhere collision resistance is required. HMAC-MD5 is not broken in the same way: RFC 6151 (March 2011) says the attacks on HMAC-MD5 do not seem to indicate a practical vulnerability when it is used as a message authentication code, and that it is not urgent to stop using it in existing protocols. However, new protocol designs should not employ HMAC-MD5; HMAC-SHA-256 is an alternative.

**Key points to grade:**

1. MD5 unacceptable for digital signatures
2. No practical vulnerability known for HMAC-MD5 as a MAC (RFC 6151)
3. Not urgent to replace existing use, but new designs should not employ HMAC-MD5

**Expected model failure:** Says HMAC-MD5 is equally broken, or that MD5 is fine because it is 'only broken for passwords'.

**Why it is hard:** Requires separating collision resistance from MAC security.

**Source:** [RFC 6151: Updated Security Considerations for the MD5 Message-Digest and the HMAC-MD5 Algorithms](https://www.rfc-editor.org/rfc/rfc6151), Sections 1-3 (March 2011)

**Verification:** primary_source_checked_online (2026-10-22)

---

## AQ-010: security | difficulty 2 | trap: misconception

**Question**

> A startup stores user passwords encrypted with AES-256, keeping the key in the application server's configuration file, and argues this is stronger than hashing. Evaluate the design and state what should be used instead.

**Reference answer:** It is a poor design: encryption is reversible, and a server compromise also exposes the key, so all passwords can be recovered. Passwords should be stored with a slow, salted password hashing function such as Argon2id (preferred), scrypt, bcrypt or PBKDF2 with a high work factor, using a unique salt per password.

**Key points to grade:**

1. Encryption is reversible and the key sits on the same server
2. Use a password hashing function (Argon2id, scrypt, bcrypt, PBKDF2)
3. Unique salt per password
4. Work factor makes brute force expensive

**Expected model failure:** Praises AES-256 as 'military grade' and approves the design.

**Why it is hard:** 'Stronger algorithm' sounds persuasive but misses the threat model.

**Source:** [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html), Algorithm choice and salting sections

**Verification:** needs_manual_check

---

## AQ-011: databases | difficulty 3 | trap: edge_case

**Question**

> A table users has 10 rows and 3 of them have email = NULL. What do these queries return? (1) SELECT COUNT(*) FROM users WHERE email = NULL; (2) SELECT COUNT(email) FROM users; (3) SELECT COUNT(*) FROM users WHERE email <> 'a@x.com'; assume no row has that exact email.

**Reference answer:** (1) 0, because comparing with NULL yields UNKNOWN, not true; use IS NULL, which would return 3. (2) 7, because COUNT(column) ignores NULLs. (3) 7, because NULL <> 'a@x.com' is UNKNOWN, so the 3 NULL rows are excluded.

**Key points to grade:**

1. Query 1 returns 0 (use IS NULL for 3)
2. Query 2 returns 7
3. Query 3 returns 7, not 10
4. Three-valued logic: comparison with NULL is UNKNOWN

**Expected model failure:** Answers 3 for query 1 and 10 for query 3.

**Why it is hard:** Needs three-valued logic applied to three different queries.

**Source:** [PostgreSQL Documentation: Comparison Functions and Operators](https://www.postgresql.org/docs/current/functions-comparison.html), NULL handling in comparisons

**Verification:** executed_locally (2026-10-22)

---

## AQ-012: databases | difficulty 4 | trap: misconception

**Question**

> A blog states: 'The C in ACID and the C in the CAP theorem both mean consistency, so an ACID-compliant database is automatically CAP-consistent.' Evaluate this claim.

**Reference answer:** The claim is wrong because the two terms mean different things. Consistency in ACID means a transaction takes the database from one valid state to another, preserving defined constraints and invariants. Consistency in CAP means linearizability (atomic consistency) across replicas. An ACID database on one node says nothing about linearizability across a replicated, partitioned system; CAP says that during a network partition a system must choose between consistency and availability.

**Key points to grade:**

1. Different meanings of 'consistency'
2. ACID C = preserves invariants/constraints
3. CAP C = linearizability across replicas
4. CAP trade-off applies during partitions

**Expected model failure:** Treats both as the same concept and agrees with the blog.

**Why it is hard:** Same word, different formal definitions; a model must know both sources.

**Source:** Gilbert and Lynch (2002), Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services; Haerder and Reuter (1983), Principles of transaction-oriented database recovery, CAP definition of atomic consistency; ACID paper

**Verification:** needs_manual_check

---

## AQ-013: python | difficulty 2 | trap: numerical

**Question**

> In Python, what does print(0.1 + 0.2 == 0.3) output, why, and what is the recommended way to compare the two values?

**Reference answer:** It prints False. 0.1 and 0.2 cannot be represented exactly in binary floating point, and the sum is 0.30000000000000004. Compare with a tolerance, for example math.isclose(0.1 + 0.2, 0.3), or use decimal.Decimal when exact decimal arithmetic is needed.

**Key points to grade:**

1. Prints False
2. Binary floating point cannot represent 0.1 and 0.2 exactly
3. Sum is 0.30000000000000004
4. Use math.isclose or Decimal

**Expected model failure:** Says it prints True, or blames a Python bug.

**Why it is hard:** Easy to state, but models sometimes 'round' mentally.

**Source:** [Python Tutorial: Floating-Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html), Whole page

**Verification:** executed_locally (2026-10-22)

---

## AQ-014: python | difficulty 3 | trap: multi_step_reasoning

**Question**

> What does this Python program print?
> 
> def add(x, items=[]):
>     items.append(x)
>     return items
> 
> a = add(1)
> b = add(2)
> c = add(3, [])
> print(a, b, c, a is b)

**Reference answer:** It prints: [1, 2] [1, 2] [3] True. The default list is created once, when the function is defined, so the first two calls share it and a and b are the same object. The third call passes a new list.

**Key points to grade:**

1. Output is [1, 2] [1, 2] [3] True
2. Default argument evaluated once at definition time
3. a and b are the same list

**Expected model failure:** Predicts [1] [2] [3] False.

**Why it is hard:** Requires tracing object identity across three calls.

**Source:** [Python Tutorial: Default Argument Values](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values), More on Defining Functions, important warning about mutable defaults

**Verification:** executed_locally (2026-10-22)

---

## AQ-015: python | difficulty 2 | trap: subtle_distinction

**Question**

> In Python, what is the value of True + True, does isinstance(True, int) return True, and what does sum([True, False, True]) return?

**Reference answer:** True + True is 2, isinstance(True, int) is True, and sum([True, False, True]) is 2. bool is a subclass of int, with True equal to 1 and False equal to 0.

**Key points to grade:**

1. True + True equals 2
2. isinstance(True, int) is True
3. sum([True, False, True]) equals 2
4. bool is a subclass of int

**Expected model failure:** Says True + True is an error or True.

**Why it is hard:** Tests knowledge of the type hierarchy rather than syntax.

**Source:** [Python Documentation: Built-in Functions, class bool](https://docs.python.org/3/library/functions.html#bool), bool is a subclass of int

**Verification:** executed_locally (2026-10-22)

---

## AQ-016: unicode_time | difficulty 4 | trap: multi_step_reasoning

**Question**

> In the ISO 8601 week-date system, which ISO year, week number and weekday number does 1 January 2021 fall in?

**Reference answer:** ISO year 2020, week 53, weekday 5 (Friday). ISO week 1 is the week containing the first Thursday of the year; 1 January 2021 is a Friday, so it belongs to the last week of 2020, and 2020 has 53 ISO weeks.

**Key points to grade:**

1. ISO year 2020
2. Week 53
3. Weekday 5 (Friday)
4. Week 1 contains the first Thursday

**Expected model failure:** Answers 2021, week 1.

**Why it is hard:** The calendar year and the ISO year differ, and the rule must be applied in several steps.

**Source:** [Python Documentation: datetime.date.isocalendar()](https://docs.python.org/3/library/datetime.html#datetime.date.isocalendar), date.isocalendar()

**Verification:** executed_locally (2026-10-22)

---

## AQ-017: unicode_time | difficulty 4 | trap: subtle_distinction

**Question**

> In Python 3, len('é') can be 1 or 2 depending on how the string was created. Explain how both can happen and give the UTF-8 byte length in each case.

**Reference answer:** The character can be one code point, U+00E9 (precomposed), giving len 1 and 2 bytes in UTF-8, or two code points, 'e' followed by U+0301 (combining acute accent), giving len 2 and 3 bytes (1 + 2). The two strings look identical but compare unequal until normalized (NFC or NFD).

**Key points to grade:**

1. Precomposed U+00E9: len 1, 2 UTF-8 bytes
2. Decomposed e + U+0301: len 2, 3 UTF-8 bytes
3. Strings look the same but are not equal
4. Normalization (NFC/NFD) resolves it

**Expected model failure:** Says len is always 1 and 'é' is always 2 bytes.

**Why it is hard:** Requires separating code points, bytes and visual characters.

**Source:** [Unicode Standard Annex #15: Unicode Normalization Forms; RFC 3629: UTF-8](https://unicode.org/reports/tr15/), UAX #15 introduction; RFC 3629 Section 3

**Verification:** executed_locally (2026-10-22)

---

## AQ-018: python | difficulty 2 | trap: edge_case

**Question**

> What is the time complexity of looking up a key in a Python dict in the average case and in the worst case, and what causes the worst case?

**Reference answer:** Average case O(1) (amortized); worst case O(n), which happens when many keys collide in the hash table, for example keys with the same hash value.

**Key points to grade:**

1. Average O(1)
2. Worst case O(n)
3. Cause is hash collisions

**Expected model failure:** Says it is always O(1).

**Why it is hard:** Models state the average case and forget the worst-case behavior.

**Source:** [Python Wiki: TimeComplexity](https://wiki.python.org/moin/TimeComplexity), dict operations table

**Verification:** needs_manual_check

---

## AQ-019: python | difficulty 4 | trap: outdated_fact

**Question**

> A blog post says: 'Python threads can never run Python code in parallel because of the GIL, and that will never change.' Evaluate this claim as of Python 3.14 and name the relevant PEPs.

**Reference answer:** The claim is outdated. In the default CPython build the GIL still lets only one thread execute Python bytecode at a time, although I/O and C extensions that release the GIL can run concurrently. PEP 703 made the GIL optional through an experimental free-threaded build in Python 3.13, and PEP 779 (accepted June 2025) made the free-threaded build officially supported, but still optional, in Python 3.14. The default build still has the GIL, and making free-threading the default is a later decision.

**Key points to grade:**

1. Default build still has the GIL
2. PEP 703 introduced the free-threaded build (experimental in 3.13)
3. PEP 779: officially supported but optional in 3.14
4. 'Never change' is false

**Expected model failure:** Repeats the old claim, or says the GIL was removed completely in 3.14.

**Why it is hard:** Fast-moving fact: models often stop at 3.13 'experimental' or overshoot to 'GIL removed'.

**Source:** [PEP 779: Criteria for supported status for free-threaded Python](https://peps.python.org/pep-0779/), Phase II; Python 3.14 release notes

**Verification:** primary_source_checked_online (2026-10-22)

---

## AQ-020: javascript | difficulty 2 | trap: subtle_distinction

**Question**

> In JavaScript, what does typeof null return and does that mean null is an object? What does typeof NaN return and what does NaN === NaN evaluate to?

**Reference answer:** typeof null returns 'object', a legacy quirk; null is actually a primitive value (the Null type). typeof NaN returns 'number', and NaN === NaN is false; use Number.isNaN() or Object.is() to test for NaN.

**Key points to grade:**

1. typeof null is 'object' (legacy quirk)
2. null is a primitive
3. typeof NaN is 'number'
4. NaN === NaN is false

**Expected model failure:** Says typeof null is 'null' or that NaN equals itself.

**Why it is hard:** Four small facts must all be correct.

**Source:** [MDN Web Docs: typeof operator; ECMAScript specification](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof), typeof operator table

**Verification:** needs_manual_check

---

## AQ-021: java | difficulty 3 | trap: edge_case

**Question**

> In Java, what does int x = Integer.MAX_VALUE; x = x + 1; evaluate to, does it throw an exception, and how can overflow be detected?

**Reference answer:** x becomes -2147483648. Java does not throw: integer overflow silently wraps around using two's complement arithmetic. Overflow can be detected with Math.addExact, which throws ArithmeticException, or by checking ranges before the operation.

**Key points to grade:**

1. Result is -2147483648
2. No exception is thrown
3. Silent two's complement wraparound
4. Math.addExact throws ArithmeticException

**Expected model failure:** Says it throws an overflow exception, or gives 2147483648.

**Why it is hard:** Models import behavior from other languages.

**Source:** [The Java Language Specification, Section 4.2.2: Integer Operations](https://docs.oracle.com/javase/specs/jls/se21/html/jls-4.html#jls-4.2.2), Section 4.2.2

**Verification:** needs_manual_check

---

## AQ-022: unicode_time | difficulty 3 | trap: numerical

**Question**

> What UTC date and time does the Unix timestamp 2147483647 represent, and why is the next second a problem for systems that store time as a signed 32-bit integer?

**Reference answer:** It is 2038-01-19 03:14:07 UTC. 2147483647 is 2^31 - 1, the maximum signed 32-bit value; the next second overflows and wraps to -2147483648, which represents 1901-12-13 20:45:52 UTC. This is the Year 2038 problem.

**Key points to grade:**

1. 2038-01-19 03:14:07 UTC
2. 2^31 - 1 is the maximum signed 32-bit integer
3. Overflow wraps to a negative value (1901)
4. Year 2038 problem

**Expected model failure:** Gives a wrong date or claims it affects all 64-bit systems.

**Why it is hard:** Requires date arithmetic with the epoch.

**Source:** [POSIX.1-2017 Base Definitions, Section 4.16: Seconds Since the Epoch](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap04.html#tag_04_16), Section 4.16

**Verification:** executed_locally (2026-10-22)

---

## AQ-023: software_testing | difficulty 3 | trap: misconception

**Question**

> A team reports 100% statement coverage and concludes that every decision outcome has been tested. Give a short code example showing the conclusion is wrong and name the stronger coverage criterion.

**Reference answer:** Example: 'if x > 0: y = 1' with one test where x = 1 executes every statement (100% statement coverage) but never exercises the case where the condition is false. Branch (decision) coverage is stronger: 100% branch coverage guarantees 100% statement coverage, but not the other way around.

**Key points to grade:**

1. Concrete example with an untested false branch
2. Statement coverage does not imply decision coverage
3. Branch coverage subsumes statement coverage

**Expected model failure:** Agrees that 100% statement coverage means all outcomes are tested.

**Why it is hard:** Tests understanding of coverage subsumption.

**Source:** ISTQB Certified Tester Foundation Level Syllabus v4.0, Section 4.3 White-box test techniques

**Verification:** needs_manual_check

---

## AQ-024: software_testing | difficulty 3 | trap: numerical

**Question**

> A form field accepts integer ages from 18 to 65 inclusive. List the test values for 2-value boundary value analysis and for 3-value boundary value analysis.

**Reference answer:** 2-value BVA: 17, 18, 65, 66. 3-value BVA: 17, 18, 19, 64, 65, 66 (each boundary together with its neighbors on both sides).

**Key points to grade:**

1. 2-value: 17, 18, 65, 66
2. 3-value: 17, 18, 19, 64, 65, 66

**Expected model failure:** Lists 18 and 65 only, or uses 0 and 100 as the boundaries.

**Why it is hard:** Off-by-one precision under a clear technique definition.

**Source:** ISTQB Certified Tester Foundation Level Syllabus v4.0, Section 4.2.2 Boundary value analysis

**Verification:** needs_manual_check

---

## AQ-025: software_testing | difficulty 2 | trap: subtle_distinction

**Question**

> In ISTQB terminology, what is the difference between an error (mistake), a defect (fault, bug) and a failure? Give one example chain.

**Reference answer:** An error (mistake) is a human action that produces an incorrect result; a defect is the flaw it leaves in a work product such as code or a requirement; a failure is the observable deviation when the defective code is executed under the right conditions. Not every defect causes a failure. Example: a developer misreads a requirement (error), writes '<' instead of '<=' (defect), and the system rejects a valid boundary input (failure).

**Key points to grade:**

1. Error is a human mistake
2. Defect is the flaw in the work product
3. Failure is the observed deviation at run time
4. A defect does not always cause a failure

**Expected model failure:** Treats the three terms as synonyms.

**Why it is hard:** Terminology precision under an authoritative glossary.

**Source:** ISTQB Certified Tester Foundation Level Syllabus v4.0, Section 1.2.3 Errors, defects, failures and root causes

**Verification:** needs_manual_check

---

## AQ-026: tooling | difficulty 3 | trap: subtle_distinction

**Question**

> A bad commit has already been pushed to a shared main branch and other developers have pulled it. Which is safer: 'git reset --hard HEAD~1' followed by a force push, or 'git revert HEAD'? Explain why.

**Reference answer:** git revert HEAD is safer: it adds a new commit that undoes the bad change, keeps history intact and does not disturb anyone who has already pulled. git reset --hard HEAD~1 plus a force push rewrites shared history, forces others to repair their local branches, and can discard work.

**Key points to grade:**

1. git revert is the safe choice for shared branches
2. revert creates a new commit and preserves history
3. reset --hard plus force push rewrites shared history

**Expected model failure:** Recommends reset because it 'cleanly removes' the commit.

**Why it is hard:** Needs reasoning about a shared-history context, not command definitions only.

**Source:** [Git Documentation: git-revert and git-reset](https://git-scm.com/docs/git-revert), git-revert; git-reset 'DISCUSSION' section

**Verification:** needs_manual_check

---

## AQ-027: tech_history | difficulty 3 | trap: edge_case

**Question**

> On what date did the ARPANET switch from NCP to TCP/IP, and which RFC documented the transition plan?

**Reference answer:** The cutover (the 'flag day') was on 1 January 1983, and the plan was documented in RFC 801, 'NCP/TCP Transition Plan' (November 1981).

**Key points to grade:**

1. 1 January 1983
2. RFC 801
3. NCP replaced by TCP/IP

**Expected model failure:** Gives 1969, 1974 or 1989, or cites the wrong RFC.

**Why it is hard:** Models blur ARPANET's founding, TCP's design and the 1983 switch.

**Source:** [RFC 801: NCP/TCP Transition Plan](https://www.rfc-editor.org/rfc/rfc801), Whole document

**Verification:** needs_manual_check

---

## AQ-028: tech_history | difficulty 3 | trap: misconception

**Question**

> A student claims the World Wide Web became free for anyone to use when Tim Berners-Lee wrote his proposal in 1989. Which date and event actually put the Web software into the public domain, and which organization issued it?

**Reference answer:** The student is wrong. CERN issued a statement on 30 April 1993 that put the Web software (the basic line-mode client, the basic server and the library of common code) into the public domain. The 1989 document was only a proposal, and the first servers and browsers ran at CERN by the end of 1990.

**Key points to grade:**

1. Claim is wrong
2. 30 April 1993
3. Issued by CERN
4. 1989 was a proposal, not a release

**Expected model failure:** Accepts 1989 or 1991 as the date, or credits the W3C.

**Why it is hard:** Several nearby dates (1989, 1990, 1991, 1993) invite confusion.

**Source:** [CERN: Licensing the Web](https://home.cern/science/computing/the-birth-of-the-web/licensing-web/), Public releases of Web software

**Verification:** primary_source_checked_online (2026-10-22)

---

## AQ-029: tech_history | difficulty 3 | trap: false_premise

**Question**

> Since the Unix kernel was written in C from its very first version in 1969, how did the C language come to be designed around Unix?

**Reference answer:** The premise is false. Unix began in 1969 in assembly language on a PDP-7. C was developed by Dennis Ritchie in the early 1970s (derived from B), and the Unix kernel was rewritten in C around 1973. C was therefore created in part to make Unix portable and easier to maintain.

**Key points to grade:**

1. Rejects the premise
2. Original Unix was in assembly
3. C was developed in the early 1970s by Dennis Ritchie
4. Kernel rewritten in C around 1973

**Expected model failure:** Accepts the premise and explains 'Unix written in C in 1969'.

**Why it is hard:** The question is built on a confident false chronology.

**Source:** Dennis M. Ritchie, The Development of the C Language (1993), Sections on Unix and the PDP-11

**Verification:** needs_manual_check

---
