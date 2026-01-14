import glob
import re
import os

BLOCKS_FILE = "BLOCKS.md"
SECTION_ORDER = [
    "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟", "1️⃣1️⃣", "1️⃣2️⃣"
]

# --- Database of Heuristics ---
def get_heuristics(title):
    t = title.lower()
    h = {
        "objective": "Learn to use this feature with the Pico.",
        "concepts": ["Basic Electronics", "Programming Logic"],
        "hardware": ["Raspberry Pi Pico"],
        "wiring": ["Standard Setup"],
        "blocks": [],
        "logic": "1. Run Loop.\n2. Do action.\n3. Wait.",
        "flow": "The program runs in a continuous loop.",
        "code_hints": []
    }
    
    # --- OLED / Display ---
    if "oled" in t or "display" in t or "screen" in t or "menu" in t or "draw" in t or "graph" in t:
        h["objective"] = "Master the OLED display to show text, graphics, or data."
        h["concepts"] = ["I2C Protocol", "Pixel Coordinates", "Display Buffers"]
        h["hardware"].append("SSD1306 OLED Display")
        h["wiring"] = ["SDA -> GP0", "SCL -> GP1", "VCC -> 3.3V", "GND -> GND"]
        h["blocks"] = ["Init OLED ...", "OLED Show", "OLED Print [Text] ...", "OLED Fill (Clear)"]
        h["logic"] = "1. Init OLED (SDA 0, SCL 1).\n2. Loop:\n    * Clear Screen.\n    * Draw Content.\n    * Show Screen.\n    * Wait."
        h["flow"] = "We draw to the memory buffer first, then send it to the screen with 'Show'."
        h["code_hints"].append("oled")
    
    # --- Servo ---
    if "servo" in t or "arm" in t or "pan" in t or "tilt" in t:
        h["objective"] = "Control a servo motor specifically to specific angles."
        h["concepts"] = ["PWM", "Duty Cycle", "Mechanical Movement"]
        h["hardware"].append("Servo Motor")
        h["wiring"] = ["Signal -> GP0", "VCC -> 5V/3.3V", "GND -> GND"]
        h["blocks"] = ["Servo Pin [0] Angle [90]", "Wait [1] [seconds]"]
        h["logic"] = "1. Loop:\n    * Move Servo to 0.\n    * Wait.\n    * Move Servo to 90.\n    * Wait."
        h["code_hints"].append("servo")

    # --- Motor / DC ---
    if "motor" in t or "fan" in t or "wheel" in t:
        h["objective"] = "Drive a DC motor using a driver module."
        h["concepts"] = ["H-Bridge", "Motor Driver", "High Current"]
        h["hardware"].append("DC Motor + Driver (L9110/L298)")
        h["wiring"] = ["IA -> GP14", "IB -> GP15"]
        h["blocks"] = ["DC Motor ... Speed [100]%", "Set Pin [14] to [HIGH]"]
        h["code_hints"].append("motor")

    # --- Sensor ---
    if "sensor" in t or "detect" in t or "measure" in t or "read" in t:
        h["objective"] = "Read real-world data from a sensor."
        h["concepts"] = ["Analog vs Digital", "Sampling"]
        h["wiring"] = ["Signal -> GP26 (Analog) or GP14 (Digital)"]
        if "temp" in t or "humi" in t:
             h["hardware"].append("DHT11 or Thermistor")
             h["blocks"].append("read sensor [DHT11 Temp] on Pin [15]")
        elif "dist" in t or "ultra" in t:
             h["hardware"].append("Ultrasonic Sensor (HC-SR04)")
             h["blocks"].append("Ultrasonic dist (cm) Trig [14] Echo [15]")
        else:
             h["hardware"].append("Generic Sensor")
             h["blocks"].append("read [Analog] Pin [26]")
        
        h["logic"] = "1. Loop:\n    * Read Sensor Value.\n    * Log Value.\n    * Wait."
    
    # --- LED / Light ---
    if "led" in t or "light" in t or "blink" in t or "flash" in t or "traffic" in t:
        h["objective"] = "Control Digital Outputs to switch lights."
        h["concepts"] = ["GPIO", "Voltage Levels"]
        h["hardware"].append("LED (330ohm Resistor)")
        h["wiring"] = ["Positive -> GP15", "Negative -> GND"]
        h["blocks"] = ["set Pin [15] to [HIGH]", "wait [1] [seconds]"]
        h["logic"] = "1. Loop:\n    * Turn On.\n    * Wait.\n    * Turn Off.\n    * Wait."
    
    # --- Button / Switch ---
    if "button" in t or "switch" in t or "press" in t:
        h["objective"] = "React to user input via a pushbutton."
        h["concepts"] = ["Digital Input", "Pull-up/Pull-down"]
        h["hardware"].append("Pushbutton")
        h["wiring"] = ["Pin 1 -> GP14", "Pin 2 -> GND"]
        h["blocks"] = ["Button (Debounced) Pin [14]", "If / Else"]
        h["logic"] = "1. Loop:\n    * If Button Pressed:\n        * Do Action.\n    * Else:\n        * Stop."
        
    return h

