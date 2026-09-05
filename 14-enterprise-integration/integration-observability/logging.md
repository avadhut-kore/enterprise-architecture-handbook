# Structured Logging in Enterprise Integration

## 1. The Standard of Structured Logging
Unstructured string logging (`log.info("Processing order for " + id)`) is unacceptable in distributed enterprise integration. All integration services, gateways, and middleware must emit **structured JSON logs** conforming to a unified corporate schema.

## 2. Enterprise Integration Log Schema
```json
{
  "@timestamp": "2026-09-05T12:30:45.102Z",
  "log.level": "INFO",
  "service.name": "payment-orchestrator",
  "service.version": "3.4.1",
  "trace.id": "4bf92f3577b34da6a3ce929d0e0e4736",
  "span.id": "00f067aa0ba902b7",
  "correlation.id": "CORR-2026-991827",
  "event.action": "PAYMENT_INITIATED",
  "integration": {
    "source_system": "MOBILE_APP",
    "target_system": "CORE_BANKING",
    "protocol": "REST_HTTPS",
    "idempotency_key": "IDEMP-8172910"
  },
  "http": {
    "method": "POST",
    "route": "/v1/transfers",
    "status_code": 201,
    "duration_ms": 142.5
  },
  "message": "Payment transfer successfully authorized and ledger entry created"
}
```

## 3. Golden Rules of Integration Logging
1. **Never Log Sensitive Data**: Strip credit card PANs, passwords, session tokens, and unencrypted PII before log formatting.
2. **Always Include Trace Context**: Inject W3C `traceparent` and correlation IDs into every log line to enable instant log aggregation across 20+ microservices.
3. **Log at System Boundaries**: Log ingress requests, external vendor invocations, and database transactions; avoid spamming high-frequency internal loops.
