from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path


def run_checkov(path: Path) -> list[dict] | None:
    if not shutil.which("checkov"):
        return None
    try:
        proc = subprocess.run(
            ["checkov", "-f", str(path), "-o", "json", "--quiet"],
            capture_output=True,
            text=True,
            timeout=120,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if not proc.stdout.strip():
        return None
    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return None
    findings = []
    results = data.get("results", {}) if isinstance(data, dict) else {}
    for item in results.get("failed_checks", []) or []:
        findings.append(
            {
                "policy_id": item.get("check_id"),
                "severity": item.get("severity", "UNKNOWN"),
                "description": item.get("check_name"),
                "file": item.get("file_path") or str(path),
                "source": "checkov",
            }
        )
    return findings
