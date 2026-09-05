# Model Routing Decision Framework

## 1. Decision Criteria & Trade-Off Matrix

```mermaid
flowchart TD
    Req["Inbound Request"] --> Classifier["Analyze Intent & Constraint"]
    
    Classifier --> C1{"Task Type?"}
    C1 -->|Classification / Entity Extraction| RouteSLM["Route to Small Language Model (SLM)\ne.g., Llama-3-8B / GPT-4o-mini\n(Cost: $0.15/M, Latency: < 200ms)"]
    C1 -->|Standard RAG / Summarization| RouteGeneral["Route to General Enterprise Model\ne.g., Claude 3.5 Haiku / GPT-4o\n(Cost: $1.50/M, Latency: < 800ms)"]
    C1 -->|Deep Multi-Step Reasoning / Math| RouteReasoning["Route to Reasoning Model\ne.g., OpenAI o1 / DeepSeek-R1\n(Cost: $15.00/M, Latency: 5s - 30s)"]
    
    RouteSLM --> QualityCheck{"Validation Check"}
    QualityCheck -->|Pass| Return["Return Output"]
    QualityCheck -->|Fail / Low Confidence| Escalate["Escalate to General Model"]
```

---

## 2. Multi-Dimensional Routing Scorecard

| Dimension | Tier 1: SLM (< 10B) | Tier 2: General (70B) | Tier 3: Reasoning Frontier |
| :--- | :--- | :--- | :--- |
| **P99 Latency Target** | $< 250\text{ms}$ | $< 1,200\text{ms}$ | $10\text{s} - 45\text{s}$ |
| **Relative Cost per 1k Tokens** | $0.05\times$ | $1.0\times$ (Baseline) | $10.0\times$ |
| **JSON Schema Conformance** | $92\%$ | $99.2\%$ | $99.8\%$ |
| **Complex Logic / Code Synthesis** | Poor | Strong | Industry Leading |
| **Recommended Routing Share** | $\sim 65\%$ of enterprise traffic | $\sim 30\%$ of enterprise traffic | $\sim 5\%$ of enterprise traffic |
