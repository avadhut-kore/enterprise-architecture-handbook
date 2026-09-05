# Human-in-the-Loop (HITL) Architecture

## 1. Asynchronous Human Approval Gates

AI systems must never execute high-risk state mutations (financial transfers, record deletions, contract dispatches) without explicit human verification.

**Human-in-the-Loop Architecture** decouples automated AI drafting from human review using asynchronous pause-and-resume workflows.

```mermaid
sequenceDiagram
    autonumber
    participant AI as AI Processing Worker
    participant Engine as Durable Workflow Engine (Temporal)
    participant UI as Human Reviewer Dashboard
    actor Reviewer as Operations Specialist
    participant API as Core Banking API

    AI->>Engine: Complete Draft Analysis (Discrepancy Found)
    Note over Engine: Confidence Score: 0.74 (Threshold < 0.85)<br/>Workflow PAUSES statefully
    Engine->>UI: Create Human Review Task (Task-891)
    Reviewer->>UI: Inspect AI Draft, Citations & Proposed Transfer
    Reviewer->>UI: Click "Approve with Edit: Amount = $4,500"
    UI->>Engine: Signal Workflow (Approval Received)
    Note over Engine: Workflow RESUMES execution
    Engine->>API: Execute Transaction with Human-Approved Parameters
    API-->>Engine: Transaction Confirmed
```

---

## 2. Escalation Invariants
* **Confidence-Based Routing**:
  * $\text{Confidence} \ge 0.95$: Automatic execution (Straight-Through Processing).
  * $0.80 \le \text{Confidence} < 0.95$: Async human peer review queue.
  * $\text{Confidence} < 0.80$: Route to senior operations escalation.
* **Durable Timeouts**: If a human reviewer does not respond within 24 hours, escalate to a secondary reviewer or gracefully abort.
