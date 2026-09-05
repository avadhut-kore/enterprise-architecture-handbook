# Modern SAP API Integration Architecture

## 1. Overview & Strategy
SAP S/4HANA exposes modern APIs through the SAP Business Accelerator Hub (`api.sap.com`). Integration architects must adhere to the **Clean Core** paradigm by strictly utilizing public, standard APIs (OData v2/v4, REST, SOAP) rather than custom ABAP RFC function modules.

## 2. Communication Scenarios and Communication Arrangements
In S/4HANA Cloud and on-premise:
- **Communication Scenario**: Grouping of related APIs (e.g., `SAP_COM_0008` for Business Partner integration).
- **Communication User**: Dedicated service account authenticated via OAuth 2.0 or mutual TLS certificates.
- **Communication Arrangement**: Runtime binding linking the communication scenario to an authenticated user and technical endpoint.

## 3. Recommended Architectural Patterns
- Utilize the SAP Cloud SDK (Java / TypeScript) for type-safe client consumption with built-in resilience, tenancy, and destination caching.
- Buffer high-frequency inbound invocations through an enterprise API gateway (Kong, Envoy, Apigee) to prevent overloading the SAP application server dialog processes.
