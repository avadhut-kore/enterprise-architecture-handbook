# API Extraction and the Routing Facade Pattern

## 1. Architectural Role of the Facade
The API Facade acts as an abstraction barrier between external clients (mobile apps, web frontends, third-party B2B partners) and the internal service topography. Clients consume a stable, unified API contract unaware of whether a request is fulfilled by the legacy monolith or a newly extracted microservice.

---

## 2. Routing Facade Implementation (Envoy Proxy Example)

```yaml
static_resources:
  listeners:
  - name: ingress_listener
    address:
      socket_address: { address: 0.0.0.0, port_value: 443 }
    filter_chains:
    - filters:
      - name: envoy.filters.network.http_connection_manager
        typed_config:
          "@type": type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager
          route_config:
            name: enterprise_routes
            virtual_hosts:
            - name: api_backend
              domains: ["api.enterprise.com"]
              routes:
              # Extracted Microservice: Orders
              - match: { prefix: "/v1/orders" }
                route:
                  cluster: orders_microservice_cluster
                  timeout: 3.0s
              # Legacy Monolith Fallback: All remaining endpoints
              - match: { prefix: "/" }
                route:
                  cluster: legacy_monolith_cluster
                  timeout: 10.0s
```
