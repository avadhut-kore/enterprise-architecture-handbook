# LLD Module & Domain Layer Specification

## 1. Domain Invariants & Business Rules
* **Invariant 1**: An order cannot be placed with zero line items.
* **Invariant 2**: Price calculations must use arbitrary-precision decimals (`BigDecimal`), never IEEE floating point.
* **Invariant 3**: State transitions must strictly follow the state machine:
  `DRAFT` $ightarrow$ `PENDING_PAYMENT` $ightarrow$ `PAID` $ightarrow$ `FULFILLED` / `CANCELLED`.
