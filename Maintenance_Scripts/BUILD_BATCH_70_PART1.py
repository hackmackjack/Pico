
import os

def generate_batch_70_part1():
    header = """
# 🏁 Batch 70: Morse Code 4

---
"""
    projects = []

    # 0691: Intro Morse
    projects.append({
        "id": "0691",
        "title": "Introduction to Morse Code",
        "objective": "Blink the text 'HELLO' in Morse Code on the LED. (H=...., E=., L=.-.., O=---).",
        "concepts": ["Symbol Encoding", "Communication Primitives", "Timing Standards", "Strings"],
        "hardware": ["Pico", "LED"],
        "interface": "| **LED** | GP25 | Onboard LED |",
        "blocks": ["*   **from Actuators, drag `pwm_duty`**", "*   **from Loops, drag `for_in_list`**"],
        "vars": ["**unit**: Float"],
        "guide": """**A. Init**:
  *   `unit` = 0.2s.
**B. Function `dot()`**:
  *   LED On. Wait `unit`. LED Off. Wait `unit`.
**C. Function `dash()`**:
  *   LED On. Wait `unit`*3. LED Off. Wait `unit`.
**D. Loop**:
  *   H: dot,dot,dot,dot. Wait `unit`*3 (Letter Gap).
  *   E: dot. Gap.
  *   L: dot,dash,dot,dot. Gap.
  *   L: dot,dash,dot,dot. Gap.
  *   O: dash,dash,dash. Wait `unit`*7 (Word Gap).
  *   **Snap** into `pico_forever`.""",
        "flow": "Morse code relies on strict timing ratios. Dash = 3x Dot. Letter Gap = 3x Dot. Word Gap = 7x Dot.",
        "code": """import machine, time
led = machine.Pin(25, machine.Pin.OUT)
unit = 0.2

def dot():
    led.on(); time.sleep(unit); led.off(); time.sleep(unit)

def dash():
    led.on(); time.sleep(unit*3); led.off(); time.sleep(unit)

def gap():
    time.sleep(unit*2) # +1 from dot/dash = 3 units

while True:
    # H
    dot(); dot(); dot(); dot(); gap()
    # E
    dot(); gap()
    # L
    dot(); dash(); dot(); dot(); gap()
    # L
    dot(); dash(); dot(); dot(); gap()
    # O
    dash(); dash(); dash()
    time.sleep(unit*7)""",
        "mistakes": ["**Timing**: Forgetting that every dot/dash includes a trailing gap of 1 unit. So Letter Gap is just 2 *additional* units.", "**Visibility**: Use an external LED if the onboard one is hard to see."],
        "next": ["**Function**: Create `send_letter('H')`.", "**Speed**: Change `unit` to 0.1s."]
    })

    # 0692: Blinking (Speed)
    projects.append({
        "id": "0692",
        "title": "Blinking Morse Code",
        "objective": "Variable Speed: Use a Switch to toggle between Fast (10 WPM) and Slow (5 WPM) Morse Code transmission.",
        "concepts": ["WPM Calculations", "Variable Timing", "User Configuration", "Mode Switching"],
        "hardware": ["Pico", "Switch", "LED"],
        "interface": "| **Switch** | GP14 | Speed |\n| **LED** | GP16 | Signal |",
        "blocks": ["*   **from Logic, drag `if_else`**", "*   **from Variables, drag `set_variable`**"],
        "vars": ["**unit**: Float"],
        "guide": """**A. Loop**:
1.  **Check Switch**:
  *   If Switch On: `unit` = 0.06 (Fast).
  *   Else: `unit` = 0.12 (Slow).
2.  **Send**:
  *   Send "SOS" (... --- ...).
  *   **Snap** into `pico_forever`.""",
        "flow": "WPM = 1.2 / unit_seconds. So 0.12s = 10 WPM. 0.06s is actually 20 WPM.",
        "code": """import machine, time
sw = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(16, machine.Pin.OUT)

def flash(duration):
    led.on(); time.sleep(duration); led.off(); time.sleep(unit)

while True:
    if sw.value(): unit = 0.06
    else: unit = 0.12
    
    # S
    flash(unit); flash(unit); flash(unit)
    time.sleep(unit*2)
    # O
    flash(unit*3); flash(unit*3); flash(unit*3)
    time.sleep(unit*2)
    # S
    flash(unit); flash(unit); flash(unit)
    time.sleep(unit*6)""",
        "mistakes": ["**Scope**: `unit` needs to be global or passed as arg.", "**Hardcoding**: Writing '0.06' everywhere instead of using variable."],
        "next": ["**Pot**: Continuously variable speed.", "**Farnsworth**: Fast chars, slow gaps."]
    })

    # 0693: Manual
    projects.append({
        "id": "0693",
        "title": "Manual Morse Code Control",
        "objective": "Straight Key: Press button to produce a specific tone (Sine Wave/Square Wave). Practice tapping SOS.",
        "concepts": ["Telegraphy", "Manual Keying", "Audio Feedback", "Human Interface Device"],
        "hardware": ["Pico", "Button", "Buzzer"],
        "interface": "| **Button** | GP14 | Key |\n| **Buzzer** | GP16 | Tone |",
        "blocks": ["*   **from Smart IO, drag `pico_gpio_read`**", "*   **from Actuators, drag `pwm_tone`**"],
        "vars": ["None"],
        "guide": """**A. Loop**:
1.  **Poll**:
  *   If Btn:
      *   Buzzer Freq 600Hz.
  *   Else:
      *   Buzzer Off.
  *   **Snap** into `pico_forever`.""",
        "flow": "The simplest form of digital communication. The human brain handles the encoding.",
        "code": """import machine, time
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
buz = machine.PWM(machine.Pin(16))

while True:
    if btn.value():
        buz.freq(600); buz.duty_u16(32768)
    else:
        buz.duty_u16(0)
    time.sleep(0.01)""",
        "mistakes": ["**Bounce**: Key clicks might stutter. (Debounce usually not needed for audio keying as fingers are slow).", "**Latency**: `time.sleep` > 0.05 will feel laggy."],
        "next": ["**Iambic Paddle**: Two buttons (Dot/Dash) for automatic timing.", "**Decoder**: Pico prints what you tap."]
    })

    # 0694: Sequences (Dictionary)
    projects.append({
        "id": "0694",
        "title": "Morse Code Sequences",
        "objective": "Full Alphabet: Create a Dictionary mapping 'A' to '.-', 'B' to '-...', etc. Define a function to play any string.",
        "concepts": ["Data Structures (Dictionaries)", "Lookup Tables", "Parsing", "Character Iteration"],
        "hardware": ["Pico", "Buzzer"],
        "interface": "| **Buzzer** | GP16 | Audio |",
        "blocks": ["*   **from Variables, drag `create_map`**", "*   **from Functions, drag `define_function`**"],
        "vars": ["**morse**: Dict"],
        "guide": """**A. Init**:
  *   `morse` = {'A': '.-', 'B': '-...', 'C': '-.-.' ...}
**B. Function `play(text)`**:
  *   Loop `char` in `text`:
      *   `code` = `morse`[`char`].
      *   Loop `symbol` in `code`:
           *   If `.`: Dot().
           *   If `-`: Dash().
      *   Gap().
**C. Loop**:
  *   Call `play("SOS")`. Wait 2s.
  *   Call `play("CAB")`. Wait 2s.
  *   **Snap** into `pico_forever`.""",
        "flow": "Validates the power of software. We define the rules (Dict) and the logic (Player) once, then transmit anything.",
        "code": """import machine, time
buz = machine.PWM(machine.Pin(16))
unit = 0.1
morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'S': '...', 'O': '---'
}

def tone(duration):
    buz.freq(600); buz.duty_u16(32768); time.sleep(duration); buz.duty_u16(0); time.sleep(unit)

def play(text):
    for char in text:
        if char in morse:
            code = morse[char]
            for symbol in code:
                if symbol == '.': tone(unit)
                elif symbol == '-': tone(unit*3)
            time.sleep(unit*2) # Letter gap
    time.sleep(unit*4) # Word gap

while True:
    play("SOS")
    play("ABC")""",
        "mistakes": ["**Case Sensitivity**: 'a' is not in `morse`. Use `char.upper()`.", "**KeyError**: Crashing if a character (e.g., Space) is missing."],
        "next": ["**Space Handling**: Treat space as 7-unit silence.", "**Numbers**: Add 0-9."]
    })

    # 0695: Interactive
    projects.append({
        "id": "0695",
        "title": "Interactive Morse Code",
        "objective": "Translator: User types a character in the Python Console. The Pico blinks that character.",
        "concepts": ["Serial Input", "UART/USB Communication", "Interactive Shell", "String Processing"],
        "hardware": ["Pico", "LED"],
        "interface": "| **USB** | Console | Input |",
        "blocks": ["*   **from Text, drag `input_prompt`**", "*   **from Logic, drag `if_compare`**"],
        "vars": ["**msg**: String"],
        "guide": """**A. Loop**:
1.  **Input**:
  *   `msg` = Input("Type Char: ").
2.  **Process**:
  *   Convert `msg` to Upper Case.
  *   Lookup in Dict.
  *   Blink Pattern.
  *   **Snap** into `pico_forever`.""",
        "flow": "Bridges the gap between the PC keyboard and the microcontroller hardware.",
        "code": """import machine, time
led = machine.Pin(16, machine.Pin.OUT)
unit = 0.2
morse = {'A': '.-', 'B': '-...', 'C': '-.-.'} # Add more

def play(code):
    for symbol in code:
        led.on()
        if symbol == '.': time.sleep(unit)
        else: time.sleep(unit*3)
        led.off()
        time.sleep(unit)

while True:
    msg = input("Char: ").upper()
    if msg in morse:
        play(morse[msg])
    else:
        print("Unknown")""",
        "mistakes": ["**Blocking Input**: `input()` pauses the whole program until Enter is pressed. (Acceptable here).", "**Empty Input**: Pressing Enter with no text might crash."],
        "next": ["**Reverse**: Pico sends text to PC via USB HID (Keyboard).", "**Buffer**: Type a whole sentence."]
    })

    # OUTPUT
    final_md = header
    
    for p in projects:
        final_md += f"""
## {int(p['id']) - 600}. Project {p['id']}: {p['title']}

### 2. Learning Objective
{p['objective']}

### 3. Concepts Introduced
"""
        for c in p['concepts']:
            final_md += f"*   **{c}**\n"
            
        final_md += f"""
### 4. Hardware Required
"""
        for h in p['hardware']:
            final_md += f"*   **{h}**\n"

        final_md += f"""
### 5. Wiring / Interfaces
{p['interface']}

### 6. Blocks Used
"""
        for b in p['blocks']:
            final_md += f"{b}\n"

        final_md += f"""
### 7. Variables
"""
        for v in p['vars']:
            final_md += f"*   **{v}**\n"

        final_md += f"""
### 8. Step-by-Step Guide
{p['guide']}

### 9. Execution Flow
{p['flow']}

### 10. Generated Code
```python
{p['code']}
```

### 11. Common Mistakes
"""
        for m in p['mistakes']:
            final_md += f"*   {m}\n"

        final_md += f"""
### 12. Try This Next
"""
        for n in p['next']:
            final_md += f"*   {n}\n"
            
        final_md += "\n---\n"

    with open(r'd:\MFF\Pico\Documentation\Docs_0601_0700.md', 'a', encoding='utf-8') as f:
        f.write(final_md)

if __name__ == "__main__":
    generate_batch_70_part1()
