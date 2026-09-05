# SAP FI/CO Integration and Universal Journal (ACDOCA)

## 1. Architectural Architecture of ACDOCA
In SAP S/4HANA, the Universal Journal (`ACDOCA`) table represents the single source of truth for financial accounting (FI) and managerial controlling (CO).

## 2. Integration Guidelines
- Operational sub-ledgers (billing engines, card processors) must post summarized journal entries rather than raw micro-transactions to protect database sizing and reporting performance.
- Direct database writes to `ACDOCA` are strictly prohibited; all postings must pass through standard SAP Accounting BAPIs (`BAPI_ACC_DOCUMENT_POST`) to guarantee balanced debits and credits, tax calculation, and document numbering.
