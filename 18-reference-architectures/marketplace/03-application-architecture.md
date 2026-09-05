# Application Architecture: Marketplace Platform

## 1. Escrow Split-Payment State Machine
Unlike direct e-commerce where merchant and platform are the same legal entity, marketplaces must handle **two-sided payment separation**:
1. **Charge Phase**: Customer pays $100. Funds arrive in platform escrow holding account.
2. **Hold Phase**: Order status: `IN_ESCROW`. Funds remain locked while seller fulfills order.
3. **Release Trigger**: Buyer confirms delivery (or 14 days elapse post-shipment with zero disputes).
4. **Split Disbursement**:
   - Platform keeps $15 (15% commission fee posted to platform revenue ledger).
   - Seller receives $85 transferred to their connected bank account via Stripe Connect ACH.
