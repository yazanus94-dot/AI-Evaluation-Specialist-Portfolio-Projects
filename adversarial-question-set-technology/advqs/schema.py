"""Schema and quality rules for adversarial evaluation questions."""
from __future__ import annotations

import json
import re
from collections import Counter
from typing import Dict, List

TRAP_TYPES = ("false_premise", "outdated_fact", "multi_step_reasoning", "subtle_distinction", "edge_case",
              "numerical", "misconception", "over_generalization")
TOPICS = ("web_protocols", "networking", "security", "databases", "python", "javascript", "java",
          "software_testing", "unicode_time", "tech_history", "tooling")
VERIFICATION_STATUSES = ("primary_source_checked_online", "executed_locally", "needs_manual_check", "verified_by_author")

REQUIRED = ("id", "topic", "difficulty", "trap_type", "question", "reference_answer", "key_points",
            "expected_model_failure", "why_hard", "source", "verification")
ID_PATTERN = re.compile(r"^AQ-\d{3}$")


def load_questions(path: str) -> List[dict]:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def validate_question(q: dict) -> List[str]:
    """Return a list of problems for one question (empty list = valid)."""
    errs: List[str] = []
    for field in REQUIRED:
        if field not in q or q[field] in (None, "", []):
            errs.append(f"missing field: {field}")
    if errs:
        return errs
    if not ID_PATTERN.match(q["id"]):
        errs.append("id must look like AQ-001")
    if q["topic"] not in TOPICS:
        errs.append(f"unknown topic: {q['topic']}")
    if q["trap_type"] not in TRAP_TYPES:
        errs.append(f"unknown trap_type: {q['trap_type']}")
    if not isinstance(q["difficulty"], int) or not 1 <= q["difficulty"] <= 5:
        errs.append("difficulty must be an integer 1-5")
    if not isinstance(q["key_points"], list) or len(q["key_points"]) < 2:
        errs.append("key_points must list at least 2 gradable points")
    if len(q["question"].split()) < 12:
        errs.append("question is too short to be unambiguous (under 12 words)")
    if len(q["reference_answer"].split()) < 12:
        errs.append("reference_answer is too short")
    src = q["source"]
    for f in ("title", "reference"):
        if not src.get(f):
            errs.append(f"source.{f} is required")
    if src.get("url") is not None and not str(src["url"]).startswith("https://"):
        errs.append("source.url must start with https://")
    ver = q["verification"]
    if ver.get("status") not in VERIFICATION_STATUSES:
        errs.append(f"unknown verification status: {ver.get('status')}")
    elif ver["status"] != "needs_manual_check" and not ver.get("date"):
        errs.append("verified questions need a verification date")
    if q["trap_type"] == "false_premise" and "premise" not in q["reference_answer"].lower():
        errs.append("false_premise questions must say in the reference answer that the premise is false")
    if q["trap_type"] == "outdated_fact" and not re.search(r"\b(19|20)\d{2}\b", q["reference_answer"]):
        errs.append("outdated_fact questions must date the facts in the reference answer")
    return errs


def validate_dataset(questions: List[dict]) -> Dict[str, List[str]]:
    """Map question id (or 'dataset') to problems; an empty dict means the dataset is clean."""
    problems: Dict[str, List[str]] = {}
    for q in questions:
        errs = validate_question(q)
        if errs:
            problems[q.get("id", "?")] = errs
    ids = Counter(q.get("id") for q in questions)
    for i, n in ids.items():
        if n > 1:
            problems.setdefault(str(i), []).append("duplicate id")
    texts = Counter(" ".join(q.get("question", "").lower().split()) for q in questions)
    for t, n in texts.items():
        if n > 1 and t:
            problems.setdefault("dataset", []).append(f"duplicate question text: {t[:50]}")
    return problems
