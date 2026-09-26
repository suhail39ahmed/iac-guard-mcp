from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .checkov_runner import run_checkov
from .policies import builtin_review, explain


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="iac-guard", description="review_diff over Terraform/Bicep fixtures")
    p.add_argument("path", type=Path, help="File to review (e.g. fixtures/bad_nsg.tf)")
    p.add_argument("--prefer-checkov", action="store_true", help="Try Checkov first if installed")
    args = p.parse_args(argv)

    if not args.path.exists():
        print(f"Not found: {args.path}", file=sys.stderr)
        return 2

    findings: list[dict] = []
    engine = "builtin-regex"
    if args.prefer_checkov:
        ck = run_checkov(args.path)
        if ck is not None:
            findings = ck
            engine = "checkov"
    if not findings:
        findings = builtin_review(args.path)
        engine = "builtin-regex"

    out = {
        "tool": "review_diff",
        "engine": engine,
        "file": str(args.path),
        "findings": findings,
        "explanation": explain(findings),
        "passed": len(findings) == 0,
    }
    print(json.dumps(out, indent=2))
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
