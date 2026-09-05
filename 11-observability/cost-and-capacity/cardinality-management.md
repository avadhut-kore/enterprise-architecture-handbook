# Metric Cardinality Management & Explosion Control

## 1. Executive Summary
A **Cardinality Explosion** occurs when a metric label contains an unbounded or high-entropy set of values (such as `user_id`, `email`, `credit_card_number`, `order_uuid`, or dynamic query strings).

Because time-series databases allocate memory and index blocks for every unique permutation of metric name and label key-value pairs, a single runaway label can generate **millions of active time series within minutes**, crashing Prometheus servers and generating massive SaaS overage bills.

---

## 2. The Multiplicative Mathematics of Cardinality

$$\text{Total Time Series} = \prod_{i=1}^{N} \text{Cardinality of Label } i$$

### Numerical Example:
Suppose a developer defines an innocent-looking HTTP metric:
```
http_requests_total{service="checkout", method="POST", status="200", user_id="12345"}
```
- `service` = 1 value
- `method` = 4 values (`GET`, `POST`, `PUT`, `DELETE`)
- `status` = 5 values (`200`, `400`, `401`, `404`, `500`)
- `user_id` = **1,000,000 unique active users**
- **Resulting Active Series**:
  $$1 \times 4 \times 5 \times 1,000,000 = \mathbf{20,000,000 \text{ Active Time Series!}}$$
This will instantly crash standard Prometheus pods and incur tens of thousands of dollars in cloud SaaS penalties.

---

## 3. Production Prometheus Metric Relabeling Defense

To protect the metrics backend, edge collectors and Prometheus instances must enforce aggressive relabeling drop rules:

```yaml
# /etc/prometheus/scrape_configs/checkout.yaml
scrape_configs:
  - job_name: "checkout_service"
    kubernetes_sd_configs:
      - role: pod
    metric_relabel_configs:
      # DEFENSE 1: Drop high-cardinality labels automatically
      - regex: "(user_id|email|order_id|session_token)"
        action: labeldrop

      # DEFENSE 2: Normalize unbounded path endpoints
      # Convert /orders/a1b2-c3d4-e5f6 into /orders/:id
      - source_labels: [__name__, path]
        regex: "http_requests_total;/orders/[a-f0-9\\-]+"
        target_label: path
        replacement: "/orders/:id"

      # DEFENSE 3: Hard limit on total series scraped per scrape target
    sample_limit: 10000  # Discards scrape if pod exceeds 10k unique series
```
