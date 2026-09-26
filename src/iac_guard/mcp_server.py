"""Optional MCP stdio server (requires: pip install -e '.[mcp]')."""
from __future__ import annotations

import sys
from pathlib import Path


def main() -> None:
    try:
        from mcp.server.fastmcp import FastMCP
    except ImportError:
        print(
            "mcp package not installed. Run: pip install -e '.[mcp]'\n"
            "Or use the CLI: python -m iac_guard --help",
            file=sys.stderr,
        )
        raise SystemExit(1) from None

    from .checkov_runner import run_checkov
    from .policies import builtin_review, explain

    mcp = FastMCP("iac-guard-mcp")

    @mcp.tool()
    def review_diff(path: str, prefer_checkov: bool = False) -> dict:
        """Review a Terraform/Bicep file; return findings JSON + explanation."""
        p = Path(path)
        findings: list[dict] = []
        engine = "builtin-regex"
        if prefer_checkov:
            ck = run_checkov(p)
            if ck is not None:
                findings = ck
                engine = "checkov"
        if not findings:
            findings = builtin_review(p)
            engine = "builtin-regex"
        return {
            "tool": "review_diff",
            "engine": engine,
            "file": str(p),
            "findings": findings,
            "explanation": explain(findings),
            "passed": len(findings) == 0,
        }

    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
