# Contract-First API Products & Lifecycle Management

## 1. Managing APIs as Long-Term Enterprise Products

APIs must be versioned deterministically:
* **Semantic Versioning in URLs**: Major versions in URL paths (`/v1/accounts`, `/v2/accounts`); minor and patch versions communicated via response headers.
* **Deprecation Policy**: A published API version must be supported for a minimum of 12 months after formal deprecation notification before decommissioning.
