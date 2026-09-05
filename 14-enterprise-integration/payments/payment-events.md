# Payment Event Streams and Webhook Architecture

## 1. Payment Domain Event Streams
Every state change across the payment lifecycle publishes a standardized CloudEvent to internal event streams (Kafka / EventBridge):
- `com.enterprise.payment.initiated`
- `com.enterprise.payment.authorized`
- `com.enterprise.payment.captured`
- `com.enterprise.payment.settled`
- `com.enterprise.payment.disputed`

## 2. Outbound Webhook Delivery Architecture
Merchant integrations rely on webhooks for asynchronous transaction notifications:
1. **HMAC Signing**: All payloads carry an `X-Signature: sha256=...` header computed using the merchant's private webhook secret.
2. **Backoff Schedule**: Failed webhook deliveries (HTTP non-2xx) retry on an exponential schedule: 1m, 5m, 15m, 1h, 6h, 24h.
3. **Dead Letter Webhooks**: If delivery fails after 72 hours, the notification moves to a customer-visible DLQ portal for manual retry.
