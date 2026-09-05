# Cross-Language Architecture: Configuration Management Patterns

## 1. Architectural Purpose & Problem Context
Options pattern, @ConfigurationProperties, Pydantic Settings, and Zod config validation.

---

## 2. Cross-Language Architectural Comparison Matrix

```
+--------------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| Architectural Dimension  | .NET 8+               | Java 21+              | Python 3.12+          | Node.js 20+ (TS)      |
+--------------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| Dominant Pattern         | Clean / Vertical Slice| Clean / Hexagonal     | FastAPI / Pragmatic   | Fastify / Clean TS    |
| Primary Tooling          | Native / MediatR      | Spring Boot 3+        | Pydantic v2 / Asyncio | Zod / BullMQ          |
| Concurrency Paradigm     | Async/Await ThreadPool| Virtual Threads (Loom)| Asyncio Event Loop    | libuv Event Loop      |
| Type Safety              | Strict Static         | Strict Static         | Gradual (Mypy)        | Static (TypeScript)   |
+--------------------------+-----------------------+-----------------------+-----------------------+-----------------------+
```

---

## 3. Engineering Recommendations for Architects
- Match architectural patterns to runtime idioms; avoid forcing heavy Java-style XML/annotation patterns onto Python or Node.js.
- Ensure all services adhere to identical cross-boundary standards (RFC 7807 errors, W3C traceparent headers, OpenAPI contracts).
