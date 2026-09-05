# HL7 v2 Messaging Architecture Library

## 1. Overview
Health Level Seven version 2 (HL7 v2.x) remains the most widely deployed clinical messaging standard in the world, powering point-to-point communication between inpatient hospital bedside monitors, lab analyzers, and EHR engines.

## 2. Directory Structure
- [hl7-v2.md](hl7-v2.md): Core architectural principles of HL7 v2 and MLLP transport.
- [messages.md](messages.md): Message catalog: ADT, ORU, ORM, MDM, SIU.
- [segments.md](segments.md): Anatomy of MSH, PID, PV1, OBR, OBX segments.
- [acknowledgements.md](acknowledgements.md): ACK mechanisms: Original vs. Enhanced acknowledgment modes.
- [interfaces.md](interfaces.md): Interface engines, port allocations, and socket management.
- [message-mapping.md](message-mapping.md): Mapping HL7 v2 pipe-delimited records to JSON/FHIR.
- [transformation.md](transformation.md): Custom Z-segment handling and string transformations.
- [validation.md](validation.md): Conformance testing and message validation rules.
- [error-handling.md](error-handling.md): Reject (AR), Error (AE), and socket disconnect recovery.
- [integration-engines.md](integration-engines.md): Evaluating Mirth Connect, Rhapsody, and Intersystems Ensemble.
- [examples/oru-r01-lab-result.md](examples/oru-r01-lab-result.md): Full annotated production HL7 v2 message.
