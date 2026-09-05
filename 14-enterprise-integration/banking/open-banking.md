# Open Banking and Regulatory API Integration (PSD2 / FDX)

## 1. Open Banking Specifications
- **PSD2 / Open Banking UK**: Enforces Payment Initiation Service Providers (PISP) and Account Information Service Providers (AISP) integrations.
- **FDX (Financial Data Exchange - US)**: RESTful open finance standard eliminating credential screen scraping.

## 2. Strong Customer Authentication (SCA) Flow
Open banking requires OAuth 2.0 with dynamic linking (binding the authorization code cryptographically to the payee and payment amount):
```
[Fintech App / PISP] ──(Redirect)──> [Bank Open Banking Consent Portal]
                                            │ (User logs in via FaceID/2FA)
                                            ▼
                               [Consent Grant Minted with Hash(Payee + Amount)]
                                            │
                                            ▼
[Fintech App] ◄── (Authorization Code) ─────┘
```
