# Fuzzy Search & Levenshtein Automata

## 1. Edit Distance & Typos
* **Levenshtein Distance**: Minimum single-character edits (insertions, deletions, substitutions) required to transform string $A$ into $B$.
* **Levenshtein Automaton (Lucene)**: Translates the edit distance constraint into a finite state machine, intersecting with the inverted index dictionary in $O(1)$ time per term.
