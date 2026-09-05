# AI Threat Modeling Framework (STRIDE for GenAI)

## 1. Adapting STRIDE to Foundation Models

Classical threat modeling focuses on network ports, user accounts, and SQL databases. System architects must adapt the STRIDE methodology to analyze AI-specific failure modes:

| STRIDE Category | Classical Threat | GenAI / LLM Threat Equivalent | Enterprise Mitigation |
| :--- | :--- | :--- | :--- |
| **Spoofing** | Forging user identity or IP. | Impersonating trusted agent personas or spoofing tool callbacks. | Cryptographic tool signatures; mTLS between agent runtimes and tools. |
| **Tampering** | Modifying database records or packets. | Poisoning training datasets; manipulating RAG vector embeddings; prompt injection. | Ingestion hash verification; immutable S3 WORM audit storage; input sanitizers. |
| **Repudiation** | Denying an action took place. | Agent executing financial transactions without an auditable reasoning trace. | Append-only decision logging recording prompt, context, model weights, and tool response. |
| **Information Disclosure** | Data breach, credential leak. | Model outputting training data memorization; cross-tenant RAG leaks; system prompt extraction. | Pre-filtering vector search by tenant ID; output DLP scanning; canary token egress monitors. |
| **Denial of Service** | Network flooding, resource exhaustion. | Denial-of-Wallet (DoW) via massive context injection or recursive agent loops. | Token-per-minute (TPM) quotas; maximum recursion depth ceilings; semantic caching. |
| **Elevation of Privilege** | Escalating from user to root. | Agent jailbreak granting unauthorized access to administrative enterprise tools. | Scoped tool execution (ABAC); read-only database replicas; human review gates. |
