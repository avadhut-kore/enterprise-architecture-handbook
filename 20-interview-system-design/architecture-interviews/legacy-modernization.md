# System Design Case: Legacy Modernization & Mainframe Offload

> A comprehensive, 20-part senior architectural design for modernizing a 25-year-old on-premise mainframe core banking system using the Strangler Fig pattern, Change Data Capture (CDC), and an event-driven cloud mesh with zero downtime.

---

## 1. Business Context & Problem Statement
A global retail bank processes all customer account ledgers, deposits, and wire transfers on a 25-year-old on-premise IBM z/OS COBOL / DB2 mainframe. The mainframe hardware costs $15M/year in MIPS (Millions of Instructions Per Second) licensing. The bank's new mobile banking app generates 50x more read traffic than historical ATM baselines, threatening to overwhelm mainframe MIPS capacity. The executive board mandates modernizing the system to a cloud-native architecture on AWS with **zero downtime, zero data loss, and zero disruption to daily customer operations**.

---

## 2. Candidate Prompt & Executive Premise
> *"Architect a multi-year modernization roadmap and target cloud architecture to offload 90% of read traffic from an on-premise COBOL/DB2 mainframe core to cloud microservices within 12 months, followed by systematic write migration and eventual mainframe decommissioning."*

---

## 3. Clarifying Questions to Ask the Interviewer
1. *Can we perform a big-bang weekend cutover?* (Absolute zero tolerance for big-bang cutovers. Regulators require zero customer-impacting downtime).
2. *Can we modify the legacy COBOL application code to emit events?* (No. COBOL developers are scarce, and modifying legacy code introduces unacceptable operational risk).
3. *What is our peak read and write traffic?* (Read: 15,000 queries/sec; Write: 1,200 transactions/sec).
4. *What is our compliance boundary?* (PCI-DSS and banking regulatory compliance require automated reconciliation showing zero ledger discrepancy between mainframe and cloud).

---

## 4. Expected Functional Scope & Boundaries
* **In Scope**:
  * Strangler Fig facade and enterprise API routing.
  * Non-invasive Change Data Capture (CDC) on mainframe DB2 logs.
  * Cloud-native read models (PostgreSQL / Redis) populated via Kafka.
  * Real-time automated data reconciliation engine.
  * Shadow traffic (Traffic Mirroring) verification.
* **Out of Scope**:
  * Replacing branch office teller hardware.

---

## 5. Non-Functional Requirements (NFRs) & Concrete Targets
* **Availability**: 99.999% during entire multi-year migration.
* **Replication Latency**: Mainframe-to-cloud CDC lag $< 500\text{ms}$ (p95).
* **Data Consistency**: Zero balance drift between mainframe and cloud.
* **Cost Reduction**: Reduce annual mainframe MIPS licensing expenses by $> 60\%$.

---

## 6. High-Level Architecture (The Event-Driven Strangler Fig)

```mermaid
flowchart TD
    DigitalChannels([Mobile Banking / Web / ATMs]) --> APIGW[Enterprise API Gateway & Strangler Facade]
    
    subgraph OnPremMainframe [On-Premise Mainframe Core]
        LegacyCOBOL[Legacy COBOL Application]
        MainframeDB[(DB2 Transactional Database)]
        CDC[Change Data Capture: IBM Infosphere / Debezium]
    end
    
    subgraph CloudPlatform [AWS Cloud Landing Zone]
        KafkaMesh[[Apache Kafka Event Mesh]]
        AccountReadSvc[Cloud Account Read Microservices]
        CloudDB[(Cloud Read Database: AWS Aurora PostgreSQL)]
        CloudCache[(Redis Core Cache)]
        ReconEngine[Continuous Automated Reconciliation Worker]
    end
    
    APIGW -->|Read Traffic (90%): Strangled to Cloud| AccountReadSvc
    APIGW -->|Write Traffic (Phase 1): Proxied to Mainframe| LegacyCOBOL
    
    LegacyCOBOL --> MainframeDB
    MainframeDB -->|Non-Invasive Log Sniffing| CDC
    CDC -->|Direct Connect Private Fiber Link| KafkaMesh
    
    KafkaMesh --> AccountReadSvc
    AccountReadSvc --> CloudDB
    AccountReadSvc --> CloudCache
    
    ReconEngine <--> MainframeDB
    ReconEngine <--> CloudDB
```

