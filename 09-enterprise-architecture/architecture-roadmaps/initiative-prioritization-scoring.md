# Initiative Prioritization Scoring Model

A configurable multi-dimensional algorithm to rank enterprise transformation programs during annual planning.

---

## 1. The Prioritization Formula

$$\text{Initiative Priority Score} = \frac{(\text{Strategic Value} \times 0.35) + (\text{Risk Reduction} \times 0.30) + (\text{Urgency} \times 0.20)}{(\text{Capital Capex} \times 0.15) + (\text{Dependency Complexity} \times 0.20)}$$

---

## 2. Annual Initiative Ranking Sample

| Initiative Name | Strategic Value (0.35) | Risk Reduction (0.30) | Urgency (0.20) | Cost / Complexity Penalty | Priority Score | Allocation Decision |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Enterprise Identity & Zero Trust** | 9.0 | 9.8 | 9.5 | 4.2 | **9.24** | **Funded (P0)** |
| **Cloud-Native Payment Engine** | 9.5 | 8.5 | 9.0 | 5.8 | **8.86** | **Funded (P0)** |
| **Global Customer MDM Hub** | 8.5 | 7.5 | 8.0 | 5.0 | **7.92** | **Funded (P1)** |
| **Internal Portal UI Redesign** | 4.0 | 1.5 | 3.0 | 2.5 | **3.40** | **Deferred** |
