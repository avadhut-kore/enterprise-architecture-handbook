# Outbound Webhook Delivery Specification

## 1. Delivery Guarantees & Security
* All outbound webhook payloads MUST be signed with an HMAC-SHA256 signature passed in the `X-Signature-SHA256` header.
* Delivery retry schedule: Exponential backoff with jitter (immediate, 1m, 5m, 15m, 1h, 6h, 24h).
* Automatic circuit breaking: Disable webhook endpoint after 50 consecutive failed deliveries.
