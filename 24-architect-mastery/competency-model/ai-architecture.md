# Competency Deep Dive: AI & Generative AI Systems Architecture

> **"Generative AI is not magic; it is a high-throughput, non-deterministic distributed computing workload. An architect must evaluate AI through the same rigorous lens of latency, FinOps unit economics, security guardrails, and operational failure modes as any other mission-critical tier."**

---

## 1. Definition & Core Essence

**AI & Generative AI Systems Architecture** is the discipline of integrating, serving, and governing machine learning and foundational large language models (LLMs) in enterprise software. It encompasses:
* Model serving & inference acceleration: vLLM, TensorRT-LLM, NVIDIA Triton, continuous batching, PagedAttention, KV cache management, and quantization (FP8, INT4).
* Retrieval-Augmented Generation (RAG): Document chunking strategies, dense vector embeddings, hybrid search (BM25 + HNSW), re-ranking, and semantic prompt caching.
* Autonomous agent architectures: Multi-agent orchestration (LangGraph, AutoGen), tool calling, stateful memory, and deterministic guardrails.
* AI security & governance: Prompt injection defense, data loss prevention (DLP), proprietary data isolation, and model evaluation harnesses (RAGAS).

---

## 2. Why It Matters for Modern Architects

* **Solution Architects**: Prevents teams from deploying brittle, unmonitored LLM prototypes into production that leak sensitive data or hallucinate false legal commitments.
* **Technical Architects**: Governs the self-hosted GPU cluster vs commercial SaaS API (OpenAI/Anthropic) decision, preventing massive token invoice explosions.
* **Enterprise Architects**: Establishes corporate foundational model governance, sovereign AI hosting policies, and evaluates enterprise AI copilots.

---

## 3. 5-Tier Behavioral Capability Progression

| Level | Behavioral Capability Anchor |
| :--- | :--- |
| **L1 (Practitioner)** | Calls commercial LLM APIs using basic prompts and handles JSON responses in application code. |
| **L2 (Independent)** | Builds basic RAG pipelines using LangChain or LlamaIndex with vector databases; implements semantic chunking and basic embeddings. |
| **L3 (Advanced)** | Architects hybrid search (BM25 + Dense Vector), semantic prompt caching, and guardrails against prompt injection; implements evaluation harnesses. |
| **L4 (Architect)** | Architects production high-throughput LLM serving infrastructure (vLLM, TensorRT-LLM) with continuous batching and PagedAttention ([Model Serving](../../12-ai/model-serving/README.md)); sizes GPU memory for peak QPS. |
| **L5 (Strategic)** | Formulates corporate Enterprise AI Strategy: proprietary model fine-tuning vs retrieval, sovereign AI hosting, multi-agent enterprise orchestration, and AI intellectual property protection. |

---

## 4. Practical Experiences & Apprenticeship Exercises

1. **Benchmark Continuous Batching & PagedAttention**: Run a benchmark comparing naive sequential LLM serving against vLLM with PagedAttention under concurrent load; measure throughput (tokens/sec) and TTFT (time-to-first-token).
2. **Build a Production Hybrid Search RAG Pipeline**: Implement a RAG architecture combining Elasticsearch BM25 full-text search with a vector DB HNSW index and a cross-encoder re-ranker; measure precision@k.
3. **Implement Defense Against Indirect Prompt Injection**: Architect a guardrail layer that sanitizes untrusted third-party web content before feeding it into an LLM context window.

---

## 5. Objective Evidence of Capability (What to Inspect in Git)

- [ ] Complete Enterprise AI Architecture Specification detailing model serving topologies, latency budgets, and GPU cluster sizing.
- [ ] Threat Model and Data Loss Prevention (DLP) specification for enterprise GenAI applications.
- [ ] FinOps Token Cost Model comparing self-hosted open-weights models against commercial SaaS APIs.

---

## 6. Common Cognitive Gaps & Blind Spots

* **AI-First Hype Delusion**: Using generative AI for deterministic workflows (e.g., calculations, regex parsing) where traditional algorithms are 100x faster, cheaper, and 100% accurate.
* **Ignoring TTFT & Streaming Latency**: Designing user interfaces that wait 10 seconds for a full LLM response instead of implementing server-sent events (SSE) token streaming.
* **Vector-Only Search Blindness**: Assuming vector embeddings capture exact keyword searches (e.g., part numbers, SKU codes, legal names), resulting in terrible search recall without hybrid BM25 search.

---

## 7. Authoritative Repository Links

* AI Core: [`12-ai/`](../../12-ai/README.md)
* Production Model Serving: [`12-ai/model-serving/`](../../12-ai/model-serving/README.md)
* Search & Vector Indexing: [`06-data/search/`](../../06-data/search/README.md)
* AI Capstone Strategy: [`24-architect-mastery/ai-architecture/`](../ai-architecture/README.md)

---

## 8. Diagnostic Assessment Questions

1. *How does PagedAttention eliminate virtual memory fragmentation in GPU KV caches during high-concurrency LLM inference?*
2. *Why is hybrid search (combining BM25 lexical search with dense vector search) essential for enterprise RAG systems?*
3. *What are the financial and operational break-even points between licensing a commercial LLM API versus self-hosting a cluster of Llama-3-70B models?*
