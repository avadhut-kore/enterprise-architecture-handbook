# Autonomous Action Limits & Circuit Breakers

## 1. The Danger of Unbounded Agency

When AI agents are given tools to mutate enterprise systems (e.g., creating Jira tickets, updating CRM leads, modifying database rows), an undetected logic flaw or model hallucination can trigger **cascading data corruption across thousands of records in seconds**.

---

## 2. Rate-of-Change Circuit Breakers

The AI Gateway must enforce **Rate-of-Change (RoC) Fences** on all state-mutating tool invocations:

```mermaid
flowchart TD
    ToolCall["Agent Calls Tool: 'update_customer_record'"] --> RoCCheck{"Rate-of-Change Limit Check\n(Max 50 updates per hour per tenant)"}
    
    RoCCheck -->|< 50 updates/hr| Allow["Allow Execution"]
    RoCCheck -->|>= 50 updates/hr| Trip["TRIP CIRCUIT BREAKER:\n1. Pause agent execution\n2. Revert agent status to 'SUSPENDED'\n3. Page on-call Operations Engineer"]
```

### Invariant: Emergency Dead-Man Switch
Every autonomous agent platform must expose an instantaneous global kill switch in the control plane (`POST /v1/admin/agents/kill-all`), immediately terminating all active agent execution containers and severing tool database credentials within 500ms.
