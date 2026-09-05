# Mermaid Diagram Lint & Review Checklist

Use this checklist to verify that Mermaid diagrams render cleanly without syntax errors across GitHub, Azure DevOps, and documentation portals.

- [ ] Does the diagram render without syntax errors in GitHub/GitLab preview?
- [ ] Are all node labels containing special characters (parentheses, brackets, colons) wrapped in double quotes (`["Label (with Parens)"]`)?
- [ ] Is diagram directionality explicitly defined (`graph TB` or `graph LR`)?
- [ ] Are connections labeled with protocols (e.g., `HTTPS`, `gRPC`, `Kafka`)?
- [ ] Are subgraphs given both a unique machine ID and a descriptive display title (`subgraph S1 ["Display Title"]`)?
- [ ] Are consistent `classDef` color styles applied across different functional tiers?
- [ ] Are sequence diagrams numbered with `autonumber`?
- [ ] Does the diagram remain readable on mobile or narrow viewport screens?
