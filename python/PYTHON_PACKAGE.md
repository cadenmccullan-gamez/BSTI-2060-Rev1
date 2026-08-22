# BSTI-2060-Rev.1 Python Package

This package contains the Python reference implementation for the BSTI-2060-Rev.1 telemetry envelope, integrity verification, supported stream-rate validation, and FastAPI validation endpoints.

## Installation and Verification

Run the following from the `python/` directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m pytest -q
```

The package is an engineering reference implementation. It is not a clinical device, a safety-certified system, a regulated medical product, or authorization for use with humans. The parent repository contains the consolidated technical specification, shared TypeScript reference implementation, requirements traceability, and system-level limitations.
