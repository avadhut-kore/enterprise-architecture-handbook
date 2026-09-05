# Business Architecture & Requirements: Global EdTech Platform

## 1. Business Context & User Personas
- **Students**: Need seamless, zero-buffer video playback across low-bandwidth mobile networks, offline course downloads, and interactive quizzes.
- **Educators & Instructors**: Require intuitive course authoring, automated gradebook scoring, and real-time class engagement analytics.
- **Institutional Administrators**: Require integration with School Information Systems (SIS) via LTI and OneRoster standards.

---

## 2. Scale Model & Capacity Assumptions

| Scale Parameter | Baseline Scale | 10x Scale Target | 100x Scale Target |
| :--- | :--- | :--- | :--- |
| **Enrolled Students** | 500,000 students | 5,000,000 students | 50,000,000 students |
| **Concurrent Video Streams** | 20,000 streams | 200,000 streams | 2,000,000 streams |
| **Simultaneous Exam Submissions**| 5,000 exams/min | 50,000 exams/min | 500,000 exams/min |
| **Video Storage (Transcoded)** | 50 TB | 500 TB | 5 PB |
| **Daily Telemetry Events** | 25 Million events | 250 Million events | 2.5 Billion events |
