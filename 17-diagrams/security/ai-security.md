# AI & Large Language Model (LLM) Security Architecture

Security defense pipeline for generative AI workloads mitigating prompt injection, data leakage, model theft, and insecure output handling (OWASP LLM Top 10).

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph UserLayer ["User Ingress"]
        PromptReq["User Prompt / API Query"]
    end

    subgraph InputGuardrailTier ["Tier 1: Input Security Guardrails"]
        PromptInspect["Prompt Injection & Jailbreak Detector (NeMo Guardrails)"]
        PIIFilter["PII Anonymization & Redaction Engine"]
        ContextChecker["Vector Embedding Semantic Similarity Filter"]

        PromptReq --> PromptInspect
        PromptInspect --> PIIFilter
        PIIFilter --> ContextChecker
    end

    subgraph CoreModelTier ["Tier 2: AI Execution Perimeter"]
        RAGStore[("Vector DB (Chroma/Pinecone)<br/>[Document ACLs Enforced]")]
        LLM["Foundation Model (Self-Hosted / Azure OpenAI)"]

        ContextChecker -->|"Filtered Semantic Search"| RAGStore
        RAGStore -->|"Grounded Context"| LLM
    end

    subgraph OutputGuardrailTier ["Tier 3: Output Security Guardrails"]
        Hallucination["Hallucination & Groundedness Checker"]
        OutputSanitizer["Output Sanitizer (XSS, Code Injection, Sensitive Data Leak)"]
        AuditTelemetry["LLM Observability & Audit Store"]

        LLM --> Hallucination
        Hallucination --> OutputSanitizer
        OutputSanitizer --> AuditTelemetry
        OutputSanitizer -->|"Sanitized Safe Response"| SafeUser["End User / Client App"]
    end

    classDef inGuard fill:#e8f4f8,stroke:#007791,stroke-width:2px;
    classDef model fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px;
    classDef outGuard fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    class PromptInspect,PIIFilter,ContextChecker inGuard;
    class RAGStore,LLM model;
    class Hallucination,OutputSanitizer,AuditTelemetry outGuard;
```

## PlantUML Specification

```plantuml
@startuml
actor User
participant "Input Guardrail" as inGuard
participant "RAG Vector DB" as vector
participant "LLM Engine" as llm
participant "Output Guardrail" as outGuard

User -> inGuard : Submit Prompt
inGuard -> inGuard : Detect Prompt Injection & Redact PII
inGuard -> vector : Fetch Authorized Documents (ACL Check)
vector -> llm : Augment Prompt with Context
llm -> outGuard : Generate Raw Output
outGuard -> outGuard : Scan for Code Execution & Sensitive Data
outGuard -> User : Safe Screened Response
@enduml
```

## Architectural Design Considerations

* **OWASP Top 10 for LLM**: Prioritize mitigations for Prompt Injection (LLM01), Insecure Output Handling (LLM02), and Sensitive Information Disclosure (LLM06).
* **Document-Level ACLs in RAG**: Enforce user identity and enterprise authorization checks during vector similarity searches to prevent privilege escalation through AI context.
* **Model Sandboxing**: Execute all LLM-generated code or tool calls inside isolated, network-restricted execution environments (e.g., gVisor, Firecracker).

## Related Documentation & Patterns

* [Threat Model](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/threat-model.md)
* [Data Classification](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/data-classification.md)
* [Trust Boundaries](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/trust-boundaries.md)
