# API Authentication Standards

## 1. Supported Authentication Mechanisms
1. **OAuth 2.0 Bearer Tokens (JWT)**: Used for public mobile/web and microservice-to-microservice traffic.
2. **Mutual TLS (mTLS)**: Mandatory for high-security banking, partner B2B integrations, and inter-service mesh.
3. **API Keys**: Permitted only for low-risk read-only public developer APIs; strictly combined with IP whitelisting.
