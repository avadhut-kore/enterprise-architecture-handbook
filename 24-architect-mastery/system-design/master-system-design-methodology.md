# Master System Design Methodology: The 18-Step Framework

This 18-step framework provides a structured, comprehensive approach to designing distributed systems, whether for executive design reviews, customer architecture workshops, or Principal Architect interviews.

```
[1. Requirements & Scope Clarification]
                 │
                 ▼
[2. Non-Functional Requirements & SLOs]
                 │
                 ▼
[3. Scale & Capacity Estimation (Traffic, Storage, Memory, Bandwidth)]
                 │
                 ▼
[4. Data Model & Schema Design]
                 │
                 ▼
[5. API & Contract Design (gRPC, REST, GraphQL)]
                 │
                 ▼
[6. High-Level Architecture Block Diagram]
                 │
                 ▼
[7. Deep-Dive: Core Workflows & Data Flows]
                 │
                 ▼
[8. Data Storage Strategy (SQL vs NoSQL vs Search vs Cache)]
                 │
                 ▼
[9. Caching Strategy & Invalidation Policies]
                 │
                 ▼
[10. Asynchronous Processing & Messaging Topology]
                 │
                 ▼
[11. Scalability & Partitioning Strategy (Sharding, Consistent Hashing)]
                 │
                 ▼
[12. High Availability, Replication & Consistency Semantics]
                 │
                 ▼
[13. Fault Tolerance, Circuit Breaking & Resilience]
                 │
                 ▼
[14. Security, Zero Trust & Compliance Architecture]
                 │
                 ▼
[15. Observability, Telemetry & SRE Metrics]
                 │
                 ▼
[16. Cloud Economics & Unit Cost Modeling]
                 │
                 ▼
[17. Failure Mode Analysis & Red-Teaming]
                 │
                 ▼
[18. Target State Roadmap & Evolutionary Milestones]
```

## Step Details and Architectural Rules
- **Never jump to technology**: Always clarify read/write ratios, peak multipliers, and consistency requirements before mentioning Kafka, Postgres, or Kubernetes.
- **Quantify every constraint**: Convert abstract requirements like "fast" into quantifiable numbers: "p99 read latency < 25ms at 50,000 QPS."

## Related Modules
- [Question Frameworks](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/question-frameworks/architecture-question-frameworks.md)
- [Interview System Design Library](../../20-interview-system-design/README.md)
