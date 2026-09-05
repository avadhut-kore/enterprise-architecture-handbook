# Enterprise AI Architecture Design Patterns (`ai-patterns/`)

## Executive Summary

This directory establishes 15 production-grade AI design patterns. Each pattern adheres to a strict 11-section architectural specification:
1. Intent & Context
2. Problem Statement
3. Architecture & Topology (Mermaid)
4. Key Components & Contracts
5. Data Flow & Sequence
6. Security & Governance Invariants
7. Reliability & Failure Modes
8. Cost & Performance Economics
9. Trade-Off Analysis
10. When to Use
11. When NOT to Use

---

## Pattern Catalog

* **[Semantic Cache Pattern](semantic-cache-pattern.md)** — Intercepts semantically identical prompts using vector similarity in Redis to return pre-computed completions in <15ms, eliminating upstream GPU compute and token costs.
* **[Model Gateway & Fallback Pattern](model-gateway-fallback-pattern.md)** — Centralized reverse proxy that dynamically abstracts multiple LLM providers, providing transparent 429/503 circuit breaking and automatic failover.
* **[Hybrid Search & Reranking Pattern](hybrid-search-reranking-pattern.md)** — Combines sparse lexical BM25 keyword search with dense HNSW vector retrieval, aggregating ranks via Reciprocal Rank Fusion and neural cross-encoder rerankers.
* **[Parent-Child Chunking Pattern](parent-child-chunking-pattern.md)** — Decouples the retrieval unit from the generation unit: embeds small 128-token child chunks for precision, returning 1024-token parent sections for LLM context.
* **[Graph-Augmented RAG (GraphRAG) Pattern](graph-augmented-rag-pattern.md)** — Combines knowledge graphs (Neo4j) with vector embeddings to enable global corpus summarization, entity relationship traversal, and multi-hop reasoning.
* **[ReAct (Reason + Act) Agent Pattern](react-agent-pattern.md)** — Autonomous execution loop that interleaves reasoning thoughts, discrete tool invocations, and environmental observations to accomplish open-ended goals.
* **[Supervisor Multi-Agent Pattern](supervisor-multi-agent-pattern.md)** — Coordinates multiple specialized worker agents (Coder, Analyst, Writer) via a centralized supervisor agent that decomposes goals and aggregates outputs.
* **[Human-in-the-Loop (HITL) Approval Pattern](human-in-the-loop-approval-pattern.md)** — Asynchronously pauses durable workflows at high-risk transaction boundaries, resuming execution only upon cryptographically signed human authorization.
* **[LLM-as-a-Judge Evaluation Pattern](llm-as-a-judge-evaluation-pattern.md)** — Uses frontier foundation models guided by explicit scoring rubrics to evaluate candidate model outputs for faithfulness, relevance, and safety in CI/CD.
* **[Asynchronous AI Batch Pipeline Pattern](asynchronous-ai-batch-pipeline-pattern.md)** — Decouples high-volume document summarization and embedding ingestion from transactional paths using Kafka event streams and backpressure-resilient workers.
* **[Streaming Token Response Pattern](streaming-token-response-pattern.md)** — Streams token chunks from model serving runtimes to web/mobile clients via Server-Sent Events (SSE) over HTTP/2, keeping Time-to-First-Token under 800ms.
* **[Fine-Tuning Distillation Pattern](fine-tuning-distillation-pattern.md)** — Distills the specialized reasoning capabilities of a 70B+ frontier model into a compact 8B parameter model using high-quality synthetic task outputs.
* **[Tenant-Isolated Vector Index Pattern](tenant-isolated-vector-index-pattern.md)** — Enforces multi-tenant data boundaries in shared vector storage via hardware-level pre-filtering and cryptographically authenticated tenant ID injection.
* **[Dynamic Tool Discovery Pattern](dynamic-tool-discovery-pattern.md)** — Enables AI agents to query a central Model Context Protocol (MCP) registry to discover, authenticate, and invoke enterprise tools dynamically at runtime.
* **[Self-Reflective Agent Pattern](self-reflective-agent-pattern.md)** — Evaluates draft model generations against internal verification questions, automatically triggering iterative correction cycles before presenting answers.
