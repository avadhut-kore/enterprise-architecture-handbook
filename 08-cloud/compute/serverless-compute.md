# Serverless Compute Architecture

## Executive Summary

Serverless compute abstracts the server completely. Code executes strictly on-demand, scaling automatically from zero to thousands of concurrent executions with billing granular to the millisecond.

---

## 1. FaaS Execution Lifecycle

```mermaid
graph LR
    Trigger[Event Trigger: HTTP / Queue] --> Sched[Provider Scheduler]
    Sched --> Cold[Cold Start: Download Image + Spin MicroVM + Bootstrap Runtime]
    Cold --> Exec[Execution: Run Handler Logic]
    Exec --> Warm[Warm Instance: Retained in Memory for ~15 Mins]
    Warm -->|Next Event Arrives| FastExec[Warm Execution: Sub-Millisecond Dispatch!]
```

---

## 2. Serverless Architectural Constraints

1. **State Externalization**: Local instance memory and ephemeral storage (`/tmp`) are destroyed when the execution environment scales down. All state must reside in external datastores (DynamoDB, Redis, S3).
2. **Connection Starvation**: Because FaaS scales elastically into thousands of concurrent execution environments, each opening database connections, direct connectivity to traditional RDBMS pools will crash the database. Connection poolers (RDS Proxy, PgBouncer) are mandatory.
3. **Execution Ceilings**: FaaS platforms enforce hard timeouts (AWS Lambda: 15 minutes; Cloud Functions: 60 minutes). Long-running batch jobs must be broken into Step Functions or migrated to container jobs.
