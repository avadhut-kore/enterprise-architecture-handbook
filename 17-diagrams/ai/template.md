# AI Systems Architecture Blueprint Starter Template

Production-ready boilerplate template for modeling enterprise generative AI workloads, vector pipelines, foundation models, and guardrails.

## Mermaid Architecture Diagram

```mermaid
graph TB
    subgraph UserTier ["1. User Ingress"]
        Client["Client Application"]
    end

    subgraph AIGatewayTier ["2. AI Gateway & Guardrails"]
        Gateway["AI Gateway (AuthN & Rate Limiting)"]
        Guardrails["Input & Output Guardrails"]
        Client --> Gateway
        Gateway --> Guardrails
    end

    subgraph ContextTier ["3. RAG Retrieval & Memory"]
        VectorStore[("Enterprise Vector Store (Pinecone)")]
        DocCorpus["Document Knowledge Store"]
        Guardrails <--> VectorStore
        DocCorpus -.-> VectorStore
    end

    subgraph ModelTier ["4. Foundation Model Execution"]
        LLM["Foundation Model (Azure OpenAI / Self-Hosted)"]
        Guardrails -->|"Augmented Prompt"| LLM
    end
```

## PlantUML Specification

```plantuml
@startuml
package "User Tier" {
  [Client App]
}
package "AI Gateway & Security" {
  [AI Gateway] --> [Guardrails Engine]
}
package "Context & Knowledge" {
  database "Vector DB" as vdb
}
package "Model Execution" {
  [LLM Foundation Model]
}
[Client App] --> [AI Gateway]
[Guardrails Engine] <--> vdb
[Guardrails Engine] --> [LLM Foundation Model]
@enduml
```

## Architectural Design Considerations

* **Standard Starter**: Copy and adapt this template when proposing new generative AI or LLM architectures.
* **Explicit Guardrails**: Always demarcate prompt guardrails between client applications and downstream foundation models.
* **Decoupled Context**: Treat enterprise context retrieval as an independent, secured tier.

## Related Documentation & Patterns

* [Enterprise AI Gateway](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/ai/ai-gateway.md)
* [RAG Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/ai/rag-architecture.md)
* [AI Review Checklist](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/ai/checklists.md)
