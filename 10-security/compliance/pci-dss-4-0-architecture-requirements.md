# PCI-DSS 4.0 Architecture & CDE Scope Reduction

## Executive Summary

The primary architectural goal in PCI-DSS compliance is **minimizing the Cardholder Data Environment (CDE) scope**. 

---

## 1. Scope Reduction via Tokenization

```mermaid
flowchart LR
    Customer["Customer Browser"] --> HostedFields["Payment Gateway Hosted Fields (Stripe/Adyen)"]
    HostedFields -->|Direct Tokenization| PaymentProcessor["Third-Party Payment Processor"]
    PaymentProcessor -->>HostedFields: Returns Nonce / Token
    HostedFields -->|Submits Nonce| EnterpriseBackend["Enterprise Application Server"]
    EnterpriseBackend --> DB[("Enterprise Database")]
```
- **Architectural Result**: Cardholder credit card numbers **never touch enterprise servers, memory, logs, or databases**. Enterprise PCI scope is reduced from full SAQ D (300+ controls) to SAQ A (minimal controls).
