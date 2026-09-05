# Distributed Design Principle: Loose Coupling

## 1. Core Principle Definition

Coupling measures the degree of direct interdependence between software components. **Loose Coupling** ensures that a change, failure, or performance degradation in one service does not propagate to or require synchronized changes in other services.

---

## 2. Dimensions of Coupling

```
+--------------------------+----------------------------+----------------------------+
| Dimension                | Tight Coupling             | Loose Coupling             |
+--------------------------+----------------------------+----------------------------+
| Spatial Coupling         | Hardcoded IP / Hostnames   | Service Discovery / DNS    |
| Temporal Coupling        | Synchronous Blocking RPC   | Asynchronous Event Streams |
| Data Model Coupling      | Shared Database Tables     | Private DB / Public Schema |
| Protocol Coupling        | Proprietary Binary Wire    | Standard REST / gRPC / JSON|
+--------------------------+----------------------------+----------------------------+
```

---

## 3. Architectural Defenses

- **Contract-First APIs**: Define API contracts using OpenAPI or Protobuf schemas; ensure backward compatibility via semantic versioning.
- **Publish Domain Events, Not Database Rows**: Avoid leaking internal database column structures in external events.
