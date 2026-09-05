# HTTP Methods & Semantics

## 1. Safety & Idempotency Matrix

| HTTP Method | Safe? | Idempotent? | Cacheable? | Primary Semantics |
| :--- | :--- | :--- | :--- | :--- |
| **GET** | **Yes** (Read-only) | **Yes** | **Yes** | Retrieve resource representation. |
| **HEAD** | **Yes** | **Yes** | **Yes** | Retrieve headers only (no response body). |
| **OPTIONS**| **Yes** | **Yes** | No | Probe supported methods and CORS headers. |
| **POST** | No (Mutates) | **No** (Retries create duplicates) | Only with explicit headers | Create new subordinate resource; trigger action. |
| **PUT** | No | **Yes** (Complete replace) | No | Full replacement of target resource state. |
| **PATCH** | No | **No** (Unless JSON Merge Patch) | No | Partial update of resource fields. |
| **DELETE** | No | **Yes** (Deleting 5 times = resource gone) | No | Remove target resource. |
