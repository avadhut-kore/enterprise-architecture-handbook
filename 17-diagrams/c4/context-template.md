# C4 Architecture Templates

Minimal, copy-pasteable starter templates in Mermaid and PlantUML.

---

## 1. C4 Context Template (Mermaid)

```mermaid
flowchart TD
    subgraph Users["Users"]
        User["<User Name>
[Person]
<Description of role>"]
    end

    subgraph SystemBoundary["<System Name> Boundary"]
        System["<System Name>
[Software System]
<Description of core capability>"]
    end

    subgraph External["External Systems"]
        ExtSystem["<External System Name>
[Software System]
<Description of dependency>"]
    end

    User -->|<Action: Protocol>| System
    System -->|<Action: Protocol>| ExtSystem
```

---

## 2. C4 Container Template (Mermaid)

```mermaid
flowchart TD
    subgraph Clients["Client Layer"]
        ClientApp["<Client Application>
[Container: Web / Mobile]
<Tech Stack>"]
    end

    subgraph SystemBoundary["<System Name> Boundary"]
        Gateway["<API Gateway>
[Container: Reverse Proxy]
<Tech Stack>"]
        BackendService["<Backend Service>
[Container: Microservice]
<Language / Framework>"]
        MessageQueue["<Message Queue>
[Container: Broker]
<Kafka / RabbitMQ>"]
        Database[("<Database Store>
[Container: Persistence]
<PostgreSQL / MongoDB>")]
    end

    ClientApp -->|HTTPS / JSON| Gateway
    Gateway -->|gRPC / mTLS| BackendService
    BackendService -->|SQL / TCP| Database
    BackendService -.->|AMQP / Publish| MessageQueue
```

---

## 3. C4 Component Template (Mermaid)

```mermaid
flowchart TD
    subgraph ContainerBoundary["<Container Name> Boundary"]
        Controller["<API Controller>
[Component]
Handles HTTP requests and serialization."]
        ServiceHandler["<Domain Service>
[Component]
Executes business logic and workflows."]
        Repository["<Data Repository>
[Component]
Abstracts database persistence operations."]
        ExternalAdapter["<External API Adapter>
[Component]
Translates protocols for third-party systems."]
    end

    subgraph ExternalDeps["External Dependencies"]
        DB[("<Database>")]
        ExtAPI["<External Service>"]
    end

    Controller --> ServiceHandler
    ServiceHandler --> Repository
    ServiceHandler --> ExternalAdapter
    Repository --> DB
    ExternalAdapter --> ExtAPI
```
