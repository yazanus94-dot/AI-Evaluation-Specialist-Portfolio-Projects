import argparse
import os
import os
import sys

from .lint import load_glossary
from .report import catalogue_markdown, summary_markdown
from .schema import load_evaluations, validate_dataset
from .scoring import load_rubric


def _ensure_parent(path):
    """Create the output directory if it does not exist yet."""
    parent = os.path.dirname(os.path.abspath(path))
    if parent:
        os.makedirs(parent, exist_ok=True)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="arabic_eval", description="Validate the Arabic evaluation set and build reports.")
    p.add_argument("data_dir", nargs="?", default="data")
    p.add_argument("--catalogue", help="write the readable catalogue (Markdown)")
    p.add_argument("--summary", help="write the summary statistics (Markdown)")
    args = p.parse_args(argv)

    rubric = load_rubric(os.path.join(args.data_dir, "rubric.json"))
    glossary = load_glossary(os.path.join(args.data_dir, "glossary.csv"))
    items = load_evaluations(os.path.join(args.data_dir, "evaluations.json"))
    problems = validate_dataset(items, rubric)
    if problems:
        for i, errs in problems.items():
            for e in errs:
                print(f"{i}: {e}")
        return 1
    print(f"OK: {len(items)} evaluations valid")
    if args.catalogue:
        _ensure_parent(args.catalogue) or open(args.catalogue, "w", encoding="utf-8").write(catalogue_markdown(items))
    if args.summary:
        _ensure_parent(args.summary) or open(args.summary, "w", encoding="utf-8").write(summary_markdown(items, rubric, glossary))
    return 0


if __name__ == "__main__":
    sys.exit(main())
