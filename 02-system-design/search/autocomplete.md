# Autocomplete Architecture (Trie Data Structure)

## 1. Prefix Trees (Tries)
Autocomplete prefix searches utilize a Trie where every tree node represents a character:

```mermaid
flowchart TD
    Root[Root] --> A[a]
    A --> P1[p]
    P1 --> P2[p]
    P2 --> L[l]
    L --> E[e: 'apple' - Weight: 95]
    P2 --> S[s: 'apps' - Weight: 80]
```
* **Time Complexity**: Finding top suggestions takes $O(K)$ where $K$ is the prefix length, independent of total catalog size.
