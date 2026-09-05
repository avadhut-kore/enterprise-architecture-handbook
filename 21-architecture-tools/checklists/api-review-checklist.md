# Enterprise API Design & Review Checklist

Ensure all published APIs (REST, GraphQL, gRPC) comply with enterprise standards, security postures, and developer experience best practices.

---

## 1. Contract & Interface Design
* [ ] **Contract-First Approach**: Is the API specified in OpenAPI 3.1, Protocol Buffers, or GraphQL SDL prior to backend coding?
* [ ] **Resource-Oriented Naming**: Are RESTful endpoints modeled around nouns rather than verbs (e.g., `POST /orders`, not `POST /createOrder`)?
* [ ] **Pluralized Resource Nouns**: Are collections consistently pluralized (`/users`, `/invoices`, `/products`)?
* [ ] **Appropriate HTTP Verbs**: Are standard HTTP methods used correctly (`GET` safe/idempotent, `POST` mutate, `PUT` replace, `PATCH` partial update, `DELETE` remove)?

---

## 2. Status Codes & Error Responses
* [ ] **Accurate HTTP Status Codes**: Are standard codes returned (`200 OK`, `201 Created`, `204 No Content`, `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `409 Conflict`, `422 Unprocessable Entity`, `429 Too Many Requests`, `500 Internal Error`)?
* [ ] **RFC 7807 Problem Details**: Do error responses follow RFC 7807 (`type`, `title`, `status`, `detail`, `instance`, `code`)?
* [ ] **No Leaked Stack Traces**: Are internal exceptions, stack traces, and database connection strings stripped from public error responses?

---

## 3. Versioning, Pagination & Filtering
* [ ] **Explicit URI Versioning**: Is major versioning declared in the URI path (e.g., `/api/v1/`)?
* [ ] **Cursor-Based Pagination**: For large datasets, is cursor-based pagination implemented (`limit`, `cursor`) rather than offset-based pagination to prevent performance degradation?
* [ ] **Field Filtering & Sparse Fieldsets**: Can clients request specific fields to conserve mobile bandwidth?

---

## 4. Security & Rate Limiting
* [ ] **OAuth2 Token Validation**: Is every non-public endpoint protected by JWT validation against enterprise JWKS?
* [ ] **Scope Enforced**: Are granular OAuth2 scopes verified on every mutation (`read:customers`, `write:orders`)?
* [ ] **Rate Limiting Configured**: Are tier-based rate limits enforced per IP and per client token with `X-RateLimit-*` headers?
* [ ] **Payload Size Capped**: Is maximum request body size restricted (e.g., max 10MB) to prevent buffer overflow or DoS memory exhaustion?
* [ ] **CORS Properly Configured**: Are CORS headers restricted to authorized enterprise origins (`Access-Control-Allow-Origin: *` prohibited on authenticated APIs)?

---

## 5. Performance & Caching
* [ ] **HTTP Caching**: Do safe `GET` responses emit valid `Cache-Control` and `ETag` headers?
* [ ] **Gzip / Brotli Compression**: Is response payload compression enabled on the API gateway for text payloads?
* [ ] **Connection Keep-Alive**: Does the API support HTTP/2 connection reuse and multiplexing?
