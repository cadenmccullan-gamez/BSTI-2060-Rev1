from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Any, Literal

from .telemetry import Integrity, TelemetryEnvelope, verify_envelope

app = FastAPI(title="BSTI-2060-Rev.1 Telemetry API", version="0.1.0")

class IntegrityModel(BaseModel):
    algorithm: Literal["HMAC-SHA-256"]
    tag: str = Field(min_length=16)
    keyId: str = Field(min_length=1)

class EnvelopeModel(BaseModel):
    version: Literal["1.0"]
    sourceNode: Literal["HIN", "AIMN"]
    sequence: int = Field(ge=0)
    timestampMs: int = Field(ge=0)
    stream: Literal["thermal_hydration", "ecg", "status", "isolation"]
    quality: Literal["valid", "degraded", "unavailable", "stale", "isolated"]
    payload: dict[str, Any]
    integrity: IntegrityModel

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "bsti-2060-rev1"}

@app.post("/v1/telemetry/validate")
def validate_telemetry(envelope: EnvelopeModel) -> dict[str, Any]:
    key = b"development-only-key"
    parsed = TelemetryEnvelope(
        version=envelope.version,
        sourceNode=envelope.sourceNode,
        sequence=envelope.sequence,
        timestampMs=envelope.timestampMs,
        stream=envelope.stream,
        quality=envelope.quality,
        payload=envelope.payload,
        integrity=Integrity(**envelope.integrity.model_dump()),
    )
    if not verify_envelope(parsed, key):
        raise HTTPException(status_code=400, detail="telemetry integrity validation failed")
    return {"accepted": True, "sequence": envelope.sequence, "stream": envelope.stream}
