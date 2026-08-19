import assert from "node:assert/strict";
import test from "node:test";
import { assertSupportedRate, signEnvelope, verifyEnvelope } from "../src/telemetry.js";

const key = Buffer.from("development-only-key");
const body = {
  version: "1.0" as const,
  sourceNode: "HIN" as const,
  sequence: 1,
  timestampMs: 1700000000000,
  stream: "ecg" as const,
  quality: "valid" as const,
  payload: { samples: [0.1, 0.2, 0.3] }
};

test("signs and verifies a telemetry envelope", () => {
  const envelope = signEnvelope(body, key);
  assert.equal(verifyEnvelope(envelope, key), true);
});

test("rejects a modified payload", () => {
  const envelope = signEnvelope(body, key);
  const modified = { ...envelope, payload: { samples: [9.9] } };
  assert.equal(verifyEnvelope(modified, key), false);
});

test("enforces decoupled polling rates", () => {
  assert.doesNotThrow(() => assertSupportedRate("ecg", 250));
  assert.doesNotThrow(() => assertSupportedRate("thermal_hydration", 10));
  assert.throws(() => assertSupportedRate("ecg", 10));
});
