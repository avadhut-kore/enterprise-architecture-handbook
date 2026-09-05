# Function Calling & Tool Primitives

## 1. How Function Calling Operates Under the Hood

Function calling (or tool calling) does **NOT** mean the LLM executes code directly. The foundation model is a pure mathematical text predictor. 

Function calling is a 4-step protocol where the model is fine-tuned to emit a specialized structured token sequence indicating its *intent* to invoke an external function, delegating actual execution to the host application runtime.

```mermaid
sequenceDiagram
    autonumber
    actor Client as Application Client
    participant App as Application Backend
    participant LLM as Foundation Model
    participant API as External Enterprise API

    Client->>App: "What is the balance for account ACC-901?"
    App->>LLM: Prompt + Tools Definition (JSON Schema for get_account_balance)
    Note over LLM: Model detects tool match;<br/>generates tool call JSON: `{"name": "get_account_balance", "args": {"id": "ACC-901"}}`
    LLM-->>App: Return Tool Call Specification (stop_reason: tool_calls)
    Note over App: App inspects tool call;<br/>validates authorization & parameters
    App->>API: GET /v1/accounts/ACC-901 (Execute API)
    API-->>App: Return `{"balance": 15420.50, "currency": "USD"}`
    App->>LLM: Send Original Conversation + Tool Result Payload
    Note over LLM: Model synthesizes tool output into natural response
    LLM-->>App: "Account ACC-901 currently has a balance of $15,420.50 USD."
    App-->>Client: Stream Final Response
```

---

## 2. Architectural Security Principles for Tools
1. **Zero Autonomous Write Execution**: Read-only tools can be executed automatically; state-mutating tools (e.g., `transfer_funds`, `delete_record`) require explicit human approval.
2. **Strict Schema Validation**: Tool argument payloads returned by the model must be validated against runtime schemas before being passed to internal RPC clients.
