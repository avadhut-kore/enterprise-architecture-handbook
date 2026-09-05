# Mermaid Entity-Relationship (ER) Diagrams

ER diagrams model relational schemas, primary/foreign key mappings, and table cardinalities using Crow's Foot notation.

## E-Commerce Core Relational Schema

```mermaid
erDiagram
    CUSTOMERS ||--o{ ORDERS : places
    ORDERS ||--|{ ORDER_ITEMS : contains
    PRODUCTS ||--o{ ORDER_ITEMS : referenced_in
    ORDERS ||--|| PAYMENTS : settled_by

    CUSTOMERS {
        uuid id PK
        string email
        string full_name
        timestamp created_at
    }

    ORDERS {
        uuid id PK
        uuid customer_id FK
        decimal total_amount
        string status
        timestamp order_date
    }

    ORDER_ITEMS {
        uuid id PK
        uuid order_id FK
        uuid product_id FK
        int quantity
        decimal unit_price
    }

    PRODUCTS {
        uuid id PK
        string sku
        string name
        decimal current_price
    }

    PAYMENTS {
        uuid id PK
        uuid order_id FK
        string provider
        decimal amount
        string status
    }
```

## Crow's Foot Cardinality Syntax
* `||--||` : Exactly one to exactly one
* `||--o{` : One to zero or many
* `||--|{` : One to one or many
* `}o--o{` : Zero or many to zero or many
