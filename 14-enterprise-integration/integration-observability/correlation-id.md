# Correlation ID Architecture in Multi-System Flows

## 1. Architectural Role of Correlation IDs
While a **Trace ID** tracks technical execution spans across codebases, a **Correlation ID** (often tied to a business transaction like `order_id` or `payment_reference`) provides a human-readable identifier that business analysts, customer support agents, and security auditors can use to search logs across disparate third-party vendor platforms.

## 2. Ingress Generation and Egress Forwarding Pattern
1. **Ingress**: If an incoming request contains `X-Correlation-ID`, validate its format (UUID or standardized prefix). If missing, generate a new UUIDv4 at the edge gateway.
2. **Propagation**: Forward the correlation ID in HTTP headers, gRPC metadata, Kafka record headers, and JMS properties.
3. **Egress**: Include the correlation ID in outbound webhooks and vendor API payloads.
4. **Response**: Echo the `X-Correlation-ID` header back to the client in the HTTP response.
