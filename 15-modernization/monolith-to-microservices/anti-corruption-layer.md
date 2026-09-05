# Anti-Corruption Layer (ACL) Implementation

## 1. Preserving Domain Autonomy
An Anti-Corruption Layer (ACL) translates between two distinct domain models without allowing concepts from one to contaminate the other.

```
[Modern Orders Microservice] 
  (Speaks Clean Domain Language: OrderStatus.PLACED, CustomerId, Money)
                    │
                    ▼
     [Anti-Corruption Layer (ACL)]
     ├── Inbound Translator: Converts Legacy DB Rows to Clean Domain Entities
     ├── Outbound Translator: Converts Clean Domain Events to Legacy CPYBOOK/SQL
     └── Adapter Sockets: Handles Legacy RPC and Data Padding
                    │
                    ▼
[Legacy Monolith]
  (Speaks Obsolete Model: CUST_STAT_CD_01, TX_AMT_PACKED_COMP3)
```

---

## 2. Production Code Implementation (Java / Spring)
```java
@Component
public class LegacyCustomerAclAdapter implements CustomerLookupPort {
    private final LegacyMonolithClient legacyClient;

    public LegacyCustomerAclAdapter(LegacyMonolithClient legacyClient) {
        this.legacyClient = legacyClient;
    }

    @Override
    public CustomerDomainEntity findCustomer(CustomerId id) {
        LegacyCustomerRecord raw = legacyClient.fetchRecord(id.value());
        
        // Translate legacy codes to modern domain enums
        CustomerStatus status = switch (raw.getStatusCode()) {
            case "01" -> CustomerStatus.ACTIVE;
            case "09" -> CustomerStatus.SUSPENDED;
            default -> CustomerStatus.UNKNOWN;
        };

        return new CustomerDomainEntity(
            id,
            new CustomerName(raw.getFirstName().trim(), raw.getLastName().trim()),
            status
        );
    }
}
```
