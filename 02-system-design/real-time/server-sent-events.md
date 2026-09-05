# Server-Sent Events (SSE) Architecture

## 1. Unidirectional Server-to-Client Streaming
Server-Sent Events (SSE) is an HTTP standard (`text/event-stream`) enabling servers to continuously push asynchronous text updates to clients over a persistent HTTP/2 or HTTP/1.1 connection.

```http
HTTP/1.1 200 OK
Content-Type: text/event-stream
Cache-Control: no-cache
Connection: keep-alive

event: stock_tick
id: 10482
data: {"symbol": "AAPL", "price": 224.50}

event: stock_tick
id: 10483
data: {"symbol": "GOOG", "price": 178.10}
```

---

## 2. When SSE Trumps WebSockets
* **Built-in Automatic Reconnection**: Native browser `EventSource` automatically reconnects upon disconnection, sending `Last-Event-ID` header so the server resumes streaming without data loss.
* **HTTP/2 Multiplexing**: Over HTTP/2, dozens of SSE streams share a single TCP connection, eliminating port exhaustion.
* **Firewall & Proxy Compatibility**: Runs over standard HTTPS port 443; zero firewall blocking.
* *Ideal Fit*: GenAI LLM token streaming (ChatGPT style), live financial tickers, real-time sports scores.
