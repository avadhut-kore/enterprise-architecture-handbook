# OAuth 2.0 & OpenID Connect in Enterprise Integration

## 1. Scope and Applicability
OAuth 2.0 (RFC 6749) is the enterprise standard for delegated authorization. In system integration scenarios, the **Client Credentials Grant** (Section 4.4) is the primary flow, while the **Token Exchange** (RFC 8693) flow handles identity propagation across multi-tier microservice topologies.

## 2. Enterprise Token Exchange Architecture (RFC 8693)

```
[External User] ──(1) User JWT──> [Edge API Gateway]
                                          │
                               (2) Exchange User JWT for
                               Internal Downstream Token
                                          ▼
                              [Corporate IdP (Keycloak)]
                                          │ (3) Mint Constrained Token
                                          ▼
                                [Internal Downstream API]
```

## 3. Client Credentials Flow Implementation

```http
POST /oauth2/v1/token HTTP/1.1
Host: idp.enterprise.internal
Content-Type: application/x-www-form-urlencoded
Authorization: Basic base64(client_id:client_secret)

grant_type=client_credentials&scope=payments:read+payments:execute&audience=https://core-ledger.internal
```

### Response
```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjIwMjYtMDktMDV...zkx",
  "token_type": "Bearer",
  "expires_in": 900,
  "scope": "payments:read payments:execute"
}
```

## 4. Best Practices for Integration Architectures
1. **Audience Restriction (`aud`)**: Every token must specify the target service (`aud: https://core-ledger.internal`). Gateways must reject tokens minted for other audiences.
2. **Short Lifespans**: Keep access token TTL $\le 15$ minutes. Never issue refresh tokens to M2M integration clients; let them request new access tokens via client credentials.
3. **mTLS Token Binding (RFC 8705)**: Bind tokens to the sender's client certificate (`cnf` claim containing cert hash) to prevent stolen token replay attacks.
