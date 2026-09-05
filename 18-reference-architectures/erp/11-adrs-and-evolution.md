# Architecture Decision Records & Evolution Roadmap: ERP

## 1. Canonical Architecture Decision Records

### ADR-001: Adoption of SAP Clean Core and Sidecar Extensibility
- **Status**: Accepted
- **Context**: Custom ABAP code modifications inside the ERP core prevent automated quarterly software updates and create severe technical debt.
- **Decision**: Strictly prohibit custom modifications inside the ERP core codebase; deploy all custom enterprise extensions on cloud-native sidecars communicating via public APIs and Kafka events.
- **Consequences**: Enables zero-downtime ERP updates; requires operating a cloud microservices sidecar cluster.

---

## 2. Evolution Roadmap (1x to 100x Scale)
- **Stage 1 (1x)**: Standard ERP core running on single in-memory instance.
- **Stage 2 (10x)**: Clean Core sidecars on Kubernetes; automated ISO 20022 bank integration.
- **Stage 3 (100x)**: Multi-region distributed ledger consolidation; AI-driven predictive cash flow forecasting.
