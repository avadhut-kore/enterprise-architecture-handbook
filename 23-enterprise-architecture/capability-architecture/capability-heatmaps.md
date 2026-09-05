# Capability Heatmaps

Capability heatmaps are the primary visual communication tool used by Enterprise Architects to present portfolio health, strategic priorities, and investment decisions to the C-suite.

---

## 1. Types of Capability Heatmaps

```mermaid
quadrantChart
    title Capability Investment Matrix: Strategic Importance vs Technical Health
    x-axis "Low Technical Health (Fragile / Legacy)" --> "High Technical Health (Modern / Cloud)"
    y-axis "Commodity Capability" --> "Strategic Core Differentiator"
    quadrant-1 "Protect & Exploit<br/>(Core strengths, modern platforms)"
    quadrant-2 "High-Priority Modernization<br/>(Critical to strategy, severe tech risk)"
    quadrant-3 "Eliminate / Outsource<br/>(Commodity function on legacy debt)"
    quadrant-4 "Tolerate / Maintain<br/>(Commodity function, stable system)"
    "Real-Time Fraud Detection": [0.25, 0.90]
    "Customer KYC & Onboarding": [0.30, 0.85]
    "Mobile Trading Engine": [0.80, 0.92]
    "General Ledger": [0.75, 0.30]
    "Internal Expense Approval": [0.20, 0.15]
    "Email Campaign Dispatch": [0.85, 0.25]
```

---

## 2. The 3 Standard Enterprise Heatmap Overlays

1. **Strategic Investment Heatmap**:
   * *Red*: Capability marked for immediate capital investment and transformation.
   * *Yellow*: Capability marked for sustaining maintenance / minor upgrades.
   * *Gray*: Capability marked for cost containment, outsourcing, or retirement.
2. **Technical Health / Risk Heatmap**:
   * Visualizes underlying software age, CVE vulnerabilities, unsupported runtimes, and lack of DR.
3. **Capability Duplication Heatmap**:
   * Highlights capabilities supported by multiple competing applications across business units (e.g., 5 different CRM systems across 4 regions).
