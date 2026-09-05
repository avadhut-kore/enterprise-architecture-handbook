# Data Domains & Enterprise Ownership

Defining enterprise data domain boundaries and assigning strict executive stewardship.

---

## 1. The Enterprise Data Domain Hierarchy

```mermaid
classDiagram
    class CustomerDomain {
        +CustomerID
        +LegalName
        +TaxID
        +PrimaryAddress
        +ContactPhone
        +KYCStatus
    }
    class AccountDomain {
        +AccountID
        +CustomerID_FK
        +LedgerBalance
        +CurrencyCode
        +AccountStatus
    }
    class TransactionDomain {
        +TransactionID
        +AccountID_FK
        +Amount
        +Timestamp
        +Counterparty
    }
    CustomerDomain "1" --> "many" AccountDomain : owns
    AccountDomain "1" --> "many" TransactionDomain : records
```

---

## 2. Data Stewardship Responsibilities
Every core enterprise data entity must have:
* **Business Data Owner**: VP or Director who decides access rights, data definitions, and retention lifecycles.
* **Data Steward**: Operational lead responsible for resolving data quality anomalies, deduplication rules, and schema definitions.
* **Data Custodian (Technical Architect)**: Engineering owner of the database clusters, backup integrity, encryption keys, and DR failover.
