# Enterprise Architecture Anti-Patterns

The master catalog of 24 lethal Enterprise Architecture anti-patterns that derail digital transformations, inflate technology debt, and destroy business alignment.

---

## 1. Catalog Index

| # | Anti-Pattern Name | Core Manifestation | Failure Impact |
| :-: | :--- | :--- | :--- |
| 1 | [Architecture Disconnected from Business](architecture-disconnected-from-business.md) | Architects design complex distributed systems or adopt new paradigms w... | Projects deliver technically impressive systems that fail to... |
| 2 | [EA as Documentation Department](ea-as-documentation-department.md) | The Enterprise Architecture team spends 90% of its time producing mass... | Architecture is seen as an administrative overhead tax rathe... |
| 3 | [Architecture Ivory Tower](architecture-ivory-tower.md) | Architects work in isolation from delivery squads, handing down rigid ... | Engineering squads actively bypass architecture, creating ra... |
| 4 | [Framework-First Architecture](framework-first-architecture.md) | Attempting to implement 100% of TOGAF, Zachman, or ArchiMate before ma... | Paralysis by methodology; 18 months of framework meetings wi... |
| 5 | [Diagram-First Architecture](diagram-first-architecture.md) | Believing that an architectural drawing in Visio or PowerPoint represe... | Diagrams gloss over critical NFRs (latency, consistency, con... |
| 6 | [Governance Bottleneck](governance-bottleneck.md) | Every minor architectural change, schema tweak, and tool selection req... | Delivery velocity grinds to a halt; project managers view ar... |
| 7 | [Architecture by Committee](architecture-by-committee.md) | Architecture decisions require unanimous consensus across 25 stakehold... | Systems become Frankenstein monsters containing every stakeh... |
| 8 | [Technology-Driven Strategy](technology-driven-strategy.md) | Adopting emerging technologies (microservices, blockchain, generative ... | Massive capital expenditure on complex infrastructure that a... |
| 9 | [Standardization Everywhere](standardization-everywhere.md) | Enforcing rigid technology uniformity across fundamentally different b... | Product teams are crippled by ill-fitting tools; top enginee... |
| 10 | [Standardization Nowhere](standardization-nowhere.md) | Allowing complete, unconstrained developer freedom where every squad p... | Extreme technology sprawl (14 languages, 9 databases); impos... |
| 11 | [One-Size-Fits-All Architecture](one-size-fits-all-architecture.md) | Applying identical architectural patterns (e.g., event-driven microser... | Simple internal CRUD tools become bloated distributed system... |
| 12 | [Capability-Map Theater](capability-map-theater.md) | Building elaborate, color-coded Level-4 business capability maps in en... | Capability maps become ornamental wall art while capital bud... |
| 13 | [Endless Architecture Studies](endless-architecture-studies.md) | Spending 12 months conducting comparative vendor analyses and POCs whi... | Analysis paralysis; missed strategic market windows; million... |
| 14 | [No Transition Architecture](no-transition-architecture.md) | Designing a gorgeous target-state architecture but providing zero inte... | Projects attempt high-risk 'big-bang' cutovers that inevitab... |
| 15 | [Target-State Fantasy](target-state-fantasy.md) | Designing target architectures that assume infinite budget, zero legac... | Blueprints that are completely detached from organizational ... |
| 16 | [Ignoring Organizational Readiness](ignoring-organizational-readiness.md) | Architecting advanced cloud-native platforms for an organization whose... | Multi-million dollar platforms sit unused or fail in product... |
| 17 | [Ignoring Economics & FinOps](ignoring-economics.md) | Designing architectures without calculating 5-year Total Cost of Owner... | Architectures suffer massive budget shock when production sc... |
| 18 | [Ignoring Technical Debt](ignoring-technical-debt.md) | Continuously delivering new features while hiding architectural debt, ... | Compound architectural debt causes catastrophic outages, sec... |
| 19 | [Ignoring Operations & SRE](ignoring-operations.md) | Designing systems that look elegant in architecture diagrams but are a... | Outages stretch to days because systems lack distributed tra... |
| 20 | [Ignoring Security & Compliance](ignoring-security.md) | Treating security as a late-stage checklist item 2 weeks before produc... | Critical architectural flaws (e.g., plain-text PII in databa... |
| 21 | [Ignoring Data Ownership & Lineage](ignoring-data-ownership.md) | Treating data as an incidental side-effect of applications rather than... | Incompatible customer definitions across systems; conflictin... |
| 22 | [Ignoring Vendor Lock-In](ignoring-vendor-lock-in.md) | Building core proprietary business logic directly inside a proprietary... | The vendor doubles licensing prices or discontinues features... |
| 23 | [Ignoring Regional Constraints](ignoring-regional-constraints.md) | Designing a single centralized global architecture that ignores local ... | Severe regulatory fines (e.g., violating China PIPL, EU GDPR... |
| 24 | [AI-First Strategy Without Business Value](ai-first-enterprise-strategy-without-business-value.md) | Mandating that every business process and application must incorporate... | Massive GPU costs, non-deterministic hallucinations in trans... |

---

## 2. Navigating the Anti-Patterns
Every anti-pattern specification provides:
1. **The Symptom**: How to spot this anti-pattern in your organization.
2. **The Root Cause**: Why enterprises fall into this trap.
3. **The Damage**: Quantified financial, operational, and architectural consequences.
4. **The Remediation**: Concrete, step-by-step architectural playbooks to escape the anti-pattern.
