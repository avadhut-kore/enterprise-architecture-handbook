# System Design Checklist: Data Modeling & Persistence

## 1. Storage Paradigm & Sharding
- [ ] Storage engine selected based on access patterns (RDBMS vs NoSQL vs Graph)?
- [ ] Entity relationship model (ERD) documented with cardinalities?
- [ ] Primary keys use collision-resistant distributed IDs (UUIDv7, Snowflake)?
- [ ] Sharding key selected with high cardinality to eliminate hotspotting?

## 2. Indexing & Integrity
- [ ] Indexes created for all query `WHERE`, `ORDER BY`, and `JOIN` clauses?
- [ ] Write amplification factor calculated for all secondary indexes?
- [ ] Soft deletion strategy (`is_deleted` or tombstone events) defined?
- [ ] Cross-shard query patterns explicitly eliminated from OLTP paths?
