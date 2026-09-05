# Model Parameter Scale & Efficiency Trade-Offs

## 1. Sizing the Model to the Task

A common architectural anti-pattern is deploying massive 70B+ parameter models for simple classification, routing, or extraction tasks.

Foundation models fall into three distinct parameter tiers, each offering a distinct trade-off between reasoning depth, inference latency, and infrastructure cost:

```mermaid
flowchart LR
    subgraph Small ["Small Models (SLMs: 3B - 8B)"]
        S1["e.g., Llama-3-8B, GPT-4o-mini"]
        S2["VRAM: 8GB - 16GB (Fits on 1 cheap GPU)"]
        S3["Speed: 100+ tokens/sec"]
        S4["Cost: $0.15 / M tokens"]
    end
    subgraph Medium ["Medium Models (14B - 32B)"]
        M1["e.g., Qwen-2.5-32B, Mistral-Small"]
        M2["VRAM: 32GB - 64GB (Fits on 1x A100/H100)"]
        M3["Speed: 40 - 70 tokens/sec"]
        M4["Cost: $0.60 / M tokens"]
    end
    subgraph Large ["Large / Frontier Models (70B - 405B)"]
        L1["e.g., Llama-3-70B, GPT-4o, Claude 3.5"]
        L2["VRAM: 140GB - 800GB (Requires 2 to 8 GPUs)"]
        L3["Speed: 20 - 40 tokens/sec"]
        L4["Cost: $2.50 - $15.00 / M tokens"]
    end
```

---

## 2. Assignment Guidelines
* **Use Small Language Models (SLMs)** for: Intent classification, entity extraction, sentiment analysis, query rewriting, spell checking, and PII masking.
* **Use Medium Models** for: Standard RAG question-answering, document summarization, draft email synthesis, and conversational customer support.
* **Use Large / Frontier Models** for: Complex multi-step reasoning, mathematical problem solving, automated architectural code generation, and ambiguous strategic analysis.
