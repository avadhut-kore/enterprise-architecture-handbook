# Resource Modeling & URI Design

## 1. Golden Rules of URI Construction
1. **Nouns, Never Verbs**: URIs represent resources, not remote procedure calls.
   * *Anti-Pattern*: `POST /api/createOrder`, `POST /api/deleteCustomer?id=5`
   * *RESTful*: `POST /v1/orders`, `DELETE /v1/customers/5`
2. **Plural Nouns**: Standardize on plural naming for collections: `/v1/users`, `/v1/accounts`.
3. **Hierarchical Relationships**:
   * Top-level collection: `/v1/users`
   * Individual instance: `/v1/users/42`
   * Sub-resource collection: `/v1/users/42/orders`
   * Sub-resource instance: `/v1/users/42/orders/1099`
4. **Avoid Deep Nesting (>2 Levels)**:
   * *Anti-Pattern*: `/v1/companies/1/departments/4/teams/8/employees/12/tasks/99`
   * *Refactored*: `/v1/employees/12/tasks/99` (flatten into top-level resource with foreign ID).
