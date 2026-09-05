# Dynamic Context Assembly & The Knapsack Token Budget

## 1. Deterministic Context Budget Allocation

When assembling a prompt from heterogeneous enterprise sources (system instructions, conversation history, user preferences, enterprise RAG documents, and tool definitions), the total token count can easily exceed model limits.

A **Dynamic Context Assembler** treats context allocation as a **Bounded Knapsack Problem**, prioritizing context segments based on architectural criticality.

```mermaid
flowchart TD
    TotalBudget["Total Token Context Budget: 8,192 Tokens"] --> Allocator["Dynamic Context Assembler"]
    
    subgraph Priorities ["Priority Tiers (Highest to Lowest)"]
        P1["Priority 1 (Mandatory): System Instructions & Safety Rules (500 tokens)"]
        P2["Priority 2 (Mandatory): Current User Query & Output Schema (300 tokens)"]
        P3["Priority 3 (High): Top-1 Most Relevant Retrieved RAG Chunk (800 tokens)"]
        P4["Priority 4 (Medium): Last 2 Conversation Turns (600 tokens)"]
        P5["Priority 5 (Opportunistic): Additional RAG Chunks 2-5 (Remaining Tokens)"]
    end

    Allocator --> Priorities
    Priorities --> FinalPrompt["Final Optimized Prompt\n(Never Exceeds Budget; Zero Overflow Errors)"]
```
