# Golden Datasets Curation & Maintenance Architecture

## 1. The Golden Dataset as an Enterprise Asset

A **Golden Dataset** is a version-controlled, high-quality collection of test queries, reference contexts, expected answers, and negative adversarial probes. It is the enterprise's primary defense against silent regressions.

```mermaid
flowchart TD
    Sources["Raw Data Sources:\n- Historical Customer Support Logs\n- Production Edge-Case Outages\n- Domain Expert Curated Scenarios\n- Synthetic Test Generations (Evol-Instruct)"] --> Curation["Deduplication & Quality Filter"]
    
    Curation --> GoldenSet[("Golden Dataset Repository\n(Git LFS / DVC / JSONL Format)")]
    
    subgraph TestDistribution ["Balanced Test Distribution"]
        T1["Standard Factual Queries (60%)"]
        T2["Complex Multi-Hop Reasoning (20%)"]
        T3["Adversarial Prompt Injections (10%)"]
        T4["Out-of-Scope / Negative Probes (10%)"]
    end

    GoldenSet --> TestDistribution
```

---

## 2. Continuous Dataset Evolution
* Whenever a production incident or user thumbs-down report occurs, the failure scenario must be anonymized and committed to the Golden Dataset as a new regression test case.
