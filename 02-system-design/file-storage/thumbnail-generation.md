# Thumbnail & Image Pipeline Architecture

## 1. On-Demand vs. Pre-Generated Thumbnails
* **Pre-Generated (E-Commerce Standard)**: Upon user upload, background workers generate standard dimensions ($64\times 64$, $256\times 256$, $1024\times 1024$) in WebP/AVIF formats.
* **Dynamic Edge Resize (Cloudflare Images / Thumbor)**: An edge worker resizes images dynamically on the fly based on query parameters (`/image.jpg?w=200&h=200`), caching the result at edge PoPs.
