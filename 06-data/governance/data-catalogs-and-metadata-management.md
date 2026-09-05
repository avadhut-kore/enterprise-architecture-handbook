# Data Governance: Data Catalogs & Metadata Management Architecture

## 1. Architectural Purpose & Problem Context
Deploying enterprise catalogs (OpenMetadata, DataHub, Collibra): automated crawler discovery, business glossaries, schema indexing, and search.

---

## 2. Governance Operating Model

```mermaid
flowchart TD
    Steering[Executive Data Governance Board] --> CDO[Chief Data Officer CDO]
    CDO --> Owners[Domain Data Owners]
    Owners --> Stewards[Business & Technical Stewards]
    Stewards --> Platform[Automated Data Catalog & Governance Platform]
```

---

## 3. Production Invariants
- All production datasets must be registered in the enterprise data catalog with explicit domain ownership tags.
- Access to sensitive or restricted data tiers requires explicit, time-bounded approval workflows.
