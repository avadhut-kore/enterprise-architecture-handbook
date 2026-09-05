# Clean Architecture (Onion & Dependency Inversion)

Robert C. Martin's Clean Architecture concentric circles enforcing the fundamental Dependency Rule: source code dependencies must point inward.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph CleanCircles ["The Dependency Rule (Inward Flow)"]
        subgraph OuterCircle ["Frameworks & Drivers (Blue)"]
            UI["Web UI / Mobile Apps"]
            DB["PostgreSQL / DynamoDB"]
            Ext["External Devices & Cloud SDKs"]
            
            subgraph GreenCircle ["Interface Adapters (Green)"]
                Presenters["Controllers & Presenters"]
                Gateways["Database Gateways"]
                
                subgraph RedCircle ["Application Business Rules (Red)"]
                    UseCases["Use Cases / Interactors"]
                    
                    subgraph YellowCircle ["Enterprise Business Rules (Yellow)"]
                        Entities["Entities / Aggregate Roots / Value Objects"]
                    end
                end
            end
        end
    end

    UI --> Presenters
    DB --> Gateways
    Presenters --> UseCases
    Gateways --> UseCases
    UseCases --> Entities

    classDef blue fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef green fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef red fill:#ffebee,stroke:#c62828,stroke-width:2px;
    classDef yellow fill:#fffde7,stroke:#fbc02d,stroke-width:2px;
    class OuterCircle,UI,DB,Ext blue;
    class GreenCircle,Presenters,Gateways green;
    class RedCircle,UseCases red;
    class YellowCircle,Entities yellow;
```

## PlantUML Specification

```plantuml
@startuml
rectangle "1. Frameworks & Drivers (Web, DB, Devices)" as c1 #e1f5fe {
  rectangle "2. Interface Adapters (Controllers, Gateways)" as c2 #e8f5e9 {
    rectangle "3. Use Cases (Application Rules)" as c3 #ffebee {
      rectangle "4. Entities (Enterprise Business Rules)" as c4 #fffde7
    }
  }
}
c1 --> c2 : Inward Dependency
c2 --> c3 : Inward Dependency
c3 --> c4 : Inward Dependency
@enduml
```

## Architectural Design Considerations

* **The Dependency Rule**: Nothing in an inner circle can know anything at all about something in an outer circle (no imports, no data formats).
* **Entities**: Encapsulate most general and high-level enterprise business rules; least likely to change when external factors change.
* **Use Cases**: Coordinate the flow of data to and from entities, executing user intents.

## Related Documentation & Patterns

* [Hexagonal Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/application/hexagonal.md)
* [Layered Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/application/layered.md)
* [Low-Level Design](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/architecture/low-level-design.md)
