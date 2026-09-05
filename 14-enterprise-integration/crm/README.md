# Customer Relationship Management (CRM) Integration Architecture Library

## 1. Overview
CRM platforms (Salesforce, Microsoft Dynamics 365, HubSpot) manage lead generation, sales opportunities, customer support cases, and marketing journeys. 

Integrating CRM with core enterprise systems requires managing bidirectional customer identity synchronization, near real-time field sync, and strict cloud governor limits.

## 2. Directory Structure
- [crm-integration.md](crm-integration.md): Core architectural principles for CRM integration.
- [customer-360.md](customer-360.md): Aggregating transactional history, orders, and support into Customer 360.
- [master-customer-data.md](master-customer-data.md): Resolving master data conflicts between CRM and ERP.
- [examples/salesforce-erp-sync.md](examples/salesforce-erp-sync.md): Production bidirectional account sync bridge.
- [salesforce/](salesforce/README.md): Dedicated architectural deep-dive into Salesforce enterprise integration.
