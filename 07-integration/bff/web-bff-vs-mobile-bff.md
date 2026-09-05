# BFF Architecture: Web BFF vs Mobile BFF Architecture

## 1. Architectural Purpose & Problem Context
Tailoring payloads: low-bandwidth stripped payloads for mobile vs rich data structures for desktop portals; mobile battery conservation.

---

## 2. BFF Architecture Blueprint

```mermaid
flowchart TD
    Web[Web SPA / SSR] --> WebBFF[Node.js / Next.js Web BFF]
    Mobile[iOS / Android App] --> MobileBFF[Mobile BFF: Compact Payloads]

    WebBFF -->|gRPC / Internal REST| ServiceA[Order Microservice]
    WebBFF -->|gRPC / Internal REST| ServiceB[Catalog Microservice]
    MobileBFF -->|gRPC / Internal REST| ServiceA
    MobileBFF -->|gRPC / Internal REST| ServiceB
```

---

## 3. Production Invariants
- BFFs must be owned by the corresponding frontend application engineering squads.
- BFFs must not contain core business logic or directly mutate database schemas; they are aggregation and transformation layers.
