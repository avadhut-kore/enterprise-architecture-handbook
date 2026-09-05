# Timeout Architecture in Distributed Integration

## 1. The Peril of Missing Timeouts
In distributed enterprise integrations, unbounded timeouts are the single most common cause of catastrophic cascading failure. A single lagging downstream dependency (e.g., a slow database query or locked mainframe socket) holds connection threads, exhausting thread pools and starving all upstream callers until the entire platform crashes.

## 2. Timeout Hierarchy Across the Call Stack

```
[Web / Mobile Client]       (Timeout: 10.0s)
         │
         ▼
[Edge API Gateway]          (Timeout: 8.0s)
         │
         ▼
[Orchestrator Service]      (Timeout: 5.0s)
         │
    ─────┴─────────────────
    │                     │
    ▼                     ▼
[Payment Core] (2.0s)   [Fraud Engine] (800ms)
```

### Golden Rule: Deadlines Must Decrease Downstream
Each layer down the call stack must have a shorter timeout than its upstream caller, accounting for network latency, serialization overhead, and retry budgets.

## 3. Types of Timeouts
1. **Connect Timeout**: Time allowed to establish the TCP handshake and complete TLS negotiation (typically 500ms - 1000ms).
2. **Read / Socket Timeout**: Maximum allowed idle time between incoming data packets from the server (typically 2000ms - 5000ms).
3. **Overall Request Timeout / Deadline**: Total end-to-end time budget allocated for the entire operation. Supported natively by gRPC context deadlines.

## 4. gRPC Context Deadline Propagation
```go
// Client propagating strict timeout deadline
ctx, cancel := context.WithTimeout(context.Background(), 2500*time.Millisecond)
defer cancel()

resp, err := paymentClient.Authorize(ctx, &PaymentRequest{
    PaymentId: "PAY-10029",
    Amount:    5000,
})
if err != nil {
    if status.Code(err) == codes.DeadlineExceeded {
        log.Warn("Payment service exceeded deadline; executing fallback")
    }
}
```
