# Enterprise Insurance Claims Processing Architecture

This reference architecture models an automated property and casualty (P&C) insurance claims processing engine featuring multi-channel First Notice of Loss (FNOL), OCR document intelligence, real-time fraud scoring, and human-in-the-loop adjuster workflows.

## 1. Business Context & Architectural Drivers
* **Processing Speed**: Straight-Through Processing (STP) target of 60% of low-complexity auto and property claims under $2,500 without human intervention.
* **Fraud Detection**: Reduce claims fraud leakage by executing real-time anomaly detection across policy history, social networks, and damage telemetry.
* **Document Ingestion**: Multi-modal intake supporting scanned PDFs, smartphone photos, police reports, and dashcam videos.

## 2. C4 Level 1: System Context

```mermaid
graph TB
    subgraph Claimants ["External Stakeholders"]
        Policyholder["Policyholder<br/>[Person]<br/>Submits FNOL claim with damage photos"]
        RepairShop["Auto Repair Facility<br/>[External Partner]<br/>Submits repair estimates and invoices"]
        Adjuster["Claims Adjuster<br/>[Person]<br/>Investigates and approves complex claims"]
    end

    subgraph ClaimsPlatform ["Enterprise Claims Processing Platform"]
        ClaimsCore["Claims Management System<br/>- FNOL Intake Gateway<br/>- OCR Document Intelligence<br/>- Automated Adjudication Engine<br/>- Adjuster Workbench"]
    end

    subgraph EnterpriseBackbone ["Enterprise Systems"]
        PolicyAdmin["Policy Administration System (Guidewire / Duck Creek)"]
        PaymentSystem["Enterprise Disbursement Gateway"]
    end

    Policyholder -->|"Submits claim via Mobile App"| ClaimsCore
    RepairShop -->|"Uploads repair invoices via Portal"| ClaimsCore
    Adjuster -->|"Reviews complex claims via Workbench"| ClaimsCore
    ClaimsCore <-->|"Verifies policy coverage & deductibles"| PolicyAdmin
    ClaimsCore -->|"Issues claim payouts"| PaymentSystem
```

## 3. C4 Level 2: Container Architecture & Workflow Engine

```mermaid
graph TB
    subgraph ClientChannels ["Intake Channels"]
        MobileApp["Claimant Mobile App (Flutter)"]
        WebPortal["Adjuster Web Portal (React)"]
    end

    subgraph IngressGateway ["API Layer"]
        KongGW["Kong API Gateway"]
        MobileApp --> KongGW
        WebPortal --> KongGW
    end

    subgraph ClaimsProcessingEKS ["Claims Processing Cluster (AWS EKS)"]
        FNOLSvc["FNOL Intake Service<br/>[Container: Go]"]
        DocAI["Document Intelligence Service<br/>[Container: Python / Tesseract / LayoutLM]"]
        FraudSvc["Fraud Detection ML Service<br/>[Container: Python / XGBoost]"]
        WorkflowSvc["Claims Orchestration Service<br/>[Container: Java / Temporal Workflow Engine]"]
        SettlementSvc["Disbursement Service<br/>[Container: Node.js]"]

        KongGW --> FNOLSvc
        FNOLSvc --> WorkflowSvc
        WorkflowSvc --> DocAI
        WorkflowSvc --> FraudSvc
        WorkflowSvc --> SettlementSvc
    end

    subgraph StorageTier ["Data & Object Persistence"]
        DocStore[("Claim Attachments Store<br/>[AWS S3 Bucket - AES-256]")]
        ClaimsDB[("Claims Relational Store<br/>[PostgreSQL Aurora]")]
        FraudGraph[("Entity Resolution Knowledge Graph<br/>[Neo4j Database]")]

        DocAI --> DocStore
        WorkflowSvc --> ClaimsDB
        FraudSvc --> FraudGraph
    end
```

## 4. End-to-End FNOL to Settlement Sequence

```mermaid
sequenceDiagram
    autonumber
    actor Claimant as Policyholder
    participant App as Mobile App
    participant FNOL as FNOL Intake Service
    participant DocAI as Document AI Service
    participant Fraud as Fraud Scoring Engine
    participant Temporal as Temporal Workflow Engine
    participant Adjuster as Adjuster Portal
    participant Pay as Payout Gateway

    Claimant->>App: Submit Claim (Damage Photos, Police Report)
    App->>FNOL: POST /claims/fnol
    FNOL->>Temporal: Start Workflow: ClaimProcessingWorkflow
    FNOL-->>Claimant: Claim Registered (#CLM-2918)

    Temporal->>DocAI: Extract Repair Estimate & Validate Documents
    DocAI-->>Temporal: Extracted Amount: $1,850.00
    
    Temporal->>Fraud: Evaluate Fraud Score (Claimant, Estimate, Graph)
    Fraud-->>Temporal: Fraud Risk Score: 12 (LOW RISK)

    alt Claim Eligible for Straight-Through Processing (STP)
        Note over Temporal: Amount < $2,500 AND Fraud Score < 20
        Temporal->>Pay: Issue Direct Deposit Settlement ($1,850.00)
        Pay-->>Temporal: Payout Success
    else High Value or Elevated Fraud Score
        Temporal->>Adjuster: Assign Claim to Adjuster Task Queue
        Adjuster->>Temporal: Adjuster Reviews & Approves Claim
        Temporal->>Pay: Issue Approved Settlement
    end

    Temporal-->>Claimant: Send Notification (Claim Settled)
```

## 5. Architectural Decisions
* **Temporal Workflow Orchestration**: Claims lifecycles span hours to weeks; Temporal provides durable execution, automated timers, and guaranteed state recovery across system restarts.
* **Graph Database for Fraud Detection**: Neo4j maps relationships between claimants, body shops, attorneys, and doctors to uncover organized claims fraud rings.
