# Decision Framework: Public Cloud vs Private On-Premises

```yaml
status: approved
decision_type: framework
scope: enterprise-infrastructure
owners: architecture-review-board
review_cadence: annual
```

## 1. Decision Flowchart

```mermaid
graph TD
    Start[Evaluate Infrastructure Requirement] --> Q1{Strict Legal Mandate for On-Soil Physical Vault?}
    Q1 -->|Yes| OnPrem[On-Premises Private Data Center / Colocation]
    Q1 -->|No| Q2{Hardware Utilization Steady-State > 85% at Massive Scale (> 10,000 Cores)?}
    Q2 -->|Yes| OnPrem
    Q2 -->|No| Q3{Requires Rapid Scaling, Global Reach, or Modern Managed PaaS?}
    Q3 -->|Yes| Cloud[Public Cloud Platform: AWS / Azure / GCP]
    Q3 -->|No| Hybrid[Hybrid Topology]
```

---

## 2. Comparative Scoring Scorecard

| Dimension | Weight | Choose Public Cloud | Choose On-Premises |
| :--- | :---: | :--- | :--- |
| **Traffic Elasticity** | 25% | Highly volatile, viral, or seasonal traffic bursts. | Flat, completely predictable 24/7 compute consumption. |
| **Time to Market** | 20% | Greenfield products requiring instant API provisioning. | Mature, low-change systems with annual release cadences. |
| **Capital Allocation** | 15% | OpEx model (Pay as you consume from cash flow). | CapEx-friendly balance sheet for multi-million dollar hardware. |
| **Operational Staffing**| 15% | Lean software teams without physical datacenter sysadmins. | In-house 24/7 hardware, SAN storage, and networking staff. |
| **Egress Volume** | 15% | Modest data transfer out. | Petabytes of continuous unmetered outbound network traffic. |
| **Compliance** | 10% | Standard SOC2, ISO, PCI-DSS certifications sufficient. | Sovereign air-gapped defense enclaves. |
