# Enterprise AI Architecture Decision Frameworks (`decision-frameworks/`)

## Executive Summary

Architectural decisions in AI are too often driven by vendor marketing and industry hype rather than objective engineering evaluation. 

This directory establishes **18 formal decision scorecards** to guide enterprise architects through complex AI trade-offs, providing weighted scoring rubrics, quantitative formulas, and concrete boundary conditions.

---

## Decision Frameworks Catalog

* **[AI Suitability Decision Framework](ai-suitability-framework.md)** — Evaluates whether a problem should use AI or deterministic software based on value, determinism, data, accuracy, explainability, latency, cost, and risk. Explicitly supports: 'Do not use AI'.
* **[AI vs. Non-AI Decision Framework](ai-vs-non-ai.md)** — Decision matrix comparing traditional software engineering, static heuristics, and machine learning models.
* **[LLM vs. Traditional ML Decision Framework](llm-vs-traditional-ml.md)** — Choosing between statistical tree models (XGBoost/LightGBM) and Large Language Models for classification, scoring, and prediction.
* **[LLM vs. Rules Engine Decision Framework](llm-vs-rules-engine.md)** — Comparing deterministic business rules engines (Drools, OPA) vs. probabilistic LLMs for compliance, pricing, and eligibility logic.
* **[RAG vs. Fine-Tuning Decision Framework](rag-vs-fine-tuning.md)** — Selecting between dynamic context retrieval (knowledge injection) and parameter fine-tuning (style, format, domain syntax).
* **[RAG vs. Structured SQL Query Decision Framework](rag-vs-structured-query.md)** — Evaluating when to use vector retrieval vs. relational text-to-SQL for enterprise business reporting and aggregations.
* **[Vector DB vs. Enterprise Search Engine Decision Framework](vector-db-vs-search-engine.md)** — Choosing between dedicated vector databases (Qdrant, Milvus) and unified enterprise search (Elasticsearch, OpenSearch).
* **[Hosted Cloud API vs. Self-Hosted Model Decision Framework](hosted-model-vs-self-hosted.md)** — Evaluating commercial cloud APIs vs. private Kubernetes GPU clusters based on volume, privacy, latency, and operational cost.
* **[Single Model vs. Multi-Model Platform Decision Framework](single-model-vs-multi-model.md)** — Evaluating the architectural trade-offs of standardizing on one flagship model vs. dynamically routing across heterogeneous models.
* **[Single Agent vs. Orchestrated Workflow Decision Framework](single-agent-vs-workflow.md)** — Determining when an autonomous agent loop is required vs. when a predictable state machine workflow is superior.
* **[Agent vs. Deterministic Workflow Decision Framework](agent-vs-deterministic-workflow.md)** — Architectural boundary rules: when to enforce deterministic execution vs. when to allow probabilistic agent autonomy.
* **[Single Agent vs. Multi-Agent System Decision Framework](single-agent-vs-multi-agent.md)** — Evaluating the coordination overhead, token cost inflation, and latency penalty of multi-agent networks vs. a single agent.
* **[Human-in-the-Loop vs. Full Automation Decision Framework](human-in-the-loop-vs-full-automation.md)** — Risk-tiered gating criteria governing when AI can act autonomously vs. when mandatory human approval is non-negotiable.
* **[Central AI Gateway vs. Direct Provider Access Decision Framework](central-ai-gateway-vs-direct-access.md)** — Weighing the architectural governance of an enterprise gateway against the latency and simplicity of direct SDK calls.
* **[Synchronous AI vs. Asynchronous AI Decision Framework](synchronous-ai-vs-asynchronous-ai.md)** — Evaluating real-time user-facing token streaming vs. decoupled event-driven queues (Kafka/Celery) for AI tasks.
* **[Real-Time Inference vs. Batch Inference Decision Framework](realtime-inference-vs-batch-inference.md)** — Analyzing latency SLAs, throughput economics, and infrastructure utilization for online vs. offline AI workloads.
* **[CPU vs. GPU Inference Decision Framework](cpu-vs-gpu-inference.md)** — Determining when quantized Small Language Models can run economically on modern CPU instruction sets (AVX-512) vs. GPUs.
* **[Small Model (SLM) vs. Large Model (LLM) Decision Framework](small-model-vs-large-model.md)** — Evaluating 8B parameter models vs. 70B+ parameter models across accuracy, latency, and cost per million tokens.
