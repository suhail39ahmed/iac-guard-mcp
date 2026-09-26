# iac-guard-mcp

![License](https://img.shields.io/badge/license-Apache_2.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Status](https://img.shields.io/badge/status-0.1.0%20MVP-green.svg)

**IaC `review_diff` for agents: Checkov (optional) or builtin regex policies over Terraform/Bicep — structured findings JSON.**

> Who it's for: Cloud security + platform SAs embedding IaC review into agent workflows.

## Why this exists

PR bots that only say "looks fine" are useless. `iac-guard` reviews fixtures (or diffs) for classic Azure foot-guns — open NSGs, public blobs — and returns findings plus a static explanation template agents can cite.

## Install

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
# optional MCP SDK transport:
pip install -e ".[mcp]"
# optional Checkov:
pip install checkov
```

Or with pipx (once published to PyPI): `pipx install iac-guard-mcp` — until then use editable install from this repo.

## 30-second demo

```bash
python -m iac_guard --help
python -m iac_guard fixtures/bad_nsg.tf || true
python -m iac_guard fixtures/bad_nsg.bicep || true
```

Or simply:

```bash
make demo
```

## What it is NOT

- Not a full OPA / Gatekeeper platform
- Not an auto-remediator that runs terraform apply
- Not a substitute for org policy + Defender for Cloud

## Architecture

![Architecture](assets/architecture.svg)

## Roadmap

- [ ] More builtin Azure policies (private endpoints, TLS)
- [ ] PR comment formatter
- [ ] MCP tool for multi-file diffs

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md). Be kind — [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md). Security reports: [SECURITY.md](./SECURITY.md).

## MCP / Cursor plug-in

Install the optional MCP extra, then point Cursor (or any MCP host) at the stdio server:

```bash
pip install -e ".[mcp]"
```

Example `~/.cursor/mcp.json` entry:

```json
{
  "mcpServers": {
    "iac-guard-mcp": {
      "command": "python",
      "args": ["-m", "iac_guard.mcp_server"],
      "cwd": "/absolute/path/to/iac-guard-mcp"
    }
  }
}
```

Without the SDK, list tool schemas via CLI (`tools` subcommand where available) or see `src/iac_guard/` for the JSON-RPC-shaped tool table.

## License

Apache-2.0
