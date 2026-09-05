# DATA-FIN-001: Double-Entry Financial Ledger Data Design

---
**Metadata**:
* **Document ID**: DATA-FIN-001
* **Title**: Double-Entry Financial Ledger Data Design
* **Version**: 1.0.0
* **Status**: Approved
* **Engine**: PostgreSQL 16 (Serializable Isolation)
---

## 1. Double-Entry Schema DDL
```sql
CREATE TABLE accounts (
    account_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    currency VARCHAR(3) NOT NULL,
    account_type VARCHAR(32) NOT NULL, -- ASSET, LIABILITY, EQUITY, REVENUE, EXPENSE
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE journal_entries (
    journal_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    reference_id VARCHAR(64) NOT NULL UNIQUE,
    posted_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    description TEXT NOT NULL
);

CREATE TABLE ledger_lines (
    line_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    journal_id UUID NOT NULL REFERENCES journal_entries(journal_id),
    account_id UUID NOT NULL REFERENCES accounts(account_id),
    amount NUMERIC(18, 4) NOT NULL,
    direction VARCHAR(6) NOT NULL CHECK (direction IN ('DEBIT', 'CREDIT')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_ledger_lines_account ON ledger_lines(account_id, created_at);
```

## 2. Transaction Integrity Rule
All entries into `ledger_lines` must occur in a single atomic transaction where:
`SUM(CASE WHEN direction = 'DEBIT' THEN amount ELSE -amount END) = 0.00`.
