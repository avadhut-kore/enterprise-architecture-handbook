# Fast Healthcare Interoperability Resources (FHIR) Architecture Library

## 1. Overview
HL7 FHIR (Fast Healthcare Interoperability Resources) is the modern RESTful JSON/XML healthcare standard mandated by the US ONC, European digital health authorities, and major global healthcare networks.

## 2. Directory Structure
- [resources.md](resources.md): Core resource taxonomy across Administrative, Clinical, Financial, and Workflow.
- [resource-model.md](resource-model.md): Extensible resource data modeling and element semantics.
- [profiles.md](profiles.md): FHIR profiling and Implementation Guides (US Core, mCODE).
- [extensions.md](extensions.md): Defining and governing complex enterprise extensions.
- [terminology.md](terminology.md): ValueSet, CodeSystem, and ConceptMap terminologies.
- [rest.md](rest.md): RESTful interaction model: CRUD, Search parameters, Batch, and Transactions.
- [subscriptions.md](subscriptions.md): FHIR R5 event notifications via Webhooks and WebSockets.
- [bulk-data.md](bulk-data.md): Bulk Data Access ($export) architecture and NDJSON pipelines.
- [interoperability.md](interoperability.md): Semantic interoperability and conformance checking.
- [security.md](security.md): SMART on FHIR OAuth 2.0 authorization, PKCE, and consent.
- [consent.md](consent.md): FHIR Consent resources and granular access policy enforcement.
- [identity.md](identity.md): Patient matching and cross-referencing with Identifier systems.
- [mapping.md](mapping.md): Mapping legacy formats (HL7 v2, CDA) to FHIR resources.
- [validation.md](validation.md): StructureDefinition validation engines and JSON Schema verification.
- [versioning.md](versioning.md): Multi-version co-existence (DSTU2 vs STU3 vs R4 vs R5).
- [examples/patient-resource.md](examples/patient-resource.md): Full annotated production FHIR Patient resource.
