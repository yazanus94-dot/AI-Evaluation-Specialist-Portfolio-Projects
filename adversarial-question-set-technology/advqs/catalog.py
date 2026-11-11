"""Human-readable catalogue and statistics for the question set."""
from __future__ import annotations

from collections import Counter
from typing import List


def stats_markdown(questions: List[dict]) -> str:
    n = len(questions)
    by = lambda key: Counter(q[key] for q in questions)
    out = ["# Dataset Summary", "", f"**{n} questions** | average difficulty **{sum(q['difficulty'] for q in questions) / n:.1f}** / 5", "",
           "## By topic", "", "| Topic | Questions |", "|---|---|"]
    out += [f"| {k} | {v} |" for k, v in sorted(by("topic").items())]
    out += ["", "## By trap type", "", "| Trap type | Questions |", "|---|---|"]
    out += [f"| {k} | {v} |" for k, v in sorted(by("trap_type").items())]
    out += ["", "## By difficulty", "", "| Difficulty | Questions |", "|---|---|"]
    out += [f"| {k} | {v} |" for k, v in sorted(by("difficulty").items())]
    ver = Counter(q["verification"]["status"] for q in questions)
    out += ["", "## Source verification status", "", "| Status | Questions |", "|---|---|"]
    out += [f"| {k} | {v} |" for k, v in sorted(ver.items())]
    return "\n".join(out) + "\n"


def catalog_markdown(questions: List[dict]) -> str:
    out = ["# Question Catalogue", "",
           "Each entry has the question, the reference answer, the gradable key points, the trap and the source.", ""]
    for q in questions:
        src = q["source"]
        link = f"[{src['title']}]({src['url']})" if src.get("url") else src["title"]
        out += [f"## {q['id']}: {q['topic']} | difficulty {q['difficulty']} | trap: {q['trap_type']}", "",
                "**Question**", "", "> " + q["question"].replace("\n", "\n> "), "",
                f"**Reference answer:** {q['reference_answer']}", "",
                "**Key points to grade:**", ""]
        out += [f"{i}. {p}" for i, p in enumerate(q["key_points"], 1)]
        out += ["", f"**Expected model failure:** {q['expected_model_failure']}", "",
                f"**Why it is hard:** {q['why_hard']}", "",
                f"**Source:** {link}, {src['reference']}", "",
                f"**Verification:** {q['verification']['status']}"
                + (f" ({q['verification']['date']})" if q["verification"].get("date") else ""), "", "---", ""]
    return "\n".join(out)
