# Application Logging: Security Event Logging & SIEM Integration

## 1. Architectural Purpose & Problem Context
Logging failed logins, permission denials, and privilege escalations for security monitoring.

---

## 2. Structural Log Format Example

```json
{
  "timestamp": "2026-09-05T12:00:00.123Z",
  "level": "INFO",
  "service": "ordering-service",
  "environment": "production",
  "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
  "span_id": "00f067aa0ba902b7",
  "user_id": "usr_998124",
  "message": "Order successfully placed",
  "order_id": "ord_5521",
  "total_cents": 4999
}
```

---

## 3. Production Invariants
- All logs must be written to `stdout` in JSON format; let container runtimes and log shippers (Fluentbit/Vector) handle ingestion.
- Never log plaintext credentials, tokens, or unmasked PII.
