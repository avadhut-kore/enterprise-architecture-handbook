# PCI-DSS Scoping and Scope Reduction Strategies

## 1. Scoping Categories under PCI-DSS v4.0
- **Category 1 (CDE Systems)**: Systems that store, process, or transmit Cardholder Data (CHD) or Sensitive Authentication Data (SAD). Full PCI-DSS controls apply.
- **Category 2 (Connected / Impacting Systems)**: Systems that have network connectivity to the CDE or can impact its security (e.g., jump hosts, Active Directory, DNS, CI/CD pipelines).
- **Category 3 (Out-of-Scope Systems)**: Systems completely isolated from CDE with no network connectivity and no shared credentials or services.

## 2. Scope Reduction Architecture
By implementing client-side hosted fields and point-to-point tokenization, enterprise architectures minimize Category 1 systems to an isolated microservice pod or eliminate Category 1 entirely by outsourcing tokenization to a PCI Level 1 Service Provider.
