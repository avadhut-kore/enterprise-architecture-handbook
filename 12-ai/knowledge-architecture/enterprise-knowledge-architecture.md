# Enterprise Knowledge Architecture

## 1. The 3 Tiers of Enterprise Knowledge

Enterprise knowledge exists across three distinct architectural layers, each requiring a specialized ingestion and representation strategy:

```mermaid
flowchart TD
    subgraph Tier1 ["Tier 1: Highly Structured Data"]
        DB[("Relational DBs / ERP / CRM\n(PostgreSQL / SAP / Salesforce)")]
        T1Strategy["Architectural Strategy:\nText-to-SQL / Scoped GraphQL APIs / Semantic Models"]
        DB --> T1Strategy
    end

    subgraph Tier2 ["Tier 2: Semi-Structured Business Data"]
        Docs[("JSON / CSV / Jira / ServiceNow Tickets / OpenAPI Specs")]
        T2Strategy["Architectural Strategy:\nJSON Flattening / Hybrid Search / Relational Metadata"]
        Docs --> T2Strategy
    end

    subgraph Tier3 ["Tier 3: Unstructured Knowledge"]
        Unstruct[("PDF Contracts / Word / Confluence / Slack Transcripts")]
        T3Strategy["Architectural Strategy:\nDocument Parsing / Semantic Chunking / Vector DBs"]
        Unstruct --> T3Strategy
    end
```

---

## 2. The Fallacy of "Vectorizing Everything"
A common enterprise anti-pattern is dumping relational database tables into a vector database. **Relational data must remain in relational databases**. If a user asks *"What was our total revenue in Q3 across the European division?"*, a vector search will hallucinate an answer. The correct architecture uses structured API tool calling (Text-to-SQL with strict schema guards) to query the relational database directly.
