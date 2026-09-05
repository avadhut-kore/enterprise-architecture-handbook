# Data Architecture: Customer 360 & Activity Streams

## 1. Polyglot Persistence Model
- **PostgreSQL (System of Engagement Core)**: Stores relational entities (Accounts, Contacts, Opportunities, Quotes, Line Items). Strong ACID compliance prevents pipeline state corruption.
- **Wide-Column Store (DynamoDB / Cassandra)**: Stores append-only customer activity timelines (emails sent, web pages viewed, chat transcripts, phone call recordings). Partition key: `account_id`, Sort key: `timestamp_utc`.
- **Search Cluster (OpenSearch)**: Full-text inverted index powering sub-second global search across millions of customer accounts and notes.

---

## 2. Relational Entity Relationship Schema (DDL Snippet)
```sql
CREATE TABLE accounts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    parent_account_id UUID REFERENCES accounts(id),
    name VARCHAR(255) NOT NULL,
    industry VARCHAR(100),
    annual_revenue NUMERIC(15, 2),
    billing_country VARCHAR(2),
    created_at TIMESTAMPTZ DEFAULT clock_timestamp(),
    updated_at TIMESTAMPTZ DEFAULT clock_timestamp()
);

CREATE TABLE opportunities (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    account_id UUID NOT NULL REFERENCES accounts(id),
    name VARCHAR(255) NOT NULL,
    stage VARCHAR(50) NOT NULL, -- DISCOVERY, PROPOSAL, CLOSED_WON
    amount NUMERIC(15, 2) NOT NULL,
    close_date DATE NOT NULL,
    owner_user_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT clock_timestamp()
);
```
