# Observability Redaction & Privacy Architecture

## 1. The Accidental Telemetry Data Breach

Logging full raw user prompts and completions directly into centralized APM log stores (Datadog, Splunk, Elasticsearch) is a major data breach risk: developers and SREs viewing traces gain unauthorized access to customer credit card numbers, passwords, and proprietary company secrets.

---

## 2. Architectural Redaction Pipeline
The OpenTelemetry Collector must sit between the AI Gateway and centralized log stores, running an in-stream **Redaction Processor**:

```mermaid
flowchart LR
    GW["AI Gateway Trace Emission"] --> OTelCol["OTel Collector (Redaction Processor)"]
    OTelCol --> Filter{"Config: capture_prompt_payloads?"}
    Filter -->|false (Strict Production)| DropText["Strip `gen_ai.prompt` and `gen_ai.completion` attributes\nRetain ONLY token counts, latency, and model metadata"]
    Filter -->|true (Staging / Debug)| MaskPII["Execute Regex & NER Masking on Prompt Strings"]
    DropText & MaskPII --> CentralLogs[("Centralized Telemetry Store")]
```
