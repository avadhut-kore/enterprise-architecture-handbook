# Architecture Modernization: Anti-Corruption Layer (ACL) Pattern

## 1. Architectural Objective & Context

Prevent legacy domain models, archaic data formats (SOAP, fixed-width flat files, cryptic database schemas), and technical debt from polluting the clean, modern domain models of newly developed enterprise services.

---

## 2. Architectural Blueprint: The ACL Boundary

```mermaid
flowchart LR
    subgraph ModernDomain [Modern Microservice Subsystem]
        ModernSvc[Order Microservice]
        CleanModel[Modern Domain Model]
    end

    subgraph TranslationBoundary [Anti-Corruption Layer (ACL)]
        Adapter[Protocol Adapter]
        Translator[Domain Translator & Semantic Mapper]
        Facade[Legacy Facade Interface]
    end

    subgraph LegacySubsystem [Legacy Mainframe / ERP]
        LegacyCore[COBOL Mainframe / SAP Core]
        LegacySchema[(Cryptic EBCDIC DB)]
    end

    ModernSvc --> CleanModel
    CleanModel --> Adapter
    Adapter --> Translator
    Translator --> Facade
    Facade --> LegacyCore
    LegacyCore --> LegacySchema
```

---

## 3. Core Components of an Anti-Corruption Layer

```
+--------------------------+-------------------------------------------------+
| Component                | Architectural Responsibility                    |
+--------------------------+-------------------------------------------------+
| Adapter                  | Converts protocols (e.g., gRPC/REST to SOAP/TCP)|
| Translator               | Maps cryptic fields (e.g., CUST_TYP_01 to Tier) |
| Facade                   | Simplifies complex multi-step legacy workflows  |
+--------------------------+-------------------------------------------------+
```

### Semantic Transformation Example
```
Legacy Schema Field          Modern Domain Model Field
--------------------         -------------------------
TX_ID_9901                  orderId (UUID)
CD_STAT_V2 == 'A'           orderStatus: "ACTIVE"
AMT_CENT_NET                totalPrice: Money(amount, currency)
```

---

## 4. Deployment Topologies for ACL

1. **In-Process Library**: Embedded directly within the modern microservice as an external integration package. Lowest latency, but couples the modern service build to the translation logic.
2. **Standalone Microservice**: Deployed as an independent translation proxy. Isolates resource usage, enables independent deployment, and allows multiple modern services to share the same legacy adapter.

---

## 5. Production Considerations & Sunsetting

- **Lifecycle & Sunset Plan**: The ACL is inherently temporary scaffolding. Ensure the ACL codebase has a designated sunset roadmap to prevent it from becoming permanent technical debt.
- **Error Mapping**: Translate legacy error codes into standard RFC 7807 Problem Details HTTP errors to prevent cryptic legacy exceptions from leaking to API consumers.
