# Release Status — BSTI-2060-Rev.1

**Status:** Public engineering reference implementation  
**Version:** Revision 1 source baseline  
**Maturity:** Pre-certification development; not a clinical or consumer medical product.

## Reviewer Route

Review the [README](README.md), consolidated [technical specification](docs/BSTI-2060-Rev1-consolidated.md), [requirements traceability](docs/requirements-traceability.md), telemetry contract in `contracts/`, TypeScript implementation in `typescript/`, and Python implementation in `python/`.

## Verified Quality Gates

| Component | Check | Result |
|---|---|---|
| TypeScript | `npm test` | Passed |
| TypeScript | `npm run build` | Passed |
| Python | `python -m pip install -e ".[dev]"` from `python/` | Passed |
| Python | `python -m pytest -q` from `python/` | Passed |

The cross-language checks are defined in `.github/workflows/ci.yml` for push and pull-request review.

## Public Review Boundary

The repository provides protocol and validation reference code. It does not establish safety, biocompatibility, electrical safety, cybersecurity, clinical performance, manufacturing quality, regulatory clearance, authorization for human use, or a completed hardware system.

## Current Non-Goals

Do not represent this codebase as a medical device, diagnostic system, medical advice, or a deployable patient-care product. The repository documents engineering concepts that require qualified design controls, verification, validation, cybersecurity analysis, and regulatory review before any clinical or commercial use.
