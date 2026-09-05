# Data Architecture: Marketplace Platform

## 1. Multi-Sided Relational Schema (DDL Snippet)
```sql
CREATE TABLE sellers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    business_name VARCHAR(255) NOT NULL,
    payout_account_id VARCHAR(100) NOT NULL, -- Stripe Connect Account ID
    commission_rate NUMERIC(4, 2) DEFAULT 0.15, -- 15% Platform Take-Rate
    kyc_status VARCHAR(50) NOT NULL, -- PENDING, VERIFIED, SUSPENDED
    created_at TIMESTAMPTZ DEFAULT clock_timestamp()
);

CREATE TABLE marketplace_orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    buyer_id UUID NOT NULL,
    seller_id UUID NOT NULL REFERENCES sellers(id),
    total_charged NUMERIC(10, 2) NOT NULL,
    platform_commission NUMERIC(10, 2) NOT NULL,
    seller_payout_amount NUMERIC(10, 2) NOT NULL,
    escrow_status VARCHAR(50) NOT NULL -- HELD, RELEASED, REFUNDED, DISPUTED
);
```
