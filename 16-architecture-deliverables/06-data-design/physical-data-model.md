# Physical Data Modeling Standards

## 1. Datatypes & Precision Rules
* Currency and financial amounts: `NUMERIC(18, 4)`, NEVER `FLOAT` or `DOUBLE`.
* Timestamps: `TIMESTAMPTZ` (UTC with timezone), NEVER local timestamp strings.
* Identifiers: `UUIDv7` (time-ordered UUIDs) to preserve B-Tree index locality.
