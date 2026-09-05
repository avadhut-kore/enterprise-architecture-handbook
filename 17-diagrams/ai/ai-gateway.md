# Enterprise AI Gateway Architecture (LLM Proxy & Guardrails)

Centralized enterprise AI Gateway providing intelligent model routing, rate limiting, semantic caching, PII masking, and prompt guardrails.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph AppClients ["Enterprise Applications"]
        App1["Customer Support Bot"]
        App2["Internal Analytics Copilot"]
        App3["Coding Assistant"]
    end

    subgraph AIGatewayCluster ["Enterprise AI Gateway (LiteLLM / Portkey / Cloudflare AI)"]
        AuthRate["Authentication & Token Rate Limiter"]
        PIIMask["PII Redaction & Sanitizer (Presidio)"]
        SemanticCache["Semantic Vector Cache (Redis)"]
        Guardrails["Prompt Guardrails (NeMo Guardrails / Llama Guard)"]
        Router["Smart Model Router & Fallback Engine"]

        AuthRate --> PIIMask
        PIIMask --> SemanticCache
        SemanticCache -->|"Cache Miss"| Guardrails
        Guardrails --> Router
    end

    subgraph FoundationProviders ["Downstream Model Providers"]
        OpenAI["Azure OpenAI (GPT-4o)"]
        Anthropic["Anthropic Bedrock (Claude 3.5 Sonnet)"]
        SelfHosted["Self-Hosted vLLM (Llama 3)"]

        Router -->|"Primary Route"| OpenAI
        Router -.->|"Automatic Fallback on 429/500"| Anthropic
        Router -->|"Cost Optimization Route"| SelfHosted
    end

    App1 --> AuthRate
    App2 --> AuthRate
    App3 --> AuthRate
    SemanticCache -->|"Sub-10ms Cache Hit"| AppClients
```

## PlantUML Specification

```plantuml
@startuml
actor Client
participant "AI Gateway" as gw
database "Semantic Cache" as cache
participant "Guardrails Engine" as guard
participant "Azure OpenAI" as oai
participant "AWS Bedrock" as bedrock

Client -> gw : Submit Prompt
gw -> cache : Check Semantic Similarity
cache --> Client : Return Cached Answer (if similarity > 0.95)
cache -> guard : Cache Miss -> Check Injection & PII
guard -> oai : Forward Clean Prompt
oai --> gw : Rate Limit (429) Error
gw -> bedrock : Automatic Failover Call
bedrock -> gw : Successful Response
gw -> Client : Filtered Response
@enduml
```

## Architectural Design Considerations

* **Semantic Caching**: Store prompt embeddings in Redis; if a incoming prompt is semantically identical (>95% cosine similarity) to an existing answer, return cached output instantly.
* **Provider Fallback**: Automatically failover to an alternative model provider (e.g., fallback from Azure OpenAI to AWS Bedrock) when HTTP 429 (rate limited) or 503 errors occur.
* **Cost & Token Tracking**: Record exact prompt and completion token counts per application team to enforce departmental chargebacks.

## Related Documentation & Patterns

* [Security: AI Security](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/ai-security.md)
* [Autonomous LLM Agent](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/ai/llm-agent-workflow.md)
* [RAG Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/ai/rag-architecture.md)
