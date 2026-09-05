# OpenID Connect (OIDC) Identity Propagation in Integration

## 1. Purpose of OIDC in Integration
While OAuth 2.0 governs what an integration client can *do*, OpenID Connect 1.0 establishes who the original *caller* or *system subject* is. In enterprise integration pipelines where actions are executed on behalf of a human user (e.g., initiating a loan transfer from mobile banking through ERP to core banking), OIDC propagates the verified caller identity through all integration middleware.

## 2. Identity Propagation Approaches

| Approach | Implementation | Pros | Cons |
| :--- | :--- | :--- | :--- |
| **Pass-Through Token** | Edge bearer token forwarded to all internal tiers | Simple; preserves complete caller context | Violates least privilege; internal services see full user claims |
| **Token Exchange (RFC 8693)**| Edge swaps external token for scoped internal token | Strict least privilege; audit trail preserved | Extra latency at boundary; requires robust token exchange IdP |
| **Trusted Header Forwarding** | Gateway validates token and injects `X-User-Id` | High performance; simple for internal apps | Highly insecure if internal network is breached; susceptible to spoofing |

## 3. Validating Identity via JWKS
```python
import jwt
from jwt import PyJWKClient

JWKS_URL = "https://idp.enterprise.internal/.well-known/jwks.json"
jwks_client = PyJWKClient(JWKS_URL)

def validate_integration_identity(token: str, expected_audience: str) -> dict:
    signing_key = jwks_client.get_signing_key_from_jwt(token)
    payload = jwt.decode(
        token,
        signing_key.key,
        algorithms=["RS256"],
        audience=expected_audience,
        issuer="https://idp.enterprise.internal"
    )
    return payload  # Contains 'sub', 'roles', 'tenant_id'
```
