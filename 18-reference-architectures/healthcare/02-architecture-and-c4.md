# C4 Architecture Model & Cloud Mapping: Healthcare Platform

## 1. C4 Level 1: System Context Diagram

```mermaid
C4Context
title System Context: Healthcare Interoperability Platform
Person(patient, "Patient", "Views records on SMART on FHIR Mobile App")
Person(doctor, "Physician", "Reviews longitudinal chart in Clinical Portal")
System(health_plat, "Healthcare Interoperability Platform", "FHIR R4 CDR, EMPI, and HL7 Integration Engine")
System_Ext(ehr, "Hospital EHR (Epic / Cerner)", "System of Record for hospital inpatient admissions")
System_Ext(lis, "Laboratory Information System", "Instruments generating blood test lab observations")
System_Ext(pacs, "PACS Imaging Archive", "Stores CT/MRI DICOM binary imaging files")

Rel(patient, health_plat, "Consents and reads health records", "SMART on FHIR / HTTPS")
Rel(doctor, health_plat, "Views integrated chart", "HTTPS")
Rel(ehr, health_plat, "Transmits patient ADT feeds", "MLLP / TCP")
Rel(lis, health_plat, "Transmits lab results (ORU_R01)", "MLLP / TCP")
Rel(health_plat, pacs, "Queries medical imaging metadata", "DICOMweb WADO-RS")
```

---

## 2. Technology-Neutral to Cloud Provider Mapping

| Component | Technology-Neutral | AWS Implementation | Azure Implementation | GCP Implementation |
| :--- | :--- | :--- | :--- | :--- |
| **FHIR Server (CDR)** | HAPI FHIR / Microsoft FHIR| AWS HealthLake | Azure Health Data Services | Google Cloud Healthcare API |
| **HL7 v2 Integration Engine**| Mirth Connect / NextGen | Amazon EKS Container Pods | Azure Kubernetes Service | GKE Container Pods |
| **Patient Identity Store**| Relational / Graph | Amazon Aurora PostgreSQL | Azure Database for PostgreSQL | Cloud SQL for PostgreSQL |
| **Object & DICOM Storage**| S3 / Medical Imaging | AWS HealthImaging / S3 | Azure Blob Storage | Cloud Healthcare DICOM API |
