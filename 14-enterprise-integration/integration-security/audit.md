# Security Audit Logging and Tamper-Evidence

## 1. What to Log in Integration Flows
Every integration transaction crossing boundaries must generate a structured security audit log:
- **Timestamp**: High-precision UTC timestamp (ISO 8601 with milliseconds).
- **Correlation ID / Trace ID**: OpenTelemetry compliant distributed trace context.
- **Actor Identity**: Authenticated client ID, certificate subject DN, or authenticated user ID.
- **Source & Destination**: Client IP address, gateway node, target endpoint URI.
- **Action & Result**: HTTP verb, gRPC method, HTTP response status code, authorization outcome (`ALLOW`/`DENY`).
- **Payload Digest**: Cryptographic hash (SHA-256) of the request/response body (never log plaintext sensitive data).

## 2. Tamper-Evident Write-Ahead Audit Trail
To satisfy SOX, PCI-DSS, and regulatory audits, audit logs must be streamed in real-time to an immutable, append-only log store (e.g., AWS S3 with Object Lock or dedicated WORM compliance clusters).
