# Module-Based Organization for Modular Monoliths

## 1. Strict Module Encapsulation

```text
modules/
├── Inventory/
│   ├── Inventory.Contracts/    # PUBLIC: Interfaces, DTOs, Integration Events
│   └── Inventory.Internal/     # PRIVATE: Domain logic, EF Core mappings, DB tables
├── Shipping/
│   ├── Shipping.Contracts/     # PUBLIC
│   └── Shipping.Internal/      # PRIVATE
```
Modules depend strictly on other modules' `.Contracts` projects, never on `.Internal`.
