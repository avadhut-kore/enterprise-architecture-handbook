# The Universal Enterprise Structured Log Schema

## 1. Executive Summary
Unstructured string logging (`logger.info("User " + userId + " logged in from " + ip)`) is completely un-parseable at enterprise scale without fragile, CPU-intensive regular expressions.

All applications in an enterprise fleet must emit **single-line, valid JSON objects** adhering to the **Universal Enterprise Structured Log Schema**. Emitting structured JSON enables instant field-level filtering, automated indexing, and direct correlation with distributed traces.

---

## 2. The Universal JSON Schema Spec

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "EnterpriseStructuredLog",
  "type": "object",
  "required": [
    "timestamp",
    "severity",
    "service",
    "environment",
    "message",
    "trace_id",
    "span_id"
  ],
  "properties": {
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "ISO-8601 UTC timestamp with millisecond precision (YYYY-MM-DDTHH:mm:ss.sssZ)"
    },
    "severity": {
      "type": "string",
      "enum": ["TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL"]
    },
    "service": {
      "type": "string",
      "description": "Canonical service name matching OpenTelemetry service.name"
    },
    "version": {
      "type": "string",
      "description": "Application version or Git commit hash"
    },
    "environment": {
      "type": "string",
      "enum": ["production", "staging", "development"]
    },
    "host": {
      "type": "string",
      "description": "Kubernetes pod name or physical hostname"
    },
    "trace_id": {
      "type": "string",
      "pattern": "^[0-9a-f]{32}$",
      "description": "W3C 128-bit Trace ID in hexadecimal format"
    },
    "span_id": {
      "type": "string",
      "pattern": "^[0-9a-f]{16}$",
      "description": "W3C 64-bit Span ID in hexadecimal format"
    },
    "message": {
      "type": "string",
      "description": "Concise human-readable log message"
    },
    "error": {
      "type": "object",
      "properties": {
        "class": { "type": "string" },
        "code": { "type": "string" },
        "message": { "type": "string" },
        "stack_trace": { "type": "string" }
      }
    },
    "context": {
      "type": "object",
      "description": "Arbitrary key-value metadata specific to the event (PII-free)"
    }
  }
}
```

---

## 3. Concrete Production Example

```json
{
  "timestamp": "2026-09-05T14:22:18.492Z",
  "severity": "ERROR",
  "service": "payment-processing-service",
  "version": "3.14.2",
  "environment": "production",
  "host": "payment-pod-7bf88c9f5d-kx92j",
  "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
  "span_id": "00f067aa0ba902b7",
  "message": "Downstream payment rail gateway rejected credit card authorization",
  "error": {
    "class": "com.enterprise.payment.GatewayTimeoutException",
    "code": "PAY_GATEWAY_TIMEOUT_504",
    "message": "Read timed out after 3000ms connecting to api.stripe.com",
    "stack_trace": "com.enterprise.payment.GatewayTimeoutException: Read timed out...\n\tat com.enterprise.payment.StripeClient.authorize(StripeClient.java:84)"
  },
  "context": {
    "tenant_id": "enterprise-acme-corp",
    "payment_method": "card",
    "currency": "USD",
    "amount_cents": 14900,
    "retry_attempt": 2
  }
}
```

---

## 4. Architectural Rules for Log Formatting

1. **Standard Output Emission**: Applications must log strictly to `stdout` / `stderr`. They must never write directly to local disk files or execute remote network socket calls inside application threads. Container runtimes (Docker/containerd) buffer stdout and allow node agents to collect them asynchronously.
2. **Single-Line Invariant**: Multiline stack traces must be serialized as escaped `\n` characters within the single JSON `"stack_trace"` attribute. Splitting a stack trace across 50 separate stdout lines breaks log aggregation parsers.
