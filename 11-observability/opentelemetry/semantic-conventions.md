# OpenTelemetry Semantic Conventions

## 1. Executive Summary
Telemetry without standardized naming is incomprehensible across an enterprise. If Service A records HTTP status as `http.status`, Service B records it as `response_code`, and Service C records it as `statusCode`, automated correlation, cross-service dashboards, and generalized alerting break down.

The **OpenTelemetry Semantic Conventions** establish standard names and types for span attributes, metric names, and resource attributes across HTTP, database, RPC, and messaging domains.

---

## 2. Standard Resource Attributes

Attached to every metric, log, and span emitted by a process:

| Attribute Key | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `service.name` | `string` | Logical name of the service (Mandatory). | `payment-auth-service` |
| `service.version` | `string` | Version or Git commit SHA of the service. | `2.4.1` |
| `service.instance.id` | `string` | Unique instance or container identifier. | `pod-7f9b8c-x14` |
| `deployment.environment` | `string` | Stage environment name. | `production`, `staging` |

---

## 3. Standard HTTP Span Attributes (Client & Server)

| Attribute Key | Direction | Requirement | Example |
| :--- | :--- | :--- | :--- |
| `http.request.method` | Ingress / Egress | Required | `POST`, `GET` |
| `http.response.status_code` | Ingress / Egress | Required | `200`, `500` |
| `url.path` | Ingress | Required | `/api/v1/checkout` |
| `http.route` | Ingress | Recommended (Low Cardinality) | `/api/v1/users/{id}` |
| `url.full` | Egress | Conditional | `https://api.stripe.com/v1/charges` |
| `network.peer.address` | Client / Server | Recommended | `10.244.3.18` |

---

## 4. Standard Database Client Span Attributes

| Attribute Key | Requirement | Description | Example |
| :--- | :--- | :--- | :--- |
| `db.system` | Required | Database management system type. | `postgresql`, `mysql`, `redis` |
| `db.name` | Recommended | Name of the database catalog. | `customer_ledger` |
| `db.operation` | Required | Operation being performed. | `SELECT`, `INSERT`, `HGET` |
| `db.collection.name` | Recommended | Table or collection name. | `users`, `orders` |
| `db.query.text` | Optional (Sanitized) | Parameterized query string (No literals!). | `SELECT * FROM orders WHERE id = ?` |

---

## 5. Standard Messaging (Kafka / MQ) Span Attributes

| Attribute Key | Direction | Description | Example |
| :--- | :--- | :--- | :--- |
| `messaging.system` | Producer / Consumer | Messaging platform name. | `kafka`, `rabbitmq` |
| `messaging.destination.name`| Producer / Consumer | Topic or queue name. | `payment.completed.v1` |
| `messaging.operation` | Producer / Consumer | Operation type. | `publish`, `receive`, `settle` |
| `messaging.kafka.consumer.group`| Consumer | Kafka consumer group name. | `fraud-detection-workers` |
| `messaging.kafka.message.offset`| Consumer | Message offset partition index. | `41829` |
