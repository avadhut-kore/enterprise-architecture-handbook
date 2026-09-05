# Clinical Data Repositories (CDR) and Data Models

## 1. The Role of a CDR
A Clinical Data Repository (CDR) consolidates real-time patient observations, medications, diagnoses, and lab results across departmental silos into an enterprise-wide longitudinal patient record.

## 2. Storage Architectures for Clinical Data
- **Relational Stores (PostgreSQL / SQL Server)**: Best for transactional HL7/FHIR persistence with relational integrity.
- **Document / JSON Stores (MongoDB / Couchbase)**: Highly suited for native storage of complex FHIR JSON resource trees.
- **Graph Databases (Neo4j)**: Ideal for modeling deep clinical ontology relationships and disease-symptom-medication pathways.
