# OIDC Claims & UserInfo Endpoint Architecture

## Executive Summary

Claims are name-value pairs asserted by an OpenID Provider about an authenticated entity. Standardizing claim semantics ensures seamless identity federation across enterprise platforms.

---

## 1. Standard Identity Claims
- `sub` (**Subject**): Unique, never-reassigned identifier for the user within the issuer namespace.
- `iss` (**Issuer**): HTTPS URL of the identity provider that issued the token.
- `aud` (**Audience**): The OAuth `client_id` of the application for which this token was minted.
- `exp` (**Expiration Time**): Unix timestamp after which the token is invalid.
- `iat` (**Issued At**): Unix timestamp when the token was minted.
- `auth_time`: Time when the actual user authentication occurred (vital for re-authentication checks on high-value operations).

---

## 2. The UserInfo Endpoint
For heavy claims (e.g., high-resolution avatar photos, detailed organizational hierarchy data), the ID token contains only a reference. The client presents its Access Token to the `/userinfo` endpoint to fetch supplementary profile claims without bloating the ID token size.
