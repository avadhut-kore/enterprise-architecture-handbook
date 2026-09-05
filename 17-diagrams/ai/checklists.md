# Enterprise AI Architecture Review Checklist

This checklist provides a structured 25-point evaluation for generative AI architectures, LLM pipelines, and AI security.

## 1. Security & Safety Guardrails
- [ ] Are input guardrails implemented to prevent Prompt Injection (OWASP LLM01)?
- [ ] Is PII automatically detected and redacted before prompts are transmitted to external model providers?
- [ ] Are output guardrails configured to sanitize generated code and prevent Cross-Site Scripting (XSS)?
- [ ] Are document-level access control lists (ACLs) enforced during vector similarity search?

## 2. RAG & Retrieval Architecture
- [ ] Is hybrid search (dense embeddings + BM25 keyword matching) implemented with Reciprocal Rank Fusion?
- [ ] Is a cross-encoder reranker model utilized to score retrieved candidate passages?
- [ ] Are source citations returned alongside answers to allow users to verify factual grounding?
- [ ] Is vector database indexing latency bounded to support necessary real-time document updates?

## 3. Reliability, Latency & Cost Optimization
- [ ] Is an enterprise AI Gateway deployed to provide centralized token rate limiting and multi-provider failover?
- [ ] Is semantic caching implemented to return instant answers for repeated user queries?
- [ ] Are autonomous agents bounded with strict maximum iteration loops (e.g., max 10 steps)?
- [ ] Are token usage metrics and API costs tracked per team for chargeback reporting?
