import re
import os

DOC_FILE = "Documentation/Docs_0101_0200.md"

def read_file(filepath):
    if not os.path.exists(filepath): return ""
    with open(filepath, 'r') as f: return f.read()

def write_file(filepath, content):
    with open(filepath, 'w') as f: f.write(content)

def parse_code_to_steps(code_block, variables):
    steps = []
    lines = code_block.split('\n')

    step_count = 1

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"): continue

        # Loop start
        if "while True:" in line:
            steps.append("\n**B. Main Loop Phase**")
            steps.append(f"{step_count}. **Start Loop**:")
            steps.append(f"    *   From **Loops**, drag **`pico_forever`**.")
            step_count += 1
            continue

        # Digital Write: pin.value(1)
        m_write = re.search(r"(\w+)\.value\((0|1)\)", line)
        if m_write:
            var_name = m_write.group(1)
            val = m_write.group(2)
            state = "HIGH (1)" if val == "1" else "LOW (0)"
            steps.append(f"{step_count}. **Control `{var_name}`**:")
            steps.append(f"    *   From **Smart IO**, drag **`pico_gpio_write`**.")
            steps.append(f"    *   Set Pin to **`{var_name}`** and State to **{state}**.")
            step_count += 1
            continue

        # PWM Write: pin.duty_u16(val)
        m_pwm = re.search(r"(\w+)\.duty_u16\(([\w\d]+)\)", line)
        if m_pwm:
            var_name = m_pwm.group(1)
            val = m_pwm.group(2)
            steps.append(f"{step_count}. **Control `{var_name}` (PWM)**:")
            steps.append(f"    *   From **Smart IO**, drag **`pico_pwm_write`**.")
            steps.append(f"    *   Set Pin to **`{var_name}`** and Duty to **{val}**.")
            step_count += 1
            continue

        # Wait: time.sleep(x)
        m_wait = re.search(r"time\.sleep\(([\d\.]+)\)", line)
        if m_wait:
            dur = m_wait.group(1)
            steps.append(f"{step_count}. **Wait**:")
            steps.append(f"    *   From **Smart IO**, drag **`pico_wait`**.")
            steps.append(f"    *   Set duration to **{dur}** seconds.")
            step_count += 1
            continue

        # If
        if line.startswith("if "):
            cond = line[3:-1].replace("==", "equals").replace("!=", "not equal")
            steps.append(f"{step_count}. **Logic Check**:")
            steps.append(f"    *   From **Logic**, drag **`controls_if`**.")
            steps.append(f"    *   Condition: `{cond}`.")
            step_count += 1
            continue

        # Else
        if line.startswith("else:"):
            steps.append(f"    *   **Else**:")
            continue

    return "\n".join(steps)

def process_project(content):
    # Extract ID
    m_id = re.search(r"## Project (\d{4}):", content)
    if not m_id: return content
    pid = m_id.group(1)

    # Extract Code
    code_match = re.search(r"### 10\. Generated Code\n```python\n(.*?)\n```", content, re.DOTALL)
    if not code_match:
        print(f"[{pid}] No code found, skipping.")
        return content
    code = code_match.group(1)

    init_steps = []
    init_steps.append("**A. Initialization Phase**")
    step_num = 1

    # 1. Pin Inits: var = Pin(15, Pin.OUT)
    pin_defs = re.findall(r"(\w+) = Pin\((\d+|[\"']LED[\"'])(?:, ([^\)]+))?\)", code)
    for name, pin, mode in pin_defs:
        # Check if it's wrapped in PWM or ADC later?
        # Actually regex captures just the Pin part.

        # Refine mode
        mode_str = "Output" if "OUT" in mode else "Input"
        pull = ""
        if "PULL_DOWN" in mode: pull = ", Pull-Down"
        if "PULL_UP" in mode: pull = ", Pull-Up"

        init_steps.append(f"{step_num}. **Initialize `{name}`**:")
        init_steps.append(f"    *   From **Variables**, create variable **`{name}`**.")
        init_steps.append(f"    *   From **Smart IO**, drag **`Pin`** block.")
        init_steps.append(f"    *   Set to **GP{pin.strip('\"')}{pull}** ({mode_str}).")
        init_steps.append(f"    *   **Snap** into `start`.")
        step_num += 1

    # 2. PWM Inits: var = PWM(Pin(15)) - Logic usually nested
    # We might miss this if we only look for direct assignment.
    # Let's look for `var = PWM(...)`
    pwm_defs = re.findall(r"(\w+) = PWM\(Pin\((\d+)\)\)", code)
    for name, pin in pwm_defs:
        init_steps.append(f"{step_num}. **Initialize `{name}` (PWM)**:")
        init_steps.append(f"    *   From **Variables**, create variable **`{name}`**.")
        init_steps.append(f"    *   From **Smart IO**, drag **`PWM`** block.")
        init_steps.append(f"    *   Set Pin to **GP{pin}**.")
        init_steps.append(f"    *   **Snap** into `start`.")
        step_num += 1

    # 3. ADC Inits: var = ADC(26)
    adc_defs = re.findall(r"(\w+) = ADC\((\d+)\)", code)
    for name, pin in adc_defs:
        init_steps.append(f"{step_num}. **Initialize `{name}` (ADC)**:")
        init_steps.append(f"    *   From **Variables**, create variable **`{name}`**.")
        init_steps.append(f"    *   From **Smart Sensors**, drag **`ADC`** block.")
        init_steps.append(f"    *   Set Pin to **GP{pin}**.")
        step_num += 1

    # 4. I2C/OLED Inits
    if "ssd1306.SSD1306_I2C" in code:
        init_steps.append(f"{step_num}. **Initialize OLED**:")
        init_steps.append(f"    *   From **Smart Display**, drag **`pico_oled_init`**.")
        init_steps.append(f"    *   Set Width: 128, Height: 64, SDA: GP0, SCL: GP1.")
        step_num += 1

    # Logic Steps
    logic_steps = parse_code_to_steps(code, {})

    new_s8 = "### 8. Step-by-Step Guide\n\n" + "\n".join(init_steps) + "\n" + logic_steps

    # Replace S8
    s8_start = content.find("### 8. Step-by-Step Guide")
    s9_start = content.find("### 9. Execution Flow")

    if s8_start != -1 and s9_start != -1:
        print(f"[{pid}] Replaced S8.")
        return content[:s8_start] + new_s8 + "\n\n" + content[s9_start:]
    else:
        print(f"[{pid}] S8/S9 markers not found.")
        return content

def main():
    content = read_file(DOC_FILE)
    if not content: return

    parts = re.split(r"(?=## Project \d{4}:)", content)
    header = parts[0]
    projects = parts[1:]

    new_projects = []
    for p in projects:
        new_p = process_project(p)
        new_projects.append(new_p)

    final_content = header + "".join(new_projects)
    write_file(DOC_FILE, final_content)
    print("Batch expansion complete.")

if __name__ == "__main__":
    main()
