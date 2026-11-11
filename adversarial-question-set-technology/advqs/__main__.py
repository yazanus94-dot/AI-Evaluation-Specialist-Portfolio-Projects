import argparse
import sys

from .catalog import catalog_markdown, stats_markdown
from .schema import load_questions, validate_dataset


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="advqs", description="Validate the adversarial question set and build its catalogue.")
    p.add_argument("data", nargs="?", default="data/questions.json")
    p.add_argument("--catalog", help="write the full catalogue to this Markdown file")
    p.add_argument("--stats", help="write the dataset summary to this Markdown file")
    args = p.parse_args(argv)

    questions = load_questions(args.data)
    problems = validate_dataset(questions)
    if problems:
        for qid, errs in problems.items():
            for e in errs:
                print(f"{qid}: {e}")
        print(f"\n{len(problems)} item(s) with problems")
        return 1
    print(f"OK: {len(questions)} questions valid")
    if args.catalog:
        open(args.catalog, "w", encoding="utf-8").write(catalog_markdown(questions))
        print(f"catalogue written to {args.catalog}")
    if args.stats:
        open(args.stats, "w", encoding="utf-8").write(stats_markdown(questions))
        print(f"summary written to {args.stats}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
