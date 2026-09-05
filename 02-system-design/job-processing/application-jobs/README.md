# In-Application Background Job Processing

While distributed batch architectures (Phase 3) handle planetary-scale data pipelines, **in-application background processing** handles asynchronous tasks within a service: sending welcome emails, generating invoice PDFs, processing file uploads, and scheduling periodic cleanup jobs.

---

## Knowledge Index
- [In-Application Background Jobs](background-jobs.md)
- [Worker Thread & Pool Architecture](worker-architecture.md)
- [Scheduled Jobs & In-App Cron](scheduled-jobs.md)
- [Retryable Jobs & Exponential Backoff](retryable-jobs.md)
- [Idempotent Job Processing](idempotent-jobs.md)
- [Long-Running Jobs & Heartbeats](long-running-jobs.md)
- [Job Status Tracking & Progress APIs](job-status.md)
- [Job Cancellation & Graceful Draining](job-cancellation.md)
- [Job Prioritization & Priority Queues](job-priorities.md)
- [Job Monitoring & Dead-Letter Alerts](job-monitoring.md)