def generate_header_imports(code_snippets):
    imports = set()
    imports.add("import time")
    full_code = "\n".join(code_snippets)
    if "machine" in full_code or "Pin(" in full_code or "ADC(" in full_code or "PWM" in full_code:
        imports.add("import machine")
        imports.add("from machine import Pin, ADC, PWM, I2C")
    if "math." in full_code: imports.add("import math")
    if "random." in full_code: imports.add("import random")
    if "SSD1306" in full_code or "oled" in full_code: imports.add("from ssd1306 import SSD1306_I2C")
    if "neopixel" in full_code: imports.add("import neopixel")
    return list(sorted(imports))

def regenerate_file(filename):
    print(f"Regenerating {filename}...")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract existing Header and Footer
    # Header: From start until first Project Title (exclusive) - Actually Header is per project
    # Preamble: # 🏁 Batch X...
    
    parts = re.split(r'(^## 1️⃣.*)', content, flags=re.MULTILINE)
    new_content = parts[0]
    
    for i in range(1, len(parts), 2):
        if i+1 >= len(parts): break
        header_line = parts[i]
        old_body = parts[i+1]
        
        # Extract ID and Title
        title_match = re.search(r'Project (\d+): (.*)', header_line)
        proj_id = title_match.group(1) if title_match else "???"
        title = title_match.group(2).strip() if title_match else "Unknown"
        
        # Get Heuristics
        h = get_heuristics(title)
        
        # Build Body
        body = "\n"
        
        # 2. Objective
        body += f"### 2️⃣ Learning Objective\n{h['objective']}\n\n"
        
        # 3. Concepts
        body += "### 3️⃣ Concepts Introduced\n"
        for c in h["concepts"]: body += f"*   {c}\n"
        body += "\n"
        
        # 4. Hardware
        body += "### 4️⃣ Hardware Required\n"
        for hw in h["hardware"]: body += f"*   {hw}\n"
        body += "\n"
        
        # 5. Wiring
        body += "### 5️⃣ Wiring / Interfaces\n"
        for w in h["wiring"]: body += f"*   {w}\n"
        body += "\n"
        
        # 6. Blocks
        body += "### 6️⃣ Blocks Used\n"
        for b in h["blocks"]:
             # Try to format roughly matching audit requirement
             body += f"🔹 **{b.split('[')[0].strip()}**\n"
             body += f"*   **Category:** Standard\n"
             body += f"*   **Block:** `{b}`\n"
        body += "\n"
        
        # 7. Variables (Generic)
        body += "### 7️⃣ Variables & State\n"
        body += "*   **val:** Generic variable for data.\n\n"
        
        # 8. Logic
        body += "### 8️⃣ Block Logic\n"
        body += h["logic"] + "\n\n"
        
        # 9. Flow
        body += "### 9️⃣ Execution Flow (Plain English)\n"
        body += h["flow"] + "\n\n"
        
        # 10. Code - Reuse existing if possible, else generate
        # Try to find existing code block in old_body
        existing_code = re.search(r'### 🔟.*?(```python.*?```)', old_body, re.DOTALL)
        if existing_code:
            body += f"### 🔟 Generated Code (Reference Only)\n{existing_code.group(1)}\n\n"
        else:
            # Generate new code
            imports = generate_header_imports(h["code_hints"] + [h["logic"]])
            body += "### 🔟 Generated Code (Reference Only)\n```python\n"
            body += "\n".join(imports) + "\n\n"
            body += "# Hardware Init (Custom)\n\n while True:\n    # Logic\n    time.sleep(1)\n```\n\n"

        # 11 & 12 - Try to rescue or generic
        existing_mistakes = re.search(r'### 1️⃣1️⃣.*?(?=### 1️⃣|$)', old_body, re.DOTALL)
        if existing_mistakes:
            parts = existing_mistakes.group(0).split('Mistakes')
            if len(parts) > 1:
                 body += f"### 1️⃣1️⃣ Common Mistakes{parts[1]}"
            else:
                 body += f"### 1️⃣1️⃣ Common Mistakes\n{existing_mistakes.group(0)}\n"
        else:
            body += "### 1️⃣1️⃣ Common Mistakes & Debug Tips\n*   **Wiring**: Check your connections.\n\n"
            
        existing_next = re.search(r'### 1️⃣2️⃣.*?(?=---|$)', old_body, re.DOTALL)
        if existing_next:
            parts = existing_next.group(0).split('Next')
            if len(parts) > 1:
                body += f"### 1️⃣2️⃣ Try This Next{parts[1]}"
            else:
                body += f"### 1️⃣2️⃣ Try This Next\n{existing_next.group(0)}\n"
        else:
            body += "### 1️⃣2️⃣ Try This Next\n*   Experiment with different values.\n\n"
            
        body += "---\n\n"
        
        new_content += header_line + body

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    files = sorted(glob.glob("Pico_500_Batch_*.md"))
    for f in files:
        regenerate_file(f)
    print("All files regenerated.")

if __name__ == "__main__":
    main()
