# FIX CRITICAL ERROR: Delete wrong content (0382-0400) and regenerate from problem statements

target_file = r'd:\MFF\Pico\Documentation\Docs_0301_0400.md'

# Read current file
with open(target_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Keep only up to end of Project 0381 (line 9990: "---")
correct_content = lines[:9991]

# Write back only the correct portion
with open(target_file, 'w', encoding='utf-8') as f:
    f.writelines(correct_content)

print("✅ Deleted incorrect Projects 0382-0400")
print("📋 Ready to regenerate with CORRECT problem statements")
print("   - Batch 39 (0382-0390): Kitchen Timer 2")
print("   - Batch 40 (0391-0400): Metronome 2")
