# Planning, Reasoning & Reflection in Agent Architecture

## 1. Cognitive Architectures for Agents

A simple ReAct agent operates myopically—deciding only one step at a time. Complex enterprise tasks require hierarchical planning and self-correction:

```mermaid
flowchart TD
    subgraph Planning ["1. High-Level Planning"]
        Goal["Complex Task"] --> Decompose["Task Decomposer (Plan-and-Solve)\nEmits DAG of 4 Sub-Tasks"]
    end

    subgraph Execution ["2. Sub-Task Execution"]
        Decompose --> Step1["Sub-Task 1: Fetch Invoices"]
        Step1 --> Step2["Sub-Task 2: Extract Totals"]
        Step2 --> Step3["Sub-Task 3: Reconcile Ledger"]
    end

    subgraph Reflection ["3. Self-Reflection Gate"]
        Step3 --> Critic["Self-Reflection Critic\n'Did Step 3 identify any discrepancies?'"]
        Critic --> ErrorFound{"Discrepancy Detected?"}
        ErrorFound -->|Yes| Backtrack["Backtrack & Execute Forensic Query"]
        Backtrack --> Step3
        ErrorFound -->|No| Finalize["Finalize Output"]
    end
```

---

## 2. The Plan-and-Solve Pattern
* Separates **Planning** from **Execution**. A larger, high-reasoning model (e.g., Claude 3.5 Sonnet) generates an immutable, structured execution plan (JSON DAG). 
* Smaller, faster models (e.g., GPT-4o-mini) execute each atomic step sequentially, reducing token costs by 70% compared to allowing the large model to wander through continuous unconstrained loops.
