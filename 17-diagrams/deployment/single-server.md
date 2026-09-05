# Single-Server Deployment Topology (LAMP / Monolith)

```mermaid
flowchart TD
    subgraph Host["Single Virtual Machine / Bare Metal Host"]
        NGINX["Nginx Reverse Proxy & Static Files"]
        App["Application Server (PHP / Node / Python)"]
        DB[("Local Database (PostgreSQL / MySQL)")]
    end
    Internet["Internet Users"] -->|Port 443 (HTTPS)| NGINX
    NGINX -->|Unix Socket / Localhost| App
    App -->|Localhost TCP 5432| DB
```
