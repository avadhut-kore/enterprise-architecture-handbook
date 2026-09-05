# Request Signing & Replay Protection (HMAC-SHA256)

## Executive Summary

For high-stakes financial transactions, webhook deliveries, and inter-banking APIs, TLS and bearer tokens are insufficient. The request payload itself must be cryptographically signed to guarantee **Integrity, Authenticity, and Non-Repudiation**.

---

## 1. Cryptographic Request Signing Specification

To send a signed request:
1. Client computes the canonical request string:
   $$\text{CanonicalString} = \text{HTTP\_METHOD} + "\n" + \text{URI} + "\n" + \text{Timestamp} + "\n" + \text{Nonce} + "\n" + \text{SHA256}(\text{RequestBody})$$
2. Client computes the HMAC signature:
   $$\text{Signature} = \text{HMAC-SHA256}(K_{\text{shared\_secret}}, \text{CanonicalString})$$
3. Client attaches headers:
   - `X-Signature: hex(Signature)`
   - `X-Timestamp: 1772712000`
   - `X-Nonce: 4f8a9b2c...`

### Server-Side Validation:
1. **Clock Skew Check**: If $|\text{current\_time} - \text{Timestamp}| > 300\text{ seconds}$, reject with HTTP 401 (prevents delayed replay).
2. **Nonce De-duplication**: Check if `Nonce` exists in Redis cache. If found, reject (replay attack!). If not found, store in Redis with 5-minute TTL.
3. **Signature Recomputation**: Recompute HMAC over canonical string. If signatures do not match byte-for-byte, reject with HTTP 401.
