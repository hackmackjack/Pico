import re
from pathlib import Path

def extract_keywords(hardware_block, problem_text):
    keywords = []
    # Extract hardware keywords
    common_hw = ["LED", "Button", "Buzzer", "Motor", "LDR", "Potentiometer", "Temp", "Ultrasonic", "Servo", "Relay", "Display", "OLED", "RGB", "Switch", "Keypad"]
    text = hardware_block + " " + problem_text
    
    hw_found = []
    for hw in common_hw:
        if hw.lower() in text.lower():
            hw_found.append(hw)
            
    # Extract specific numbers (durations like 0.5, 10, etc that are critical)
    import re
    # Look for 'X seconds', 'X times'
    params = re.findall(r'(\d+\.?\d*)\s*(?:seconds|times|s|ms)', problem_text)
    
    return hw_found, list(set(params))

def check_coverage(keywords, text, is_blocks_section=False):
    missing = []
    text_lower = text.lower()
    
    # Mapping for ALL Sections
    # If key is X, accept Y as valid presence
    COMMON_PROXIES = {
        "LED": ["pico_gpio_write", "led", "pin", "light", "lamp"],
        "Button": ["pico_gpio_read", "button", "irq", "btn", "press", "click", "switch", "input"],
        "Switch": ["pico_gpio_read", "switch", "toggle", "slide"],
        "Buzzer": ["pico_gpio_write", "pico_pwm", "buzzer", "music", "pwm", "buzz", "beep", "sound", "note", "tone"],
        "Motor": ["pico_gpio_write", "pico_pwm", "motor", "fan", "spin", "driver"],
        "Servo": ["servo", "angle"],
        "LDR": ["pico_adc", "analog", "read_u16", "adc", "light", "dark", "brightness", "level"],
        "Potentiometer": ["pico_adc", "analog", "pot", "dial", "turn", "knob"],
        "Ultrasonic": ["distance", "sonar", "ultrasonic", "pulse", "echo", "trigger", "cm"],
        "Temp": ["adc", "temp", "dht", "deg", "heat", "cool"],
        "Display": ["display", "lcd", "oled", "segment", "screen", "show", "print"],
        "RGB": ["rgb", "neopixel", "ws2812", "color", "red", "green", "blue"],
    }

    for k in keywords:
        search_terms = [k.lower()]
        
        # Apply proxies to ALL sections now, but keep block-specifics if needed
        # Actually, unifying the proxy list is safer for semantic checking.
        if k in COMMON_PROXIES:
            search_terms.extend(COMMON_PROXIES[k])
                
        # Handle specific number flexibility (e.g. 0.5s -> 500ms)
        try:
            val = float(k)
            # If it's a number, look for it OR its ms equivalent
            search_terms.append(str(int(val * 1000))) # 0.5 -> 500
        except:
            pass
            
        found = False
        for term in search_terms:
            if term.lower() in text_lower:
                found = True
                break
        if not found:
            missing.append(k)
    return missing

def parse_problems(path):
    content = Path(path).read_text(encoding='utf-8')
    projects = {}
    
    sections = content.split('### Project ')
    for sec in sections[1:]: 
        try:
            proj_num = sec[:4]
            lines = sec.split('\n')
            
            # Problem Statement
            prob_text = ""
            if "**Problem Statement:**" in sec:
                parts = sec.split("**Problem Statement:**")[1].split("**Hardware Requirements:**")[0]
                prob_text = parts.strip().replace('\n', ' ')

            # Hardware
            hw_text = ""
            if "**Hardware Requirements:**" in sec:
                hw_part = sec.split("**Hardware Requirements:**")[1].split("**Expected Behavior:**")[0]
                hw_text = hw_part.strip()
            
            projects[proj_num] = {'problem': prob_text, 'hardware': hw_text}
        except Exception:
            pass
    return projects

def parse_docs_full(path):
    content = Path(path).read_text(encoding='utf-8')
    projects = {}
    sections = re.split(r'## 1\S+ Project (\d{4}):', content)
    
    for i in range(1, len(sections), 2):
        proj_num = sections[i]
        body = sections[i+1]
        
        sec6 = ""
        sec8 = ""
        sec10 = ""
        
        if "### 6️⃣ Blocks Used" in body:
            sec6 = body.split("### 6️⃣ Blocks Used")[1].split("### 7️⃣")[0]
        if "### 8️⃣ Step-by-Step Guide" in body:
            sec8 = body.split("### 8️⃣ Step-by-Step Guide")[1].split("### 9️⃣")[0]
        if "### 10️⃣ Generated Code" in body:
            sec10 = body.split("### 10️⃣ Generated Code")[1].split("### 11️⃣")[0]
            
        projects[proj_num] = {'sec6': sec6, 'sec8': sec8, 'sec10': sec10}
        
    return projects

def generate_report():
    prob_path = r"d:\MFF\Pico\Problem_Statements\Projects_0101_0200.md"
    doc_path = r"d:\MFF\Pico\Documentation\Docs_0101_0200.md"
    
    probs = parse_problems(prob_path)
    docs = parse_docs_full(doc_path)
    
    report = "# Semantic Alignment Report: Projects 0101-0200\n"
    report += "Validating that Hardware and Key Parameters from the Problem Statement are present in all 3 Key Sections.\n"
    report += "*Note*: 'Missing' in Block section implies neither the direct term nor its functional block counterpart (e.g. 'Button' vs 'pico_gpio_read') was found.\n\n"
    report += "| ID | Hardware / Params | 6️⃣ Blocks (HW Only) | 8️⃣ Guide | 🔟 Code | Result |\n"
    report += "| :--- | :--- | :--- | :--- | :--- | :--- |\n"
    
    for i in range(101, 201):
        pid = f"{i:04d}"
        p_data = probs.get(pid, {'problem':'', 'hardware':''})
        d_data = docs.get(pid, {'sec6':'', 'sec8':'', 'sec10':''})
        
        hw_keys, param_keys = extract_keywords(p_data['hardware'], p_data['problem'])
        
        # Section 6: Check only Hardware (using proxies)
        miss6 = check_coverage(hw_keys, d_data['sec6'], is_blocks_section=True)
        
        # Section 8 & 10: Check Hardware + Params
        all_keys = hw_keys + param_keys
        miss8 = check_coverage(all_keys, d_data['sec8'], is_blocks_section=False)
        miss10 = check_coverage(all_keys, d_data['sec10'], is_blocks_section=False)
        
        status = "✅"
        if miss6 or miss8 or miss10:
            status = "⚠️ Mismatch"
            
        k_str = ", ".join(all_keys) if all_keys else "None"
        m6_str = f"Missing: {', '.join(miss6)}" if miss6 else "✅"
        m8_str = f"Missing: {', '.join(miss8)}" if miss8 else "✅"
        m10_str = f"Missing: {', '.join(miss10)}" if miss10 else "✅"
        
        report += f"| {pid} | {k_str} | {m6_str} | {m8_str} | {m10_str} | {status} |\n"
            
    Path("semantic_audit_report_101_200.md").write_text(report, encoding='utf-8')
    print("Report generated: semantic_audit_report_101_200.md")

if __name__ == "__main__":
    generate_report()
