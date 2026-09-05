# Load Balancer Configuration Standards
* Health check paths `/healthz` must check internal connectivity; return 503 within 3 seconds if unhealthy.
