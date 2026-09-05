# Large File Upload Strategies

## 1. The Peril of Monolithic HTTP Uploads
Uploading a 10 GB video file over a single monolithic HTTP `POST` request is fragile:
* A single dropped network packet at 9.8 GB aborts the upload, forcing the client to restart from 0 GB.
* API Gateway memory buffers saturate attempting to buffer multi-gigabyte payloads.
