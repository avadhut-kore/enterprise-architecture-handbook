# Distributed Tracing and Context Propagation

## 1. The W3C Trace Context Standard
When a single business transaction spans an API Gateway, an iPaaS flow, a Kafka cluster, and an ERP backend, distributed tracing is the only way to visualize the end-to-end path. Integration components must support the **W3C Trace Context** specification (`traceparent` header).

```
W3C traceparent format:
00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
│  │                                │                │
│  └─ Trace ID (16 bytes)           └─ Span ID (8 B) └─ Trace Flags (Sampled)
└─ Version
```

## 2. Asynchronous Context Propagation Across Kafka

```
[Producer Service] ──> Injects traceparent into Kafka Record Header
                              │
                              ▼
                         [Kafka Broker] (Carries header unchanged)
                              │
                              ▼
[Consumer Service] ──> Extracts traceparent from Header ──> Creates Child Span
```

## 3. OpenTelemetry Implementation
```python
from opentelemetry import trace
from opentelemetry.propagate import extract, inject

tracer = trace.get_tracer("integration.bridge")

def process_incoming_event(headers: dict, payload: dict):
    # Extract distributed context from incoming transport headers
    parent_context = extract(headers)
    
    with tracer.start_as_current_span("process_event", context=parent_context) as span:
        span.set_attribute("integration.payload_size", len(str(payload)))
        span.set_attribute("integration.partner_id", payload.get("partner_id"))
        # Execute business integration logic
```
