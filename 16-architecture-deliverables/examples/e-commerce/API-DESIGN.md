# API-ECOM-001: Checkout REST API Specification
* `POST /v1/checkouts`: Initiates checkout session with `Idempotency-Key` header.
* Returns RFC 7807 Problem Details on invalid payment method or out-of-stock items.
