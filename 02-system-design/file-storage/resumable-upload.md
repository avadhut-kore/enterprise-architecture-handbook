# Resumable Uploads & The TUS Protocol

## 1. The TUS Open Protocol Standard
TUS (tus.io) is an open HTTP protocol standard for reliable, resumable file uploads:
1. Client creates upload resource via `POST /files`.
2. Client streams bytes using `PATCH /files/{id}` with `Upload-Offset: 0`.
3. If connection drops at byte $52,428,800$, client queries `HEAD /files/{id}`.
4. Server returns `Upload-Offset: 52428800`.
5. Client resumes sending from byte $52,428,800$ without data loss.
