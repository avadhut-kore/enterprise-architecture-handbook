# Long-Running Agentic Workflows Architecture

## 1. Managing Workflows that Span Days or Weeks

Enterprise tasks—such as a multi-stage vendor compliance audit—involve AI processing, human reviews, external partner webhooks, and asynchronous batch evaluations spanning days or weeks.

```mermaid
flowchart TD
    Start["Initiate Vendor Audit Workflow"] --> Step1["Day 1: AI Extracts Clauses from 50 PDFs"]
    Step1 --> Step2["Day 2: Dispatch Webhook to Vendor for Missing Security Certs"]
    Step2 --> Sleep["Workflow Enters Durable Sleep (Consumes 0 RAM / 0 CPU)"]
    Sleep --> Event["Day 5: Vendor Submits SOC 2 Report via Webhook"]
    Event --> Step3["Day 5: AI Analyzes SOC 2 Report"]
    Step3 --> Step4["Day 6: Human Security Officer Approves Audit"]
    Step4 --> Complete["Workflow Terminates Successfully"]
```

---

## 2. Architectural Technology Selection
* **Do NOT use**: Python `time.sleep()`, long-held HTTP connections, or in-memory Celery task queues for long-running workflows.
* **Use**: **Temporal, Cadence, or AWS Step Functions**. State is recorded as an append-only event history; worker instances can be restarted, patched, or rescheduled without losing workflow state.
