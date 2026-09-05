# PlantUML Syntax Guide & Architectural Cheatsheet

## Fundamental Directives
All PlantUML blocks begin with `@startuml` and terminate with `@enduml`.

## Skinparam Modernization Defaults
Add these defaults to prevent default retro yellow/red UML styling:
```plantuml
@startuml
skinparam handwritten false
skinparam monochrome false
skinparam shadowing false
skinparam defaultFontName "Segoe UI", Arial, sans-serif
skinparam defaultFontSize 12
skinparam roundcorner 6
@enduml
```

## Architectural Elements
* Component: `[Component Name]` or `component "Name" as id`
* Database: `database "DB Name" as db`
* Queue: `queue "Topic Name" as q`
* Node/Server: `node "Host Machine" as host`
* Interface: `interface "REST API" as iface`

## Connector Arrows
* Sync call: `A -> B : Message`
* Async message: `A ->> B : Event`
* Return response: `B --> A : Result`
* Dependency: `A ..> B : Depends on`
