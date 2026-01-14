#!/usr/bin/env python3
"""
Elite Standard Header Cleanup Script
Automatically fixes emoji headers in sections 7, 9-12 across all projects
"""

import re
import sys

def fix_emoji_headers(content):
    """
    Remove emojis from section headers and standardize format
    Returns: (fixed_content, changes_count)
    """
    changes = 0
    
    # Section 7: Variables
    pattern = r'### 7️⃣ Variables & State'
    replacement = '### 7. Variables'
    content, count = re.subn(pattern, replacement, content)
    changes += count
    
    # Also handle variation without "& State"
    pattern = r'### 7️⃣ Variables'
    replacement = '### 7. Variables'
    content, count = re.subn(pattern, replacement, content)
    changes += count
    
    # Section 9: Execution Flow
    pattern = r'### 9️⃣ Execution Flow \(Plain English\)'
    replacement = '### 9. Execution Flow'
    content, count = re.subn(pattern, replacement, content)
    changes += count
    
    pattern = r'### 9️⃣ Execution Flow'
    replacement = '### 9. Execution Flow'
    content, count = re.subn(pattern, replacement, content)
    changes += count
    
    # Section 10: Generated Code
    pattern = r'### 🔟 Generated Code \(Reference Only\)'
    replacement = '### 10. Generated Code'
    content, count = re.subn(pattern, replacement, content)
    changes += count
    
    pattern = r'### 🔟 Generated Code'
    replacement = '### 10. Generated Code'
    content, count = re.subn(pattern, replacement, content)
    changes += count
    
    # Section 11: Common Mistakes
    pattern = r'### 1️⃣1️⃣ Common Mistakes & Debug Tips'
    replacement = '### 11. Common Mistakes'
    content, count = re.subn(pattern, replacement, content)
    changes += count
    
    pattern = r'### 1️⃣1️⃣ Common Mistakes'
    replacement = '### 11. Common Mistakes'
    content, count = re.subn(pattern, replacement, content)
    changes += count
    
    # Section 12: Try This Next
    pattern = r'### 1️⃣2️⃣ Try This Next'
    replacement = '### 12. Try This Next'
    content, count = re.subn(pattern, replacement, content)
    changes += count
    
    # Also fix Section 6 emoji (just header, not content)
    pattern = r'### 6️⃣ Blocks Used'
    replacement = '### 6. Blocks Used'
    content, count = re.subn(pattern, replacement, content)
    changes += count
    
    return content, changes


def main():
    """Main execution"""
    input_file = r'd:\MFF\Pico\Documentation\Docs_0401_0500.md'
    
    print("🔧 Elite Standard Header Cleanup")
    print("=" * 50)
    
    # Read file
    print(f"📖 Reading: {input_file}")
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return 1
    
    # Fix headers
    print("🔨 Fixing emoji headers...")
    fixed_content, changes = fix_emoji_headers(content)
    
    # Write back
    print(f"💾 Writing changes...")
    try:
        with open(input_file, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return 1
    
    # Summary
    print("=" * 50)
    print(f"✅ Complete!")
    print(f"📊 Total replacements made: {changes}")
    print(f"📁 File updated: {input_file}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
