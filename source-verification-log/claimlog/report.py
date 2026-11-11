"""Summary statistics and the readable verification log."""
from __future__ import annotations

from collections import Counter
from typing import List

LABEL = {"supported": "SUPPORTED", "partially_supported": "PARTIALLY SUPPORTED", "contradicted": "CONTRADICTED",
         "unverifiable": "UNVERIFIABLE"}


def summary_markdown(claims: List[dict]) -> str:
    n = len(claims)
    count = lambda key: Counter(c[key] for c in claims)
    wrong = [c for c in claims if c["verdict"] != "supported"]
    out = ["# Verification Summary", "",
           f"**{n} AI-style claims checked.** {n - len(wrong)} fully supported, {len(wrong)} not fully supported "
           f"({len(wrong) / n:.0%}).", "", "## Verdicts", "", "| Verdict | Claims |", "|---|---|"]
    out += [f"| {v} | {k} |" for v, k in count("verdict").most_common()]
    out += ["", "## Error types (claims with a problem)", "", "| Error type | Claims |", "|---|---|"]
    out += [f"| {v} | {k} |" for v, k in Counter(c["error_type"] for c in wrong).most_common()]
    out += ["", "## Severity of problems", "", "| Severity | Claims |", "|---|---|"]
    sev = Counter(c["severity"] for c in wrong)
    out += [f"| {s} | {sev.get(s, 0)} |" for s in ("high", "medium", "low")]
    out += ["", "## By domain", "", "| Domain | Claims | With a problem |", "|---|---|---|"]
    dom = Counter(c["domain"] for c in claims)
    domw = Counter(c["domain"] for c in wrong)
    out += [f"| {d} | {k} | {domw.get(d, 0)} |" for d, k in sorted(dom.items())]
    out += ["", "## How each claim was verified", "", "| Method | Claims |", "|---|---|"]
    out += [f"| {m} | {k} |" for m, k in Counter(c["verification"]["method"] for c in claims).most_common()]
    high = [c for c in wrong if c["severity"] == "high"]
    out += ["", "## High-severity findings", ""]
    out += [f"- **{c['id']}**: {c['ai_claim']}" for c in high] or ["- none"]
    return "\n".join(out) + "\n"


def catalogue_markdown(claims: List[dict]) -> str:
    out = ["# Verification Log", "",
           "Each entry: the claim as an AI might state it, the verdict, the correct statement, a short evidence summary, "
           "the sources and the reviewer's written rationale.", ""]
    for c in claims:
        out += [f"## {c['id']}: {LABEL[c['verdict']]} ({c['domain']})", "",
                "> " + c["ai_claim"], "",
                f"**Error type:** {c['error_type']} | **Severity:** {c['severity']}", "",
                f"**Correct statement:** {c['correct_statement']}", "",
                f"**Evidence:** {c['evidence']}", "", "**Sources:**", ""]
        out += [f"- [{s['title']}]({s['url']}), {s['reference']} ({s['source_type']})" for s in c["sources"]]
        v = c["verification"]
        out += ["", f"**Verification:** {v['method']} on {v['date']}" + (f" (test: `{v['test']}`)" if v.get("test") else ""), "",
                f"**Rationale:** {c['rationale']}", "", "---", ""]
    return "\n".join(out)
