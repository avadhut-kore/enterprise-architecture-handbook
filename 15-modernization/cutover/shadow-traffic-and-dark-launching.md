# Shadow Traffic & Dark Launching Architecture

## 1. Production Shadowing Pipeline
Shadow traffic captures live production requests and forks a duplicate copy to the candidate modernized service without delaying the real customer response:

```
[Real Customer Request]
            │
            ▼
     [Envoy API Gateway]
            │
     ┌──────┴───────────────────────────────────┐
     ▼ (Synchronous)                            ▼ (Asynchronous Shadow Copy)
[Legacy Production Monolith]             [Candidate Modern Service]
     │ (Returns HTTP 200)                       │ (Executes in-memory)
     ▼                                          ▼
[Customer Response]                     [Shadow Response Interceptor]
                                                │
                                                ▼ (Compares JSON bodies)
                                       [Diff Comparator Engine]
```

## 2. Guardrails for Dark Launching
- Strip write credentials: The shadow service must have read-only permissions to test databases.
- Suppress downstream integrations: Outbound emails, SMS messages, and payment processor calls must be mocked.
