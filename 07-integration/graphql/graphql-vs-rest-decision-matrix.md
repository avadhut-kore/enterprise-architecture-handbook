# GraphQL Architecture: GraphQL vs REST Comprehensive Decision Matrix

## 1. Architectural Purpose & Problem Context
Architectural trade-off evaluation: client flexibility vs server complexity, caching friction, payload size, and operational overhead.

---

## 2. GraphQL Federation Topology

```mermaid
flowchart TD
    Client[Web Client / Mobile App] --> Gateway[Apollo Router / Supergraph Gateway]
    Gateway --> SubA[Order Subgraph Service]
    Gateway --> SubB[Product Subgraph Service]
    Gateway --> SubC[User Subgraph Service]
```

---

## 3. Production Invariants
- Disable GraphQL introspection in production to prevent schema harvesting by unauthorized actors.
- Enforce mandatory query depth and complexity score limits on public GraphQL gateways.
- All entity relationship resolvers must utilize DataLoader batching to eliminate N+1 query cascades.
