# Distributed Tracing Architecture & Sampling Strategies

## Executive Summary

Distributed tracing reconstructs the complete execution journey of a request as it traverses across load balancers, microservices, asynchronous message queues, and databases.

---

## 1. W3C Trace Context Propagation

```text
HTTP Request Header:
traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
              │                    │                                │        │
           Version             Trace ID                          Span ID   Flags (Sampled)
```
- Every service downstream parses `traceparent`, attaches its own newly generated `span_id`, and propagates the header to the next outbound RPC or database query.

---

## 2. Head vs Tail Sampling

- **Head Sampling**: The initial ingress gateway decides randomly at the start of a request whether to record the trace (e.g., 5% sample rate). Disadvantage: May drop the 0.01% of requests that subsequently fail with a 500 error deep in the stack.
- **Tail Sampling**: The OpenTelemetry Collector buffers all spans in memory until the request completes. If the request encounters an HTTP 5xx error or exceeds the latency SLA, it is **100% sampled and retained**; clean fast requests are sampled at 1%.
