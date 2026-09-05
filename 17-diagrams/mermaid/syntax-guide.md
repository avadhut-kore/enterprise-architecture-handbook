# Mermaid Syntax Guide & Architectural Cheatsheet

## Directionality Directives
Mermaid flowcharts support five fundamental layout directions:
* `graph TB` or `graph TD`: Top-to-Bottom / Top-Down (best for hierarchical layers and trees).
* `graph BT`: Bottom-to-Top (best for dependency graphs pointing upward).
* `graph LR`: Left-to-Right (best for data pipelines, queues, and sequence flows).
* `graph RL`: Right-to-Left.

## Node Shape Syntax
```mermaid
graph LR
    Rect[Rectangle: Node]
    Round(Rounded Rectangle: Node)
    Stadium([Stadium Pill: Process])
    Subproc[[Subroutine / External]]
    Cylinder[(Cylinder: Database)]
    Circle((Circle: State))
    Diamond{"Diamond: Decision"}
    Hexagon{{Hexagon: Preparation}}
    Parallelogram[/Parallelogram: I/O/]
    Trap[\Trapezoid: Manual/\]
```

## Line Styles & Link Annotations
```mermaid
graph LR
    A -->|"Solid with Arrow"| B
    C ---|"Solid Line (Undirected)"| D
    E -.->|"Dotted / Dashed Arrow"| F
    G ==>|"Thick / Bold Arrow"| H
    I --x|"Cross Head (Failed / Blocked)"| J
    K --o|"Circle Head (Aggregation)"| L
```

## Special Character Escaping
In Mermaid, avoid unquoted parentheses, square brackets, or semicolons inside node names. Always wrap node labels in double quotes:
* Correct: `DB[("PostgreSQL Database (Cluster)")]`
* Incorrect: `DB[(PostgreSQL Database (Cluster))]`
