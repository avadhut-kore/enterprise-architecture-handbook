# Clarifying Questions & Scope Discovery

## 1. High-Impact Questioning Framework

When given a broad prompt ("Design Twitter" or "Design Uber"):

```
1. Functional Scope:
   - "What are the primary actions users take in the MVP?"
   - "Should we support real-time push, or is polling acceptable?"
   - "Are we designing the mobile client experience, the backend platform, or both?"

2. Scale & Geography:
   - "What is the expected Daily Active User (DAU) count?"
   - "Is this service globally distributed across multiple regions or single-datacenter?"

3. Consistency & Edge Constraints:
   - "In terms of consistency, is it acceptable for timeline reads to lag writes by 2 seconds, or is strict linearizability required?"
   - "What are the retention rules for historical data?"
```

---

## 2. Strong Candidate vs Weak Candidate Responses

- **Weak Candidate**: Immediately starts drawing database boxes and Kafka queues without asking questions.
- **Strong Candidate**: "Before designing the architecture, let's clarify the core user workflows. For a YouTube clone, should we focus on the video upload and transcoding pipeline, or the search and recommendation engine? Let's assume we prioritize upload and playback first."
