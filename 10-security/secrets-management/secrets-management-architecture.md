# Secrets Management Architecture: Static vs Dynamic Secrets

## Executive Summary

- **Static Secrets (Legacy)**: Passwords created by engineers, stored in configuration, and unchanged for months. High risk of leak.
- **Dynamic Secrets (Modern Standard)**: Ephemeral credentials generated on-the-fly by secret engines (e.g., HashiCorp Vault generates a unique PostgreSQL user with a 1-hour lease). When the lease expires, Vault automatically drops the user from the database.
