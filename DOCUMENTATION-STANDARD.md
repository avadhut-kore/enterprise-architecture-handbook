# Enterprise Architecture Documentation Standard

This document establishes the universal authoring, structural, and quality standards for all technical documentation, architecture designs, and pattern write-ups created in this repository.

---

## 1. Documentation Philosophy

To guarantee that this repository serves as a world-class engineering reference rather than a superficial definition catalog:

> **The 9 Mandatory Inquiries for Every Technical Document:**
> 1. **What problem does this solve?** (Root business and technical drivers)
> 2. **When should you use it?** (Precise fit indicators and criteria)
> 3. **When should you NOT use it?** (Anti-patterns, boundary limits, disqualifiers)
> 4. **What alternatives exist?** (Direct technology and architectural competitors)
> 5. **What are the trade-offs?** (Explicit penalties: latency, cost, complexity)
> 6. **What can fail?** (Production failure modes, split-brains, network partitions)
> 7. **What does production operation look like?** (Day-2 telemetry, runbooks, maintenance)
> 8. **What does it cost?** (FinOps, licensing, human cognitive overhead)
> 9. **How does it scale and secure?** (Horizontal ceilings, bottlenecks, Zero Trust posture)

---

## 2. Standard Document Schema

All technical architecture documents must draw from the standardized 19-point schema below. **Authors should selectively include only the sections relevant to the document's specific scope**, while preserving the relative ordering:

```text
┌─────────────────────────────────────────────────────────────┐
│             STANDARD ARCHITECTURE DOCUMENT SCHEMA           │
├─────────────────────────────────────────────────────────────┤
│  1. Document Metadata & Header Block                        │
│  2. Purpose                                                 │
│  3. Problem Statement                                       │
│  4. Context & Background                                    │
│  5. Functional Requirements (FRs)                           │
│  6. Non-Functional Requirements (NFRs)                      │
│  7. Constraints (Regulatory, Technical, Budget)             │
│  8. Candidate Options & Alternatives                        │
│  9. Decision & Rationale (ADR Link)                         │
│ 10. Architecture Blueprint & C4 Diagrams                    │
│ 11. Implementation Details & Contract Schemas               │
│ 12. Security & Zero Trust Architecture                      │
│ 13. Performance & Latency Budgets                           │
│ 14. Scalability & Capacity Limits                           │
│ 15. Observability & Telemetry (Logs, Metrics, Traces)       │
│ 16. Failure Scenarios & Resiliency Mechanics                │
│ 17. Cost Modeling & FinOps                                  │
│ 18. Trade-off Matrix (Gains vs. Sacrifices)                 │
│ 19. Operational Considerations & Day-2 Runbooks             │
│ 20. References & Prior Art                                  │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Detailed Section Guidelines

### 1. Document Metadata Header
Every document must start with a standardized header comment or block:
```markdown
# [Document Title]

> **Domain**: [e.g., 07-integration / 13-architecture-patterns]  
> **Status**: [Draft | In-Review | Approved | Deprecated]  
> **Last Updated**: [YYYY-MM-DD]  
> **Author**: [Role / Name]  
> **Target Audience**: [Solution Architects, Platform Engineers, Developers]
```

### 2. Purpose & Problem
* Clearly state what the document accomplishes.
* Articulate the precise pain point or systemic deficiency that this document addresses.

### 3. Context & Background
* Detail existing system state, organizational structure, traffic patterns, or legacy debt.

### 4. Requirements & NFRs
* List functional boundaries.
* Quantify NFRs numerically: Latency (p95/p99 in ms), Throughput (RPS), Availability (nines), RPO/RTO.

### 5. Constraints
* Outline immovable boundaries (budget caps, cloud provider mandates, compliance regimes).

### 6. Options & Decision
* Present at least 2 distinct approaches evaluated.
* Detail the chosen path and link to the corresponding ADR.

### 7. Architecture Blueprint
* Visual model using Mermaid diagrams (C4 Context, Container, Component, or Sequence).
* Detail component interactions, communication protocols, and boundary interfaces.

### 8. Implementation & Schemas
* Include concrete code snippets, configuration blocks, or interface definitions (OpenAPI, Protobuf, SQL schema, Terraform).

### 9. Security & Compliance
* Threat model analysis (STRIDE), authentication (OAuth2/OIDC), authorization (RBAC/ABAC), data protection at rest and in transit.

### 10. Performance & Scalability
* Benchmark data, caching strategies, horizontal sharding keys, bottlenecks.

### 11. Observability
* Structured JSON logging format, trace context propagation headers, RED metrics (Rate, Errors, Duration), alerting thresholds.

### 12. Failure Scenarios & Resiliency
* What happens when downstream services timeout?
* Circuit breaker configurations, retry backoff with jitter, dead letter handling, data reconciliation.

### 13. Cost Modeling (FinOps)
* Resource cost estimates per million transactions, storage lifecycle policies, licensing overhead.

### 14. Trade-off Matrix
* A structured comparison table explicitly documenting what is gained versus what is sacrificed.

### 15. Operational Considerations
* Deployment strategy (Canary, Blue/Green), backup verification, rollback procedure, on-call alert triage.

### 16. References
* Links to whitepapers, RFCs, official specifications, and internal ADRs.

---

## 4. Markdown & Styling Rules

1. **GitHub-Flavored Markdown (GFM)**: All documentation must render natively on GitHub and markdown preview tools.
2. **Mermaid for Visual Architecture**:
   * Use native ````mermaid```` code blocks.
   * Prefer `flowchart TD` or `flowchart LR` for system topologies.
   * Prefer `sequenceDiagram` for distributed request flows.
   * Prefer `stateDiagram-v2` for state lifecycles.
3. **Fenced Code Blocks**: Always specify the exact syntax highlighting language (`csharp`, `java`, `python`, `typescript`, `sql`, `json`, `yaml`, `bash`).
4. **File Naming Standard**:
   * Lowercase `kebab-case` for general documents (e.g., `distributed-caching-guide.md`).
   * Uppercase `KEBAB-CASE` for primary templates and root policies (e.g., `ADR-TEMPLATE.md`, `ARCHITECTURE-PRINCIPLES.md`).
5. **No Proprietary Formats**: Never commit binary Word documents (`.docx`), PowerPoint (`.pptx`), or Visio (`.vsdx`) for core technical architecture. Everything is versioned plain-text Markdown.
