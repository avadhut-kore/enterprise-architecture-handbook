# Architecture Modernization: Strangler Fig Application Migration

## 1. Architectural Objective & Context

Incrementally replace specific capabilities of an existing monolithic enterprise application with modern services by intercepting calls at the perimeter until the legacy system is completely deprecated and removed.

---

## 2. Architectural Blueprint: Edge Proxy Interception

```mermaid
flowchart TB
    Client[Client Applications]
    EdgeProxy[Strangler Intercepting Reverse Proxy (Envoy/Kong)]

    subgraph LegacyEstate [Legacy Monolith]
        LegacyApp[Monolithic Application]
        LegacyCart[Legacy Cart Logic]
        LegacyCheckout[Legacy Checkout Logic]
    end

    subgraph ModernEstate [Modern Microservices Fleet]
        NewAuth[New Identity Service]
        NewCatalog[New Catalog Service]
    end

    Client --> EdgeProxy
    EdgeProxy -->|/api/auth/*| NewAuth
    EdgeProxy -->|/api/products/*| NewCatalog
    EdgeProxy -->|/* (All Other Paths)| LegacyApp

    LegacyApp -.-> LegacyCart
    LegacyApp -.-> LegacyCheckout
```

---

## 3. Step-by-Step Modernization Execution

1. **Deploy Interceptor Proxy**: Place an API Gateway or reverse proxy directly between all incoming traffic and the legacy application. Configure it to route 100% of traffic to the legacy app initially.
2. **Identify Smallest Discrete Vertical Slice**: Choose a well-defined bounded context (e.g., User Authentication or Product Catalog).
3. **Build the Replacement Microservice**: Implement the modern service adhering to the same API contract or using an Anti-Corruption Layer for translation.
4. **Re-route Gateway Path**: Update the gateway route for that specific URL prefix (e.g., `/api/auth`) to point to the new service.
5. **Repeat Incrementally**: Strangle remaining modules one by one until the legacy application contains no active paths.
6. **Decommission**: Terminate the legacy application instances and reclaim infrastructure.

---

## 4. Key Architectural Traps

- **Shared Stateful Sessions**: If the legacy app stores user sessions in local server memory, users will be logged out when visiting strangler services. Externalize sessions into a shared Redis store first.
- **Creeping Scope**: Keep strangler slices small and focused. Do not attempt to redesign 10 features at once inside a single slice.
