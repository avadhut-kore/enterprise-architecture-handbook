# Case Study: Airbnb Booking Engine & Inventory Concurrency

## 1. Company & Business Context

Airbnb operates an online marketplace for vacation rentals and experiences, listing over 7.7 million active accommodations across 220 countries. Unlike hotel chains where rooms in a category are interchangeable fungible inventory, Airbnb listings are **unique, single-instance assets**: a physical apartment in Paris can only be booked by one guest for any given calendar night.

The primary architectural requirement is preventing double bookings under high concurrent traffic spikes (e.g., New Year's Eve in New York) while supporting complex pricing rules, temporal calendar holds, instant book flows, and host approvals.

---

## 2. Scale & Workload Profile

```
+------------------------------------+---------------------------------------+
| Metric                             | Production Volume                     |
+------------------------------------+---------------------------------------+
| Active Listings Worldwide          | 7.7+ Million Unique Properties        |
| Annual Guest Bookings              | > 450 Million Nights Booked           |
| Concurrent Checkout Attempts       | Thousands per Minute per Hot Listing  |
| Calendar Search QPS                | > 100,000 Search Queries / Second     |
| Double-Booking Tolerance Rate      | Strict Zero Double-Booking Invariant  |
| Availability Search Freshness      | < 1 Second Post-Reservation           |
+------------------------------------+---------------------------------------+
```

---

## 3. Original Architecture (The Ruby on Rails Monolith)

Airbnb started on a monolithic Rails application ("Monomyth"):
- **Row Locking in MySQL**: Reservations locked listing rows using `SELECT FOR UPDATE`.
- **Contention & Deadlocks**: During popular booking events, multiple guests attempted to checkout for the same dates, creating severe lock contention, query timeouts, and cascading connection starvation across the web servers.

---

## 4. Modern Target Architecture: Distributed Booking Engine & Temporal Holds

Airbnb transitioned to a service-oriented architecture (SOA) featuring a dedicated Booking Engine, Temporal Calendar Service, and distributed locking coordination.

```mermaid
flowchart TB
    subgraph GuestLayer [Guest Checkout]
        Guest[Guest Browser / App]
    end

    subgraph APITier [API Gateway & Orchestration]
        APIGateway[Edge Gateway]
        CheckoutService[Checkout Orchestrator]
    end

    subgraph ReservationCore [Booking Engine Services]
        LockManager[Distributed Lock Manager (Redlock)]
        CalendarService[Calendar & Availability Service]
        PricingService[Dynamic Pricing Engine]
        PaymentGateway[Payments Service]
    end

    subgraph DataTier [Storage & Event Stream]
        MySQLSharded[(Sharded MySQL Reservation DB)]
        KafkaEvents[Reservation Kafka Event Bus]
        SearchIndexer[Elasticsearch Search Index]
    end

    Guest -->|1. Request Hold (listing_id, dates)| APIGateway
    APIGateway --> CheckoutService
    CheckoutService --> LockManager
    LockManager -->|2. Acquire Mutex| CalendarService
    CalendarService -->|3. Verify & Place 15-min Soft Hold| MySQLSharded
    CheckoutService --> PricingService
    CheckoutService --> PaymentGateway
    PaymentGateway -->|4. Authorize Card| PaymentGateway
    CheckoutService -->|5. Commit Hard Reservation| MySQLSharded
    LockManager -->|6. Release Mutex| CalendarService
    MySQLSharded --> KafkaEvents
    KafkaEvents --> SearchIndexer
```

---

## 5. Architectural Inventions & Mechanics

### A. Two-Phase Reservation Protocol (Soft Hold to Hard Booking)
To prevent holding database locks while waiting for payment processor network calls:
1. **Phase 1: Soft Hold (15 Minutes)**:
   - When a guest begins checkout, an atomic record is written to the Calendar service reserving the dates with a status of `TENTATIVE_HOLD` and a short TTL timestamp.
   - Other guests viewing the listing immediately see the dates as unavailable.
   - If the guest abandons checkout or payment fails, the hold expires automatically without administrative cleanup.
2. **Phase 2: Hard Commitment**:
   - Once the payment gateway confirms authorization, the status transitions to `CONFIRMED` via an atomic state machine update.

### B. Bounded Context & Eventual Search Indexing
- The search cluster (Elasticsearch) does not participate in the transactional booking flow.
- When reservations are committed in MySQL, a Change Data Capture (CDC) pipeline emits an event to Kafka.
- Downstream consumer services update the search index asynchronously within hundreds of milliseconds.
- Stale search results (showing an occupied listing as available) are intercepted at checkout time by the Calendar Service's authoritative check.

### C. Sharded MySQL with Optimistic Versioning
- Reservations are sharded by `listing_id`.
- The database uses optimistic locking via integer version columns:
  $$\text{UPDATE calendars SET status = 'BOOKED', version = version + 1 WHERE listing\_id = ? AND date = ? AND version = ?}$$
- If another checkout updated the calendar first, the statement affects zero rows and triggers an immediate conflict response without blocking worker threads.

---

## 6. Distributed Trade-Offs & Decisions

```
+-----------------------------------+----------------------------------------+
| Dimension                         | Airbnb Architectural Choice            |
+-----------------------------------+----------------------------------------+
| Booking Invariant Model           | Strict CP for Reservation, AP for Search|
| Lock Duration                     | Short Memory Lock, Decoupled Async Pay |
| Storage Strategy                  | Sharded MySQL Partitioned by listing_id|
| Search Availability Sync          | Asynchronous Eventual Consistency (CDC)|
+-----------------------------------+----------------------------------------+
```

---

## 7. Engineering Lessons & Enterprise Takeaways

1. **Never Hold Database Locks Across External API Calls**: External payment processors take 500ms–2000ms. Holding database locks across network boundaries guarantees database collapse. Use soft holds with timeouts.
2. **Partition Around the Contention Entity**: Sharding reservations by `listing_id` ensures all updates for a single apartment execute against a single database shard, avoiding distributed cross-shard transactions.
3. **Embrace Asymmetry in Availability**: It is acceptable for search results to be slightly stale as long as the checkout gateway strictly validates availability authoritatively before processing payment.
