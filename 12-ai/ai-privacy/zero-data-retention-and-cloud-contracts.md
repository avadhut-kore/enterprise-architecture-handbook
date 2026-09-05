# Zero Data Retention (ZDR) Architecture & Verification

## 1. The Core Compliance Requirement

Under GDPR Article 28 and HIPAA Business Associate Agreements (BAAs), an enterprise cannot allow a third-party vendor to store customer data at rest or use it for secondary purposes (such as foundation model retraining).

### Invariants for ZDR Deployments
1. **Explicit API Endpoint Routing**: Many providers offer different endpoints for public consumer use vs. enterprise enterprise use. Ensure all gateway SDKs route exclusively to enterprise ZDR endpoints (e.g., Azure OpenAI Dedicated or AWS Bedrock Private Endpoints).
2. **Abuse Monitoring Opt-Out**: Standard consumer LLM APIs store prompts on disk for 30 days for human abuse review. Enterprises must execute formal opt-out agreements ensuring human review logging is completely disabled.
