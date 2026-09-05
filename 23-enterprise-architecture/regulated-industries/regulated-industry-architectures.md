# Regulated Industry Architecture Playbooks

Deep architectural constraints, regulatory compliance mandates, data models, and reference patterns across 12 core global industries.

---

## 1. Banking & Capital Markets
* **Key Regulations**: Basel III/IV, PCI-DSS 4.0, Dodd-Frank, MiFID II, PSD2/PSD3, FFIEC, DORA.
* **Architectural Invariants**: Sub-millisecond ACID ledger consistency; multi-region active-active disaster recovery with RPO=0; strict cryptographic tokenization of payment credentials; immutable audit trails for financial transactions.
* **Reference Pattern**: Event-driven ledger replication using Kafka with Raft consensus; HSM-backed key storage; automated regulatory reporting pipelines.

---

## 2. Insurance (P&C, Life, Reinsurance)
* **Key Regulations**: Solvency II, NAIC Model Laws, IFRS 17, HIPAA.
* **Architectural Invariants**: Actuarial data separation; long-term policy retention (up to 70 years); automated claims fraud detection; separation of catastrophe risk modeling engines from transactional policy admin.
* **Reference Pattern**: Lakehouse architecture for multi-decade claims analytics; decoupled quoting engine with auto-scaling during open enrollment.

---

## 3. Healthcare Providers & Payers
* **Key Regulations**: HIPAA, HITECH, HL7/FHIR, CMS Interoperability Rule.
* **Architectural Invariants**: End-to-end PHI encryption; strict role-based access control (RBAC) with break-glass clinical emergency overrides; FHIR JSON API gateways; audit logging of every record view.
* **Reference Pattern**: Zero-Trust API gateway with automated PHI redaction proxies; hybrid edge deployment for intensive care unit (ICU) medical device telemetry.

---

## 4. Pharmaceuticals & Life Sciences
* **Key Regulations**: FDA 21 CFR Part 11, GxP, EMA Clinical Trial Regulation, HIPAA.
* **Architectural Invariants**: Cryptographic electronic signatures for clinical data entries; immutable audit logs; cold-chain distribution IoT telemetry; strict air-gapped clinical trial data vaults.
* **Reference Pattern**: Blockchain or append-only distributed ledgers for drug provenance; high-performance cloud computing (HPC) for molecular modeling.

---

## 5. Retail & Omnichannel Commerce
* **Key Regulations**: PCI-DSS 4.0, GDPR/CCPA, FTC Consumer Protection.
* **Architectural Invariants**: Tokenized cardholder data isolated in third-party vaults; real-time omnichannel inventory tracking; decoupled cart and checkout to survive 10x flash sale surges.
* **Reference Pattern**: Composable MACH (Microservices, API-first, Cloud-native, Headless) commerce architecture with CDN edge caching.

---

## 6. Manufacturing & Industrial Systems
* **Key Regulations**: ISA-95, OSHA, ISO 9001, IEC 62443 (Industrial Cybersecurity).
* **Architectural Invariants**: Air-gapped Purdue Model network segmentation separating shop-floor SCADA/OT systems from corporate IT; millisecond latency for robotic safety controllers; local edge autonomy during WAN outages.
* **Reference Pattern**: Industrial IoT (IIoT) edge gateways running MQTT Sparkplug B streaming to cloud predictive maintenance pipelines.

---

## 7. Logistics, Shipping & Supply Chain
* **Key Regulations**: US Customs C-TPAT, IMO Maritime Safety, Dangerous Goods Regulations (IATA).
* **Architectural Invariants**: Geolocation tracking telemetry; offline-first mobile synchronization for remote drivers/vessels; B2B EDI 850/856 translator gateways.
* **Reference Pattern**: Event-driven logistics tracking mesh with geo-partitioned distributed databases and automated carrier rating APIs.

---

## 8. Telecommunications
* **Key Regulations**: FCC CALEA, 3GPP 5G Standards, EU Electronic Communications Code, GDPR.
* **Architectural Invariants**: Sub-millisecond session establishment; carrier-grade availability (99.9999% - 6 Nines); lawful interception interfaces; high-throughput CDR (Call Detail Record) processing.
* **Reference Pattern**: TM Forum Open Digital Architecture (ODA); cloud-native 5G core deployed on bare-metal Kubernetes with SR-IOV networking.

---

## 9. Government & Public Sector
* **Key Regulations**: FedRAMP High, DoD IL5/IL6, CJIS, FISMA, EU GDPR.
* **Architectural Invariants**: Isolated sovereign cloud enclaves; zero cross-border data egress; citizen data access auditability; multi-factor biometric authentication.
* **Reference Pattern**: Multi-tenant sovereign government cloud with automated continuous compliance monitoring and citizen identity federation.

---

## 10. Energy & Utilities
* **Key Regulations**: NERC CIP (North American Electric Reliability), FERC, Nuclear Regulatory Commission.
* **Architectural Invariants**: Physical unidirectional security gateways (data diodes); critical infrastructure isolation; real-time smart grid telemetry (DNP3 / IEC 61850).
* **Reference Pattern**: Defense-in-depth air-gapped SCADA topology with outbound-only data diode replication to corporate analytics.

---

## 11. Travel & Hospitality
* **Key Regulations**: FAA/ICAO Aviation Regulations, PCI-DSS, TSA Secure Flight, EU Passenger Name Record (PNR).
* **Architectural Invariants**: High-throughput global inventory locks (seat/room reservations); global GDS (Global Distribution System) integration; sub-second search latency across 50 partner airlines.
* **Reference Pattern**: Distributed in-memory caching grids (Redis Enterprise) with distributed transaction sagas for flight/hotel reservation bundles.

---

## 12. B2B Enterprise SaaS
* **Key Regulations**: SOC 2 Type II, ISO 27001, GDPR, CCPA, FedRAMP Moderate.
* **Architectural Invariants**: Multi-tenant data isolation; zero noisy-neighbor performance impact; automated tenant provisioning; customer-managed encryption keys (BYOK).
* **Reference Pattern**: Cell-based multi-tenant architecture with tenant-keyed row-level security (RLS) in PostgreSQL.
