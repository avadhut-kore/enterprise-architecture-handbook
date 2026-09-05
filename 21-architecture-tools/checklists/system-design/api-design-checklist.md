# System Design Checklist: API Architecture & Contracts

## 1. Contract & Interface Standards
- [ ] API protocol selected with clear rationale (REST vs gRPC vs GraphQL)?
- [ ] API contract formalized in OpenAPI 3.0 / Protobuf specification?
- [ ] URI design adheres to resource-oriented REST conventions?
- [ ] HTTP status codes used correctly (200, 201, 202, 400, 401, 403, 404, 409, 422, 500, 503)?

## 2. Resiliency & Enterprise Invariants
- [ ] Explicit `Idempotency-Key` mechanism implemented for all non-idempotent mutations?
- [ ] Standard pagination implemented for collections (Keyset / Cursor-based preferred)?
- [ ] Rate limiting and throttling headers included (`RateLimit-Limit`, `RateLimit-Remaining`)?
- [ ] Error responses follow RFC 7807 Problem Details JSON format?
