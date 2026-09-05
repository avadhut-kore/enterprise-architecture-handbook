# Reference Architecture 07: Healthcare & Clinical Systems Observability

## 1. System Context & Overview
Healthcare IT architectures integrate Electronic Health Records (EHR), picture archiving systems (PACS), and clinical APIs governed by **HIPAA, HITECH, and HL7 FHIR** standards. Observability must provide deep operational tracing across clinical transactions while guaranteeing the absolute masking of **Protected Health Information (PHI)**.

---

## 2. Architecture Diagram

```mermaid
flowchart TD
    subgraph Hospital_Integration ["Clinical Integration Network"]
        EHR["EHR System (Epic / Cerner)"]
        Engine["Clinical Integration Engine (Mirth / HL7 V2)"]
        FHIR_API["FHIR REST Gateway (HAPI FHIR / Azure Health)"]
        
        EHR -->|HL7 MLLP| Engine
        Engine -->|FHIR JSON| FHIR_API
    end

    subgraph PHI_Sanitization ["OpenTelemetry Healthcare Sanitizer"]
        OTel_Health["OTel Collector (HIPAA Compliant)\n- Strips 18 HIPAA PHI Identifiers\n(Patient Names, SSN, MRN, Dates of Birth)\n- Retains Clinical Resource Type (Patient, Observation)\n- Retains Diagnostic Error Codes"]
    end

    FHIR_API --> OTel_Health

    subgraph Clinical_Observability ["Clinical SRE Dashboard"]
        TSDB["Secure Telemetry Platform"]
        OTel_Health --> TSDB
        
        SLO_Engine["Clinical Latency SLO Monitor\n- Emergency Department Triage: P99 < 500ms\n- Lab Result Synchronization Freshness < 60s"]
        TSDB --> SLO_Engine
    end
```

---

## 3. Key Architectural Decisions
1. **The 18 HIPAA Identifier Sanitization**: Collectors enforce automated regex and AST schema checks that strip all 18 HIPAA identifiers (including medical record numbers, postal addresses, and biometric identifiers) prior to log ingestion.
2. **Clinical Protocol Freshness Tracking**: In clinical environments, delayed lab results directly impact patient safety. The observability platform tracks **HL7 Message Delivery Freshness** as a Tier-1 SLI.
3. **BAA Requirements**: All third-party SaaS vendors receiving telemetry must execute a formal **Business Associate Agreement (BAA)** ensuring HIPAA compliance.
