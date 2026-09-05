# Architecture Comparison: Polling vs WebSockets vs SSE

## 1. Architectural Trade-Off Matrix

```
+--------------------------+-----------------------+-----------------------+-----------------------+
| Architectural Dimension  | Short / Long Polling  | Server-Sent Events SSE| WebSockets            |
+--------------------------+-----------------------+-----------------------+-----------------------+
| Directionality           | Unidirectional (Req)  | Unidirectional (Push) | Bidirectional (Duplex)|
| Transport Protocol       | Standard HTTP/1.1 or 2| HTTP/2 persistent     | TCP Upgrade Protocol  |
| Connection State         | Stateless per request | Stateful persistent   | Stateful persistent   |
| Overhead per Message     | High (HTTP headers)   | Low (Framed text)     | Minimal (2-byte frame)|
| Proxy & Firewall Friendly| 100% Native           | 100% Native           | May require WSS bypass|
| Reconnection Handling    | Client controlled     | Automatic built-in    | Manual client code    |
| Best Use Case            | Infrequent check-ins  | Dashboards, LLM stream| Chat, Real-Time Gaming|
+--------------------------+-----------------------+-----------------------+-----------------------+
```

---

## 2. Decision Tree

```
Do you require full-duplex communication (client and server sending data continuously)?
├── YES ──► Choose WebSockets (e.g., Multiplayer gaming, live interactive whiteboard)
└── NO  ──► Do you only need server-to-client streaming (e.g., LLM tokens, stock ticker)?
              ├── YES ──► Choose Server-Sent Events (SSE over HTTP/2)
              └── NO  ──► Choose Polling with Exponential Backoff
```
