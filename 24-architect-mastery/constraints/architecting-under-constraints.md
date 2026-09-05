# Architecting Under Constraints

A greenfield project with infinite budget, zero legacy systems, and unlimited time does not exist in enterprise architecture. Great architects thrive when boundaries are tight.

## 1. The Theory of Constraints in Architecture

According to the Theory of Constraints (Goldratt), any system has at least one limiting factor that caps its throughput. Improving non-bottlenecks creates illusionary progress.

```
Identify Bottleneck -> Exploit Bottleneck -> Subordinate System -> Elevate Bottleneck -> Repeat
```

## 2. Classifying Enterprise Constraints

```
┌─────────────────────────────────────────────────────────────┐
│                      HARD CONSTRAINTS                       │
│  (Non-negotiable: Physics, Law, Zero-Tolerance Compliance)   │
├──────────────────────────────┬──────────────────────────────┤
│ Physics & Hardware           │ Regulatory & Legal           │
│ - Speed of light (Latency)   │ - GDPR / HIPAA / PCI-DSS     │
│ - CPU thermal throttling     │ - Data residency borders     │
│ - Memory bandwidth limits    │ - Audit retention mandates   │
└──────────────────────────────┴──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                      SOFT CONSTRAINTS                       │
│     (Negotiable with Cost, Time, or Political Capital)       │
├──────────────────────────────┬──────────────────────────────┤
│ Organizational / Team        │ Financial & Operational      │
│ - Existing engineer skills   │ - Fixed cloud budget caps    │
│ - Team structure (Conway)    │ - Licensing renewals         │
│ - Departmental silos         │ - Third-party API quotas     │
└──────────────────────────────┴──────────────────────────────┘
```

## 3. Strategies for Operating in Constrained Environments

### 1. The Bounded Sandbox Strategy
When constrained by legacy mainframe locks or slow corporate release cycles, isolate the core using Anti-Corruption Layers (ACL) and Strangler Fig patterns. Allow high-velocity innovation to occur in satellite microservices while protecting the constrained core.

### 2. The Creative Degradation Pattern
When constrained by external API rate limits or downstream partner SLA failures, design graceful fallback states (cached responses, queued write-behind buffers, degraded UI view).

## Related Modules
- [Legacy Modernization Patterns](../../15-modernization/README.md)
- [Master Trade-offs Library](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/trade-offs/master-trade-offs-library.md)
