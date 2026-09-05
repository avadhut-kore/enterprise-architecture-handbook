# Mermaid Mindmaps & Architectural Brainstorming

Mindmaps assist architects in brainstorming domain capabilities, organizing non-functional requirements (NFRs), and structuring system decomposition.

## Non-Functional Requirements (NFR) Architecture Taxonomy

```mermaid
mindmap
  root((System NFRs))
    Reliability
      High Availability (99.99%)
      Multi-Region DR
      Automated Failover
    Scalability
      10k TPS Peak
      Auto-scaling EKS
      Read Replica Caching
    Security
      Zero Trust (mTLS)
      FIDO2 MFA
      Envelope Encryption (KMS)
    Observability
      OpenTelemetry Tracing
      Structured JSON Logging
      SLO / Error Budgets
```

## Architectural Guidelines
* Indentation dictates hierarchy; use root nodes to center high-level architecture brainstorming.
