# Architecture Decision Records & Evolution Roadmap: EdTech

## 1. Canonical Architecture Decision Records

### ADR-001: Adoption of HLS with Multi-Bitrate ABR over WebRTC for Lectures
- **Status**: Accepted
- **Context**: Delivering live lectures to millions of global students across diverse network conditions.
- **Decision**: Use HTTP Live Streaming (HLS) with Adaptive Bitrate (ABR) delivered over global CDNs rather than raw WebRTC for recorded/broadcast lectures.
- **Consequences**: Adds 6-10 seconds latency; reduces bandwidth costs by 80% and ensures playback on low-speed 3G networks.

---

## 2. Evolution Roadmap (1x to 100x Scale)
- **Stage 1 (1x)**: Standard monolithic LMS with embedded video player.
- **Stage 2 (10x)**: Decoupled video transcoding pipeline; global CDN distribution; asynchronous exam grading.
- **Stage 3 (100x)**: AI-driven personalized learning paths; edge-computed real-time proctoring anomaly detection.
