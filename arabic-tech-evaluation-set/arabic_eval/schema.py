"""Validation of evaluation records."""
from __future__ import annotations

import json
from typing import Dict, List

from .scoring import compute_score, expected_rating

ERROR_TAGS = ("factual_error", "fabricated_source", "terminology_error", "grammar_error", "spelling_error", "dialect_mix",
              "mistranslation", "unnatural_literal_translation", "rtl_formatting_issue", "instruction_violation", "omission")
REVIEW_STATUSES = ("needs_native_review", "native_reviewed")
REQUIRED = ("id", "topic", "prompt_ar", "prompt_en", "response", "response_lang", "scores", "rating", "error_tags",
            "rationale_en", "review_status")


def load_evaluations(path: str) -> List[dict]:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def validate_evaluation(e: dict, rubric: dict) -> List[str]:
    errs: List[str] = []
    for f in REQUIRED:
        if f not in e or e[f] in (None, "") or (f == "scores" and not e[f]):
            if f == "error_tags" and e.get(f) == []:
                continue
            errs.append(f"missing field: {f}")
    if errs:
        return errs
    if e["response_lang"] not in ("ar", "en"):
        errs.append("response_lang must be ar or en")
    if e["review_status"] not in REVIEW_STATUSES:
        errs.append("unknown review_status")
    unknown = [t for t in e["error_tags"] if t not in ERROR_TAGS]
    if unknown:
        errs.append(f"unknown error tags: {unknown}")
    if not 1 <= e["rating"] <= 5:
        errs.append("rating must be 1-5")
    try:
        score, _ = compute_score(e["scores"], rubric, e["error_tags"])
    except ValueError as ex:
        return errs + [str(ex)]
    if abs(e["rating"] - expected_rating(score)) > 1:
        errs.append(f"rating {e['rating']} is inconsistent with the rubric score {score} (expected about {expected_rating(score)})")
    if e.get("computed_score") is not None and abs(e["computed_score"] - score) > 0.05:
        errs.append("computed_score does not match the rubric")
    # consistency between the reviewer's marks and the tags
    low = [c for c, v in e["scores"].items() if v <= 2]
    if not e["error_tags"] and low:
        errs.append(f"scores {low} are low but no error tag explains them")
    if e["error_tags"] and all(v == 5 for v in e["scores"].values()):
        errs.append("error tags present but every score is 5")
    if e["rating"] < 5 and not e.get("correction"):
        errs.append("a response below 5 needs a corrected version")
    if len(e["rationale_en"].split()) < 15:
        errs.append("rationale must be at least 15 words")
    if "fabricated_source" in e["error_tags"] and e["rating"] != 1:
        errs.append("a fabricated source must be rated 1")
    return errs


def validate_dataset(items: List[dict], rubric: dict) -> Dict[str, List[str]]:
    problems: Dict[str, List[str]] = {}
    for e in items:
        errs = validate_evaluation(e, rubric)
        if errs:
            problems[e.get("id", "?")] = errs
    ids = [e.get("id") for e in items]
    for i in set(ids):
        if ids.count(i) > 1:
            problems.setdefault(str(i), []).append("duplicate id")
    return problems
