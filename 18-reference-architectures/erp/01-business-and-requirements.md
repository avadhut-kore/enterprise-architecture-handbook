# Business Architecture & Requirements: Enterprise ERP

## 1. Business Context & Multi-Entity Operations
- **Universal Journal Accounting**: Every operational transaction (goods receipt, invoice payment, depreciation) must generate balancing double-entry accounting documents.
- **Global Multi-Entity Consolidation**: Supports 500 legal subsidiaries operating in 60 countries across 100 currencies with automated intercompany eliminations.

---

## 2. Scale Model & Capacity Assumptions

| Scale Parameter | Mid-Market Enterprise | Global Fortune 500 |
| :--- | :--- | :--- |
| **Legal Subsidiaries** | 25 entities | 500 entities |
| **Annual General Ledger Postings** | 5 Million entries | 100 Million entries |
| **Active Vendors & Customers** | 50,000 records | 2,000,000 records |
| **Daily Procurement Invoices** | 10,000 invoices/day | 250,000 invoices/day |
| **Peak Journal Posting TPS** | 100 TPS | 2,500 TPS |
