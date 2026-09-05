# Token Telemetry & Latency SRE Metrics

## 1. The Core SRE Metrics for GenAI

Traditional HTTP metrics (P99 request latency) are misleading for streaming LLMs because a 10-second response that streams immediately feels fast, whereas a 2-second response that blocks feels slow.

```mermaid
flowchart LR
    Req["Request Start"] --> TTFT["Time-to-First-Token (TTFT)\nTarget: < 800ms\nMeasures: Gateway + Prefill Phase"]
    TTFT --> TPOT["Time-per-Output-Token (TPOT)\nTarget: < 30ms / token (33 tps)\nMeasures: Decode Phase & GPU Bandwidth"]
    TPOT --> E2E["Total E2E Latency\nMeasures: Full generation completion"]
```

---

## 2. Multi-Window Alerting on Token Burn
* Apply SRE multi-window burn-rate alerting (from Phase 7) to **Token Budgets**:
  * If an application consumes $> 5\%$ of its monthly allocated token quota within a 1-hour window, trigger a High-Severity PagerDuty incident to halt runaway loops.
