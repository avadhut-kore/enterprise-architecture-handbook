# Database Consistency & Isolation Standards

## 1. Transaction Isolation Matrix
* Default: `READ COMMITTED` for standard CRUD operations.
* Mandatory: `SERIALIZABLE` for financial balance transfers and inventory allocation.
