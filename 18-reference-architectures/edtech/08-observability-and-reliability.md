# Observability & SRE: Global EdTech Platform

## 1. Video Playback Quality of Experience (QoE)
- **Rebuffer Ratio**: Total buffering time divided by total watch time (Target: $< 0.5\%$).
- **Video Startup Time (VST)**: Time from play button click to first video frame rendering (Target: $< 1.2\text{ seconds}$).
- **Assessment Submission Success Rate**: 99.99% successful submission without data loss.

## 2. Site Reliability Engineering (SRE) & Chaos Resilience
- **Multi-Window Multi-Burn-Rate Alerting**: Fast burn (14.4x rate over 1 hour) for immediate paging; slow burn (3x rate over 6 hours) for ticket creation.
- **Graceful Degradation**: Shed non-essential background workloads during peak traffic spikes while keeping revenue-critical paths responsive.
- **Automated Disaster Recovery (DR)**: Periodic automated failover drills verifying RPO and RTO compliance.
