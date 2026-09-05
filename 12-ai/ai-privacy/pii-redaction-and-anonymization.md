# PII Redaction & Anonymization Architecture

## 1. Reversible Pseudonymization at the Gateway

Masking PII with static redactions (`[REDACTED]`) often destroys the model's ability to understand relationships (*"Customer [REDACTED] transferred money to [REDACTED]"*).

**Reversible Pseudonymization** replaces PII with semantically coherent placeholders, maintaining a short-lived lookup table in Redis to restore real values upon completion:

```mermaid
sequenceDiagram
    autonumber
    Client->>Gateway: "Alice Smith (SSN: 000-12-3456) requested an address update."
    Note over Gateway: Gateway detects PII;<br/>Stores in Redis: {ID_1: Alice Smith, ID_2: 000-12-3456}
    Gateway->>CloudLLM: "<USER_1> (<SSN_1>) requested an address update."
    CloudLLM-->>Gateway: "Please confirm that <USER_1> has verified their identity."
    Note over Gateway: Gateway reverses lookup: replaces <USER_1> with Alice Smith
    Gateway-->>Client: "Please confirm that Alice Smith has verified their identity."
```
