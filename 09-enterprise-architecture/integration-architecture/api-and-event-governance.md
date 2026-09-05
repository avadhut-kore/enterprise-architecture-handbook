# API & Event Governance

Policies and automated gates ensuring interface contracts remain backward compatible, secure, and discoverable.

---

## 1. API Governance Rules
1. **Contract-First Design**: OpenAPI 3.0 / Protobuf specifications must be authored and approved before writing implementation code.
2. **Strict Semantic Versioning**:
   * Patch ($v1.0.1$): Bug fixes, no contract change.
   * Minor ($v1.1.0$): Additive non-breaking field additions.
   * Major ($v2.0.0$): Breaking changes (field removal or schema type change). Must support $N$ and $N-1$ versions concurrently for a 12-month deprecation window.
3. **No Direct Database Integration**: Applications must never read or write directly to another team's database; all integration occurs through governed APIs or published event topics.

---

## 2. Event Schema Registry
All event payloads published to Kafka or message brokers must be governed by a centralized Schema Registry (e.g., Confluent Schema Registry / AWS Glue).
* **Compatibility Enforcement**: Schema Registry set to `BACKWARD` or `FULL` compatibility, rejecting any producer PR that introduces breaking schema changes.
