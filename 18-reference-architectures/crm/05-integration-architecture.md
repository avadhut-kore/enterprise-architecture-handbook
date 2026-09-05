# Integration Architecture: ERP & Communications Sync

## 1. Bidirectional ERP Synchronization (Clean Core Integration)
- **Outbound (CRM $ightarrow$ ERP)**: When an opportunity shifts to `CLOSED_WON`, the Opportunity Service publishes an `opportunity.closed_won` CloudEvent to Kafka. The ERP adapter consumes the event, creates a Sales Order in SAP S/4HANA via OData v4, and returns the SAP Order ID.
- **Inbound (ERP $ightarrow$ CRM)**: As invoices are paid or goods shipped, SAP publishes events. The CRM consumes them to update the account's historical revenue balance.
- **Data Virtualization**: Historical detailed invoices are *not* duplicated in the CRM database. The CRM UI queries SAP live via an OData v4 external data connector, avoiding massive database storage licensing costs.
