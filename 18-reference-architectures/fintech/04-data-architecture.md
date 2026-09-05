# Data Architecture: Double-Entry Immutable Ledger

## 1. Immutable Ledger Relational Schema (DDL Snippet)
```sql
CREATE TABLE accounts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    account_number VARCHAR(34) UNIQUE NOT NULL,
    currency VARCHAR(3) NOT NULL,
    type VARCHAR(50) NOT NULL, -- ASSET, LIABILITY, EQUITY, REVENUE, EXPENSE
    created_at TIMESTAMPTZ DEFAULT clock_timestamp()
);

CREATE TABLE journal_entries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    transaction_reference VARCHAR(100) UNIQUE NOT NULL, -- Idempotency Key
    description TEXT NOT NULL,
    posted_at TIMESTAMPTZ DEFAULT clock_timestamp()
);

CREATE TABLE ledger_lines (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entry_id UUID NOT NULL REFERENCES journal_entries(id),
    account_id UUID NOT NULL REFERENCES accounts(id),
    amount NUMERIC(18, 4) NOT NULL, -- Positive for Debit, Negative for Credit
    CHECK (amount <> 0)
);

-- INVARIANT: sum(amount) for a given entry_id MUST equal 0.0000
```
