# The 24 Principles of Enterprise Integration Architecture

These 24 principles constitute the non-negotiable architectural foundation for integrating enterprise software systems.

---

## 1. Business & Ownership Principles

### 1. Integration Starts from Business Capabilities
Integrations exist to execute business processes (e.g., Order-to-Cash, Patient Onboarding, Loan Origination), not to connect technical databases. Every interface must align with a distinct business capability.

### 2. Explicit System-of-Record (SoR) Ownership
Every business entity (Customer, Account, Ledger Entry, Inventory) must have exactly one authoritative System of Record. Multiple systems may hold read-only cache replicas, but only the SoR is authorized to mutate master state.

### 3. Clear Data Ownership Boundaries
Data crossing a boundary must have an assigned business and technical data steward responsible for data quality, semantic definitions, and regulatory compliance.

### 4. Prefer Loose Coupling
Systems should minimize compile-time, temporal, spatial, and protocol dependencies. Downstream outages must not cascade into catastrophic upstream platform failures.

### 5. Eliminate Point-to-Point Spaghetti
Direct peer-to-peer coupling between $N$ systems grows as $O(N^2)$. Workloads must leverage managed API gateways, message buses, or event meshes to maintain bounded complexity.

---

## 2. Design & Modeling Principles

### 6. Use Canonical Data Models Selectively
A single universal corporate data model is an expensive architectural anti-pattern. Use Canonical Data Models (CDMs) strictly within specific bounded contexts (e.g., standardizing payments across channels), not as an all-encompassing enterprise monolith.

### 7. Preserve Source System Semantics
Transformations must respect source business rules. Do not force high-fidelity domain concepts into lossy, lowest-common-denominator abstractions.

### 8. Failure is a Normal Operating Condition
Networks split, cloud regions drop packets, databases lock, and third-party SaaS APIs experience downtime. Integration architectures must assume failure is occurring continuously and degrade gracefully.

### 9. Design for Mandatory Idempotency
Every state-changing integration (POST, asynchronous message consumption, webhook handling) must be idempotent. Re-delivering an identical message 10 times must produce the exact same system state as delivering it once.

### 10. Design for Exponential Retry with Full Jitter
Immediate fixed retries cause catastrophic retry storms that overwhelm recovering downstream systems. All retries must incorporate exponential backoff with randomized decorrelated jitter.

---

## 3. Resilience, Security & Operations

### 11. Design for Automated Reconciliation
In distributed systems, asynchronous event flows and network retries will eventually cause ledger or record discrepancies. Automated end-of-day reconciliation is a mandatory first-class architectural requirement, not an operational afterthought.

### 12. Design for End-to-End Distributed Observability
Every interaction across organizational boundaries must inject and propagate standard W3C TraceContext headers (`traceparent`) and persistent business correlation IDs to enable cross-platform tracing.

### 13. Secure Every Trust Boundary (Zero Trust)
Never trust internal networks. Every system-to-system boundary must enforce mutual TLS 1.3 (mTLS) with cryptographic identity certificates and short-lived OAuth 2.0 / OIDC tokens.

### 14. Minimize Sensitive Data Propagation
Do not transmit full Primary Account Numbers (PANs), Social Security Numbers (SSNs), or Protected Health Information (PHI) across integration hops unless strictly required. Replace sensitive attributes with non-reversible surrogate tokens at the edge.

### 15. Separate Real-Time from Batch Workloads
Do not force bulk analytics or nightly reconciliation files over real-time OLTP messaging channels. Segregate throughput-heavy batch ETL from low-latency interactive customer flows.

---

## 4. Contracts, Evolution & Governance

### 16. Avoid Synchronous Chains Across Unreliable Perimeters
Chaining multiple synchronous blocking HTTP calls across independent systems multiplies latency and squares unavailability ($A_{total} = A_1 \times A_2 \times A_3$). Use asynchronous choreography or message queues across unreliable boundaries.

### 17. Explicit, Machine-Readable Contracts
All interfaces must be formally defined using machine-readable contracts (OpenAPI 3.1, Protocol Buffers v3, JSON Schema, or ISO 20022 XML Schema). Undocumented payloads are strictly prohibited.

### 18. Strict Contract Versioning & Backward Compatibility
Non-breaking additive changes must be supported without bumping major versions. Breaking changes require semantic version increments (`v1` → `v2`) with a minimum 6-to-12-month deprecation overlap.

### 19. Architect for Legacy Coexistence
Legacy mainframes, COBOL backends, and on-premises ERPs cannot be replaced overnight. Architect an Anti-Corruption Layer (ACL) and Strangler Fig routing facade to enable coexistence while modernizing incrementally.

### 20. Design Defensible Rollback and Exit Paths
Every migration, cutover, or vendor integration platform must include a tested, automated rollback plan and an architectural exit strategy to mitigate vendor lock-in.

### 21. Justify Integration Platforms Economically
Do not introduce an Enterprise Service Bus (ESB) or iPaaS simply because it exists. Evaluate the operational burden, licensing costs, and latency tax against direct decoupled messaging.

### 22. Enforce Interface Abstraction Over Vendor Proprietary APIs
Isolate vendor-specific SDKs and proprietary protocols behind internal domain interfaces so that changing an external SaaS or payment processor requires zero changes to core domain logic.

### 23. Architecture Must Enforce Regulatory Guardrails
Integrations in banking, healthcare, and payments must embed regulatory constraints (PCI DSS CDE isolation, HIPAA BAA trust boundaries, GDPR data sovereignty) directly into network topologies and storage tiers.

### 24. Operationally Supportable by SRE & Support Teams
If an integration cannot be debugged by an on-call engineer at 02:00 AM using centralized dashboards, dead-letter tools, and standard runbooks, the architecture is defective.
