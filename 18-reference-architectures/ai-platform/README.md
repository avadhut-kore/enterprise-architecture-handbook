# Enterprise AI Platform Reference Architecture

## 1. Executive Summary & Architectural Vision
The Enterprise AI Platform is a centralized, multi-tenant foundation designed to power hundreds of enterprise applications with Generative AI, Retrieval-Augmented Generation (RAG), Autonomous Agent Workflows, and Traditional Machine Learning models. 

It provides an **AI Gateway** layer enforcing corporate data privacy, semantic caching, token rate limiting, multi-model dynamic routing (between external frontier APIs like OpenAI/Anthropic and self-hosted open-weight LLMs like Llama 3 on private GPUs), unified vector search, and automated model evaluation.

```
[Enterprise Applications (Web, Mobile, Slack, ERP, CRM)]
                           │
             ══════════════▼══════════════  [mTLS / API Gateway]
                Enterprise AI Gateway
                ├── Prompt Firewall & PII Redaction
                ├── Semantic Redis Cache (Exact & Cosine Sim)
                ├── Dynamic Model Router & Fallback
                └── Token Bucket Rate Limiter
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
[Frontier APIs]    [Self-Hosted vLLM]  [RAG & Agent Engine]
(GPT-4o, Claude)   (Llama 3 on GPUs)   ├── LangGraph Agent Swarm
                                       ├── Hybrid Vector Store (Qdrant)
                                       └── Tool Execution Sandbox
```

## 2. Architectural Package Contents
- [01-business-and-requirements.md](01-business-and-requirements.md): Business model, personas, scale assumptions, and NFR budgets.
- [02-architecture-and-c4.md](02-architecture-and-c4.md): C4 model (Context, Container, Component) and Cloud Mapping (AWS/Azure/GCP).
- [03-application-architecture.md](03-application-architecture.md): Service boundaries, prompt registry, agent orchestration, and tool calling.
- [04-data-architecture.md](04-data-architecture.md): Hybrid vector storage, document ingestion pipelines, chunking, and embeddings.
- [05-integration-architecture.md](05-integration-architecture.md): Model APIs, streaming SSE endpoints, enterprise connectors, and webhooks.
- [06-security-and-compliance.md](06-security-and-compliance.md): Prompt injection defense, PII masking, EU AI Act, and data sovereignty.
- [07-infrastructure-and-devops.md](07-infrastructure-and-devops.md): Kubernetes GPU node pools (vLLM on L40S/A100), Terraform IaC, and CI/CD.
- [08-observability-and-reliability.md](08-observability-and-reliability.md): TTFT, Token throughput metrics, OpenInference tracing, and model drift.
- [09-cost-and-finops.md](09-cost-and-finops.md): Token unit economics, GPU reservation TCO, and prompt caching savings.
- [10-sequences-and-flows.md](10-sequences-and-flows.md): End-to-end RAG query flow, agent tool execution, and fallback sequences.
- [11-adrs-and-evolution.md](11-adrs-and-evolution.md): Canonical ADRs (Multi-Model Router, Hybrid Search) and evolution roadmap.
