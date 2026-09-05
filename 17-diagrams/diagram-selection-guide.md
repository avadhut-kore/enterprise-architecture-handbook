# Architecture Diagram Selection Guide

This guide answers the core architectural question: **"Which diagram should I create to communicate this architectural design or decision?"**

---

## 1. Diagram Decision Matrix

| What You Need to Communicate | Primary Stakeholder | Recommended Diagram | Canonical Directory |
| :--- | :--- | :--- | :--- |
| **System boundaries, users, and external partners** | C-Suite, Product Management, ARB | C4 System Context | [`c4/context.md`](./c4/context.md) |
| **High-level building blocks & datastores** | Engineering Leads, Architects | C4 Container | [`c4/container.md`](./c4/container.md) |
| **Internal structural modularity of a service** | Senior Developers, Tech Leads | C4 Component | [`c4/component.md`](./c4/component.md) |
| **Multi-step transaction or protocol workflow** | Backend Engineers, Security Reviewers | Sequence Diagram | [`sequence/README.md`](./sequence/README.md) |
| **Infrastructure hosting, HA, and scaling topology**| DevOps, Platform Engineers, SREs | Deployment Diagram | [`deployment/README.md`](./deployment/README.md) |
| **Subnets, VPCs, firewalls, and traffic ingress** | Cloud Security, Network Engineers | Network Diagram | [`network/README.md`](./network/README.md) |
| **Trust boundaries, encryption, and authentication**| CISO, Security Engineers, Auditors | Security Architecture | [`security/README.md`](./security/README.md) |
| **Data ingestion, transformation, and storage** | Data Engineers, Compliance Officers | Data-Flow Diagram | [`data-flow/README.md`](./data-flow/README.md) |
| **Cross-enterprise systems & strategic roadmaps** | Enterprise Architects, CIO | Enterprise Landscape | [`enterprise/README.md`](./enterprise/README.md) |
| **LLM pipelines, RAG ingestion, and agent swarms**| AI/ML Engineers, Product Leads | AI Architecture | [`ai/README.md`](./ai/README.md) |

---

## 2. Interactive Selection Tree

```mermaid
flowchart TD
    Start["What is the primary architectural inquiry?"] --> Scope{"What is the dimension of focus?"}
    
    Scope -->|Who interacts & what are external dependencies?| Q1["Audience: Business & High-Level Tech"]
    Q1 --> D1["Create C4 Context Diagram"]
    
    Scope -->|What are the major applications & datastores?| Q2["Audience: Engineering Leads & Architects"]
    Q2 --> D2["Create C4 Container Diagram"]
    
    Scope -->|How do components interact over time?| Q3["Audience: Developers & Integrators"]
    Q3 --> D3["Create Sequence Diagram (Sync vs Async vs Saga)"]
    
    Scope -->|Where does code execute physically?| Q4["Audience: SREs & Cloud Engineers"]
    Q4 --> D4["Create Deployment Diagram (K8s, Multi-Region, Cloud)"]
    
    Scope -->|How are networks, subnets & IPs routed?| Q5["Audience: Network & Cloud Security"]
    Q5 --> D5["Create Network Diagram (Hub-Spoke, VPC, Ingress)"]
    
    Scope -->|Where are trust boundaries & secrets?| Q6["Audience: Security Reviewers & Auditors"]
    Q6 --> D6["Create Security / Threat Model Diagram"]
    
    Scope -->|How does data ingest, transform & persist?| Q7["Audience: Data & Analytics Teams"]
    Q7 --> D7["Create Data-Flow / Pipeline Diagram"]
    
    Scope -->|How does business strategy map to IT?| Q8["Audience: Enterprise Leadership"]
    Q8 --> D8["Create Enterprise Capability / Portfolio Map"]
```
