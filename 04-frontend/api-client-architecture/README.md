# API Client Architecture for Frontend & Mobile

In enterprise client applications, directly invoking raw `fetch()` or `axios.get()` inside UI components introduces chaotic failure handling, token leaks, and uncoordinated duplicate requests.

This directory defines the **API Client Layer**: an isolated architectural subsystem responsible for transport abstraction, authentication injection, automatic token refresh, retries, timeouts, and offline synchronization.

---

## Knowledge Index
- [API Client Layer Overview](api-client-layer.md)
- [Request Abstraction](request-abstraction.md)
- [Authentication Injection](authentication.md)
- [Silent Token Refresh](token-refresh.md)
- [Retry Strategy & Exponential Backoff](retry-strategy.md)
- [Timeout Strategy](timeout-strategy.md)
- [Error Handling & Translation](error-handling.md)
- [Request Cancellation (AbortController)](request-cancellation.md)
- [Client Pagination](pagination.md)
- [Client-Side Caching](caching.md)
- [Offline Mutation Queue](offline-queue.md)
- [Optimistic Updates](optimistic-updates.md)
- [API Versioning Consumption](api-versioning.md)
