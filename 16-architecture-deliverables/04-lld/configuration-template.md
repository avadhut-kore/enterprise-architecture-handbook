# LLD Configuration & Environment Schema

| Environment Variable | Type | Default Value | Mandatory | Description |
|---|---|---|---|---|
| `SERVER_PORT` | Integer | `8080` | No | HTTP listener port |
| `DB_JDBC_URL` | String | — | Yes | PostgreSQL connection string |
| `DB_POOL_MAX_SIZE` | Integer | `20` | No | HikariCP max database connections |
| `KAFKA_BOOTSTRAP_SERVERS` | String | — | Yes | Comma-separated broker host:port list |
| `REDIS_CLUSTER_NODES` | String | — | Yes | Redis cluster entry nodes |
