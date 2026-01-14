import glob
import re
import os

BLOCKS_FILE = "BLOCKS.md"

def load_blocks_db():
    start_db = {}
    current_category = "Unknown"
    with open(BLOCKS_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line.startswith("## "):
            current_category = re.sub(r'##\s+.*?\*\*(.*?)\*\*.*', r'\1', line)
            if "**" not in line: current_category = line.replace("## ", "").strip()
            continue
        match = re.match(r'\*\s+\*\*(.*?):\*\*\s+`?(.*?)`?$', line)
        if match:
            name = match.group(1).strip()
            text = match.group(2).strip()
            start_db[name] = {"Category": current_category, "Block": text, "Code": "", "RefName": name}
            last_block = name
            continue
        if line.startswith("*   *🐍 Code:*"):
            code_match = re.match(r'\*\s+\*🐍 Code:\*\s+`?(.*?)`?$', line)
            if code_match and 'last_block' in locals():
                start_db[last_block]["Code"] = code_match.group(1)
    return start_db

def generate_header_imports(code_snippets):
    imports = set()
    imports.add("import time")
    full_code = "\n".join(code_snippets)
    if "machine" in full_code or "Pin(" in full_code or "ADC(" in full_code:
        imports.add("import machine")
        imports.add("from machine import Pin, ADC, PWM, I2C")
    if "math." in full_code: imports.add("import math")
    if "random." in full_code: imports.add("import random")
    if "SSD1306" in full_code: imports.add("from ssd1306 import SSD1306_I2C")
    if "neopixel" in full_code: imports.add("import neopixel")
    return list(sorted(imports))

def find_blocks_in_text(text, db):
    found = []
    keys = sorted(db.keys(), key=len, reverse=True)
    text_lower = text.lower()
    for k in keys:
        if k.lower() in text_lower:
            found.append(k)
    return list(set(found))

def fix_file(filename, db):
    print(f"Fixing {filename}...")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parts = re.split(r'(^## 1️⃣.*)', content, flags=re.MULTILINE)
    new_content = parts[0]
    
    for i in range(1, len(parts), 2):
        header = parts[i]
        body = parts[i+1]
        
        # Analyze Structure by Titles, not just Numbers
        # Regex for sections: ### [Emoji] [Title]
        sections = []
        for match in re.finditer(r'(### \d+.*?)\n', body):
            title = match.group(1).lower()
            sections.append((match.start(), title))
        
        # Check presence
        has_sec6 = any("blocks used" in s[1] for s in sections) or "### 6️⃣" in body
        has_sec10 = any("generated code" in s[1] for s in sections) or "### 🔟" in body
        
        # Detect Logic Text (Usually described as "Block Logic" or just found in body)
        # We try to use the section labeled "Logic" or falling back to Section 8
        logic_text = ""
        logic_match = re.search(r'### \d+.*Logic.*?\n(.*?)(###|$)', body, re.DOTALL | re.IGNORECASE)
        if logic_match:
            logic_text = logic_match.group(1)
        else:
            # Fallback to scanning everything?
            logic_text = body

        # 1. Prepare Content 6
        detected_blocks = []
        if has_sec6:
            # Try parsing existing
            m = re.search(r'### [6|5|4].*Blocks.*?(###|$)', body, re.DOTALL | re.IGNORECASE) # Loose match
            if m:
                bullets = re.findall(r'\*\s+`?([A-Za-z0-9 /\(\)]+)`?', m.group(0))
                for b in bullets:
                     if len(b)>2: detected_blocks.append(b.strip())
        
        if not detected_blocks:
            detected_blocks = find_blocks_in_text(logic_text, db)
            
        new_sec6 = "\n### 6️⃣ Blocks Used\n"
        code_snippets = []
        if not detected_blocks:
            new_sec6 += "🔹 **Control Logic**\n*   **Category:** Logic\n*   **Block:** `Wait`\n"
        
        for b_name in detected_blocks:
             # Lookups... (Same as before)
            entry = None
            if b_name in db: entry = db[b_name]
            else:
                 for k in db:
                    if b_name.lower() == k.lower(): entry = db[k]; break
            if not entry:
                 for k in db:
                    if b_name.lower() in k.lower(): entry = db[k]; break
            
            if entry:
                new_sec6 += f"🔹 **{entry['RefName']}**\n*   **Category:** {entry['Category']}\n*   **Block:** `{entry['Block']}`\n"
                if entry['Code']: code_snippets.append(entry['Code'])
            else:
                 new_sec6 += f"🔹 **{b_name}**\n*   **Category:** Custom\n*   **Block:** `{b_name}`\n"

        # 2. Prepare Content 10
        imports = generate_header_imports(code_snippets + [logic_text])
        new_sec10 = "\n### 🔟 Generated Code (Reference Only)\n```python\n"
        new_sec10 += "\n".join(imports) + "\n\n"
        new_sec10 += "# Initialize Hardware (Reference)\n"
        if "Servo" in ",".join(detected_blocks): new_sec10 += "servo = PWM(Pin(0)); servo.freq(50)\n"
        if "OLED" in ",".join(detected_blocks): new_sec10 += "i2c = I2C(0, sda=Pin(0), scl=Pin(1)); oled = SSD1306_I2C(128, 64, i2c)\n"
        new_sec10 += "\n# Main Logic (See Block Logic)\n"
        new_sec10 += "while True:\n    # Logic from Section 8\n    time.sleep(1)\n```\n\n"

        # INSERTION LOGIC 2.0
        if has_sec6:
             # Regex replace existing
             body = re.sub(r'### \d+.*?Blocks Used.*?(?=###|$)', new_sec6, body, flags=re.DOTALL|re.IGNORECASE)
        else:
             # Insert BEFORE "Logic" or AFTER "Wiring"
             # Search for Logic Section
             logic_pos = re.search(r'### \d+.*?Logic', body, re.IGNORECASE)
             if logic_pos:
                 body = body[:logic_pos.start()] + new_sec6 + body[logic_pos.start():]
             else:
                 # Fallback: After Wiring
                 wiring_pos = re.search(r'### \d+.*?Wiring', body, re.IGNORECASE)
                 if wiring_pos:
                     # Find end of wiring section (next ###)
                     next_sec = re.search(r'###', body[wiring_pos.end():])
                     if next_sec:
                         ins_idx = wiring_pos.end() + next_sec.start()
                         body = body[:ins_idx] + new_sec6 + body[ins_idx:]
                     else:
                         body += new_sec6 # Append
                 else:
                     # Insert after header??
                     body = new_sec6 + body

        if has_sec10:
             body = re.sub(r'### \d+.*?Generated Code.*?(?=###|$)', new_sec10, body, flags=re.DOTALL|re.IGNORECASE)
        else:
             # Insert at end of file usually, or before "Common Mistakes"
             mistakes_pos = re.search(r'### \d+.*?Mistake', body, re.IGNORECASE)
             if mistakes_pos:
                 body = body[:mistakes_pos.start()] + new_sec10 + body[mistakes_pos.start():]
             else:
                 body += new_sec10

        new_content += header + body

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    db = load_blocks_db()
    files = sorted(glob.glob("Pico_500_Batch_*.md"))
    for f in files:
        fix_file(f, db)
    print("All files processed.")

if __name__ == "__main__":
    main()
