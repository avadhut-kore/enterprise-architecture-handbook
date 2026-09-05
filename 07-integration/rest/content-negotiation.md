# HTTP Content Negotiation

## 1. Proactive Client Negotiation
Content negotiation enables a single URI to serve multiple distinct representations based on client preferences declared in request headers:

* **Payload Format**: `Accept: application/json, application/x-protobuf;q=0.9`
* **Compression**: `Accept-Encoding: gzip, deflate, br, zstd`
* **Localization**: `Accept-Language: fr-CH, fr;q=0.9, en;q=0.8`

---

## 2. Server Response
The server evaluates client preferences against supported capabilities, returning the negotiated representation alongside the `Vary` header:
```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Encoding: zstd
Vary: Accept, Accept-Encoding
```
* *The `Vary` Header*: Critical for CDN caches; instructs edge proxies to cache separate responses for distinct `Accept-Encoding` formats.
