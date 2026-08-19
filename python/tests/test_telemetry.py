import pytest

from bsti2060.telemetry import assert_supported_rate, sign_envelope, verify_envelope

KEY = b"development-only-key"
BODY = {
    "version": "1.0",
    "sourceNode": "HIN",
    "sequence": 1,
    "timestampMs": 1700000000000,
    "stream": "ecg",
    "quality": "valid",
    "payload": {"samples": [0.1, 0.2, 0.3]},
}

def test_sign_and_verify():
    envelope = sign_envelope(BODY, KEY)
    assert verify_envelope(envelope, KEY)

def test_modified_payload_is_rejected():
    envelope = sign_envelope(BODY, KEY)
    modified = envelope.__class__(
        version=envelope.version,
        sourceNode=envelope.sourceNode,
        sequence=envelope.sequence,
        timestampMs=envelope.timestampMs,
        stream=envelope.stream,
        quality=envelope.quality,
        payload={"samples": [9.9]},
        integrity=envelope.integrity,
    )
    assert not verify_envelope(modified, KEY)

def test_decoupled_rates():
    assert_supported_rate("ecg", 250)
    assert_supported_rate("thermal_hydration", 10)
    with pytest.raises(ValueError):
        assert_supported_rate("ecg", 10)
