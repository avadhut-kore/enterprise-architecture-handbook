# Enterprise Architecture Master Checklist

The definitive verification checklist for Chief Architects, Enterprise Architects, and Review Boards evaluating enterprise-scale initiatives.

---

### 1. Business Strategy & Capabilities
- [ ] Corporate business strategy and target business outcomes clearly understood.
- [ ] Measurable business KPIs (revenue, cost, NPS, cycle time) defined for initiative.
- [ ] Level 1, 2, and 3 business capabilities mapped to enterprise capability model.
- [ ] Value streams and customer journeys identified; stage handoffs analyzed.
- [ ] Target operating model defined (Team Topologies, product squads, platform teams).

### 2. Applications & Systems
- [ ] Application portfolio inventory updated with owner, criticality, and lifecycle status.
- [ ] System criticality tier assigned (Tier 0 to Tier 3) with explicit RTO/RPO budgets.
- [ ] Technical health, business value, and maintenance debt scored via the TIME matrix.
- [ ] Cross-system dependencies mapped; blast radius of component failure contained.
- [ ] Application rationalization disposition selected (7R: Retain, Modernize, Replace, etc.).

### 3. Data Architecture & Governance
- [ ] Enterprise data domains, business data owners, and data stewards assigned.
- [ ] Master Data Management (MDM) Golden Records identified for customer, product, and accounts.
- [ ] Polyglot storage engines selected based on query patterns (OLTP vs OLAP).
- [ ] Automated data lineage and schema evolution contracts defined in Schema Registry.
- [ ] Data classification assigned (Public, Internal, Confidential, Restricted/PII).

### 4. Integration & Connectivity
- [ ] 3-tier API-led connectivity model applied (Experience, Process, System APIs).
- [ ] Asynchronous event streaming (Kafka) chosen for decoupled, high-throughput writes.
- [ ] OpenAPI 3.0 or Protobuf contract authored and approved prior to implementation.
- [ ] Direct database-to-database integration between distinct domains strictly prohibited.
- [ ] Backward compatibility enforced; deprecation window established for breaking changes.

### 5. Technology & Platforms
- [ ] Software runtimes, frameworks, and databases conform to Enterprise Technology Radar.
- [ ] Solution adopts approved enterprise Paved Roads (Internal Developer Platform).
- [ ] Open-source libraries vetted for permissive licenses (zero viral GPL/AGPL in commercial code).
- [ ] Software Bill of Materials (SBOM) scanned in CI/CD for known CVE vulnerabilities.
- [ ] Third-party vendor dependencies encapsulated behind Anti-Corruption Layers.

### 6. Cloud & Infrastructure
- [ ] Multi-account cloud landing zone deployed with Hub-and-Spoke networking.
- [ ] 100% of cloud resources provisioned via Infrastructure as Code (Terraform).
- [ ] Multi-AZ high availability (99.99%) and multi-region disaster recovery verified.
- [ ] FinOps resource tagging enforced (`CostCenter`, `ApplicationID`, `Owner`).
- [ ] Auto-scaling policies tested under simulated 5x peak transaction volume.

### 7. Security & Zero Trust
- [ ] Identity as the perimeter: centralized OIDC/OAuth2 with FIDO2 passwordless MFA.
- [ ] Mutual TLS (mTLS) and least-privilege RBAC enforced between all services.
- [ ] Sensitive data encrypted at rest (AES-256 GCM) with customer-managed KMS keys.
- [ ] Automated SAST/DAST security scans gating pull requests in CI/CD.
- [ ] Threat model completed and reviewed by CISO; compensating controls documented.

### 8. Enterprise AI & Intelligence
- [ ] AI use case justified: deterministic logic ruled out as cheaper/faster alternative.
- [ ] All LLM calls routed through Enterprise AI Gateway with PII scrubbing and rate limits.
- [ ] Zero Data Retention (ZDR) contracts established with foundation model vendors.
- [ ] EU AI Act risk tier assigned; human-in-the-loop controls implemented for high-risk models.
- [ ] Automated LLM evaluation pipelines (RAG Triad, hallucination checks) configured in CI.

### 9. Transformation & Governance
- [ ] Current state, target architecture, and intermediate transition plateaus documented.
- [ ] Standalone business value delivered at each intermediate migration plateau.
- [ ] Architecture Review Board (ARB) formal approval record signed and archived.
- [ ] Temporary architecture exceptions cataloged with hard <12-month expiration dates.
- [ ] Automated architectural fitness functions running in CI/CD pipeline to prevent regression.
