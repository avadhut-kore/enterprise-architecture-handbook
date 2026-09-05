# Background Jobs Architecture

## 1. Decoupling Web Requests from Execution
Executing long-running tasks within an HTTP request thread risks gateway timeouts (`HTTP 504`) and client thread starvation. Background jobs shift processing to asynchronous worker fleets:

```mermaid
sequenceDiagram
    autonumber
    Client->>API: POST /reports/generate
    API->>DB: Insert Job Record (Status: PENDING)
    API->>Queue: Enqueue Task (Payload: {report_id: 101})
    API-->>Client: HTTP 202 Accepted ({job_id: 101})
    
    Worker->>Queue: Dequeue Task
    Worker->>Worker: Generate 50-Page PDF (Takes 45 seconds)
    Worker->>S3: Upload PDF File
    Worker->>DB: UPDATE job SET status = 'COMPLETED', url = 's3://...'
```
