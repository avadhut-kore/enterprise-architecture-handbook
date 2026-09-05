# C4-PlantUML Standard Library Architecture Modeling

C4-PlantUML is the industry standard for publishing professional C4 diagrams using PlantUML macros.

## C4 Container Architecture Diagram

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

Person(customer, "Banking Customer", "Customer of the bank.")
System_Boundary(c1, "Internet Banking") {
  Container(spa, "Single-Page App", "React", "Provides banking UI")
  Container(api, "API Gateway", "Go, Envoy", "Routing & Auth")
  Container(backend, "Core Banking API", "Java", "Processes transactions")
  ContainerDb(db, "Core Database", "PostgreSQL", "Stores customer accounts")
}
System_Ext(mainframe, "Mainframe Core", "Legacy settlement engine")

Rel(customer, spa, "Uses", "HTTPS")
Rel(spa, api, "API calls", "JSON/HTTPS")
Rel(api, backend, "Routes", "gRPC")
Rel(backend, db, "Reads/Writes", "JDBC")
Rel(backend, mainframe, "Settles", "MQ Series")
@enduml
```

## Architectural Guidelines
* Include C4-PlantUML standard library files directly from GitHub or vendor them locally.
* Use `Person`, `System`, `Container`, and `Rel` macros for consistent color tokens and shape semantics.
