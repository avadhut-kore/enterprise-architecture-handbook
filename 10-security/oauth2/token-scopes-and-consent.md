# OAuth 2.0 Token Scopes & Permission Namespacing

## Executive Summary

Scopes define the coarse-grained boundaries of access granted to a client application. A well-architected scope namespace prevents privilege escalation and enables explicit user consent.

---

## 1. Recommended Scope Namespacing Pattern

Adopt the standard hierarchical notation: `<resource>:<action>` or `<domain>.<resource>.<action>`.

### Examples:
- `orders:read` - Read customer orders.
- `orders:write` - Create or update orders.
- `payments:refund:approve` - Authorize financial refunds above \$1,000.
- `user.profile.read` - Read user identity profile.

---

## 2. Scopes vs Permissions (Critical Architectural Distinction)
- **Scopes ($S$)**: Represent what the *client application* is allowed to request on behalf of the user.
- **User Permissions ($P$)**: Represent what the *user* actually has permission to do inside the enterprise system.
- **Effective Authorization**:
  $$\text{Effective Permission} = \text{Client Scopes} \cap \text{User Permissions}$$
  *Rule*: A client possessing the `payments:admin` scope cannot execute admin actions if the authenticated user is only a junior support clerk.
