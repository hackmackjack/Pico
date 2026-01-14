
import os

def generate_batch_70_part2():
    projects = []

    # 0696: Smart Switch (Beacon)
    projects.append({
        "id": "0696",
        "title": "Smart Morse Code Switch",
        "objective": "Beacon Switch: If Switch On, transmit a fixed callsign (e.g., 'ABC') every 30 seconds automatically.",
        "concepts": ["Periodic Tasks", "Automated Telemetry", "Beacon Logic", "Wait States"],
        "hardware": ["Pico", "Switch", "LED"],
        "interface": "| **Switch** | GP14 | Enable |\n| **LED** | GP16 | Transmit |",
        "blocks": ["*   **from Loops, drag `repeat`**", "*   **from Logic, drag `if_else`**"],
        "vars": ["None"],
        "guide": """**A. Loop**:
1.  **Check Switch**:
  *   If Switch On:
      *   Call `send("ABC")`.
      *   Wait 30s.
  *   Else:
      *   Wait 0.1s.
  *   **Snap** into `pico_forever`.""",
        "flow": "Used in navigation buoys and radio repeaters.",
        "code": """import machine, time
sw = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(16, machine.Pin.OUT)
unit = 0.1
morse = {'A': '.-', 'B': '-...', 'C': '-.-.'}

def send(text):
    for char in text:
        if char in morse:
            for s in morse[char]:
                led.on(); time.sleep(unit if s=='.' else unit*3); led.off(); time.sleep(unit)
            time.sleep(unit*3) # Letter gap

while True:
    if sw.value():
        send("ABC")
        time.sleep(30)
    time.sleep(0.1)""",
        "mistakes": ["**Blocking**: `time.sleep(30)` blocks turning the switch OFF. Use `ticks_ms` for responsive stop.", "**Power**: Beacons need low power sleep, not active wait."],
        "next": ["**Callsign**: Change text to unique ID.", "**Power Save**: Use `machine.lightsleep()`."]
    })

    # 0697: Alarm
    projects.append({
        "id": "0697",
        "title": "Morse Code Alarm System",
        "objective": "Crash Detection: Use a Tilt Sensor. If the board is upside down (simulating a crash), emit 'SOS' continuously on the Buzzer.",
        "concepts": ["Emergency Beacons", "Orientation Sensing", "Priority Alerts", "Looping States"],
        "hardware": ["Pico", "Tilt Sensor", "Buzzer"],
        "interface": "| **Tilt** | GP14 | Orient |\n| **Buzzer** | GP16 | Signal |",
        "blocks": ["*   **from Logic, drag `if_else`**", "*   **from Functions, drag `call_function`**"],
        "vars": ["None"],
        "guide": """**A. Loop**:
1.  **Check Orientation**:
  *   If Tilt Sensor Indicates Upside Down:
      *   Call `play("SOS")`.
  *   Else:
      *   Buzzer Off.
  *   **Snap** into `pico_forever`.""",
        "flow": "Automatic distress signals (ELT - Emergency Locator Transmitter) save lives in aviation.",
        "code": """import machine, time
tilt = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
buz = machine.PWM(machine.Pin(16))
unit = 0.1
morse_s = '...'
morse_o = '---'

def tone(d):
    buz.freq(1000); buz.duty_u16(32768); time.sleep(d); buz.duty_u16(0); time.sleep(unit)

def sos():
    for x in morse_s: tone(unit); 
    time.sleep(unit*2)
    for x in morse_o: tone(unit*3);
    time.sleep(unit*2)
    for x in morse_s: tone(unit);
    time.sleep(unit*6)

while True:
    if tilt.value() == 1: # Adjust based on sensor type
        sos()
    else:
        buz.duty_u16(0)
    time.sleep(0.1)""",
        "mistakes": ["**False Alarm**: Turbulence might trigger it briefly. Need a 'sustained' check.", "**Code Order**: S-O-S is distinct. S-S-S-O-O-O is wrong."],
        "next": ["**Latch**: Once triggered, stay on until reset button pressed.", "**Light**: Flash LED with SOS."]
    })

    # 0698: Game
    projects.append({
        "id": "0698",
        "title": "The Morse Code Game",
        "objective": "Copycat Trainer: The Pico plays a random letter. You must type that letter into the Console to score a point.",
        "concepts": ["Ear Training", "Random Stimulus", "Input Validation", "Gamification"],
        "hardware": ["Pico", "Buzzer"],
        "interface": "| **Buzzer** | GP16 | Audio |",
        "blocks": ["*   **from Variables, drag `create_map`**", "*   **from Text, drag `input_prompt`**"],
        "vars": ["**score**: Int"],
        "guide": """**A. Loop**:
1.  **Pick**:
  *   `target` = Random Key from Dict.
  *   Play `target`.
2.  **Guess**:
  *   `guess` = Input("What letter?").
  *   If `guess` == `target`: Win.
  *   Else: Fail.
3.  **Snap** into `pico_forever`.""",
        "flow": "The 'Koch Method' teaches Morse by recognizing full sounds, not counting dots.",
        "code": """import machine, time, random
buz = machine.PWM(machine.Pin(16))
unit = 0.08
morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.'}
keys = list(morse.keys())

def play(code):
    for s in code:
        buz.freq(600); buz.duty_u16(32768)
        if s == '.': time.sleep(unit)
        else: time.sleep(unit*3)
        buz.duty_u16(0); time.sleep(unit)

while True:
    target = random.choice(keys)
    print("Listen...")
    time.sleep(1)
    play(morse[target])
    
    guess = input("Letter: ").upper()
    if guess == target: print("CORRECT!")
    else: print(f"WRONG. It was {target}")
    time.sleep(1)""",
        "mistakes": ["**Timing**: If play is too slow, user counts dots. Make it fast to force pattern recognition.", "**Console**: User must look at screen, not just listen."],
        "next": ["**Words**: Play 3-letter words.", "**Callsigns**: Play standard callsigns (K1ABC)."]
    })

    # 0699: Automated
    projects.append({
        "id": "0699",
        "title": "Automated Morse Code",
        "objective": "Reverse Decoder logic: Take a list of booleans `[True, False, True, True]` (representing Short, Long, Short, Short -> L) and match it to a character.",
        "concepts": ["Reverse Lookup", "Pattern Matching", "Data Parsing", "Algorithmic Thinking"],
        "hardware": ["Pico"],
        "interface": "| **Console** | USB | Output |",
        "blocks": ["*   **from Variables, drag `create_map`**", "*   **from Logic, drag `if_compare`**"],
        "vars": ["**input**: List"],
        "guide": """**A. Logic**:
1.  **Define**: Map '.-..' -> 'L'.
2.  **Input**: List `[0, 1, 0, 0]` (0=Dot, 1=Dash).
3.  **Convert**:
  *   String `s` = "".
  *   Loop `x` in List:
      *   If `x`==0: `s` += "."
      *   Else: `s` += "-"
4.  **Find**:
  *   Loop `key, val` in Dict:
      *   If `val` == `s`: Print `key`.
  *   **Snap** into `pico_forever`.""",
        "flow": "Translating raw signal data back into human meaning.",
        "code": """import time
reverse_morse = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '.-..': 'L'
}
# 0=Dot, 1=Dash
incoming = [0, 1, 0, 0] # L

while True:
    s = ""
    for bit in incoming:
        if bit == 0: s += "."
        else: s += "-"
        
    print(f"Sequence: {s}")
    if s in reverse_morse:
        print(f"Char: {reverse_morse[s]}")
    else:
        print("Unknown")
    time.sleep(5)""",
        "mistakes": ["**Efficiency**: Looping through the whole dict is slow (O(N)). Better to have a Reverse Dict `{'.-': 'A'}` (O(1)).", "**Noise**: Real decoding deals with variable signal lengths."],
        "next": ["**Tree Search**: Implement a Binary Tree for Morse Decoding.", "**Real Input**: Use button press durations to build the list."]
    })

    # 0700: Mastering
    projects.append({
        "id": "0700",
        "title": "Mastering Morse Code",
        "objective": "Farnsworth Timing Engine: Implement a function that plays characters at high speed (15 WPM) but spaces them out (5 WPM).",
        "concepts": ["Advanced Timing", "Leitner System", "Learning Algorithms", "Psychophysics"],
        "hardware": ["Pico", "Buzzer"],
        "interface": "| **Buzzer** | GP16 | Audio |",
        "blocks": ["*   **from Functions, drag `define_function`**", "*   **from Math, drag `arithmetic`**"],
        "vars": ["**wpm_char**: Int", "**wpm_overall**: Int"],
        "guide": """**A. Init**: `wpm_char`=20. `wpm_overall`=5.
**B. Function**:
  *   `unit` = 1.2 / `wpm_char`.
  *   `farnsworth_delay` = (1.2 / `wpm_overall`) - (1.2 / `wpm_char`).
**C. Loop**:
  *   Play Char "H" (Fast).
  *   Wait `farnsworth_delay`.
  *   Play Char "I" (Fast).
  *   **Snap** into `pico_forever`.""",
        "flow": "The standard way to learn Morse. Prevents 'counting dots' by making the symbols too fast to count, while giving thinking time between them.",
        "code": """import machine, time
buz = machine.PWM(machine.Pin(16))
morse = {'H': '....', 'I': '..'}

wpm_char = 20
wpm_overall = 5

unit = 1.2 / wpm_char
# Standard word is 50 units.
# Delay calculation is complex using standard formula:
# Ta = (60*C - 37.2*W) / W  ... where C=Overall, W=CharSpeed. 
# Simplified: Just add extra gap.
extra_gap = (60/wpm_overall) - (60/wpm_char) # Rough approx for demo

def play(char):
    if char in morse:
        for s in morse[char]:
            buz.freq(600); buz.duty_u16(32768)
            time.sleep(unit if s=='.' else unit*3)
            buz.duty_u16(0); time.sleep(unit)
    time.sleep(extra_gap)

while True:
    play('H')
    play('I')""",
        "mistakes": ["**Math Error**: Farnsworth math is tricky. The key is just 'Longer Spaces'.", "**Drift**: Accumulating floating point errors."],
        "next": ["**Selectable**: Use Pot to adjust spacing live.", "**Flashcards**: Random chars with Farnsworth spacing."]
    })

    # OUTPUT
    final_md = ""
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
    generate_batch_70_part2()
