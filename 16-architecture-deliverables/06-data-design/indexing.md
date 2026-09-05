# Database Indexing Standards

## 1. Indexing Best Practices
* Every foreign key column MUST have an index to prevent full table locks during parent deletes.
* Use partial indexes for active queues: `CREATE INDEX ... WHERE status = 'PENDING';`.
* Remove redundant and unused indexes quarterly using database catalog statistics.
