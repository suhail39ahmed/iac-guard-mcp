# iac-guard-mcp

Tool **review_diff**: scan Terraform / Bicep fixtures with **Checkov** (if installed) or **builtin regex policies**, plus a static LLM-style explanation. Outputs structured findings JSON.

## What it is
- Offline IaC guardrail for agents / PR bots
- Fixtures: `fixtures/bad_nsg.tf`, `fixtures/bad_nsg.bicep`

## What it is not
- Not a full policy-as-code platform (OPA/Gatekeeper)
- Not an auto-remediator that applies terraform apply

## Architecture

```
  review_diff(file)
        |
        +--> checkov (optional)
        +--> builtin regex policies
        |
        v
  findings JSON + explanation template
```

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
python -m iac_guard.cli fixtures/bad_nsg.tf
python -m iac_guard.cli fixtures/bad_nsg.bicep; echo exit:$?
```

## Demo assets checklist
- [ ] `assets/demo.gif`
- [ ] `assets/architecture.png`
- [ ] `docs/DEMO.md`

## License
Apache-2.0
