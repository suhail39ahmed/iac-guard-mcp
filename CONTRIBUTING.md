# Contributing

Thanks for taking an interest. This repo is part of an open portfolio of
**Azure AI / DevOps** tools meant to be honest, fixture-driven, and adoptable.

## Ground rules

1. Keep demos **offline-first** with fixtures under `fixtures/`, `sample_corpus/`, `sandbox/`, or `examples/`.
2. Do not invent production metrics, star counts, or customer claims in docs.
3. No secrets in commits (see `SECURITY.md`).
4. Prefer small, reviewable PRs with a clear "why".

## Dev setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
make demo                   # or see README Quickstart
```

## Pull requests

- Update / add fixtures when changing behavior
- Keep `make demo` green
- If you change CLI flags, update README + `docs/DEMO.md`
- Be kind in review comments (see `CODE_OF_CONDUCT.md`)

## Ideas that fit well

- Better fixture coverage
- Clearer RCA / policy / eval rules
- Optional MCP SDK transport polish
- Docs / Loom script clarity

## Ideas that need discussion first

- Live cloud adapters with write privileges
- Auto-apply remediations without human approval
- Large dependency footprint for the default install
