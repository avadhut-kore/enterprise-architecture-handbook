# Two-Phase Commit Protocol (2PC)

## 1. Protocol Flow
Two-Phase Commit is the classical distributed atomic commit protocol:

```mermaid
sequenceDiagram
    autonumber
    participant C as Transaction Coordinator
    participant P1 as Participant 1 (Database A)
    participant P2 as Participant 2 (Database B)
    
    Note over C,P2: Phase 1: Prepare Phase
    C->>P1: PREPARE (Acquire locks, write undo/redo log)
    C->>P2: PREPARE (Acquire locks, write undo/redo log)
    P1-->>C: VOTE_COMMIT
    P2-->>C: VOTE_COMMIT
    
    Note over C,P2: Phase 2: Commit Phase
    C->>P1: GLOBAL_COMMIT
    C->>P2: GLOBAL_COMMIT
    P1-->>C: ACK (Release locks)
    P2-->>C: ACK (Release locks)
```

---

## 2. The Fatal Flaw: The Blocking Problem
* If the Coordinator crashes **after** participants vote `VOTE_COMMIT` but **before** issuing `GLOBAL_COMMIT`:
* All participants are left in a state of indefinite uncertainty.
* **Participants cannot unilaterally commit or abort**; they must hold exclusive locks indefinitely, freezing downstream rows and thread pools until human intervention or coordinator recovery.
