# Security Policy

## Supported versions

This project is early-stage (0.x). Security fixes land on `main` only.

## Reporting a vulnerability

Please **do not** open a public issue for security-sensitive findings.

1. Use GitHub **Security Advisories** → *Report a vulnerability* on this repository, **or**
2. Email the maintainer listed on the GitHub profile (subject: `[SECURITY] <repo-name>`).

Include:

- Affected version / commit
- Reproduction steps (minimal)
- Impact assessment

You should receive an acknowledgement within a few business days.

## What this project deliberately avoids

- No production secrets, service principals, or connection strings in the repo
- Demo paths use local fixtures only
- Live cloud calls (if any) require explicit env configuration and are opt-in

## Secrets handling for contributors

- Copy `.env.example` → `.env` locally; never commit `.env`
- Prefer least-privilege identities when wiring live Azure / ADO adapters later
