"""Builtin regex policy checks (Checkov fallback)."""
from __future__ import annotations

import re
from pathlib import Path

POLICIES = [
    {
        "id": "NSG-SSH-OPEN",
        "severity": "HIGH",
        "description": "SSH (22) should not be allowed from *",
        "patterns": [
            re.compile(r'destination_port_range\s*=\s*"22"', re.I),
            re.compile(r"destinationPortRange:\s*'22'", re.I),
        ],
        "open_source": [
            re.compile(r'source_address_prefix\s*=\s*"\*"', re.I),
            re.compile(r"sourceAddressPrefix:\s*'\*'", re.I),
        ],
    },
    {
        "id": "STORAGE-PUBLIC-BLOB",
        "severity": "HIGH",
        "description": "Storage account should not allow public blob access",
        "patterns": [re.compile(r"allow_blob_public_access\s*=\s*true", re.I)],
        "open_source": [],
    },
]


def builtin_review(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    findings = []
    for pol in POLICIES:
        hit = any(p.search(text) for p in pol["patterns"])
        if not hit:
            continue
        if pol["open_source"]:
            if not any(p.search(text) for p in pol["open_source"]):
                # SSH port without open source — still warn lightly
                pass
            elif pol["id"] == "NSG-SSH-OPEN" and not any(p.search(text) for p in pol["open_source"]):
                continue
        if pol["id"] == "NSG-SSH-OPEN":
            if not (any(p.search(text) for p in pol["patterns"]) and any(p.search(text) for p in pol["open_source"])):
                continue
        findings.append(
            {
                "policy_id": pol["id"],
                "severity": pol["severity"],
                "description": pol["description"],
                "file": str(path),
                "source": "builtin-regex",
            }
        )
    return findings


def explain(findings: list[dict]) -> str:
    if not findings:
        return "No policy violations detected by builtin checks (or Checkov)."
    lines = ["LLM-style explanation (static offline template):", ""]
    for f in findings:
        lines.append(
            f"- [{f['severity']}] {f['policy_id']}: {f['description']} "
            f"(file={f['file']}). Prefer least-privilege source prefixes and disable public blob access."
        )
    lines.append("")
    lines.append("Remediation theme: tighten ingress, use Just-In-Time / bastion, private endpoints.")
    return "\n".join(lines)
