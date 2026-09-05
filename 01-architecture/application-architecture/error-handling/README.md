# Application Error Handling Architecture

Error handling is an architectural concern, not an afterthought. In poorly architected systems, exceptions are used for control flow, sensitive database errors leak to external clients, and unhandled crashes destabilize worker threads.

This section establishes standard taxonomies, result patterns, and observability models for enterprise error management.

---

## Knowledge Index
- [Error Taxonomy](error-taxonomy.md)
- [Domain Errors](domain-errors.md)
- [Validation Errors](validation-errors.md)
- [Technical Errors](technical-errors.md)
- [Dependency Errors](dependency-errors.md)
- [API Error Model](api-error-model.md)
- [Error Codes](error-codes.md)
- [Exception Handling](exception-handling.md)
- [Global Error Handling](global-error-handling.md)
- [Retryable Errors](retryable-errors.md)
- [Non-Retryable Errors](non-retryable-errors.md)
- [Error Propagation](error-propagation.md)
- [Error Observability](error-observability.md)
