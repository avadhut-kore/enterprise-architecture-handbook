# Edge Computing & Modern CDN Architecture

## 1. Edge Compute Architecture

Edge platforms (Cloudflare Workers, Fastly Compute@Edge, AWS Lambda@Edge) execute code across hundreds of globally distributed edge PoPs within 15ms of end users:

```mermaid
flowchart TD
    User["Global User (London)"] --> Anycast["Anycast BGP Ingress (London Edge PoP / 5ms)"]
    
    subgraph EdgePoP ["Edge Compute Runtime (V8 Isolates / Wasm)"]
        AuthCheck["Verify JWT Signature (Local JWKS Cache)"]
        GeoRouting["Geo-IP & Compliance Filter"]
        EdgeCache[("Edge Key-Value Cache")]
    end

    Anycast --> EdgePoP
    EdgeCache -->|Cache Hit (8ms)| User
    EdgePoP -->|Cache Miss| Origin["Central Cloud Origin (US-East / 80ms)"]
```
