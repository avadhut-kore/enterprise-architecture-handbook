# The Enterprise Application Scorecard

A quantitative evaluation model rating enterprise applications across Business Value, Technical Health, and Operational Risk.

---

## 1. Scoring Dimensions and Weighted Rubric

$$\text{Total Score} = 0.40 \times \text{Business Value} + 0.35 \times \text{Technical Health} - 0.25 \times \text{Enterprise Risk}$$

| Evaluation Dimension | Scoring Factors (1.0 – 5.0) | Weight |
| :--- | :--- | :---: |
| **Business Value (40%)** | Strategic alignment, revenue enablement, user satisfaction, operational necessity. | 0.40 |
| **Technical Health (35%)** | Code maintainability, test automation coverage, modern runtime, API availability, cloud readiness. | 0.35 |
| **Enterprise Risk (25%)** | Unsupported vendor versions, unpatched CVEs, lack of DR/HA, single-person operational dependencies. | 0.25 |

---

## 2. Sample Portfolio Application Scorecard

```text
APPLICATION: APP-082 "Global Policy Underwriting Portal"
├── 1. Business Value Score: 4.2 / 5.0
│   ├── Critical to Commercial Lines ($420M Revenue): 5.0
│   └── User NPS (+42): 3.8
├── 2. Technical Health Score: 2.1 / 5.0
│   ├── .NET Framework 4.6 (Unsupported runtime): 1.5
│   ├── Zero automated integration tests: 1.0
│   └── Highly coupled SQL stored procedures: 2.0
├── 3. Risk Score: 4.5 / 5.0 (High Risk)
│   ├── Database running on Windows Server 2012 (EOL): 5.0
│   └── Single internal developer knows codebase: 4.8
└── DISPOSITION: TIME Category = MIGRATE / RE-ARCHITECT (High Value, High Risk)
```
