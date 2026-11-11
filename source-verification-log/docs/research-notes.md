# Research Notes

What was checked, where, and when (all on 22 October 2026).

| Claim area | Primary source read | What it confirmed |
|---|---|---|
| HTTP 418 and section numbers | IANA HTTP Status Code Registry | 418 is (Unused), RFC 9110 section 15.5.19 |
| 401 and 403 section numbers | Go net/http status table citing RFC 9110 | 401 maps to 15.5.2, 403 to 15.5.4 (secondary; open RFC 9110 to confirm) |
| RFC 7231 status | RFC 9110 datatracker page | RFC 9110 (June 2022) obsoletes RFC 7231 |
| Python free-threading | PEP 779 and the python.org discussion of it | Phase II (supported, optional) in 3.14; default build still has the GIL; PEP 703 accepted for 3.13 as experimental |
| CERN public domain release | CERN licensing page and timeline | 30 April 1993 |
| MD5 and HMAC-MD5 | RFC 6151 (March 2011) | MD5 unacceptable for signatures; no practical HMAC-MD5 vulnerability; avoid in new designs |
| SHA-1 | NIST announcement of 15 December 2022 | Deprecated for new signatures in 2011; transition completed by 31 December 2030 |
| Windows 10 | Microsoft Lifecycle page | End of support 14 October 2025 |
| Python 2 | Python.org Sunsetting Python 2, PEP 373 | Support ended 1 January 2020; 2.7.18 released 20 April 2020 |
| JSON encoding | RFC 8259 section 8.1, as quoted publicly | UTF-8 required outside closed ecosystems; no BOM from generators; parsers may ignore a BOM (secondary; open RFC 8259 to confirm) |
| Python behavior (sorting, identity, floor division, truthiness, tuples, rounding, floats, bool, SQLite) | Reproduced by running code | See `tests/test_executable_claims.py` |

## Items to re-open before relying on this log
VL-003, VL-015 and VL-016 were confirmed through secondary sources that quote the primary text. Open RFC 9110 (section numbers) and RFC 8259 (section 8.1) and confirm the wording, then change the method to `online_primary`.
