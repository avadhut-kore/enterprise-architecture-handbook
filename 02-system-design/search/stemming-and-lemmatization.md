# Stemming vs. Lemmatization

## 1. Algorithmic Reduction
* **Stemming (Porter / Snowball Algorithm)**: Heuristic chopping of word endings (`running` $\rightarrow$ `run`, `ponies` $\rightarrow$ `poni`). Fast, but produces non-words.
* **Lemmatization**: Morphological vocabulary lookup (`better` $\rightarrow$ `good`, `was` $\rightarrow$ `be`). Slower, but linguistically accurate.
