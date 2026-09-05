# Few-Shot & In-Context Learning Architecture

## 1. Zero-Shot vs. Few-Shot Performance

Large Language Models learn in-context. Providing 3 to 5 high-quality input-output exemplars (Few-Shot Prompting) dramatically improves accuracy on structured extraction and reasoning tasks compared to pure natural language instructions (Zero-Shot).

```mermaid
flowchart TD
    UserQuery["User Input Query"] --> Embedder["Embed Query via Embedding Model"]
    Embedder --> VecDB[("Exemplar Vector Store\n(Curated Gold Standard Pairs)")]
    VecDB --> RetExemplars["Retrieve Top 3 Semantically Relevant Exemplars"]
    
    RetExemplars --> Assembler["Prompt Assembler\n- System Instruction\n- Exemplar 1 (Input/Output)\n- Exemplar 2 (Input/Output)\n- Exemplar 3 (Input/Output)\n- User Input"]
    Assembler --> LLM["Foundation Model Execution"]
```

---

## 2. Dynamic Few-Shot Exemplar Selection
Static few-shot examples embedded permanently into system prompts waste valuable context tokens on irrelevant examples. **Dynamic Few-Shot Selection** uses vector search to retrieve only those exemplars that are semantically similar to the current user's specific query, maximizing relevance while minimizing token consumption.
