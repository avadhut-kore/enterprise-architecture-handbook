# Data Minimization and Redaction in Integration Pipelines

## 1. Principles of Integration Data Minimization
Under privacy regulations (GDPR Art. 5c, CCPA, HIPAA), enterprise integration architectures must implement **data minimization at the boundary**:
1. Only extract, transport, and store the minimal set of attributes strictly necessary to fulfill the immediate integration workflow.
2. Filter out unnecessary fields at the producer or edge connector before transmitting payloads across the enterprise network.

## 2. Field Redaction Pipeline Pattern

```
Incoming Customer Payload:
{
  "order_id": "ORD-9912",
  "total_amount": 149.50,
  "customer": {
    "name": "Jane Doe",
    "ssn": "999-12-3456",            <-- STRIP AT INGRESS
    "medical_history": "Asthma",     <-- STRIP AT INGRESS
    "shipping_zip": "10001"
  }
}

Forwarded to Logistics Service:
{
  "order_id": "ORD-9912",
  "shipping_zip": "10001"
}
```

## 3. Automated Masking Patterns
- **Full Masking**: Replace sensitive fields with `***REDACTED***`.
- **Partial Masking**: Mask all but the last 4 digits (e.g., `****-****-****-1234`).
- **Hashing**: Transform identifier via salted SHA-256 for analytical correlation without revealing raw identity.
