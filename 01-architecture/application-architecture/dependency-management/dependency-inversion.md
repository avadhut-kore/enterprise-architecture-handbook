# Dependency Inversion Principle (DIP)

## 1. The Two Tenets of DIP

Robert C. Martin formulated the Dependency Inversion Principle as:
1. *High-level modules should not depend on low-level modules. Both should depend on abstractions.*
2. *Abstractions should not depend on details. Details should depend on abstractions.*

---

## 2. Architectural Consequences

- **High-Level Module**: Contains core business rules (e.g., `LoanApprovalEngine`). It defines the enterprise policy and should be the most stable, reusable part of the system.
- **Low-Level Module**: Contains infrastructural mechanisms (e.g., `PostgresLoanRepository`, `SendGridNotificationClient`).
- **The Value of Inversion**: High-level business policies become independent of infrastructural changes, database migrations, and cloud vendor swaps.
