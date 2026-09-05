# Inverted Index Architecture

## 1. The Core Data Structure
An Inverted Index maps every unique word (term) in a corpus to a **Posting List** of document IDs where that word occurs:

```mermaid
flowchart LR
    Term_Apple[apple] --> P1["Doc 1 (Pos: 3)"]
    P1 --> P2["Doc 4 (Pos: 12)"]
    P2 --> P3["Doc 9 (Pos: 1)"]
    
    Term_Phone[phone] --> P4["Doc 1 (Pos: 4)"]
    P4 --> P5["Doc 7 (Pos: 2)"]
    P5 --> P6["Doc 9 (Pos: 2)"]
```

---

## 2. Query Intersection ($O(A \cap B)$)
To execute `apple AND phone`:
* Intersect the posting list of `apple` with `phone`.
* Utilizing **Skip Lists** or **Roaring Bitmaps**, intersection evaluates in microsecond time without scanning document bodies.
