# C4-Mermaid Native Architecture Modeling

Mermaid natively supports C4 model diagrams using the `C4Context`, `C4Container`, and `C4Component` keywords.

## C4 Container Diagram in Pure Mermaid

```mermaid
C4Container
    title Container Diagram for Internet Banking System

    Person(customer, "Banking Customer", "A customer of the bank with personal bank accounts.")

    System_Boundary(c1, "Internet Banking System") {
        Container(spa, "Single-Page App", "JavaScript, React", "Delivers banking features via browser.")
        Container(mobile, "Mobile App", "Flutter", "Provides banking functionality on iOS and Android.")
        Container(api, "API Gateway", "Go, Envoy", "Routes requests, validates JWT tokens, rate limiting.")
        Container(backend, "Core Banking API", "Java, Spring Boot", "Handles funds transfers and ledger operations.")
        ContainerDb(db, "Core Database", "PostgreSQL", "Stores customer records, accounts, and transactions.")
    }

    System_Ext(mainframe, "Mainframe Banking Core", "Legacy transaction processing.")
    System_Ext(email, "Email Service", "Sends transactional email notifications.")

    Rel(customer, spa, "Uses", "HTTPS")
    Rel(customer, mobile, "Uses", "HTTPS")
    Rel(spa, api, "API calls", "JSON/HTTPS")
    Rel(mobile, api, "API calls", "JSON/HTTPS")
    Rel(api, backend, "Routes to", "gRPC")
    Rel(backend, db, "Reads & writes", "JDBC")
    Rel(backend, mainframe, "Settles transactions", "MQ Series")
    Rel(backend, email, "Sends emails", "SMTP")
```

## Architectural Guidelines
* C4-Mermaid provides standardized C4 colors and shapes automatically without requiring manual `classDef` styling.
