# Cascade & Fallback Routing Architecture

## 1. The Fallback Cascade Topology

Cloud foundation model APIs regularly experience rate limit spikes (HTTP 429) or regional service degradations (HTTP 503). An enterprise cannot allow an external cloud vendor's outage to halt internal business operations.

```mermaid
flowchart TD
    Req["User Request"] --> Primary["1. Primary Target: Azure OpenAI (East US)\nModel: GPT-4o"]
    
    Primary -->|HTTP 429 / 503 / Timeout > 2s| Fallback1["2. Cross-Region Failover: Azure OpenAI (West US)\nModel: GPT-4o"]
    Fallback1 -->|HTTP 429 / 503 / Timeout > 2s| Fallback2["3. Cross-Cloud Failover: AWS Bedrock (us-east-1)\nModel: Claude 3.5 Sonnet"]
    Fallback2 -->|HTTP 429 / 503 / Timeout > 2s| Fallback3["4. On-Premise Emergency Fallback: Private vLLM Cluster\nModel: Llama-3-70B-Instruct"]
    Fallback3 -->|All Fail| CircuitBreaker["5. Circuit Breaker Trips -> Return Degraded Deterministic Error"]
```

---

## 2. Architectural Invariants
1. **Sub-150ms Switchover**: Gateway failover between providers must occur within 150ms upon receiving a 429 or 5xx error.
2. **Idempotency Key Preservation**: When retrying a failed request against a fallback provider, preserve the original transaction idempotency key to prevent duplicate billing or side effects.
