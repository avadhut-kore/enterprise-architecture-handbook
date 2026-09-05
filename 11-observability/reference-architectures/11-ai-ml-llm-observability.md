# Reference Architecture 11: Generative AI, LLMOps & Vector Retrieval Observability

## 1. System Context & Overview
Enterprise applications increasingly integrate Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and vector databases (Pinecone, Milvus, Qdrant). Traditional monitoring cannot evaluate LLM non-determinism, hallucination rates, token cost velocity, or semantic drift.

This architecture establishes **LLMOps Telemetry Standards**.

---

## 2. Architecture Diagram

```mermaid
flowchart TD
    User["User Query / Prompt"] --> App["Enterprise AI Service (LangChain / Semantic Kernel)"]
    
    subgraph RAG_Pipeline ["Retrieval-Augmented Generation (RAG) Architecture"]
        Embed["Embedding Model (text-embedding-3-small)"]
        VectorDB["Vector Database (Milvus / Pinecone)"]
        LLM["Foundation Model (OpenAI GPT-4 / Anthropic Claude)"]
        
        App -->|1. Generate Embedding| Embed
        Embed -->|2. Vector Search (Cosine Sim)| VectorDB
        VectorDB -->|3. Retrieved Context Chunks| App
        App -->|4. Augmented Prompt with Context| LLM
        LLM -->|5. Generated Completion| App
    end

    subgraph LLM_Telemetry_Engine ["OpenTelemetry LLM Instrumentation (OpenInference)"]
        OTel_LLM["OTel Collector (GenAI Semantic Conventions)\n- Captures prompt_tokens, completion_tokens\n- Measures vector retrieval latency & distance\n- Calculates cost per query ($) in real-time\n- Evaluates Hallucination & Faithfulness score"]
    end

    App -. Telemetry Events .-> OTel_LLM

    subgraph Analytics ["LLMOps Analytics Platform"]
        CostDashboard["Token Cost & Budget Tracker"]
        QualityDashboard["RAG Retrieval Precision & Recall"]
        Guardrails["Prompt Injection & Toxicity Alerting"]
        
        OTel_LLM --> CostDashboard
        OTel_LLM --> QualityDashboard
        OTel_LLM --> Guardrails
    end
```

---

## 3. Key Architectural Decisions
1. **OpenInference Semantic Conventions**: Standardized attributes (`llm.model_name`, `llm.usage.prompt_tokens`, `llm.usage.completion_tokens`, `llm.usage.total_cost`) are emitted across all AI frameworks.
2. **Vector Retrieval Quality SLIs**: The vector search step is instrumented to measure **Retrieval Distance/Relevance Score**; if average cosine distance drops below threshold, alerts flag potential model drift or stale vector indexes.
3. **PII and Prompt Injection Guardrails**: Inbound user prompts are pre-scanned for prompt injection attacks and sensitive enterprise intellectual property before invocation.
