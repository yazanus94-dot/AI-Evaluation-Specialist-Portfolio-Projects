"""Summary statistics, the readable catalogue and the lint-versus-reviewer comparison."""
from __future__ import annotations

from collections import Counter
from statistics import mean
from typing import List

from .lint import lint_text

LINT_TAG_MAP = {"terminology_error": "discouraged_term", "rtl_formatting_issue": "latin_punctuation"}


def lint_agreement(items: List[dict], glossary: List[dict]) -> dict:
    """How well does the automatic lint match the human tags? (Arabic responses only.)"""
    hits = misses = false_alarms = 0
    for e in items:
        if e["response_lang"] != "ar":
            continue
        kinds = {f["type"] for f in lint_text(e["response"], glossary)}
        for tag, kind in LINT_TAG_MAP.items():
            tagged, flagged = tag in e["error_tags"], kind in kinds
            hits += tagged and flagged
            misses += tagged and not flagged
            false_alarms += flagged and not tagged
    return {"hits": hits, "misses": misses, "false_alarms": false_alarms}


def summary_markdown(items: List[dict], rubric: dict, glossary: List[dict]) -> str:
    n = len(items)
    ratings = Counter(e["rating"] for e in items)
    out = ["# Evaluation Summary", "", f"**{n} responses evaluated.** Average rubric score "
           f"**{mean(e['computed_score'] for e in items):.1f} / 100**.", "",
           "## Ratings", "", "| Rating | Responses |", "|---|---|"]
    out += [f"| {r} | {ratings.get(r, 0)} |" for r in (5, 4, 3, 2, 1)]
    out += ["", "## Mean score per criterion (1-5)", "", "| Criterion | Mean |", "|---|---|"]
    for c in rubric["criteria"]:
        out.append(f"| {c['id']} | {mean(e['scores'][c['id']] for e in items):.2f} |")
    tags = Counter(t for e in items for t in e["error_tags"])
    out += ["", "## Error tags", "", "| Tag | Responses |", "|---|---|"]
    out += [f"| {t} | {k} |" for t, k in tags.most_common()]
    topics = {}
    for e in items:
        topics.setdefault(e["topic"], []).append(e["computed_score"])
    out += ["", "## By topic", "", "| Topic | Responses | Mean score |", "|---|---|---|"]
    out += [f"| {t} | {len(v)} | {mean(v):.1f} |" for t, v in sorted(topics.items())]
    la = lint_agreement(items, glossary)
    out += ["", "## Automatic lint versus reviewer tags", "",
            f"The lint detects discouraged transliterated terms and Latin punctuation in Arabic text. "
            f"It agreed with the reviewer on **{la['hits']}** tagged responses, missed **{la['misses']}** and raised "
            f"**{la['false_alarms']}** false alarms. Grammar, dialect and meaning still need a human reviewer."]
    gated = [e for e in items if e["gates_applied"]]
    out += ["", f"Responses capped by a rubric gate: **{len(gated)}**.", ""]
    return "\n".join(out)


def catalogue_markdown(items: List[dict]) -> str:
    out = ["# Evaluated Responses", "",
           "Arabic text is shown right-to-left. Every entry still needs a native-speaker review before publication.", ""]
    for e in items:
        dir_resp = "rtl" if e["response_lang"] == "ar" else "ltr"
        s = e["scores"]
        out += [f"## {e['id']}: {e['topic']} | rating {e['rating']} | score {e['computed_score']}", "",
                f'<div dir="rtl" lang="ar"><b>السؤال:</b> {e["prompt_ar"]}</div>', "",
                f"*English: {e['prompt_en']}*", "",
                f'<div dir="{dir_resp}"><b>Response:</b><br>{e["response"].replace(chr(10), "<br>")}</div>', "",
                "| accuracy | terminology | language | instructions | formatting |", "|---|---|---|---|---|",
                f"| {s['technical_accuracy']} | {s['terminology']} | {s['language_quality']} | {s['instruction_following']} | {s['formatting']} |", "",
                f"**Error tags:** {', '.join(e['error_tags']) or 'none'}", "",
                f"**Rationale:** {e['rationale_en']}", ""]
        if e.get("correction"):
            d = "rtl" if e["correction_lang"] == "ar" else "ltr"
            out += [f'<div dir="{d}"><b>Corrected version:</b> {e["correction"]}</div>', ""]
        out += ["---", ""]
    return "\n".join(out)
