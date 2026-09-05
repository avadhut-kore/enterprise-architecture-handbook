# Programmable Integration Engines: Apache Camel

## 1. Enterprise Integration Patterns as Code
Apache Camel implements standard Enterprise Integration Patterns (EIP) natively in Java, Kotlin, or YAML:
```java
from("kafka:orders.incoming?brokers=broker.internal:9092")
    .routeId("order-enrichment-pipeline")
    .unmarshal().json(JsonLibrary.Jackson, OrderDTO.class)
    .enrich("direct:fetch-customer-credit", new CreditEnrichmentAggregator())
    .choice()
        .when(simple("${body.creditApproved} == true"))
            .marshal().json()
            .to("kafka:orders.approved")
        .otherwise()
            .to("direct:order-cancellation-saga")
    .end();
```
