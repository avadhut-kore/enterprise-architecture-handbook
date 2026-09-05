# Search Engine & Information Retrieval Architecture

## 1. Overview & Foundational Principles
Full-text search engines (Elasticsearch, Apache Solr, Meilisearch) are specialized distributed systems optimized for searching unstructured text across billions of documents with sub-second latency. Relational database B-Tree indexes fail for text search because executing substring queries (`LIKE '%phone%'`) forces full table scans ($O(N)$). Search engines invert this model using **Inverted Indexes**.

```mermaid
flowchart LR
    Doc[Document: 'Fast iPhone 16'] --> Pipeline[Analysis Pipeline: Tokenize & Stem]
    Pipeline --> InvertedIndex[Inverted Index: Term -> Document IDs]
    InvertedIndex --> Search[Query: 'fast phone' -> Instant Match in <5ms]
```

---

## 2. Directory Structure
* [Inverted Index](inverted-index.md)
* [Tokenization](tokenization.md)
* [Stemming & Lemmatization](stemming-and-lemmatization.md)
* [Relevance Scoring](relevance-scoring.md)
* [TF-IDF Algorithm](tf-idf.md)
* [Okapi BM25 Ranking](bm25.md)
* [Fuzzy Search & Levenshtein Automata](fuzzy-search.md)
* [Autocomplete Architectures](autocomplete.md)
* [Distributed Typeahead Systems](typeahead.md)
* [Search Indexing & Lucene Segments](search-indexing.md)
* [Search Ranking & Multi-Stage Re-ranking](search-ranking.md)
* [Elasticsearch Cluster Architecture](elasticsearch-architecture.md)
