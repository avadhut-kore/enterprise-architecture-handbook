# Observability, SRE & Reliability: Enterprise AI Platform

## 1. Specialized AI Golden Signals
- **Time-to-First-Token (TTFT)**: Latency from HTTP request arrival to first generated token stream byte (Target: $< 600\text{ms}$).
- **Tokens Per Second (TPS)**: Generation throughput per GPU instance (Target: $> 80\text{ tokens/sec/user}$).
- **Cache Hit Ratio**: Percent of requests satisfied by semantic Redis cache without calling model backends.
- **Model Fallback Rate**: Percentage of requests diverted from primary model to secondary fallback due to timeouts or 5xx errors.

---

## 2. Distributed Tracing with OpenInference
Instrument all spans with OpenTelemetry extended with OpenInference attributes (`llm.model_name`, `llm.prompt_token_count`, `llm.completion_token_count`, `vector_db.top_k`).
