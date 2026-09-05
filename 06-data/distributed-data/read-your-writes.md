# Read-Your-Own-Writes Consistency

## 1. The User Experience Problem
In systems utilizing asynchronous read replicas:
1. User updates their profile bio (writes to primary).
2. Browser reloads and fetches bio (reads from a lagging replica).
3. User observes their old bio, believes the update failed, and submits it again.

**Read-Your-Own-Writes (RYOW)** consistency guarantees that an individual user will always observe the effects of their own updates, even if other users see stale data for a brief duration.

```mermaid
flowchart TD
    Client[User Submits Update] --> WriteMaster[(Primary DB)]
    WriteMaster --> SetCookie[API Sets Cookie: last_write_lsn = 482910]
    
    Client -->|Next GET Request with Cookie| Router{Read Router}
    Router -->|User LSN > Replica LSN?| ReadMaster[Route Read to Primary DB for 5s]
    Router -->|Replica In-Sync| ReadReplica[Route to Read Replica]
```

---

## 2. Implementation Strategies
* **Master Pinning Window**: Pin the updating user's subsequent reads to the primary database for 5 to 10 seconds post-mutation.
* **Log Sequence Number (LSN) Tracking**: Pass the transaction LSN in an HTTP response header or cookie; the read router queries replicas only if $\text{LSN}_{\text{replica}} \ge \text{LSN}_{\text{cookie}}$.
