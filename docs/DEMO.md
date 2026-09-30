# Demo — iac-guard-mcp

Honest fixture demos. Apache-2.0. No fabricated metrics.

## Timed Loom (60–90s)

| Time | On screen | Say |
|------|-----------|-----|
| 0:00–0:10 | Repo root | "iac-guard-mcp — review_diff for agents over Terraform and Bicep. Builtin policies; Checkov optional." |
| 0:10–0:40 | `python -m iac_guard fixtures/bad_nsg.tf` | "Bad NSG fixture — structured findings JSON agents can consume." |
| 0:40–1:05 | Bicep fixture | "Same tool surface for Bicep. Offline fixtures." |
| 1:05–1:30 | Outro | "`make demo`. Not a full OPA platform — a review_diff pattern." |

### Exact commands

```bash
cd iac-guard-mcp
python -m venv .venv && source .venv/bin/activate
pip install -e .
python -m iac_guard --help
python -m iac_guard fixtures/bad_nsg.tf || true
python -m iac_guard fixtures/bad_nsg.bicep || true
make demo
```

### Outro card

`github.com/suhail39ahmed/iac-guard-mcp`

## Shot list

1. Terraform findings JSON  
2. Bicep findings  
3. `make demo` success line  

## CI workflow (install once)

YAML template: [`docs/ci/demo.yml`](./ci/demo.yml) — copy to `.github/workflows/demo.yml` when your token has the `workflow` scope.
