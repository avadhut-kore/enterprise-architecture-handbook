# Source Authority, Document Hierarchy & Provenance

## 1. The Document Conflict Dilemma

In large enterprises, multiple documents inevitably contradict one another: a 2021 draft travel policy on an employee's personal wiki page may state a $50 meal allowance, while the official 2025 Finance policy specifies $75. If both documents are indexed naively, vector search may retrieve both, causing the LLM to hallucinate an incorrect hybrid answer.

---

## 2. Authoritative Weighting & Provenance Metadata

Every document chunk must be enriched with metadata representing **Source Authority** and **Temporal Freshness**:

```json
{
  "chunk_id": "chunk-9812",
  "document_id": "pol-finance-2025-01",
  "document_title": "Corporate Travel & Expense Policy",
  "source_repository": "official-finance-sharepoint",
  "source_authority_tier": 1,
  "status": "APPROVED_ACTIVE",
  "effective_date": "2025-01-01T00:00:00Z",
  "expiration_date": "2026-01-01T00:00:00Z"
}
```

### 2.1 Pre-Retrieval Authority Filtering
The AI Gateway must enforce metadata filters that strictly exclude documents with `status: "DEPRECATED"` or `status: "DRAFT"` from production customer-facing search queries. When multiple documents match, the reranker prioritizes Tier-1 official repositories over informal internal wikis.
