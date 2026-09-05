# Trust Boundaries in Enterprise Integration

## 1. Architectural Definition
A trust boundary defines the perimeter between computing environments operating under different administrative authorities, security postures, or governance policies. In distributed enterprise integration, traversing a trust boundary mandates zero implicit trust: every network packet, payload, and authentication token must be verified, sanitized, and authorized.

```
       Zone 0: Public / Untrusted (Internet, Third-Party SaaS)
                         │
        ═════════════════▼═════════════════  [Trust Boundary 1: API Gateway / WAF / mTLS]
       Zone 1: DMZ / Ingress Layer (Edge Reverse Proxy, OAuth2 PDP)
                         │
        ═════════════════▼═════════════════  [Trust Boundary 2: Zero Trust Mesh / Internal mTLS]
       Zone 2: Enterprise Core (Microservices, Event Brokers, iPaaS)
                         │
        ═════════════════▼═════════════════  [Trust Boundary 3: Regulated Bastion / Mainframe Gateway]
       Zone 3: High-Security Vault (Core Banking, Payment HSM, Regulated DBs)
```

## 2. Trust Boundary Traversal Patterns

| Boundary Type | Risk Level | Authentication Strategy | Payload Validation | Observability Requirements |
| :--- | :--- | :--- | :--- | :--- |
| **External to DMZ** | Extreme (Untrusted Internet) | Mutual TLS + OAuth2 (Token Exchange) | Strict JSON Schema / XML DTD denial | Full L7 WAF audit, client IP geofencing |
| **DMZ to Enterprise Core** | High (Semi-trusted edge) | mTLS + Workload Identity (SPIFFE/mTLS) | Schema enforcement, threat sanitization | Distributed trace propagation, PDP audit |
| **Core to Core (East-West)**| Medium (Internal VPC) | Service Mesh mTLS, short-lived JWT | Strict gRPC/OpenAPI contract checking | Sampling distributed traces, metric counts |
| **Core to Regulated Vault** | Critical (PCI / Core Ledger) | Dedicated proxy, hardware client certs | Strict field tokenization & masking | Immutable write-ahead tamper-evident log |

## 3. Threat Modeling Across Boundaries

```
[External SaaS Webhook] 
       │ (Untrusted Payload, spoofable source IP)
       ▼
[Webhook Receiver (DMZ)] ──> [HMAC Signature Validation] (Verify SHA-256 header)
       │
       ▼ (Sanitized & Normalized Payload)
[Ingress Message Queue] ──> [Kafka / Event Hub with mTLS SASL/SCRAM-512]
       │
       ▼
[Internal Business Core] ──> [Decrypt & Tokenize Sensitive PII]
```

### STRIDE Assessment Matrix
- **Spoofing**: Prevented via hardware-bound certificates (mTLS) and cryptographically signed tokens (JWS).
- **Tampering**: Prevented via payload HMAC-SHA256 signatures, cryptographic checksums, and TLS 1.3 cipher enforcement.
- **Repudiation**: Prevented through non-repudiation event logs containing signed message digests and timestamp authorities (RFC 3161).
- **Information Disclosure**: Prevented using envelope encryption (JWE) and field-level tokenization prior to transport.
- **Denial of Service**: Prevented via edge token bucket rate limiting, IP reputation filtering, and payload size bounds (e.g., max 10MB).
- **Elevation of Privilege**: Prevented via Policy Decision Points (PDP) enforcing Attribute-Based Access Control (ABAC).

## 4. Architectural Decision Criteria
1. **Never Forward Raw External Identity**: Translate external consumer tokens into short-lived, constrained internal actor tokens at the DMZ gateway.
2. **Isolate Regulated Subnets**: Core banking engines and cardholder environments (CDE) must never connect directly to outbound internet proxies.
3. **Canonical Diagram Reference**: Refer to [17-diagrams/security/zero-trust-architecture.md](../../17-diagrams/security/zero-trust.md).
