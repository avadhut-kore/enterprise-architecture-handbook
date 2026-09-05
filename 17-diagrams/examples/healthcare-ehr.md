# Healthcare Electronic Health Records (EHR) & Telemedicine Architecture

This reference architecture models a secure, HIPAA/HITECH-compliant healthcare digital ecosystem connecting Electronic Health Records (EHR), FHIR APIs, video telemedicine consults, and automated clinical data de-identification.

## 1. Business Context & Architectural Drivers
* **Regulatory Mandates**: HIPAA Security and Privacy Rule compliance, HITECH Act, and HL7 FHIR Release 4 interoperability mandates.
* **Latency SLA**: Real-time WebRTC audio/video latency $\le 150$ms for remote clinical examinations.
* **Data Scoping**: Absolute separation between Protected Health Information (PHI) and clinical analytics.

## 2. C4 Level 1: System Context

```mermaid
graph TB
    subgraph Personas ["Healthcare Participants"]
        Patient["Patient<br/>[Person]<br/>Books appointments & views lab results"]
        Doctor["Physician / Clinician<br/>[Person]<br/>Conducts telemedicine & writes prescriptions"]
    end

    subgraph HealthcarePlatform ["Digital Health & Telemedicine Platform"]
        SystemCore["Digital Health Engine<br/>- Patient Portal & Appointments<br/>- WebRTC Video Telemedicine<br/>- FHIR Clinical Data Layer<br/>- e-Prescription Dispatcher"]
    end

    subgraph ExternalHealthEcosystem ["External Clinical Ecosystem"]
        HospitalEHR["Hospital Core EHR (Epic / Cerner)<br/>[HL7 v2 / FHIR APIs]"]
        Pharmacy["National Pharmacy Network (Surescripts)<br/>[Electronic Prescribing]"]
        Insurance["Health Insurance Clearinghouse<br/>[EDI 837 / 835 Claims]"]
    end

    Patient -->|"Accesses health records"| SystemCore
    Doctor -->|"Conducts video consults"| SystemCore
    SystemCore <-->|"Syncs clinical charts"| HospitalEHR
    SystemCore -->|"Transmits e-prescriptions"| Pharmacy
    SystemCore -->|"Submits insurance claims"| Insurance
```

## 3. C4 Level 2: Container Architecture & HIPAA Segregation

```mermaid
graph TB
    subgraph PublicInternet ["Untrusted Patient & Clinician Devices"]
        PatientApp["Patient Mobile App (iOS/Android)"]
        DoctorWeb["Clinician EHR Portal (Chrome)"]
    end

    subgraph EdgePerimeter ["HIPAA-Compliant Ingress Layer"]
        WAF["AWS WAF & CloudFront Edge"]
        IngressALB["Application Load Balancer (TLS 1.3 Termination)"]
        PatientApp --> WAF
        DoctorWeb --> WAF
        WAF --> IngressALB
    end

    subgraph HIPAAEnclave ["HIPAA Private Application Enclave (AWS Private Subnet)"]
        AppSvc["Telemedicine Core Service<br/>[Container: Node.js / NestJS]"]
        FHIRServer["HL7 FHIR API Server (HAPI FHIR)<br/>[Container: Java Spring Boot]"]
        SignalingSvc["WebRTC Video Signaling Gateway<br/>[Container: Go]"]
        DeIDPipeline["Clinical De-Identification Pipeline<br/>[Container: Python / spaCy PHI Redactor]"]

        IngressALB --> AppSvc
        IngressALB --> SignalingSvc
        AppSvc --> FHIRServer
        FHIRServer --> DeIDPipeline
    end

    subgraph PersistenceEnclave ["PHI Storage Vault (KMS Envelope Encrypted)"]
        ClinicalDB[("Clinical FHIR Database<br/>[PostgreSQL - Column Encrypted]")]
        AuditDB[("HIPAA Immutable Access Log<br/>[WORM Object Storage]")]
        AnalyticsLake[("De-Identified Research Data Lake<br/>[S3 Parquet / Athena]")]

        FHIRServer --> ClinicalDB
        FHIRServer -.->|"Audit Every Access"| AuditDB
        DeIDPipeline --> AnalyticsLake
    end
```

## 4. Telemedicine Consultation Sequence Flow

```mermaid
sequenceDiagram
    autonumber
    actor Patient as Patient
    actor Doctor as Doctor
    participant Signal as WebRTC Signaling Server
    participant Turn as LiveKit / Twilio Media Server
    participant EHR as FHIR Clinical Server
    participant Audit as HIPAA Audit Store

    Patient->>Signal: Join Video Room (Encrypted Room Token)
    Doctor->>Signal: Join Video Room (Physician Credentials)
    Signal-->>Patient: Exchange SDP Offer & ICE Candidates
    Signal-->>Doctor: Exchange SDP Answer & ICE Candidates
    
    Patient<-->>Turn: Establish Direct Encrypted Media Stream (SRTP/DTLS)
    Doctor<-->>Turn: Establish Direct Encrypted Media Stream (SRTP/DTLS)
    
    Note over Patient,Doctor: Telemedicine Examination Conducted
    
    Doctor->>EHR: POST /fhir/Observation (Vital Signs, Diagnosis)
    Doctor->>EHR: POST /fhir/MedicationRequest (Prescription)
    EHR->>Audit: Record PHI Access (Doctor ID, Patient ID, Timestamp, Action)
    EHR-->>Doctor: 201 Created (Clinical Note Saved)
```

## 5. Security & Privacy Controls
* **Zero Trust PHI Access**: Every database read/write query records the authenticated clinician's National Provider Identifier (NPI) to satisfy HIPAA $\S 164.312$ audit controls.
* **Safe Harbor De-Identification**: Automated pipelines remove all 18 HIPAA identifiers (names, dates, zip codes, record numbers) before replicating data to research lakes.
