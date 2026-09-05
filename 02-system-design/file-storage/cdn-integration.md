# CDN Integration for Media Delivery

## 1. Edge Acceleration for Storage Buckets
Placing Cloudflare or AWS CloudFront in front of an S3 bucket delivers two critical architectural benefits:
1. **Latency Reduction**: Media files are cached at edge PoPs, cutting download latency from $80\text{ ms}$ (origin transit) to $<5\text{ ms}$.
2. **Cost Optimization**: Cloud providers charge $9\text{ cents/GB}$ for direct S3 internet egress, but only $2\text{--}4\text{ cents/GB}$ for CDN transit (with zero origin fetch fees inside the same cloud).
