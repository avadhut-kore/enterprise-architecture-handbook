# Banking Settlement and Core Reconciliation

## 1. Three-Way Reconciliation Architecture
Banking integrations require continuous reconciliation across three independent sources of truth:
1. **Channel System Log**: What the customer or payment rail initiated.
2. **Core Banking Ledger**: What was officially debited/credited in the internal books.
3. **Central Bank / Clearing House Statement**: What actually settled over the central bank wire.

## 2. Automated Break Resolution Flow
Refer to [reconciliation/reconciliation-architecture.md](../reconciliation/reconciliation-architecture.md).
