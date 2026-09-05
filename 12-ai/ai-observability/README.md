# AI Observability & Tracing Architecture (`ai-observability/`)

## Executive Summary

Observability for Artificial Intelligence systems requires tracking distributed spans that link user requests, gateway rate limiters, vector search retrievals, raw model token generations, and downstream tool execution calls.

---

## Directory Catalog

* **[OpenTelemetry GenAI Semantic Conventions](opentelemetry-genai-semantic-conventions.md)** — Standardizing spans, attributes, and events for LLM workloads.
* **[Token Telemetry & Latency Tracing](token-telemetry-and-latency-tracing.md)** — Tracking Time-to-First-Token (TTFT), Time-per-Output-Token (TPOT), and token counts.
* **[Observability Redaction & Privacy](observability-redaction-and-privacy.md)** — Ensuring sensitive prompts and confidential customer records are never logged in plain text.
