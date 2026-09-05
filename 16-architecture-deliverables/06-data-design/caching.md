# Caching & Cache Invalidation Standards

## 1. Cache-Aside Pattern with TTL
* Never cache without an explicit TTL (Time-To-Live).
* Mitigate cache stampedes using distributed mutex locks or probabilistic early expiration (XFetch).
