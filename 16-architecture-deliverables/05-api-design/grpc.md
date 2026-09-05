# gRPC & Protocol Buffers Standards

## 1. Protobuf Standards
* File naming: `package enterprise.order.v1;`
* Use standard Google Protobuf types (`google.protobuf.Timestamp`, `google.type.Money`).
* Never reuse or change field tags (`int32 order_id = 1;`). Reserved tags must be explicitly marked.
