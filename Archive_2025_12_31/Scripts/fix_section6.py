#!/usr/bin/env python3
"""
Elite Standard Section 6 Content Cleanup
Fixes the Blocks Used section content format across all projects
"""

import re

def fix_section6_content(content):
    """
    Convert emoji bullet points (🔹) to Elite Standard format
    Returns: (fixed_content, changes_count)
    """
    changes = 0
    
    # Pattern to match Section 6 blocks with emoji format
    # Example:
    # 🔹 **Digital Read**
    # *   **Category:** Pin Access
    #
    # Should become simple removal of emoji bullets for now
    # (specific block names require project-specific knowledge)
    
    # Remove emoji bullets from Section 6
    pattern = r'🔹\s\*\*'
    replacement = '*   **'
    content, count = re.subn(pattern, replacement, content)
    changes += count
    
    # Also handle variations with different spacing
    pattern = r'🔹\*\*'
    replacement = '*   **'
    content, count = re.subn(pattern, replacement, content)
    changes += count
    
    return content, changes


def main():
    """Main execution"""
    input_file = r'd:\MFF\Pico\Documentation\Docs_0401_0500.md'
    
    print("🔧 Elite Standard Section 6 Cleanup")
    print("=" * 50)
    
    # Read file
    print(f"📖 Reading: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix Section 6 content
    print("🔨 Removing emoji bullets from Section 6...")
    fixed_content, changes = fix_section6_content(content)
    
    # Write back
    print(f"💾 Writing changes...")
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    # Summary
    print("=" * 50)
    print(f"✅ Complete!")
    print(f"📊 Emoji bullets removed: {changes}")
    print(f"📁 File updated: {input_file}")
    print()
    print("⚠️  Note: Section 6 content still needs manual conversion")
    print("   from category format to 'from [Category], drag' format")
    
    return 0


if __name__ == "__main__":
    main()
