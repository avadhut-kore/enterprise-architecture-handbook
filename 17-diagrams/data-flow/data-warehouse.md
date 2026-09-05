# Enterprise Data Warehouse (EDW) Architecture & Dimensional Modeling

Classic Kimball dimensional modeling architecture detailing Star Schemas, Conformed Dimensions, Fact Tables, and Data Mart presentation layers.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph StagingLayer ["Ingestion & Staging Area"]
        StageTables[("Stage DB: Raw Tables<br/>stg_orders, stg_users, stg_inventory")]
    end

    subgraph CentralWarehouse ["Enterprise Data Warehouse (Star Schema)"]
        FactOrders[("FACT: fact_sales_order<br/>- order_id (PK)<br/>- customer_key (FK)<br/>- date_key (FK)<br/>- product_key (FK)<br/>- quantity<br/>- total_revenue")]

        DimCust[("DIM: dim_customer<br/>- customer_key (PK)<br/>- customer_id (NK)<br/>- full_name<br/>- city, state, country<br/>- scd_start, scd_end (SCD Type 2)")]
        
        DimProd[("DIM: dim_product<br/>- product_key (PK)<br/>- sku, category, brand")]
        
        DimDate[("DIM: dim_date<br/>- date_key (PK)<br/>- day, month, quarter, year")]

        FactOrders --- DimCust
        FactOrders --- DimProd
        FactOrders --- DimDate
    end

    subgraph DepartmentMarts ["Departmental Data Marts"]
        FinanceMart["Finance Data Mart<br/>(Revenue, Taxes, Margins)"]
        SupplyMart["Supply Chain Mart<br/>(Inventory Velocity, Fill Rate)"]
        MarketingMart["Marketing Mart<br/>(LTV, CAC, Retention)"]

        FactOrders --> FinanceMart
        FactOrders --> SupplyMart
        FactOrders --> MarketingMart
    end

    StageTables -->|"ELT Merge & Dimension Lookup"| CentralWarehouse

    classDef fact fill:#ffecb3,stroke:#ff6f00,stroke-width:2px;
    classDef dim fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    class FactOrders fact;
    class DimCust,DimProd,DimDate dim;
```

## PlantUML Specification

```plantuml
@startuml
class "dim_customer" as cust {
  * customer_key : PK (Surrogate)
  customer_id : Natural Key
  full_name : String
  tier : String
  effective_date : Date
  expiration_date : Date
}

class "dim_product" as prod {
  * product_key : PK
  sku : String
  category : String
  price : Decimal
}

class "dim_date" as dt {
  * date_key : PK (YYYYMMDD)
  calendar_day : Integer
  month_name : String
  fiscal_quarter : String
}

class "fact_sales_order" as fact {
  * order_item_id : PK
  -- Foreign Keys --
  customer_key : FK
  product_key : FK
  date_key : FK
  -- Measures --
  unit_quantity : Integer
  net_revenue : Decimal
  tax_amount : Decimal
}

fact --> cust
fact --> prod
fact --> dt
@enduml
```

## Architectural Design Considerations

* **Surrogate Keys**: Always generate integer surrogate keys for dimensions to decouple warehouse history from operational source database natural keys.
* **Slowly Changing Dimensions (SCD)**: Implement SCD Type 2 (with `start_date`, `end_date`, and `is_current` flags) to preserve complete historical fidelity.
* **Conformed Dimensions**: Ensure shared dimensions (Customer, Product, Date) are standardized across the enterprise to enable cross-departmental drill-downs.

## Related Documentation & Patterns

* [Data Lake](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/data-lake.md)
* [Modern Lakehouse](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/lakehouse.md)
* [Batch ETL](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/etl.md)
