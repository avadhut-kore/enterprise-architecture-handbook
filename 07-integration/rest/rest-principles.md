# REST Architectural Principles

## 1. Fielding's Six Architectural Constraints
A system is strictly "RESTful" only if it conforms to Roy Fielding's six core constraints:

```mermaid
flowchart TD
    C1[1. Client-Server Separation: UI decoupled from data storage]
    C2[2. Statelessness: No client context stored on server]
    C3[3. Cacheability: Responses must explicitly declare cacheability]
    C4[4. Layered System: Intermediaries proxies/gateways transparent]
    C5[5. Uniform Interface: Standard URIs, representations, self-describing]
    C6[6. Code on Demand Optional: Server sends executable scripts]
```

---

## 2. Richardson Maturity Model (RMM)
* **Level 0 (The Swamp of POX)**: Single URI, single HTTP method (e.g., SOAP / XML-RPC over `POST /api`).
* **Level 1 (Resources)**: Dedicated URIs for individual resources (`/orders/123`, `/customers/456`).
* **Level 2 (HTTP Verbs)**: Proper usage of standard HTTP methods (`GET`, `POST`, `PUT`, `DELETE`) and status codes (`200`, `201`, `404`).
* **Level 3 (Hypermedia Controls - HATEOAS)**: Self-describing representations containing navigational hypermedia links (`_links`).
