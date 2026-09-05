# Core Banking Architecture Styles and Integration Topology

## 1. Architectural Taxonomy
Core banking engines act as the authoritative ledger of record for deposits, loans, collateral, and customer positions. Integrations with core banking must reconcile the impedance mismatch between modern cloud channels and legacy monolithic transaction managers.

```
       Channel Tier (Mobile, Web, Branch, Open Banking APIs)
                             │
     ════════════════════════▼════════════════════════  [DMZ / API Gateway]
       Integration Tier (Event Bridge, Saga Orchestrator, CDC)
                             │
     ════════════════════════▼════════════════════════  [Private Financial Subnet]
       Core Banking Engines:
       ├── Legacy Monolith: IBM z/OS Mainframe, FIS Systematics, Fiserv DNA
       ├── Packaged Core: Temenos Transact, Finacle, SAP for Banking
       └── Modern Cloud-Native Core: Thought Machine Vault, Mambu, Engine by Starling
```

## 2. Comparative Matrix: Core Banking Generations

| Dimension | Legacy Monolith (Gen 1) | Packaged Core (Gen 2) | Cloud-Native Core (Gen 3) |
| :--- | :--- | :--- | :--- |
| **Operating System** | IBM z/OS, AIX, AS/400 | Linux / Windows Server | Kubernetes / Cloud Managed |
| **Data Store** | DB2, VSAM files, IMS DB | Oracle RAC, MS SQL Server | CockroachDB, Spanner, Aurora PostgreSQL |
| **Processing Paradigm**| Overnight batch window (EOD) | Real-time OLTP + Daily EOD | 24x7 Real-time continuous ledgering |
| **Integration Protocols**| SNA, MQ Series, Fixed CPYBOOK | SOAP / Web Services, Direct DB | REST, gRPC, Kafka Event Streams |
| **MIPS Cost Impact** | Extreme ($$$ per direct API query)| Moderate (Per-core licensing) | Low (Horizontal cloud autoscaling) |

## 3. The Modern Core Banking Event Bridge Pattern
Directly querying a mainframe core banking ledger for mobile balance inquiries incurs exorbitant MIPS software charges and risks starving OLTP transaction threads. Modern enterprise integration deploys an **Asynchronous Read Replica / Event Bridge**:

```
[Mainframe Core Banking] 
       │ (Change Data Capture / VSAM Log Scrape)
       ▼
[Kafka Event Backbone] ──> [Topic: account-balance-events]
       │
       ▼
[Low-Latency Read Cache / Redis] ◄── [Mobile Banking Gateway]
(Services 98% of balance read queries with zero MIPS consumption)
```
