# Least Recently Used (LRU) Cache

## 1. Algorithmic Mechanics ($O(1)$ Operations)
A strict LRU cache is constructed using a **Hash Map** coupled to a **Doubly Linked List**:
* **Hash Map**: Provides $O(1)$ key lookup returning the node pointer.
* **Doubly Linked List**: Maintains chronological access order. Most recently accessed nodes move to the head; evictions occur from the tail in $O(1)$ time.

```mermaid
flowchart LR
    Head[Head: Most Recently Used] <--> NodeA[Key: User_1]
    NodeA <--> NodeB[Key: User_2]
    NodeB <--> Tail[Tail: Least Recently Used -> Evicted First!]
```

---

## 2. Real-World Approximation: Redis Approximated LRU
Maintaining a true doubly linked list requires 16â€“24 bytes of pointer overhead per key, consuming hundreds of megabytes purely in metadata.
* **Redis Approximated LRU**: Samples $N$ random keys (default $N=5$) and evicts the oldest key among the sampled set.
* At $N=10$, approximated LRU achieves $99\%$ mathematical equivalence to true LRU with zero pointer memory overhead.
