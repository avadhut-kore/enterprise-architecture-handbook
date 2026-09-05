# Chunked Transfer Encoding

## 1. Streaming Payloads of Unknown Size
`Transfer-Encoding: chunked` enables HTTP clients to stream dynamically generated binary streams without pre-computing the `Content-Length` header:
* Payload is transmitted as a series of hex-encoded chunk sizes followed by chunk data.
* Terminates with an empty 0-byte chunk.
