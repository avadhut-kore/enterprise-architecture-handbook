# 19. Case Studies & Post-Mortems: Master Catalog

Welcome to the **Master Case Study & Forensic Post-Mortem Catalog** of the Enterprise Architecture Handbook. This domain catalogs real-world system failures, scaling post-mortems, legacy transformations, and forensic root-cause investigations.

## Master Case Study Collections

### 1. Global & Cross-Cutting Case Studies (This Domain)
The subdirectories within this domain provide deep forensic analyses following the 19-section post-mortem standard:
* [`cloud/`](./cloud/) — Major cloud provider outages, multi-region failover blunders, and networking partition incidents (19 post-mortems).
* [`financial/`](./financial/) — Settlement failures, ledger desynchronizations, and payment network brownouts (16 post-mortems).
* [`data-integration/`](./data-integration/) — Kafka broker lockups, schema registry poisoning, and data corruption events (11 post-mortems).
* [`application-architecture/`](./application-architecture/) — Monolith thread exhaustion, memory leaks, and distributed deadlock incidents (11 post-mortems).
* [`system-design/`](./system-design/) — Thundering herd, cache stampedes, and cascading circuit breaker trip analysis (11 post-mortems).
* [`ai-modern/`](./ai-modern/) — Prompt injection breaches, vector index divergence, and GPU compute starvation incidents (21 post-mortems).
* [`security-operations/`](./security-operations/) — Ransomware breaches, credential stuffing, and key management compromise (21 post-mortems).

---

### 2. Specialized Domain Post-Mortem Catalogs (Cross-Domain)
In accordance with our architectural principle of **Legitimate Specialization**, domain-specific operational post-mortems are curated directly within their respective domain authority:

* **[DevOps & Delivery Forensic Case Studies](../09-devops/case-studies/README.md)**:
  * 20 Production delivery failures (`cs-dev-01` to `cs-dev-20`) covering Jenkins crashes, Terraform state corruption, NPM supply chain poisoning, and runaway K8s billing.
* **[Enterprise Architecture Case Studies](../23-enterprise-architecture/case-studies/README.md)**:
  * 10 Multi-year enterprise transformation post-mortems (`cs-081` to `cs-090`) covering Global Monolith Modernization, Portfolio Rationalization, and M&A Systems Integration.
* **[Capstone Architect Mastery Post-Mortems](../24-architect-mastery/case-studies/README.md)**:
  * 20 Planetary-scale crisis post-mortems (`cs-101` to `cs-120`) covering Saving a Global Bank Core, Black Friday E-Commerce Survival, Biometric Scale-Out, and Defense Tactical Edge Recovery.
