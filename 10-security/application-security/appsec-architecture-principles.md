# Application Security Architecture Principles

## Executive Summary

1. **Treat All Input as Untrusted**: Input validation must occur at the edge, at the service boundary, and at the database boundary.
2. **Context-Aware Encoding**: Data rendered into HTML, SQL, Shell, or LDAP must be encoded specifically for the destination context.
3. **Structured Safe Formats**: Avoid dynamic string interpretation. Prefer strongly typed, structured formats (JSON, Protocol Buffers) over dynamic eval or executable serialization formats.
