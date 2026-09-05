# Agent Guardrails & Termination Criteria

## 1. The Runaway Loop Vulnerability

Autonomous agents left unchecked will enter infinite loops when tools return unexpected errors, repeatedly trying the same failing parameters and consuming thousands of dollars in tokens within minutes.

```mermaid
flowchart TD
    Loop["Agent Execution Loop"] --> Guard1{"Iteration Count > 10?"}
    Guard1 -->|Yes| Trip1["Trip Circuit Breaker: 'Max Iterations Exceeded'"]
    Guard1 -->|No| Guard2{"Token Spend > $5.00?"}
    Guard2 -->|Yes| Trip2["Trip Circuit Breaker: 'Budget Exceeded'"]
    Guard2 -->|No| Guard3{"Repetitive Action Detected?\n(Same tool + same args 3x)"}
    Guard3 -->|Yes| Trip3["Trip Circuit Breaker: 'Dead Loop Detected'"]
    Guard3 -->|No| Allow["Allow Next Tool Execution"]
```

---

## 2. Mandatory Production Guardrails
* **Max Steps Limit**: Hard ceiling of 8 to 12 iterations per task.
* **Cost Fence**: Maximum token budget per session (e.g., cap at 50,000 tokens).
* **Wall-Clock Timeout**: Automatic termination if total execution exceeds 120 seconds.
* **Repetitive Action Blocker**: An in-memory Bloom filter detects if an agent calls the identical tool with identical parameters more than twice consecutively.
