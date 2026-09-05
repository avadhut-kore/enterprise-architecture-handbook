# Tenant Context Propagation

## 1. Ambient Context Lifecycle
Once identified at the API gateway, the tenant identity must propagate across asynchronous threads, database connections, and downstream RPCs.

```mermaid
flowchart LR
    Gateway -->|Inject X-Tenant-Id Header| Microservice[Microservice]
    Microservice -->|ThreadLocal / AsyncLocalStorage| Context[TenantContext Object]
    Context -->|SET LOCAL app.current_tenant_id| DB[(Database Session)]
    Context -->|Inject Kafka Record Header| Kafka[Kafka Event]
```
