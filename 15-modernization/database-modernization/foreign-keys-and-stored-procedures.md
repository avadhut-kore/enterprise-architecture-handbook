# Breaking Foreign Keys, Stored Procedures, and Triggers

## 1. Eliminating Cross-Boundary Foreign Keys
Cross-database foreign keys cannot exist. Move referential integrity enforcement from the database engine into application validation logic:
- Replace direct SQL `JOIN orders o ON o.customer_id = c.id` with asynchronous data hydration or API composition.
- Treat `customer_id` as an opaque identifier validated at the application layer.

---

## 2. Refactoring Stored Procedures
Stored procedures bury business logic inside proprietary SQL dialects (PL/SQL, T-SQL), preventing horizontal scaling and automated unit testing:
1. **Characterization**: Trace inputs and outputs of the stored procedure.
2. **Rewrite in Application Code**: Re-implement calculation logic in modern domain entities.
3. **Feature Flag Switch**: Toggle between stored procedure execution and application logic execution.
