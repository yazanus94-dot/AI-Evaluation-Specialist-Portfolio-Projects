"""Automatic lint for Arabic technical text: discouraged terms, Latin punctuation, mixed numerals."""
from __future__ import annotations

import csv
import re
from typing import Dict, List

ARABIC = re.compile(r"[\u0600-\u06FF]")
LATIN = re.compile(r"[A-Za-z]")
DIACRITICS = re.compile(r"[\u064B-\u0652\u0640]")  # harakat and tatweel
WESTERN = re.compile(r"[0-9]")
EASTERN = re.compile(r"[\u0660-\u0669]")


def normalize(text: str) -> str:
    text = DIACRITICS.sub("", text)
    return text.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")


def load_glossary(path: str) -> List[dict]:
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            r["discouraged"] = [t for t in r["discouraged_ar"].split(";") if t]
            rows.append(r)
    return rows


def _term_pattern(term: str) -> re.Pattern:
    # optional one-letter prefix (و ف ب ل ك) and optional definite article ال
    return re.compile(r"(?<![\u0600-\u06FF])(?:[وفبلك])?(?:ال)?" + re.escape(normalize(term)) + r"(?![\u0600-\u06FF])")


def lint_text(text: str, glossary: List[dict]) -> List[dict]:
    """Return findings: {'type', 'detail', 'suggestion'}. Empty list means the text is clean."""
    findings: List[dict] = []
    norm = normalize(text)
    for entry in glossary:
        for bad in entry["discouraged"]:
            if _term_pattern(bad).search(norm):
                findings.append({"type": "discouraged_term", "detail": bad,
                                 "suggestion": f"{entry['preferred_ar']} ({entry['english']})"})
    for line in text.splitlines():
        arabic, latin = len(ARABIC.findall(line)), len(LATIN.findall(line))
        if arabic > latin:  # an Arabic sentence: Arabic punctuation expected
            for ch, ar in ((",", "،"), (";", "؛"), ("?", "؟")):
                if ch in line:
                    findings.append({"type": "latin_punctuation", "detail": ch, "suggestion": ar})
    if WESTERN.search(text) and EASTERN.search(text):
        findings.append({"type": "mixed_numerals", "detail": "Western and Arabic-Indic digits in one text",
                         "suggestion": "use one numeral style consistently"})
    return findings
