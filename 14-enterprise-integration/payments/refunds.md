# Payment Refunds, Partial Refunds, and Voids

## 1. Void vs. Refund
- **Void**: Cancels an `AUTHORIZED` transaction *before* it has been captured or cleared. The authorization hold falls off the customer's card immediately with zero transaction fees.
- **Refund**: Reverses a `CAPTURED` or `SETTLED` payment. Money is transferred from merchant to customer. Acquirer processing fees are typically non-refundable.

## 2. Partial Refund Ledgering
Multiple partial refunds may be executed against a single captured transaction, provided $\sum 	ext{Refunds} \le 	ext{Captured Amount}$.
