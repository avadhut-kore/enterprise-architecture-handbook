# Data Access: Pagination, Streaming & Batch Fetching Strategies

## 1. Architectural Purpose & Problem Context
Offset/Limit performance degradation at scale vs Keysets/Seek pagination (cursor-based), chunked streaming, and bulk insert operations.

---

## 2. Interaction Layer Architecture

```mermaid
flowchart LR
    Domain[Domain Core / Aggregate] --> Repo[Repository Interface]
    Repo --> Impl[Data Access Implementation]
    Impl --> Pool[(Database Connection Pool)]
    Pool --> DB[(Database Engine)]
```

---

## 3. Production Invariants
- Application code must never hold database connections open while waiting for network I/O or third-party HTTP calls.
- Always use cursor/keyset-based pagination for large datasets; offset-based pagination degrades quadratically ($O(N^2)$) on deep pages.
- Enforce eager loading or explicit projection in high-volume API endpoints to eliminate N+1 query cascades.
