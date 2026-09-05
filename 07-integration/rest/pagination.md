# API Pagination Patterns

## 1. Offset-Based vs. Cursor-Based Pagination

```mermaid
flowchart TD
    subgraph Offset Pagination [LIMIT 20 OFFSET 100000]
        O1[DB scans 100,020 rows -> Discards 100,000 -> Terrible Latency!]
        O2[Page Drift: If row inserted, items duplicate across pages!]
    end

    subgraph Cursor Pagination [WHERE id > cursor LIMIT 20]
        C1[DB uses B-Tree Index: O log N lookup -> Sub-5ms constant latency!]
        C2[Zero Page Drift: Stable across continuous inserts!]
    end
```

---

## 2. Cursor Pagination Implementation
* Request: `GET /v1/transactions?limit=20&cursor=tx_98124a`
* SQL Query:
  ```sql
  SELECT * FROM transactions 
  WHERE (created_at, id) < ('2026-09-05 10:00:00', 'tx_98124a')
  ORDER BY created_at DESC, id DESC 
  LIMIT 20;
  ```
* Response Payload:
  ```json
  {
    "data": [ ... ],
    "pagination": {
      "has_more": true,
      "next_cursor": "eyJjcmVhdGVkX2F0IjoxNzI1NTA4ODAwLCJpZCI6InR4Xzg4OTEifQ=="
    }
  }
  ```
