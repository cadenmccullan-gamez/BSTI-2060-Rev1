from __future__ import annotations

import base64
import hashlib
import hmac
import json
from dataclasses import asdict, dataclass
from typing import Any, Literal

SourceNode = Literal["HIN", "AIMN"]
Stream = Literal["thermal_hydration", "ecg", "status", "isolation"]
Quality = Literal["valid", "degraded", "unavailable", "stale", "isolated"]

@dataclass(frozen=True)
class Integrity:
    algorithm: Literal["HMAC-SHA-256"]
    tag: str
    keyId: str

@dataclass(frozen=True)
class TelemetryEnvelope:
    version: Literal["1.0"]
    sourceNode: SourceNode
    sequence: int
    timestampMs: int
    stream: Stream
    quality: Quality
    payload: dict[str, Any]
    integrity: Integrity

def _body(envelope: TelemetryEnvelope | dict[str, Any]) -> bytes:
    data = asdict(envelope) if isinstance(envelope, TelemetryEnvelope) else envelope
    data = {k: v for k, v in data.items() if k != "integrity"}
    return json.dumps(data, separators=(",", ":"), ensure_ascii=False).encode()

def sign_envelope(body: dict[str, Any], key: bytes, key_id: str = "development-key") -> TelemetryEnvelope:
    tag = base64.urlsafe_b64encode(hmac.new(key, _body(body), hashlib.sha256).digest()).rstrip(b"=").decode()
    return TelemetryEnvelope(**body, integrity=Integrity("HMAC-SHA-256", tag, key_id))

def verify_envelope(envelope: TelemetryEnvelope, key: bytes) -> bool:
    expected = hmac.new(key, _body(envelope), hashlib.sha256).digest()
    padded = envelope.integrity.tag + "=" * (-len(envelope.integrity.tag) % 4)
    try:
        received = base64.urlsafe_b64decode(padded)
    except ValueError:
        return False
    return envelope.integrity.algorithm == "HMAC-SHA-256" and hmac.compare_digest(received, expected)

def assert_supported_rate(stream: Stream, rate_hz: int) -> None:
    expected = {"ecg": 250, "thermal_hydration": 10}.get(stream)
    if expected is not None and rate_hz != expected:
        raise ValueError(f"Unsupported {stream} polling rate: expected {expected} Hz, received {rate_hz} Hz")
