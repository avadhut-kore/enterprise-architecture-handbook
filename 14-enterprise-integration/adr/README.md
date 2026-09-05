# Enterprise Integration Architecture Decision Records (ADRs)

## 1. Overview
This directory contains canonical Architecture Decision Records (ADRs) capturing foundational integration architecture decisions for the enterprise. Each ADR follows the strict enterprise standard defined in [16-architecture-deliverables/01-adr/template.md](../../16-architecture-deliverables/01-adr/template.md).

## 2. ADR Index
- [ADR-0001-adoption-of-kafka-event-backbone.md](ADR-0001-adoption-of-kafka-event-backbone.md): Adoption of Apache Kafka for Enterprise Event-Driven Integration.
- [ADR-0002-rejection-of-2pc-in-favor-of-saga-orchestration.md](ADR-0002-rejection-of-2pc-in-favor-of-saga-orchestration.md): Rejection of Two-Phase Commit (2PC) in Favor of Saga Orchestration.
- [ADR-0003-mandatory-mtls-tls13-for-cross-system-integration.md](ADR-0003-mandatory-mtls-tls13-for-cross-system-integration.md): Mandatory Mutual TLS (mTLS) with TLS 1.3 for Cross-System Integrations.
- [ADR-0004-standardizing-on-iso20022-for-payment-rails.md](ADR-0004-standardizing-on-iso20022-for-payment-rails.md): Standardizing on ISO 20022 XML for Real-Time and Interbank Payment Rails.
- [ADR-0005-cdc-read-replica-cache-for-core-banking.md](ADR-0005-cdc-read-replica-cache-for-core-banking.md): Decoupling Core Banking Balance Queries via CDC and Redis Read Caches.
- [ADR-0006-transactional-outbox-pattern-with-debezium.md](ADR-0006-transactional-outbox-pattern-with-debezium.md): Standardizing on Transactional Outbox Pattern with Debezium for Reliable Event Emission.
- [ADR-0007-adoption-of-hl7-fhir-r4-for-clinical-interop.md](ADR-0007-adoption-of-hl7-fhir-r4-for-clinical-interop.md): Enterprise Adoption of HL7 FHIR R4 for Healthcare and Clinical Interoperability.
- [ADR-0008-sap-clean-core-integration-via-btp-and-odata.md](ADR-0008-sap-clean-core-integration-via-btp-and-odata.md): SAP S/4HANA Clean Core Integration via SAP BTP and OData v4.
- [ADR-0009-tokenization-architecture-for-pci-dss-scope-reduction.md](ADR-0009-tokenization-architecture-for-pci-dss-scope-reduction.md): Third-Party Hosted Tokenization Architecture for PCI-DSS Scope Reduction.
- [ADR-0010-strangler-fig-pattern-for-mainframe-modernization.md](ADR-0010-strangler-fig-pattern-for-mainframe-modernization.md): Strangler Fig Modernization Pattern for Legacy IBM Mainframe Decommissioning.
