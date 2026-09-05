# Infrastructure & Media Pipelines: EdTech Platform

## 1. Adaptive Bitrate Video Pipeline
```
[Raw MP4 Video Upload] ──► [S3 Raw Bucket] ──► [EventBridge]
                                                     │
                                                     ▼
                                        [Transcoder Worker Pool (FFmpeg)]
                                        ├── 1080p @ 4500 kbps
                                        ├── 720p  @ 2500 kbps
                                        ├── 480p  @ 1200 kbps
                                        └── 360p  @ 600 kbps (Low Bandwidth)
                                                     │
                                                     ▼
                                        [S3 Transcoded Video Bucket]
                                                     │
                                                     ▼
                                          [Global CDN Edge Points]
```
