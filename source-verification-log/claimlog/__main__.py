import argparse
import sys

from .report import catalogue_markdown, summary_markdown
from .schema import load_claims, validate_log


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="claimlog", description="Validate the verification log and build its reports.")
    p.add_argument("data", nargs="?", default="data/claims.json")
    p.add_argument("--log", help="write the full verification log (Markdown)")
    p.add_argument("--summary", help="write the summary statistics (Markdown)")
    args = p.parse_args(argv)

    claims = load_claims(args.data)
    problems = validate_log(claims)
    if problems:
        for cid, errs in problems.items():
            for e in errs:
                print(f"{cid}: {e}")
        return 1
    print(f"OK: {len(claims)} claims valid")
    if args.log:
        open(args.log, "w", encoding="utf-8").write(catalogue_markdown(claims))
    if args.summary:
        open(args.summary, "w", encoding="utf-8").write(summary_markdown(claims))
    return 0


if __name__ == "__main__":
    sys.exit(main())
