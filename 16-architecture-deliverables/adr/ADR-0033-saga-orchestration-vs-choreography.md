# ADR-0033: Orchestrated Sagas for Complex Multi-Step Business Workflows

- **Status**: Accepted
- **Date**: 2026-09-05
- **Deciders**: Enterprise Architecture Review Board (ARB)
- **Technical Story**: Phase 5 Data & Integration Architecture Governance

---

## 1. Context and Problem Statement
Mandate orchestrated sagas with explicit state machines for complex multi-party financial workflows; reserve choreography for notifications.

Enterprise systems frequently encounter severe operational drift, data corruption, and integration fragility when data storage, messaging, and financial operations lack firm architectural governance.

---

## 2. Decision Drivers
- High transactional reliability, zero financial data loss, and strict audit compliance.
- Long-term maintainability, vendor lock-in mitigation, and schema backward compatibility.
- Operational simplicity and predictable total cost of ownership (TCO).

---

## 3. Considered Options
1. **Option 1**: Selected strategic architectural pattern / technology.
2. **Option 2**: Alternative approach (e.g., ad-hoc point-to-point, unmanaged dual-writes, fuzzy matching).

---

## 4. Decision Outcome
Chosen Option: **Option 1**.

### Positive Consequences
- Architectural boundaries are strictly maintained and verified in automated CI pipelines.
- Data integrity, financial reconciliation, and integration auditability are guaranteed.
- Reduced cognitive load and standardized onboarding across global engineering teams.

### Negative Consequences
- Requires initial scaffolding discipline and strict contract governance.
- Minor initial development overhead to maintain boundary abstractions and contract definitions.

---

## 5. Compliance & Verification
Automated fitness functions, contract linters, and CI/CD quality gates will enforce adherence to this decision before pull requests can be merged into production branches.
