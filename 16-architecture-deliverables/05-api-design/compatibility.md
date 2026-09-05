# API Backward Compatibility Rules

## 1. Allowed Non-Breaking Changes
* Adding new optional query parameters.
* Adding new fields to response JSON payloads.
* Adding new HTTP methods or endpoints.

## 2. Breaking Changes (Requires Major Version Bump)
* Renaming or removing existing fields in requests or responses.
* Changing field types (e.g., string to integer).
* Adding new required request parameters or headers.
* Changing HTTP response status codes.
