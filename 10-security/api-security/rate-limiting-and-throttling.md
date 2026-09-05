# Distributed Rate Limiting & Throttling Architecture

## Executive Summary

Rate limiting prevents Denial of Service (DoS), protects downstream databases from cascading failure, prevents brute-force credential stuffing, and enforces monetization tiers.

---

## 1. Algorithm Comparison

| Algorithm | Burst Handling | Memory Overhead | Smoothness | Best Enterprise Fit |
| :--- | :--- | :--- | :--- | :--- |
| **Token Bucket** | Allows bursts up to bucket capacity | Low ($O(1)$ per key) | Smooth | Public API endpoints with variable bursty traffic |
| **Leaky Bucket** | Enforces strict constant outflow | Low ($O(1)$ per key) | Perfectly flat | Internal queue ingestion and database writes |
| **Fixed Window Counter** | Allows $2\times$ burst at boundary | Minimal ($1$ integer) | Boundary spikes | Simple internal batch throttles |
| **Sliding Window Log** | Perfect accuracy | High ($O(N)$ requests) | Perfect | Low-volume, ultra-critical banking transactions |
| **Sliding Window Counter** | Excellent approximation | Low ($2$ counters) | Smooth | High-scale enterprise API Gateways (Envoy, Kong) |

---

## 2. Distributed Sliding Window Implementation with Redis

```lua
-- Lua script executed atomically in Redis
local key = KEYS[1]
local now = tonumber(ARGV[1])
local window = tonumber(ARGV[2])
local limit = tonumber(ARGV[3])
local clearBefore = now - window

-- Remove old entries
redis.call('ZREMRANGEBYSCORE', key, 0, clearBefore)

-- Count current requests in window
local currentRequests = redis.call('ZCARD', key)

if currentRequests < limit then
    redis.call('ZADD', key, now, now)
    redis.call('EXPIRE', key, math.ceil(window / 1000))
    return 1 -- ALLOWED
else
    return 0 -- REJECTED (HTTP 429 Too Many Requests)
end
```
