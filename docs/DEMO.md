# Demo — iac-guard-mcp

Loom / screen recording script (**60–90 seconds**). Speak calmly; show the terminal, not slides.

## Setup (before record)

```bash
cd iac-guard-mcp
python -m venv .venv && source .venv/bin/activate
pip install -e .
# clear scrollback; font size ~16–18pt; dark theme
```

## Exact click / type script

1. Open terminal at repo root. Say: *"This is iac-guard-mcp — IaC `review_diff` for agents: Checkov (optional) or builtin regex policies over …"*
2. Type `make demo` **or** walk the commands below one by one.
1. Run `python -m iac_guard --help` — wait for JSON / output.
2. Run `python -m iac_guard fixtures/bad_nsg.tf || true` — wait for JSON / output.
3. Run `python -m iac_guard fixtures/bad_nsg.bicep || true` — wait for JSON / output.
3. Scroll the JSON briefly. Call out one concrete field (citation path, `human_approval_required`, findings, report path, etc.).
4. Close with: *"Offline fixtures only — clone it, `make demo`, adopt the pattern."* Link the GitHub repo in the Loom description.

## Talking points (pick 2)

- Who it's for: Cloud security + platform SAs embedding IaC review into agent workflows.
- What it is NOT: Not a full OPA / Gatekeeper platform
- Honest MVP: no fabricated production metrics

## Outro card (last 3s)

`github.com/suhail39ahmed/iac-guard-mcp`
