# Environment Configuration & 12-Factor App

## 1. Twelve-Factor Rule III: Config in Environment
Store config in environment variables (`DATABASE_URL`, `LOG_LEVEL`, `PORT`).
- Environment variables are language-agnostic and universally supported across Linux, Docker, and Kubernetes.
- Avoid multi-thousand-line environment variable dumps; use `.env` only for local developer machines, never production.
