# Semantic Search Architecture (`semantic-search/`)

## Executive Summary

Traditional search engines rely on lexical keyword matching (TF-IDF, BM25). Lexical search fails when users search for concepts using synonyms, typos, or conceptual descriptions (*"automobile maintenance"* vs. *"car repair"*).

**Semantic Search** encodes human intent into dense mathematical vector spaces, matching queries based on conceptual meaning rather than exact keyword overlap.

---

## Directory Catalog

* **[Dense Retrieval Architecture](dense-retrieval-architecture.md)** — Dual-encoder semantic search pipelines, bi-directional embedding spaces, and approximate nearest neighbor lookups.
* **[Bi-Encoders vs. Cross-Encoders](bi-encoders-vs-cross-encoders.md)** — Speed vs. accuracy trade-offs in search: independent vector representation vs. full self-attention interaction.
