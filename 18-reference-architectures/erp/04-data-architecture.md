# Data Architecture: Universal Accounting Journal

## 1. The Single Source of Truth (`ACDOCA` Model)
Traditional ERPs split financial data into separate tables for General Ledger, Asset Accounting, Controlling, and Material Ledger. The modern architecture consolidates all line items into a single **Universal Journal Table**:
- Every record carries: `ledger_id`, `company_code`, `fiscal_year`, `document_number`, `posting_date`, `account_id`, `cost_center`, `amount_currency`, and `debit_credit_indicator`.
- Immutability: Journal entries **cannot be updated or deleted**; corrections require explicit reversing credit/debit adjustment documents.
