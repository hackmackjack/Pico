#!/usr/bin/env python3
"""
Triple-Sync Validator for Pico Documentation
Verifies alignment between Sections 6, 8, and 10 for Projects 0001-0035
"""

import re
from pathlib import Path
from collections import defaultdict

def extract_blocks_section6(content, project_num):
    """Extract blocks from Section 6"""
    # Match "## 1️⃣ Project 0001:" through "### 7️⃣"
    pattern = rf'## 1.*?Project {project_num:04d}:.*?### 6.*?Blocks Used.*?\n(.*?)### 7'
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return []
    
    section6 = match.group(1)
    # Extract block names from "drag `block_name`"
    blocks = re.findall(r'drag `([^`]+)`', section6)
    return blocks

def extract_blocks_section8(content, project_num):
    """Extract blocks used in Section 8"""
    # Match "## 1️⃣ Project 0001:" through "### 9️⃣"
    pattern = rf'## 1.*?Project {project_num:04d}:.*?### 8.*?Step-by-Step Guide.*?\n(.*?)### 9'
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return []
    
    section8 = match.group(1)
    
    # Extract ALL block names within backticks
    # This catches: "drag `block`", "drag a `block` block", "`block`" alone, etc.
    all_backtick_items = re.findall(r'`([^`]+)`', section8)
    
    # Filter to only known Pico blocks (start with pico_, controls_, logic_, math_, variables_, lists_, text_)
    pico_prefixes = ('pico_', 'controls_', 'logic_', 'math_', 'variables_', 'lists_', 'text_')
    blocks = [item for item in all_backtick_items if item.startswith(pico_prefixes)]
    
    # Remove duplicates while preserving order
    seen = set()
    unique_blocks = []
    for block in blocks:
        if block not in seen:
            seen.add(block)
            unique_blocks.append(block)
    
    return unique_blocks

def extract_code_section10(content, project_num):
    """Extract Python code from Section 10"""
    # Match "## 1️⃣ Project 0001:" through code block
    pattern = rf'## 1.*?Project {project_num:04d}:.*?### 10.*?Generated Code.*?\n```python\n(.*?)\n```'
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return ""
    return match.group(1)

def validate_project(content, project_num):
    """Validate triple-sync for a single project"""
    blocks_s6 = extract_blocks_section6(content, project_num)
    blocks_s8 = extract_blocks_section8(content, project_num)
    code_s10 = extract_code_section10(content, project_num)
    
    issues = []
    
    # Check if Section 6 exists
    if not blocks_s6:
        issues.append(f"  [ERROR] Section 6 not found or empty")
        return issues
    
    # Check if Section 8 exists
    if not blocks_s8:
        issues.append(f"  [ERROR] Section 8 not found or empty")
        return issues
    
    # Convert to sets for comparison
    s6_set = set(blocks_s6)
    s8_set = set(blocks_s8)
    
    # Find mismatches
    only_in_s6 = s6_set - s8_set
    only_in_s8 = s8_set - s6_set
    
    if only_in_s6:
        issues.append(f"  [WARN] Blocks in Section 6 but NOT used in Section 8: {only_in_s6}")
    
    if only_in_s8:
        issues.append(f"  [WARN] Blocks used in Section 8 but NOT listed in Section 6: {only_in_s8}")
    
    # Verify code uses declared blocks
    code_issues = []
    if code_s10:
        # Check for common block-to-code patterns
        if 'pico_forever' in s6_set and 'while True:' not in code_s10:
            code_issues.append("Missing 'while True:' for pico_forever")
        if 'pico_wait' in s6_set and 'time.sleep' not in code_s10:
            code_issues.append("Missing 'time.sleep' for pico_wait")
        if 'pico_gpio_write' in s6_set and 'Pin(' not in code_s10:
            code_issues.append("Missing 'Pin(' for pico_gpio_write")
    
    if code_issues:
        issues.append(f"  [WARN] Code-Block mismatch: {', '.join(code_issues)}")
    
    return issues

def main():
    doc_path = Path(r"d:\MFF\Pico\Documentation\Docs_0001_0100.md")
    
    if not doc_path.exists():
        print(f"❌ File not found: {doc_path}")
        return
    
    content = doc_path.read_text(encoding='utf-8')
    
    print("=" * 70)
    print("TRIPLE-SYNC VALIDATION REPORT (Projects 0081-0100)")
    print("=" * 70)
    print()
    
    total_projects = 20
    passed = 0
    failed = 0
    
    for proj_num in range(81, 101):
        issues = validate_project(content, proj_num)
        
        if not issues:
            print(f"[PASS] Project {proj_num:04d}")
            passed += 1
        else:
            print(f"[FAIL] Project {proj_num:04d}")
            for issue in issues:
                print(issue)
            failed += 1
            print()
    
    print("=" * 70)
    print(f"SUMMARY: {passed}/{total_projects} passed, {failed}/{total_projects} failed")
    print("=" * 70)
    
    if failed == 0:
        print("SUCCESS: ALL PROJECTS PASSED TRIPLE-SYNC VALIDATION!")
    else:
        print(f"WARNING: {failed} projects need attention")

if __name__ == "__main__":
    main()
