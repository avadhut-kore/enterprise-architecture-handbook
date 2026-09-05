# AI & Modern Architecture Reference Blueprints (`18-reference-architectures/ai-modern/`)

## Executive Summary

This directory establishes **20 production-grade reference architectures** for enterprise AI systems. Each blueprint provides an end-to-end architectural specification:
* Business Problem & Enterprise Context
* Functional Requirements & Non-Functional Requirements (NFRs)
* System Topology & Component Architecture (Mermaid)
* Data Flow & Runtime Sequence
* Security, Governance & Compliance Controls
* Failure Modes, Circuit Breakers & Resilience
* Cost Economics & Sizing Formulas
* Evolution & Technology Modernization Path

---

## Reference Architectures Catalog

* **[Enterprise AI Gateway Reference Architecture](enterprise-ai-gateway.md)** — Centralized high-throughput reverse proxy providing OAuth2 authentication, token rate limiting, semantic caching, PII scrubbing, dynamic model routing, and OTel tracing across heterogeneous LLM backends.
* **[Enterprise RAG Platform Reference Architecture](enterprise-rag-platform.md)** — End-to-end knowledge ingestion, hybrid search (BM25 + HNSW dense vectors), cross-encoder reranking, and citation-backed synthesis for enterprise corpora.
* **[Multi-Tenant RAG SaaS Reference Architecture](multi-tenant-rag-saas.md)** — B2B SaaS knowledge platform providing hardware-level tenant isolation, dynamic tenant context injection, scoped vector namespaces, and per-tenant usage billing.
* **[Conversational AI Assistant Reference Architecture](ai-assistant.md)** — Omnichannel conversational assistant featuring Server-Sent Events (SSE) token streaming, sliding-window session management in Redis, and optimistic client rendering.
* **[Embedded AI Copilot Reference Architecture](ai-copilot.md)** — Sub-300ms inline editing copilot with continuous bidirectional document state synchronization, AST parsing, and low-latency token completions.
* **[Durable Agentic Workflow Reference Architecture](agentic-workflow.md)** — Stateful, long-running agent execution platform built on Temporal durable execution, ReAct cognitive loops, and persistent checkpointed scratchpads.
* **[Human-in-the-Loop (HITL) Reference Architecture](human-in-the-loop-ai.md)** — Asynchronous pause-and-resume workflow architecture integrating confidence-based routing, human escalation queues, and Maker-Checker dual authorization.
* **[Enterprise AI Semantic Search Platform Reference Architecture](ai-search-platform.md)** — Two-stage enterprise search pipeline combining distributed Elasticsearch BM25 sparse retrieval with Qdrant dense vector search and Cohere rerankers.
* **[Full-Stack Enterprise AI Platform Reference Architecture](enterprise-ai-platform.md)** — Comprehensive blueprint linking Enterprise Applications, AI Gateways, Capability Platforms (LLM, RAG, Agents), and the Centralized Control Plane.
* **[Event-Driven AI Streaming Pipeline Reference Architecture](ai-event-streaming.md)** — Asynchronous Kafka-based streaming inference architecture consuming Change Data Capture (CDC) events, autoscaling consumers, and dead-letter queues.
* **[AI-Enabled Enterprise APIs Reference Architecture](ai-enterprise-apis.md)** — Standardizing REST and gRPC interfaces that encapsulate foundation models behind strict OpenAPI 3.1 contracts and circuit-breaker protections.
* **[AI Financial Platform Reference Architecture](ai-financial-platform.md)** — High-assurance banking and payments AI architecture enforcing non-delegable human fiduciary sign-off, dual-key authorizations, and WORM decision logging.
* **[AI CRM Integration Platform Reference Architecture](ai-crm-integration.md)** — Securely bridging AI assistants to Salesforce and HubSpot CRM systems via Model Context Protocol (MCP) and scoped OAuth 2.0 authorization.
* **[AI ERP Integration Platform Reference Architecture](ai-erp-integration.md)** — Connecting AI agents to SAP S/4HANA systems of record via OData/BAPI adapters, enforcing transactional rollback and audit trails.
* **[Enterprise Knowledge Platform Reference Architecture](ai-knowledge-platform.md)** — Multi-tier knowledge fabric integrating relational databases, semi-structured ticket stores, and unstructured document vector spaces.
* **[Self-Hosted Private LLM Platform Reference Architecture](self-hosted-llm-platform.md)** — Air-gapped Kubernetes GPU cluster serving open-weights models (Llama 3, Mistral) with vLLM, Tensor Parallelism on H100s, and high-speed NVMe storage.
* **[Multi-Model Orchestration Platform Reference Architecture](multi-model-ai-platform.md)** — Dynamic routing fabric orchestrating task complexity classifiers, speculative cascade fallbacks, and heterogeneous model portfolios.
* **[Automated AI Continuous Evaluation Platform Reference Architecture](ai-evaluation-platform.md)** — Automated CI/CD testing platform running golden test suites, LLM-as-a-Judge evaluations, and RAG Triad regression gates before production deployments.
* **[AI Defense-in-Depth Security Platform Reference Architecture](ai-security-architecture.md)** — End-to-end security architecture implementing input/output guardrails, indirect prompt injection neutralization, canary tokens, and egress DLP scanning.
* **[AI Observability & Tracing Platform Reference Architecture](ai-observability-architecture.md)** — Enterprise telemetry platform instrumented with OpenTelemetry GenAI Semantic Conventions, capturing TTFT, TPOT, token budgets, and evaluation drift.
