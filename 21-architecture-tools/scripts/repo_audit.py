#!/usr/bin/env python3
"""
Repository Architecture Auditor
Executes a comprehensive health audit of the enterprise-architecture-handbook repository:
- Markdown file counts and module distribution
- Placeholder directory inspection (.gitkeep detection)
- Orphaned .gitkeep detection in populated directories
- Suspiciously short / truncated files audit

Usage:
    python repo_audit.py [--root-dir .]
"""

import argparse
import os
import sys

def audit_repository(root_dir: str):
    root_dir = os.path.abspath(root_dir)
    print(f"=== AUDITING ENTERPRISE ARCHITECTURE HANDBOOK: {root_dir} ===\n")

    total_md_files = 0
    total_dirs = 0
    module_counts = {}
    placeholder_dirs = []
    orphaned_gitkeeps = []
    short_files = []

    for current_root, dirs, files in os.walk(root_dir):
        # Prune hidden and vendor directories in-place to avoid descending into them
        dirs[:] = [d for d in dirs if d not in ('.git', 'node_modules', '.venv', '__pycache__', '.gemini')]

        total_dirs += 1
        rel_path = os.path.relpath(current_root, root_dir)
        top_module = rel_path.split(os.sep)[0] if rel_path != '.' else 'root'

        md_files_in_dir = [f for f in files if f.endswith('.md')]
        all_files_in_dir = files

        total_md_files += len(md_files_in_dir)
        module_counts[top_module] = module_counts.get(top_module, 0) + len(md_files_in_dir)

        # Check .gitkeep status
        if '.gitkeep' in files:
            other_files = [f for f in files if f != '.gitkeep']
            if len(other_files) == 0:
                placeholder_dirs.append(rel_path)
            else:
                orphaned_gitkeeps.append(rel_path)

        # Check for suspiciously short files (< 10 lines)
        for md_f in md_files_in_dir:
            file_path = os.path.join(current_root, md_f)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    line_count = sum(1 for _ in f)
                    if line_count < 10:
                        short_files.append((os.path.relpath(file_path, root_dir), line_count))
            except Exception:
                pass

    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    print(f"Total Markdown Documents: {total_md_files}")
    print(f"Total Directories Scanned: {total_dirs}\n")

    print("=== TOP-LEVEL MODULE FILE COUNTS ===")
    for mod, count in sorted(module_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  • {mod:<30}: {count:>4} markdown files")

    print(f"\n=== PLACEHOLDER DIRECTORIES (Only .gitkeep): {len(placeholder_dirs)} ===")
    for p in sorted(placeholder_dirs):
        print(f"  • {p}")

    print(f"\n=== ORPHANED .gitkeep IN POPULATED DIRECTORIES: {len(orphaned_gitkeeps)} ===")
    for o in sorted(orphaned_gitkeeps):
        print(f"  [WARN] {o}")

    print(f"\n=== SUSPICIOUSLY SHORT FILES (<10 lines): {len(short_files)} ===")
    for sf, lc in sorted(short_files)[:10]:
        print(f"  • {sf} ({lc} lines)")
    if len(short_files) > 10:
        print(f"  ... and {len(short_files) - 10} more.")

    print("\n[OK] Repository Audit Complete.")

def main():
    parser = argparse.ArgumentParser(description="Audit enterprise repository structure and health.")
    parser.add_argument("--root-dir", default=".", help="Root directory of the repository")
    args = parser.parse_args()

    audit_repository(args.root_dir)

if __name__ == "__main__":
    main()
