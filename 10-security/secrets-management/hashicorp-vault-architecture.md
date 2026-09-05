# HashiCorp Vault Enterprise Architecture

## Executive Summary

HashiCorp Vault provides a unified API for managing secrets, certificates, and encryption as a service.

---

## Dynamic Database Credentials Workflow

```mermaid
sequenceDiagram
    autonumber
    participant App as Microservice Pod
    participant Vault as HashiCorp Vault
    participant DB as PostgreSQL Database

    App->>Vault: Authenticates via Kubernetes Service Account JWT
    Vault-->>App: Issues Vault Token (1-hour lease)
    App->>Vault: GET /database/creds/payment-role
    Vault->>DB: CREATE USER 'v_token_492' WITH PASSWORD '...' VALID UNTIL '1 hour';
    Vault-->>App: Returns ephemeral username & password
    App->>DB: Connects to database using dynamic credentials
    Note over App,Vault: 1 hour elapses; App does not renew lease
    Vault->>DB: REVOKE & DROP USER 'v_token_492';
```
