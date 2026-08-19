# BSTI-2060-Rev.1 Requirements Traceability

**Authors:** Alexis M Adams; Nicholas Michael Grossi  
**Status:** Initial official repository baseline

| Requirement ID | Requirement summary | Implementation | Verification |
|---|---|---|---|
| BSTI-INT-001 | Telemetry envelope shall identify version, source node, sequence, timestamp, stream, quality, payload, and integrity metadata. | `contracts/telemetry.schema.json`; `typescript/src/telemetry.ts`; `python/bsti2060/telemetry.py` | Schema validation and language-specific unit tests |
| BSTI-INT-002 | Integrity protection shall use an authenticated mechanism rather than an unspecified checksum. | `typescript/src/telemetry.ts`; `python/bsti2060/telemetry.py` | Valid-message verification and modified-payload rejection tests |
| BSTI-SNS-001 | ECG acquisition baseline shall be 250 Hz for the defined HRV use case. | `assertSupportedRate()` in both implementations | Polling-rate tests; waveform validation remains a hardware/system test |
| BSTI-SNS-002 | Thermal and hydration indices shall use a decoupled 10 Hz baseline. | `assertSupportedRate()` in both implementations | Polling-rate tests; reference-method validation remains open |
| BSTI-FLS-001 | Telemetry quality shall distinguish valid, degraded, unavailable, stale, and isolated states. | Shared JSON schema and language models | Contract validation and state-transition tests planned |
| BSTI-FLS-002 | HIN shall remain capable of local safety behavior during communications failure. | System architecture requirement; hardware implementation pending | Communications-outage and isolation testing required |
| BSTI-PWR-001 | Kinetic harvesting shall be supplemental and not the sole primary power source. | System-level requirement; power subsystem implementation pending | No-motion, movement, battery aging, and peak-load test plan required |
| BSTI-BIO-001 | Skin-contact formulation and final article require risk-based biological evaluation. | Documentation requirement; formulation implementation pending | ISO 10993-based biological evaluation plan required |
| BSTI-SEC-001 | Security lifecycle, key management, secure updates, and auditability shall be defined before production. | Protocol key identifier is represented; lifecycle controls pending | Threat model, key-management, secure-boot, update, and logging assessments required |

## Traceability status

The protocol contract and reference integrity functions are implemented as a development baseline. Hardware safety, biocompatibility, sterility, thermal regulation, radio performance, clinical performance, and production cybersecurity remain open engineering work and are not represented as verified by this repository.
