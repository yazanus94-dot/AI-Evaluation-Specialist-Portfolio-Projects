"""Schema and consistency rules for a claim verification log."""
from __future__ import annotations

import json
import re
from typing import Dict, List

VERDICTS = ("supported", "partially_supported", "contradicted", "unverifiable")
ERROR_TYPES = ("none", "factual_error", "outdated_fact", "wrong_citation", "overstatement", "unsupported_prediction")
SEVERITIES = ("none", "low", "medium", "high")
METHODS = ("online_primary", "online_secondary_quote", "executed_locally")
SOURCE_TYPES = ("primary", "secondary")
REQUIRED = ("id", "domain", "ai_claim", "verdict", "error_type", "severity", "correct_statement", "evidence",
            "sources", "verification", "rationale")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ID = re.compile(r"^VL-\d{3}$")
MAX_EVIDENCE_WORDS = 70  # evidence is summarised in the reviewer's own words, not copied


def load_claims(path: str) -> List[dict]:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def validate_claim(c: dict) -> List[str]:
    errs: List[str] = []
    for field in REQUIRED:
        if field not in c or c[field] in (None, "", []):
            errs.append(f"missing field: {field}")
    if errs:
        return errs
    if not ID.match(c["id"]):
        errs.append("id must look like VL-001")
    if c["verdict"] not in VERDICTS:
        errs.append(f"unknown verdict: {c['verdict']}")
    if c["error_type"] not in ERROR_TYPES:
        errs.append(f"unknown error_type: {c['error_type']}")
    if c["severity"] not in SEVERITIES:
        errs.append(f"unknown severity: {c['severity']}")

    # verdict must agree with error type and severity
    if c["verdict"] == "supported":
        if c["error_type"] != "none" or c["severity"] != "none":
            errs.append("a supported claim must have error_type none and severity none")
    else:
        if c["error_type"] == "none" or c["severity"] == "none":
            errs.append("a claim that is not fully supported needs an error_type and a severity")
    if c["verdict"] == "unverifiable" and c["error_type"] not in ("unsupported_prediction", "none"):
        errs.append("unverifiable claims should use error_type unsupported_prediction")
    if c["error_type"] == "unsupported_prediction" and c["verdict"] != "unverifiable":
        errs.append("unsupported_prediction is only valid for unverifiable claims")

    if len(c["evidence"].split()) > MAX_EVIDENCE_WORDS:
        errs.append(f"evidence is longer than {MAX_EVIDENCE_WORDS} words: summarise instead of copying")
    if len(c["rationale"].split()) < 15:
        errs.append("rationale must explain the verdict in at least 15 words")

    srcs = c["sources"]
    if not isinstance(srcs, list) or not srcs:
        errs.append("at least one source is required")
    else:
        for i, s in enumerate(srcs, 1):
            for f in ("title", "reference", "url", "source_type"):
                if not s.get(f):
                    errs.append(f"source {i}: missing {f}")
            if s.get("url") and not str(s["url"]).startswith("https://"):
                errs.append(f"source {i}: url must start with https://")
            if s.get("source_type") not in SOURCE_TYPES:
                errs.append(f"source {i}: unknown source_type")
        if not any(s.get("source_type") == "primary" for s in srcs):
            errs.append("at least one primary source is required")

    v = c["verification"]
    if v.get("method") not in METHODS:
        errs.append(f"unknown verification method: {v.get('method')}")
    if not DATE.match(str(v.get("date", ""))):
        errs.append("verification date must be YYYY-MM-DD")
    if v.get("method") == "executed_locally" and not v.get("test"):
        errs.append("executed_locally claims must name the test that reproduces them")
    if v.get("method") == "online_secondary_quote" and not any(s.get("source_type") == "secondary" for s in srcs):
        errs.append("online_secondary_quote needs the secondary source that was used")
    return errs


def validate_log(claims: List[dict]) -> Dict[str, List[str]]:
    problems: Dict[str, List[str]] = {}
    for c in claims:
        e = validate_claim(c)
        if e:
            problems[c.get("id", "?")] = e
    seen, texts = set(), set()
    for c in claims:
        if c.get("id") in seen:
            problems.setdefault(c["id"], []).append("duplicate id")
        seen.add(c.get("id"))
        t = " ".join(str(c.get("ai_claim", "")).lower().split())
        if t in texts:
            problems.setdefault(c.get("id", "?"), []).append("duplicate claim text")
        texts.add(t)
    return problems
