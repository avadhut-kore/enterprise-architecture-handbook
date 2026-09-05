# Asynchronous Event API & CloudEvents Standards

## 1. CloudEvents 1.0 Compliance
All domain events published to brokers (Kafka, EventBridge) must conform to CloudEvents JSON schema:
```json
{
  "specversion": "1.0",
  "id": "A234-1234-1234",
  "source": "https://orders.enterprise.com",
  "type": "com.enterprise.order.created.v1",
  "datacontenttype": "application/json",
  "time": "2026-03-15T17:31:00Z",
  "data": {
    "order_id": "ord-9988",
    "customer_id": "cust-1122"
  }
}
```
