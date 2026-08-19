import { createHmac, timingSafeEqual } from "node:crypto";

export type SourceNode = "HIN" | "AIMN";
export type Stream = "thermal_hydration" | "ecg" | "status" | "isolation";
export type Quality = "valid" | "degraded" | "unavailable" | "stale" | "isolated";

export interface TelemetryEnvelope {
  version: "1.0";
  sourceNode: SourceNode;
  sequence: number;
  timestampMs: number;
  stream: Stream;
  quality: Quality;
  payload: Record<string, unknown>;
  integrity: { algorithm: "HMAC-SHA-256"; tag: string; keyId: string };
}

export function canonicalBody(envelope: Omit<TelemetryEnvelope, "integrity">): string {
  return JSON.stringify(envelope);
}

export function signEnvelope(
  envelope: Omit<TelemetryEnvelope, "integrity">,
  key: Buffer,
  keyId = "development-key"
): TelemetryEnvelope {
  const tag = createHmac("sha256", key).update(canonicalBody(envelope)).digest("base64url");
  return { ...envelope, integrity: { algorithm: "HMAC-SHA-256", tag, keyId } };
}

export function verifyEnvelope(envelope: TelemetryEnvelope, key: Buffer): boolean {
  const { integrity, ...body } = envelope;
  if (integrity.algorithm !== "HMAC-SHA-256") return false;
  const expected = createHmac("sha256", key).update(canonicalBody(body)).digest();
  const received = Buffer.from(integrity.tag, "base64url");
  return received.length === expected.length && timingSafeEqual(received, expected);
}

export function assertSupportedRate(stream: Stream, rateHz: number): void {
  const expected = stream === "ecg" ? 250 : stream === "thermal_hydration" ? 10 : undefined;
  if (expected !== undefined && rateHz !== expected) {
    throw new Error(`Unsupported ${stream} polling rate: expected ${expected} Hz, received ${rateHz} Hz`);
  }
}
