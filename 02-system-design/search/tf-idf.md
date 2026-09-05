# TF-IDF (Term Frequency - Inverse Document Frequency)

## 1. Mathematical Formulation
$$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \text{IDF}(t, D)$$

### 1. Term Frequency (TF)
$$\text{TF}(t, d) = \frac{f(t, d)}{\sum_{t' \in d} f(t', d)}$$
Measures how frequently term $t$ appears in document $d$.

### 2. Inverse Document Frequency (IDF)
$$\text{IDF}(t, D) = \log\left(\frac{|D|}{|\{d \in D : t \in d\}|}\right)$$
Penalizes common words (e.g., "the", "and") that appear across nearly all documents.