---

## 7. The 3-Horizon Evolutionary Modernization Roadmap

```
Horizon 1: Read Offload & Strangler Facade (Months 1–6)
  - Install API Gateway in front of legacy core.
  - Deploy CDC on DB2 logs to stream changes into Kafka with zero mainframe code edits.
  - Populate cloud read models; shift 90% of mobile read queries to cloud.
  - Mainframe MIPS drops by 65%, achieving immediate financial ROI.

Horizon 2: Shadow Writing & Feature Extraction (Months 7–18)
  - Extract the first bounded context (e.g., Notifications / Beneficiary Management) to cloud.
  - Route write traffic through cloud microservices using Shadow Mirroring.
  - Validate output parity between cloud and legacy across 5 Million transactions.

Horizon 3: Write Mastership Cutover & Mainframe Decommissioning (Months 19–30)
  - Shift master write authority to cloud microservices.
  - Stream CDC in reverse (Cloud -> Mainframe) as a temporary safety rollback buffer.
  - Turn off legacy mainframe hardware permanently.
```

---

## 8. Non-Invasive Change Data Capture (CDC) Mechanics

Instead of rewriting COBOL code, CDC reads directly from the database engine's **Write-Ahead / Redo Logs**:
1. When a banking transaction executes on the mainframe, DB2 writes the mutation to its internal recovery log.
2. The CDC agent reads the log asynchronously in memory with **zero CPU impact on the active mainframe transaction engine**.
3. CDC serializes the before-and-after row image into an Apache Avro event published to an AWS Kafka topic via a private AWS Direct Connect fiber link in $< 200\text{ms}$.

---

## 9. Continuous Automated Reconciliation & Parity Engine

To prove to bank regulators and auditors that cloud data has not drifted:
* An asynchronous reconciliation engine continuously computes **cryptographic Merkle Tree hashes** across account balances in DB2 and Aurora PostgreSQL.
* If a discrepancy is detected (e.g., CDC message dropped or delayed), an automated alert fires, the discrepant account is temporarily routed to the mainframe primary, and a self-healing patch event is dispatched.

---

## 10. Trade-Off Analysis & Rejected Alternatives
* **Big-Bang Cutover vs. Evolutionary Strangler Fig**:
  * *Big-Bang*: Discard the mainframe over a long weekend and switch 100% of traffic to a newly written cloud system.
  * *Why Rejected*: High-profile enterprise failures (e.g., TSB Bank's 2018 catastrophic IT migration failure costing £330M and CEO resignation) prove that big-bang rewrites in banking are suicidal. The **Strangler Fig pattern** allows the enterprise to realize ROI in Month 6 while keeping delivery risk near zero.

---

## 11. Cost Modeling & Financial ROI
* **Mainframe MIPS Savings**:
  * Offloading 90% of read traffic reduces mainframe CPU consumption from 12,000 MIPS to 3,500 MIPS.
  * Annual software and hardware maintenance savings: **$\$8,500,000/\text{year}$**.
* **Cloud Infrastructure Run Rate**:
  * AWS Aurora, Kafka MSK, and EKS fleet costs $\approx \$450,000/\text{year}$.
  * **Net Enterprise Annual Savings**: $\mathbf{>\$8,000,000/\text{year}}$, delivering immediate executive credibility.

---

## 12. Interviewer Evaluation Rubric: Weak vs. Strong Answers
* **Weak**: Proposes rewriting all COBOL code in a big-bang migration; proposes polling the mainframe database via SQL `SELECT * WHERE updated_at > now` (instantly crashing the mainframe); forgets regulatory compliance reconciliation.
* **Strong**: Employs the Strangler Fig pattern; captures events non-invasively via DB2 log CDC; models financial MIPS savings; designs continuous Merkle-tree automated reconciliation; defines phased multi-year horizons.
