# The ISO 20022 Message Model Hierarchy

## 1. The Three-Layer Modeling Methodology
```
Level 1: Business Conceptual Model
└── Pure business domain concepts (Account, Party, Payment, Instrument)

Level 2: Logical Data Model
└── Technology-independent logical schemas and constraints

Level 3: Physical Syntax Schema (XSD)
└── Executable XML Schemas (and emerging JSON-LD bindings)
```

## 2. Standard Message Identifier Syntax
ISO 20022 messages follow a four-part naming convention: `aaaa.bbb.ccc.dd`:
- `aaaa`: Business Domain (e.g., `pacs`, `pain`, `camt`, `remt`).
- `bbb`: Message Functionality (e.g., `008` = Customer Credit Transfer).
- `ccc`: Variant / Flavor (e.g., `001`).
- `dd`: Version (e.g., `10`).
