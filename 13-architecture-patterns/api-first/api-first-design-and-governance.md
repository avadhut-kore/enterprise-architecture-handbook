# API-First Design & Governance Architecture

## 1. Design-First vs. Code-First

In code-first development, developers write code and auto-generate API documentation as an afterthought, leading to inconsistent schemas, leaky database abstractions, and frequent breaking changes.

**Design-First** mandates that the API contract (OpenAPI 3.1 YAML) is designed, reviewed by consumers, and validated by automated linters *before* any backend code is written:

```mermaid
flowchart LR
    Spec["1. OpenAPI Specification Design"] --> Lint["2. Spectral Automated Linting & ARB Review"]
    Lint --> Mock["3. Mock Server Generation (Prism)\nConsumers develop in parallel!"]
    Mock --> CodeGen["4. Server Stub & Client SDK Generation"]
    CodeGen --> Impl["5. Backend Implementation"]
```
