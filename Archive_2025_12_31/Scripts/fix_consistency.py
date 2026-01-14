
import re

DOC_FILE = r"d:\MFF\Pico\Documentation\Docs_0001_0100.md"

# Mappings for Code features -> Block Definitions
# Code Indicator -> Block String to Add
FIX_MAP = {
    'random_import': "🔹 **Random Integer** (Category: Math)",
    'if_stmt': "🔹 **If / Else** (Category: Logic)",
    'loop_for': "🔹 **repeat [10] times** (Category: Loops)",
    'loop_while': "🔹 **forever do** (Category: Loops)",  # Simplified assumption for while True
    'function_def': "🔹 **to [function]** (Category: Functions)",
    'analog_write': "🔹 **Analog Write** (Category: Smart IO)",
    'analog_read': "🔹 **Read Analog** (Category: Smart IO)"
}

def fix_consistency():
    with open(DOC_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = re.split(r'(^## 1️⃣ Project .+$)', content, flags=re.MULTILINE)
    new_content = parts[0]
    fixed_count = 0

    for i in range(1, len(parts), 2):
        header = parts[i]
        body = parts[i+1]

        # Extract Sections
        blocks_match = re.search(r'(### 6️⃣ Blocks Used\n)(.*?)(?=\n###)', body, re.DOTALL)
        code_match = re.search(r'### 🔟 Generated Code \(Reference Only\)\n```python\n(.*?)\n```', body, re.DOTALL)
        
        if not blocks_match or not code_match:
            new_content += header + body
            continue

        blocks_header = blocks_match.group(1)
        blocks_body = blocks_match.group(2)
        code_text = code_match.group(1)
        
        current_blocks_lower = blocks_body.lower()
        new_blocks_body = blocks_body

        missing = []

        # 1. Random
        if ('import random' in code_text or 'random.' in code_text) and 'random' not in current_blocks_lower:
            missing.append(FIX_MAP['random_import'])

        # 2. If/Else
        if 'if ' in code_text and ('if' not in current_blocks_lower and 'logic' not in current_blocks_lower):
            missing.append(FIX_MAP['if_stmt'])
            
        # 3. Loops (For/Repeat)
        # Check if 'for ' exists and we don't have repeat/count/loop blocks
        if 'for ' in code_text and not any(x in current_blocks_lower for x in ['repeat', 'count with', 'loop']):
             missing.append(FIX_MAP['loop_for'])

        # 4. Functions
        if 'def ' in code_text and 'function' not in current_blocks_lower:
            missing.append(FIX_MAP['function_def'])

        # 5. Analog
        if ('PWM(' in code_text or '.duty_u16(' in code_text) and not any(x in current_blocks_lower for x in ['analog write', 'pwm']):
             missing.append(FIX_MAP['analog_write'])

        if ('ADC(' in code_text or '.read_u16(' in code_text) and not any(x in current_blocks_lower for x in ['read analog', 'adc']):
             missing.append(FIX_MAP['analog_read'])

        # Apply Fixes
        if missing:
            # Add a newline if needed
            if not new_blocks_body.endswith('\n'):
                new_blocks_body += '\n'
            
            for m in missing:
                new_blocks_body += f"{m}\n"
            
            # Replace in body
            # We replace only the blocks logic part
            new_body = body.replace(blocks_header + blocks_body, blocks_header + new_blocks_body)
            new_content += header + new_body
            fixed_count += 1
            # print(f"Fixed {header.strip()} -> Added {len(missing)} blocks.")
        else:
            new_content += header + body

    with open(DOC_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Total projects fixed: {fixed_count}")

if __name__ == "__main__":
    fix_consistency()
