
import re

DOC_FILE = r"d:\MFF\Pico\Documentation\Docs_0001_0100.md"
REPORT_FILE = r"C:\Users\LocalAdmin\.gemini\antigravity\brain\cb0952c1-2c91-456d-a19a-36d44aa8a62d\consistency_audit_report.md"

def audit_consistency():
    try:
        with open(DOC_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    projects = re.split(r'^## 1️⃣ Project ', content, flags=re.MULTILINE)[1:] # Skip preamble
    report_lines = ["# Consistency Audit Report\n"]
    
    total_issues = 0
    
    for proj in projects:
        # Extract ID and Title
        title_match = re.match(r'(\d+): (.+)', proj)
        if not title_match:
            continue
        p_id = title_match.group(1)
        p_title = title_match.group(2).strip()
        
        # Extract Blocks Used
        blocks_match = re.search(r'### 6️⃣ Blocks Used\n(.*?)\n###', proj, re.DOTALL)
        blocks_text = blocks_match.group(1).lower() if blocks_match else ""
        
        # Extract Code
        code_match = re.search(r'### 🔟 Generated Code \(Reference Only\)\n```python\n(.*?)\n```', proj, re.DOTALL)
        code_text = code_match.group(1) if code_match else ""
        
        issues = []
        
        # --- Heuristics ---
        
        # 1. Random
        if 'import random' in code_text or 'random.' in code_text:
            if 'random' not in blocks_text:
                issues.append("- Code uses `random` but 'Random' block is missing.")

        # 2. Lists / Arrays
        if ('[' in code_text and ']' in code_text) and ('=' in code_text or 'append' in code_text):
            # Check if it's not just a simple list in a loop like "for i in range"
            # We look for explicit list definitions or access
            if re.search(r'=\s*\[.*\]', code_text) or re.search(r'\.append\(', code_text):
                 # UPDATED: Check for 'create list' as well
                 if 'list' not in blocks_text and 'array' not in blocks_text and 'create list' not in blocks_text:
                    issues.append("- Code uses Lists/Arrays but 'List' block is missing.")

        # 3. Functions
        if 'def ' in code_text:
            if 'function' not in blocks_text:
                 issues.append("- Code defines functions but 'Function' block is missing.")
                 
        # 4. PWM (Analog Write)
        if 'PWM(' in code_text or '.duty_u16(' in code_text:
            if 'analog write' not in blocks_text and 'pwm' not in blocks_text:
                issues.append("- Code uses PWM but 'Analog Write' block is missing.")
                
        # 5. ADC (Analog Read)
        if 'ADC(' in code_text or '.read_u16(' in code_text:
            if 'read analog' not in blocks_text and 'adc' not in blocks_text:
                 issues.append("- Code uses ADC but 'Read Analog' block is missing.")

        # 6. Loops (While/For)
        if ('while ' in code_text or 'for ' in code_text) and 'import _thread' not in code_text: 
            if 'for ' in code_text and ('count with' not in blocks_text and 'repeat' not in blocks_text and 'loop' not in blocks_text and 'forever' not in blocks_text):
                 issues.append("- Code uses `for` loops but 'Repeat/Count' block is missing.")

        # 7. Logic (If/Else)
        if 'if ' in code_text:
             if 'if' not in blocks_text and 'logic' not in blocks_text:
                 issues.append("- Code uses `if` statements but 'If/Logic' block is missing.")
                 
        if issues:
            report_lines.append(f"## Project {p_id}: {p_title}")
            report_lines.extend(issues)
            report_lines.append("")
            total_issues += len(issues)

    report_lines.append(f"\n**Total Issues Found:** {total_issues}")
    
    try:
        with open(REPORT_FILE, 'w', encoding='utf-8') as f:
            f.write('\n'.join(report_lines))
        print(f"Audit complete. Report saved to {REPORT_FILE}")
        print(f"Found {total_issues} issues.")
    except Exception as e:
        print(f"Error writing report: {e}")

if __name__ == "__main__":
    audit_consistency()
