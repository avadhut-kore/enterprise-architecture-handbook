# Enterprise Metric Design & Naming Standards

## 1. Executive Summary
Without strict naming standards, enterprise metrics devolve into an inconsistent mess of conflicting conventions (`orders_total`, `orderCount`, `orders_per_second`, `num_orders`). Standardized naming allows automated alert templates, generalized Grafana dashboards, and cross-organization analytics.

---

## 2. Canonical Enterprise Naming Formula

All enterprise metrics must follow the OpenTelemetry / Prometheus snake_case naming formula:

$$\underbrace{\text{namespace}}_{\text{Organization / Domain}}\_\underbrace{\text{subsystem}}_{\text{Service / Module}}\_\underbrace{\text{name}}_{\text{Entity being measured}}\_\underbrace{\text{unit}}_{\text{Plural base unit}}$$

```
Examples of Compliant Metric Names:
  - payment_processor_transactions_total          (Counter: Total transactions)
  - order_checkout_duration_seconds               (Histogram: Request duration in seconds)
  - inventory_warehouse_items_count               (Gauge: Current physical inventory)
  - database_connection_pool_active_connections   (Gauge: Current open pool connections)
  - messaging_kafka_consumer_lag_records          (Gauge: Lag in number of records)
```

---

## 3. The 6 Rules of Metric Design

1. **Rule 1: Always Use Base SI Units**:
   - Time must be in **seconds** (`_seconds`), never milliseconds or minutes.
   - Data size must be in **bytes** (`_bytes`), never megabytes or gigabytes.
   - Energy must be in **joules** or **watts**.
2. **Rule 2: Suffix Counters with `_total`**:
   - Any monotonically increasing counter must end with `_total` (e.g., `http_requests_total`).
3. **Rule 3: Keep Metric Names Plural**:
   - Use `orders_total`, not `order_total`; use `bytes_sent`, not `byte_sent`.
4. **Rule 4: Do Not Embed Dimensions in Metric Names**:
   - **Anti-Pattern**: `payment_success_total` and `payment_failure_total`.
   - **Compliant Pattern**: `payment_transactions_total{status="success"}` and `payment_transactions_total{status="failure"}`.
5. **Rule 5: Distinguish Units Clearly**:
   - Ratios must be suffixed with `_ratio` and bounded between $0.0$ and $1.0$ (e.g., `cache_hit_ratio`). Never store ratios as percentages ($0 - 100$).
6. **Rule 6: Mandatory Ownership Labeling**:
   - Every metric must inherit standard resource attributes (`service.name`, `deployment.environment`) from the OpenTelemetry SDK.
