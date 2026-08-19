# BSTI-2060-Rev.1

## Biometric Support and Telemetry Interface

**Authors:** Alexis M Adams; Nicholas Michael Grossi  
**Repository status:** Official engineering codebase — pre-certification development  
**System designation:** BSTI-2060-Rev.1

BSTI-2060-Rev.1 is a dual-node wearable telemetry platform for epidermal protection, thermal regulation, and authenticated vital-sign data exchange between a Human Interface Node (HIN) and an Artificial Intelligence Monitoring Node (AIMN).

This repository contains coordinated TypeScript/Node.js and Python/FastAPI reference implementations, a language-neutral telemetry schema, traceable requirements, validation tests, and engineering documentation.

> This codebase is not a clinical device, regulatory approval, sterilization validation, or authorization for human use. Hardware, biocompatibility, electrical safety, cybersecurity, and clinical claims require qualified review and formal verification before deployment.

## Repository layout

| Path | Purpose |
|---|---|
| `contracts/` | Language-neutral telemetry schemas and protocol contracts |
| `typescript/` | Node.js/TypeScript protocol and validation implementation |
| `python/` | Python/FastAPI protocol and validation implementation |
| `docs/` | Official technical specification, requirements, and verification plans |
| `.github/` | Continuous integration and repository governance |

## Core design boundaries

The Human Interface Node performs local acquisition, quality assessment, buffering, integrity protection, and isolation behavior. The Artificial Intelligence Monitoring Node receives authenticated telemetry and reports monitoring state, but it is not assumed to be the sole safety controller. Communications loss, stale data, authentication failure, and sensor degradation are represented as explicit states.

The shared envelope uses authenticated integrity metadata rather than an unspecified checksum. Production deployments must add a reviewed key-management system, authenticated transport, replay protection, audit logging, secure update controls, and threat-model evidence.

## Development commands

### TypeScript

```bash
cd typescript
npm install
npm test
npm run build
```

### Python

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Engineering references

The complete consolidated specification and reference list are in `docs/BSTI-2060-Rev1-consolidated.md`. Requirements traceability is in `docs/requirements-traceability.md`. These documents distinguish design targets from verified results.
