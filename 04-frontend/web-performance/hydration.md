# Web Performance: Hydration Bottlenecks & Island Architecture

## 1. Architectural Purpose & Problem Context
The cost of full hydration; streaming SSR with Suspense, progressive hydration, and Astro islands.

---

## 2. Metrics & Engineering Targets

```
+--------------------------+-----------------------+-----------------------+
| Metric                   | Good Target           | Poor (Needs Fix)      |
+--------------------------+-----------------------+-----------------------+
| Largest Contentful Paint | < 2.5 seconds         | > 4.0 seconds         |
| Interaction to Next Paint| < 200 milliseconds    | > 500 milliseconds    |
| Cumulative Layout Shift  | < 0.1                 | > 0.25                |
| Total Blocking Time (TBT)| < 200 milliseconds    | > 600 milliseconds    |
| Initial JS Bundle (gzip) | < 100 KB              | > 300 KB              |
+--------------------------+-----------------------+-----------------------+
```

---

## 3. Production Architecture Guidelines
- Set `Cache-Control: public, max-age=31536000, immutable` for all content-hashed JS/CSS/image assets.
- Pre-allocate space for images and ads using CSS `aspect-ratio` to eliminate Cumulative Layout Shift.
- Offload non-critical third-party analytics scripts to web workers via Partytown.
