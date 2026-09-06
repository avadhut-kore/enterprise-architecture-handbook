#!/usr/bin/env python3
"""
Architecture Documentation Linter
Validates Markdown architecture documentation for structural completeness,
broken relative file links, syntax corruptions, and Mermaid formatting.

Usage:
    python doc_linter.py --target-dir 01-architecture
    python doc_linter.py --file 01-architecture/ai-architecture/README.md
"""

import argparse
import os
import re
import sys

CORRUPTION_PATTERNS = [
    (r'\$ightarrow\$', "Corrupted LaTeX arrow '$ightarrow$' detected. Use '→' instead."),
    (r'\$eftarrow\$', "Corrupted LaTeX arrow '$eftarrow$' detected. Use '←' instead."),
    (r'\$	imes\$', "Corrupted multiplication symbol detected. Use '×' instead.")
]

REQUIRED_HEADINGS = [
    r'##\s+.*(?:Overview|Context|Problem)',
    r'##\s+.*(?:Architecture|Blueprint|Topology|Pattern)',
    r'##\s+.*(?:Trade-off|Decision|Matrix|Options|Consequences)',
    r'##\s+.*(?:Checklist|Related)'
]

def check_file(file_path: str, strict: bool = False) -> list[str]:
    issues = []
    if not os.path.isfile(file_path) or not file_path.endswith('.md'):
        return issues

    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
        lines = content.splitlines()

    # 1. Check for known syntax corruptions
    for pattern, msg in CORRUPTION_PATTERNS:
        for idx, line in enumerate(lines, 1):
            if re.search(pattern, line):
                issues.append(f"[{file_path}:{idx}] {msg}")

    # 2. Check for broken relative links
    dir_name = os.path.dirname(file_path)
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    for text, link in links:
        # Ignore web links, anchors, and mailto
        if link.startswith(('http://', 'https://', '#', 'mailto:')):
            continue
        clean_link = link.split('#')[0]
        if not clean_link:
            continue
        resolved_path = os.path.normpath(os.path.join(dir_name, clean_link))
        if not os.path.exists(resolved_path):
            issues.append(f"[{file_path}] Broken relative link: '{link}' -> Resolved to non-existent '{resolved_path}'")

    # 3. Check for unclosed Mermaid blocks and code fences
    mermaid_starts = len(re.findall(r'^\s*```mermaid', content, re.MULTILINE))
    code_block_fences = len(re.findall(r'^\s*```', content, re.MULTILINE))
    if code_block_fences % 2 != 0:
        issues.append(f"[{file_path}] Unbalanced code block fences (``` line-start count = {code_block_fences})")

    # 4. In strict mode, check for required architectural sections
    if strict:
        for heading_pattern in REQUIRED_HEADINGS:
            if not re.search(heading_pattern, content, re.IGNORECASE):
                issues.append(f"[{file_path}] Missing recommended architectural section matching pattern: '{heading_pattern}'")

    return issues

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    parser = argparse.ArgumentParser(description="Audit architecture markdown files for quality and link integrity.")
    parser.add_argument("--target-dir", default=None, help="Directory to scan recursively")
    parser.add_argument("--file", default=None, help="Specific file to scan")
    parser.add_argument("--strict", action="store_true", help="Enable strict heading completeness checks")

    args = parser.parse_args()

    if not args.target_dir and not args.file:
        parser.print_help()
        sys.exit(1)

    all_issues = []
    files_checked = 0

    if args.file:
        files_to_check = [args.file]
    else:
        files_to_check = []
        for root, _, files in os.walk(args.target_dir):
            for f in files:
                if f.endswith('.md'):
                    files_to_check.append(os.path.join(root, f))

    for fpath in files_to_check:
        files_checked += 1
        issues = check_file(fpath, strict=args.strict)
        all_issues.extend(issues)

    print(f"Audit completed: {files_checked} Markdown files scanned.")
    if all_issues:
        print(f"[FAIL] Found {len(all_issues)} issue(s):")
        for iss in all_issues:
            print(f"  • {iss}")
        sys.exit(1)
    else:
        print("[OK] Zero issues found. All files comply with architectural linting rules!")
        sys.exit(0)

if __name__ == "__main__":
    main()
