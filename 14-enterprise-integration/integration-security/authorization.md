# Integration Authorization: RBAC, ABAC, and Policy Engines

## 1. Principles of Integration Authorization
Authorization in enterprise integration determines whether an authenticated system actor possesses the requisite entitlements to invoke an operation, publish to a topic, or mutate specific fields within a payload. 

Enterprise architectures must separate **Policy Decision Points (PDP)** from **Policy Enforcement Points (PEP)**:
- **PEP (API Gateway, Message Interceptor)**: Intercepts the request and forwards the authorization query to the PDP.
- **PDP (Open Policy Agent, Keycloak Entitlements)**: Evaluates corporate governance rules against context and returns `ALLOW` or `DENY`.

## 2. Comparative Authorization Models

| Model | Mechanism | Best Suited For | Limitations |
| :--- | :--- | :--- | :--- |
| **RBAC (Role-Based)** | Static roles assigned to service accounts | Basic service-to-service invocation | Role explosion; ignores request payload context |
| **ABAC (Attribute-Based)** | Attributes of actor, resource, action, environment | Regulated data access (GDPR, HIPAA, Basel) | Performance overhead on complex evaluations |
| **ReBAC (Relationship-Based)**| Graph-based tuple relationships (Zanzibar style) | Tenant isolation, partner ecosystem sharing | Complexity in distributed graph synchronization |
| **OPA / Rego Declarative** | Decoupled policy-as-code engines | Universal ingress, Kafka topic authorization | Requires sub-millisecond local daemon caches |

## 3. Production Policy Implementation (OPA / Rego)

```rego
package enterprise.integration.authz

import future.keywords.in

default allow = false

# Allow if client has trusted scope and satisfies fine-grained payload constraints
allow {
    # Verify OAuth2 scope in token
    input.token.claims.scope[_] == "orders:write"
    
    # Verify tenant isolation: Client tenant must match request resource tenant
    input.token.claims.tenant_id == input.resource.tenant_id
    
    # Financial transaction limit check for service accounts
    is_within_transaction_limit
}

is_within_transaction_limit {
    input.action == "CREATE_TRANSFER"
    input.resource.amount <= 1000000  # Max auto-authorized batch: $1,000,000
}

is_within_transaction_limit {
    input.action != "CREATE_TRANSFER"
}
```

## 4. Message Broker (Kafka) Topic-Level Authorization
Kafka integration brokers must enforce granular ACLs based on client TLS Common Name (CN):
```bash
# Allow Payment Orchestrator to WRITE to payment-clearing-topic
kafka-acls.sh --bootstrap-server broker.internal:9092 \
  --add --allow-principal User:CN=payment-orchestrator.internal \
  --operation Write --topic payment-clearing-topic

# Allow Core Banking Connector to READ from payment-clearing-topic
kafka-acls.sh --bootstrap-server broker.internal:9092 \
  --add --allow-principal User:CN=core-banking-bridge.internal \
  --operation Read --group core-banking-cg --topic payment-clearing-topic
```

## 5. Architectural Recommendations
1. Enforce least privilege: Service accounts must never share roles or wildcard permissions (`*`).
2. Audit every denial: Authorization rejections must trigger immediate SIEM alerts for security triage.
