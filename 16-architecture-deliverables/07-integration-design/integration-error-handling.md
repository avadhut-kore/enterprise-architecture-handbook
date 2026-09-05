# Integration Error Handling Standards
* Separate transient errors (network drops, 503) from non-retryable fatal errors (400 Bad Request, schema validation failure).
