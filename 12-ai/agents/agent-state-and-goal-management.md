# Agent State & Goal Management Architecture

## 1. The Persistent Scratchpad

An agent cannot maintain state purely in volatile memory. If an agent executes a 10-step migration task that takes 5 minutes, a pod crash or network reset must not corrupt the operation.

The **Agent Scratchpad** must be persisted to a durable state store (Redis / PostgreSQL) after every single tool execution.

```mermaid
flowchart LR
    subgraph AgentState ["Durable Agent State Machine"]
        StateJSON["State Payload:\n- goal_id: 'goal-918'\n- status: 'IN_PROGRESS'\n- current_step: 4\n- plan_dag: [...]\n- tool_history: [...]\n- accumulated_data: {...}"]
    end

    StateJSON --> Storage[("Durable State Store (PostgreSQL / Redis)")]
    Storage -.->|Worker Pod Dies| ResumedWorker["New Worker Resumes from Last Checkpoint"]
```

---

## 2. Invariants for Goal Completion
1. **Explicit Halting Conditions**: The agent prompt must specify exact, deterministic success criteria.
2. **Deterministic Validation**: An external verification function (not the agent itself) must assert that the target state has been achieved (e.g., verifying that a new database row actually exists).
