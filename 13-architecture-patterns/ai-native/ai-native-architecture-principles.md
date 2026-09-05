# AI-Native Architecture Principles

## 1. Core Principles of AI-Native Design

1. **Streaming is the Default Interaction Model**: Synchronous blocking request-response is replaced by real-time Server-Sent Events (SSE) token streaming.
2. **Deterministic Guardrails Encapsulate Probabilistic Cores**: Non-deterministic models never execute state-mutating actions directly; they emit structured intents validated by deterministic policy engines.
3. **Continuous Automated Evaluation Replaces Static QA**: Systems continuously evaluate accuracy, groundedness, and hallucination drift in production.
4. **Context Window as a Tiered Cache**: Context memory is treated as a finite, expensive RAM cache managed via eviction policies.
