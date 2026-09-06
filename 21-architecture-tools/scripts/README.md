# Architecture Automation & Repository Scripts

## 1. Overview
The `scripts/` directory contains deterministic, non-destructive automation scripts designed to audit repository health, inspect directory completeness, and validate metrics across the entire enterprise architecture handbook.

---

## 2. Available Scripts

### 2.1. Repository Health & Placeholder Auditor
Scans the entire repository and generates an executive report detailing:
* Total Markdown document inventory.
* File distribution counts grouped by top-level module.
* Active placeholder directories (directories holding only `.gitkeep`).
* Orphaned `.gitkeep` files in populated directories.
* Detection of truncated or suspiciously short files ($< 10$ lines).

* **Script**: [`repo_audit.py`](repo_audit.py)
* **Usage**:
  ```bash
  python repo_audit.py --root-dir .
  ```

---

## 3. Operational Safety Standards
* **Non-Destructive by Default**: All scripts in this directory operate in read-only audit mode.
* **Zero External Dependencies**: All tools execute using standard Python 3 libraries (`os`, `sys`, `re`, `argparse`).
