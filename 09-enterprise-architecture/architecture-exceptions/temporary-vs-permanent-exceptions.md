# Temporary vs Permanent Architecture Exceptions

Guidelines for categorizing and adjudicating architecture waiver requests.

---

## 1. Temporary Exceptions (Tactical Debt)
* **Definition**: A temporary deviation driven by urgent time-to-market constraints, supply chain shortages, or an ongoing migration plateau.
* **Duration**: 90 to 365 days.
* **Requirements**: Must have an assigned engineering ticket, funded backlog story, and scheduled decommission date.
* **Example**: Permitting an acquired company's legacy MySQL database to run in AWS for 6 months while API strangler-fig migration is executed.

## 2. Permanent Exceptions (Strategic Domain Divergence)
* **Definition**: A structural deviation where the enterprise standard is fundamentally incompatible with specialized domain physics or regulations.
* **Duration**: Multi-year (reviewed bi-annually).
* **Requirements**: Must demonstrate that adopting the standard causes catastrophic business failure or massive performance degradation.
* **Example**: Permitting C++ / FPGA hardware instead of the standard enterprise Java runtime for a sub-microsecond algorithmic market-making trading engine.
