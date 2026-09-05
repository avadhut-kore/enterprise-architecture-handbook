# Architecture RACI Matrix

Defines the distribution of responsibilities across architectural roles and business stakeholders.

---

## 1. Enterprise Architecture RACI Chart

* **R (Responsible)**: The role that conducts the work to achieve the deliverable.
* **A (Accountable)**: The single individual with ultimate veto and ownership power.
* **C (Consulted)**: Subject matter experts providing input.
* **I (Informed)**: Stakeholders kept updated on progress and outcomes.

| Architectural Lifecycle Activity | Business Leader | Chief Architect | Enterprise Architect | Solution Architect | Technical Architect | Security / CISO | Product Manager |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Enterprise Business Capability Mapping** | C | I | **A / R** | C | I | I | C |
| **Enterprise Technology Strategy & Standards** | I | **A** | R | C | C | C | I |
| **Application Portfolio Rationalization (TIME)** | C | A | **R** | C | I | I | I |
| **Project Solution Architecture Design (SAD)** | I | I | C | **A / R** | C | C | C |
| **Architecture Review Board (ARB) Evaluation** | I | A | **R** | C | I | C | I |
| **Tier-1 Architecture Exception Approval** | I | **A** | R | C | I | C | I |
| **Component Code Structure & Framework Selection** | I | I | I | C | **A / R** | I | I |
| **Security & Compliance Policy Definition** | I | C | C | C | I | **A / R** | I |
| **Automated Fitness Function Configuration** | I | I | C | C | **A / R** | C | I |
| **M&A Technology Due Diligence** | C | **A** | R | C | I | C | I |
