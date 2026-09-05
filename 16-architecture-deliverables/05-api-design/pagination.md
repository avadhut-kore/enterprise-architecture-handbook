# API Pagination Standards

## 1. Keyset / Cursor Pagination (Mandatory for High-Scale Endpoints)
Never use `offset` and `limit` for collections exceeding 1,000 records due to database query degradation (`O(N)` scan).

### Query Parameters
`GET /v1/transactions?limit=50&starting_after=txn_xyz789`

### Response Envelope
```json
{
  "object": "list",
  "data": [...],
  "has_more": true,
  "next_cursor": "txn_abc123"
}
```
