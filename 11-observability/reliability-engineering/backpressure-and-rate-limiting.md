# Backpressure & Reactive Flow Control

## Executive Summary

When a fast producer generates events faster than a slow consumer can process them:
- Unbounded in-memory buffers cause `OutOfMemoryError` crashes.
- **Backpressure**: The consumer signals the producer to slow down. In streaming (Kafka), the consumer pauses partition polling until its internal worker pool drains.
