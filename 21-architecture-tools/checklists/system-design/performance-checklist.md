# System Design Checklist: Performance & Optimization

## 1. Latency & Connection Management
- [ ] End-to-end P99 latency budget allocated and verified against benchmarks?
- [ ] Connection pooling enabled for all database, cache, and HTTP client connections?
- [ ] TCP keep-alive and HTTP/2 connection reuse enabled across internal microservices?
- [ ] Query execution plans (`EXPLAIN ANALYZE`) verified: no unindexed sequential scans?

## 2. Resource Utilization
- [ ] Heavy payloads processed as streams rather than buffered in RAM?
- [ ] Gzip / Brotli compression enabled at API Gateway for responses > 1 KB?
