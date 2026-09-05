# SAD-ECOM-001: Global E-Commerce Solution Architecture Document
* **Architecture**: Event-driven microservices running on AWS EKS with Aurora PostgreSQL.
* **Core Flows**: Checkout Gateway $ightarrow$ Checkout Service $ightarrow$ Kafka Broker $ightarrow$ Warehouse Fulfillment.
