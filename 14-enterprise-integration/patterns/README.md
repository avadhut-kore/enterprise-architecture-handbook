# Enterprise Integration Patterns Library

## 1. Overview
This directory details the canonical Enterprise Integration Patterns (EIP) adapted for modern cloud-native, asynchronous, and hybrid microservice architectures.

## 2. Pattern Catalog
- [request-reply.md](request-reply.md): Synchronous RPC vs. Asynchronous Correlation ID matching.
- [pub-sub.md](pub-sub.md): Topic-based event fan-out.
- [event-notification.md](event-notification.md): Thin notifications prompting callback reads.
- [event-carried-state-transfer.md](event-carried-state-transfer.md): Fat events carrying self-contained state.
- [message-router.md](message-router.md) & [content-based-router.md](content-based-router.md): Dynamic routing.
- [message-transformer.md](message-transformer.md): Schema and protocol mediation.
- [splitter.md](splitter.md) & [aggregator.md](aggregator.md): Batch decomposition and recombination.
- [resequencer.md](resequencer.md): Stream reordering.
- [retry.md](retry.md) & [dead-letter.md](dead-letter.md): Fault recovery and quarantine.
- [idempotency.md](idempotency.md): Deduplication keys and atomic checks.
- [outbox.md](outbox.md) & [inbox.md](inbox.md): Reliable transactional boundaries.
- [saga.md](saga.md): Multi-system distributed transactions.
- [anti-corruption-layer.md](anti-corruption-layer.md): Preserving domain boundaries.
- [strangler.md](strangler.md): Incremental legacy replacement.
- [canonical-model.md](canonical-model.md): Enterprise semantic normalization.
- [reconciliation.md](reconciliation.md): Asynchronous drift detection.
- [batch-window.md](batch-window.md): Dual-speed real-time to batch bridge.
