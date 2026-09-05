# Reference Architecture 06: Regulated Payment & Financial Observability

## 1. System Context & Overview
Financial transaction systems and payment gateways are governed by stringent regulatory mandates, primarily **PCI-DSS 4.0**, SOC 2 Type II, and SWIFT security frameworks. Observability platforms must maintain complete transactional auditability while guaranteeing that **Zero Cardholder Data (PAN, CVV, PIN)** ever enters telemetry backends.

See visual modeling in [`../../17-diagrams/security/zero-trust.md`](../../17-diagrams/security/zero-trust.md).

---

## 2. Architecture Diagram

```mermaid
flowchart TD
    subgraph Cardholder_Data_Environment ["PCI-DSS CDE (Cardholder Data Environment)"]
        App["Payment Authorization Service"]
        HSM["Hardware Security Module (HSM)"]
        Vault["Tokenization Vault"]
        
        App -->|Tokenize PAN| Vault
        App -->|Cryptographic Sign| HSM
        
        subgraph Zero_PAN_Redactor ["Pre-Ingestion Redaction Engine"]
            Collector["OTel Collector (Local CDE Node)\n- In-Memory Luhn Algorithm Scanner\n- PCI Regex Redaction: 4[0-9]{12}(?:[0-9]{3})? -> [REDACTED_PAN]\n- Strips Authorization Bearer & CVV fields"]
        end
        App --> Collector
    end

    subgraph Non_CDE_Zone ["Non-CDE Corporate Telemetry Platform"]
        Central_TSDB["Secure Metrics & Traces"]
        Audit_Ledger["WORM Compliant Audit Log Store"]
    end

    Collector -->|Sanitized Telemetry (Zero PAN)| Central_TSDB
    Collector -->|Signed Audit Events| Audit_Ledger

    subgraph Reconciliation ["Payment Settlement Reconciliation Engine"]
        Gateway_Logs["Bank Gateway Clearing Files"]
        App_Ledger["Internal Double-Entry Ledger"]
        Recon_Worker["Automated Reconciliation Worker\n- Detects breaks and settlement discrepancies"]
        Gateway_Logs --> Recon_Worker
        App_Ledger --> Recon_Worker
        Recon_Worker --> Central_TSDB
    end
```

---

## 3. Key Architectural Decisions
1. **In-Memory Luhn Redaction**: Collectors run an automated Luhn check on all string values in logs and trace attributes; any 13-19 digit number matching a valid credit card algorithm is automatically masked before leaving the memory buffer.
2. **Settlement Reconciliation Observability**: Financial breaks (differences between authorized transactions and bank settlements) are tracked as high-priority business metrics (`settlement_reconciliation_break_amount_cents`), alerting financial operations teams within minutes.
3. **Immutable WORM Audit Trails**: Audit logs capturing administrative actions are routed to Write-Once-Read-Many (WORM) compliant S3 buckets with object locking to satisfy PCI-DSS audit mandates.
