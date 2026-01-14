import glob
import re
import random

# --- HEURISTICS & TEMPLATES ---

DOMAINS = {
    "OLED": {
        "titles": ["Drawing Shapes", "Animation Demo", "Invert Colors", "Scrolling Text", "Progress Bar", "Bitmap Icon", "Simple Menu", "Screen Saver", "Data Dashboard"],
        "hardware": ["SSD1306 OLED Display"],
        "wiring": ["SDA -> GP0", "SCL -> GP1"],
        "blocks": ["OLED Show", "OLED Draw Rect", "OLED Print", "OLED Clear"],
    },
    "Servo": {
        "titles": ["Sweep Motion", "Knob Control", "Dual Arm", "Gripper Logic", "Slow Motion", "Sequence Playback", "Torque Test", "Interactive Arm", "Safety Limits"],
        "hardware": ["Servo Motor"],
        "wiring": ["Signal -> GP0"],
        "blocks": ["Servo Pin [0] Angle [90]", "Wait [1]s"],
    },
    "Motor": {
        "titles": ["Speed Control", "Direction Logic", "Soft Start", "Emergency Stop", "Ramp Up/Down", "H-Bridge Safety", "Dual Motor Drive", "Tank Turn", "Fan Controller"],
        "hardware": ["DC Motor", "L9110 Driver"],
        "wiring": ["IA -> GP14", "IB -> GP15"],
        "blocks": ["DC Motor Speed [50]%", "Set Pin [14] HIGH"],
    },
    "Sensor": {
        "titles": ["Data Logger", "Threshold Alarm", "Min/Max Recorder", "Calibration Tool", "Average Reading", "Noise Filter", "Graph Plotter", "Night Mode Trigger", "Security Tripwire"],
        "hardware": ["Analog/Digital Sensor"],
        "wiring": ["Signal -> GP26"],
        "blocks": ["Read Analog Pin [26]", "Log Data"],
    },
    "IoT": {
        "titles": ["WiFi Scan", "Connect to AP", "HTTP Get", "Web Server", "Remote Switch", "Cloud Data Push", "Time Sync (NTP)", "Weather Fetcher", "Mobile Control"],
        "hardware": ["Raspberry Pi Pico W"],
        "wiring": ["Internal WiFi"],
        "blocks": ["Connect WiFi", "HTTP Request"],
    },
    "Logic": {
        "titles": ["Toggle Logic", "Counter Loop", "Random Decision", "State Machine", "Debounce Button", "Sequence Timer", "Password Check", "Reaction Game", "Morse Code"],
        "hardware": ["Button", "LED"],
        "wiring": ["Btn -> GP14", "LED -> GP15"],
        "blocks": ["If/Else", "Wait", "Variable"],
    }
}

DEFAULT_DOMAIN = "Logic"

def get_domain(focus_text):
    ft = focus_text.lower()
    if "oled" in ft or "display" in ft or "screen" in ft: return "OLED"
    if "servo" in ft or "arm" in ft: return "Servo"
    if "motor" in ft or "fan" in ft: return "Motor"
    if "sensor" in ft or "measure" in ft or "temp" in ft: return "Sensor"
    if "wifi" in ft or "iot" in ft or "cloud" in ft: return "IoT"
    return "Logic"

def generate_project_content(id_num, title, domain_key):
    template = DOMAINS.get(domain_key, DOMAINS[DEFAULT_DOMAIN])
    
    content = f"\n## 1️⃣ Project {id_num}: {title}\n"
    content += f"### 2️⃣ Learning Objective\nExplore advanced concepts in {domain_key} using {title}.\n\n"
    
    content += "### 3️⃣ Concepts Introduced\n"
    content += f"*   {domain_key} Control\n*   Automation\n\n"
    
    content += "### 4️⃣ Hardware Required\n*   Raspberry Pi Pico\n"
    for h in template["hardware"]: content += f"*   {h}\n"
    content += "\n"
    
    content += "### 5️⃣ Wiring / Interfaces\n"
    for w in template["wiring"]: content += f"*   {w}\n"
    content += "\n"
    
    content += "### 6️⃣ Blocks Used\n"
    for b in template["blocks"]:
        content += f"🔹 **{b.split(' ')[0]}**\n"
        content += f"*   **Category:** {domain_key}\n"
        content += f"*   **Block:** `{b}`\n"
    content += "\n"
    
    content += "### 7️⃣ Variables & State\n*   **state:** Holds the current status.\n\n"
    
    content += "### 8️⃣ Block Logic\n1. Initialize System.\n2. Loop:\n    * Check Conditions.\n    * Update Output.\n    * Wait.\n\n"
    
    content += "### 9️⃣ Execution Flow (Plain English)\nThe system continuously monitors inputs and updates the interface based on the logic defined.\n\n"
    
    content += "### 🔟 Generated Code (Reference Only)\n```python\nimport time\nimport machine\n\n# Setup\n# ...\n\nwhile True:\n    # Logic\n    time.sleep(0.1)\n```\n\n"
    
    content += "### 1️⃣1️⃣ Common Mistakes & Debug Tips\n*   **Power**: Ensure external power is connected if needed.\n\n"
    
    content += "### 1️⃣2️⃣ Try This Next\n*   Modify the timing parameters.\n\n"
    content += "---\n\n"
    
    return content

def restore_file(filename):
    print(f"Restoring {filename}...")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get Batch Info
    batch_num_match = re.search(r'Batch_(\d+)', filename)
    batch_num = int(batch_num_match.group(1)) if batch_num_match else 0
    
    # Get Focus
    focus_match = re.search(r'\*Focus: (.*?)\*', content)
    focus_text = focus_match.group(1) if focus_match else "General"
    
    domain = get_domain(focus_text)

    # Determine Starting ID
    start_id = (batch_num - 1) * 10 + 1
    
    # TRUNCATE / RESET Logic
    # We want to keep the Header and the First Project.
    # Split by Project Header.
    # [Pre, Proj1_Header, Proj1_Body, Proj2_Header, Proj2_Body, ...]
    parts = re.split(r'(^## 1️⃣.*)', content, flags=re.MULTILINE)
    
    # Safety Check: Must have at least Pre + Proj1
    if len(parts) < 3:
        print(f"Skipping {filename} (Structure unclear, < 3 parts)")
        return

    # Keep exactly: Pre + Proj1_Header + Proj1_Body
    new_content = parts[0] + parts[1] + parts[2]
    new_content = new_content.strip() + "\n\n"
    
    # Generate Projects 2-10 (Index 1-9 in list)
    titles = DOMAINS.get(domain, DOMAINS[DEFAULT_DOMAIN])["titles"]
    
    for i in range(1, 10): # Generate 9 more
        current_id = start_id + i
        t_title = titles[(i-1) % len(titles)]
        id_str = f"{current_id:03d}"
        new_content += generate_project_content(id_str, t_title, domain)
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    files = sorted(glob.glob("Pico_500_Batch_*.md"))
    for f in files:
        restore_file(f)
    print("All files restored.")

if __name__ == "__main__":
    main()
