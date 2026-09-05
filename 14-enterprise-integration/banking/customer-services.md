# Customer Information File (CIF) and MDM Integration

## 1. The CIF Integration Challenge
In legacy banking, customer information is fragmented across disparate core systems: retail checking has a record, mortgage servicing has another, and commercial loans maintain a third. A unified Customer 360 requires integrating with the master **Customer Information File (CIF)** or Enterprise Master Data Management (MDM) platform.

## 2. Customer Integration Sync Flow
```
[Branch CRM / Salesforce] ──(KYC Completed)──> [API Gateway]
                                                    │
                                                    ▼
                                          [Customer MDM Hub]
                                                    │ (Golden Record Created)
                                                    ▼
                                          [Kafka: customer.events]
                                                    │
                    ┌───────────────────────────────┴───────────────────────────────┐
                    ▼                                                               ▼
        [Core Banking Retail CIF]                                       [Digital Channels DB]
```
