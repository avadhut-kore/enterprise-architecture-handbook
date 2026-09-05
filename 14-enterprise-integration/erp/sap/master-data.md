# SAP Master Data Governance (MDG) and Synchronization

## 1. Centralized Master Data Management
SAP Master Data Governance (MDG) provides domain-specific governance for creating, changing, and distributing master data across enterprise systems.

## 2. Golden Record Architecture
- **Business Partner (BP)**: In S/4HANA, Customers and Vendors are unified under the Business Partner data model (`BUT000`).
- **Change Request Workflow**: Any modification to critical financial or tax fields initiates a multi-stage approval workflow.
- **Outbound Distribution**: Upon approval, MDG publishes change events via the SAP Event Mesh and standard OData endpoints to synchronize downstream CRMs and data warehouses.
