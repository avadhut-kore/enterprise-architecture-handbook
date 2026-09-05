# LLD Error Handling & Exception Mapping Specification

## 1. Exception Hierarchy
```text
PlatformBaseException (abstract)
├── ValidationException -> HTTP 400 Bad Request
├── ResourceNotFoundException -> HTTP 404 Not Found
├── DuplicateRequestException -> HTTP 409 Conflict
├── OptimisticLockException -> HTTP 409 Conflict / Automatic Retry
└── DownstreamTimeoutException -> HTTP 504 Gateway Timeout
```

## 2. Standard RFC 7807 Error Response
```json
{
  "type": "https://api.enterprise.com/errors/invalid-order-state",
  "title": "Invalid Order State Transition",
  "status": 409,
  "detail": "Order ord-123 is in CANCELLED status and cannot be marked as PAID.",
  "instance": "/api/v1/orders/ord-123/pay",
  "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736"
}
```
