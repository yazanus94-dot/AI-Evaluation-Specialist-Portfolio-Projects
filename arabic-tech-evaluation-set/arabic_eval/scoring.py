"""Weighted rubric scoring with gates (caps) for serious problems."""
from __future__ import annotations

import json
import math
from typing import Dict, List, Sequence, Tuple


def load_rubric(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        rubric = json.load(f)
    total = sum(c["weight"] for c in rubric["criteria"])
    if abs(total - 1.0) > 1e-9:
        raise ValueError(f"criterion weights must sum to 1.0, got {total}")
    return rubric


def compute_score(scores: Dict[str, int], rubric: dict, error_tags: Sequence[str] = ()) -> Tuple[float, List[str]]:
    """Return (score 0-100, list of gate messages that applied)."""
    lo, hi = rubric["scale"]["min"], rubric["scale"]["max"]
    ids = [c["id"] for c in rubric["criteria"]]
    missing = [i for i in ids if i not in scores]
    if missing:
        raise ValueError(f"missing scores: {missing}")
    for i in ids:
        if not lo <= scores[i] <= hi:
            raise ValueError(f"{i} score {scores[i]} outside {lo}-{hi}")
    score = 100 * sum(c["weight"] * (scores[c["id"]] - lo) / (hi - lo) for c in rubric["criteria"])
    applied: List[str] = []
    for gate in rubric["gates"]:
        cond = gate["if"]
        hit = (cond == "fabricated_source" and "fabricated_source" in error_tags) or (
            "<=" in cond and scores[cond.split("<=")[0].strip()] <= int(cond.split("<=")[1]))
        if hit and score > gate["cap"]:
            score = gate["cap"]
            applied.append(gate["reason"])
    return round(score, 1), applied


def expected_rating(score: float) -> int:
    """Map a 0-100 score to the 1-5 scale: 0-20 -> 1, 20-40 -> 2, ... 80-100 -> 5."""
    return max(1, min(5, math.ceil(score / 20)))
