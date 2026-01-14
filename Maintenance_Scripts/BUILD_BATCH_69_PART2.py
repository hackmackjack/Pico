
import os

def generate_batch_69_part2():
    projects = []

    # 0686: Smart Switch (Reset Protection)
    projects.append({
        "id": "0686",
        "title": "Smart Counting Machine Switch",
        "objective": "Reset Protection: To reset the counter to 0, the Reset Button must be held DOWN for a full 3 seconds.",
        "concepts": ["Long Press Logic", "Destructive Actions", "Safety Interlocks", "State Clearing"],
        "hardware": ["Pico", "Count Button", "Reset Button"],
        "interface": "| **Count** | GP14 | Inc |\n| **Reset** | GP15 | Clear |",
        "blocks": ["*   **from Layers, drag `repeat_until`**", "*   **from Time, drag `time_ticks_ms`**"],
        "vars": ["**count**: Int"],
        "guide": """**A. Loop**:
1.  **Count**:
  *   If Btn A: `count`+=1.
2.  **Reset Check**:
  *   If Btn Rset Pressed:
      *   `start` = `time`.
      *   Wait Until Released OR (`time` - `start` > 3000).
      *   If Timer > 3000:
           *   `count` = 0.
           *   Print "CLEARED".
  *   **Snap** into `pico_forever`.""",
        "flow": "Prevents accidental data loss. Common in factory settings.",
        "code": """import machine, time
count_btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
reset_btn = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
count = 0

while True:
    if count_btn.value():
        count += 1
        print(count)
        while count_btn.value(): time.sleep(0.01)
        
    if reset_btn.value():
        start = time.ticks_ms()
        held = True
        while time.ticks_diff(time.ticks_ms(), start) < 3000:
            if not reset_btn.value():
                held = False
                break
            time.sleep(0.1)
        
        if held:
            count = 0
            print("RESET DONE")
            while reset_btn.value(): time.sleep(0.1)
            
    time.sleep(0.01)""",
        "mistakes": ["**Feedback**: The user doesn't know when 3s is up. A blinking LED helps.", "**Re-trigger**: Must wait for release after reset."],
        "next": ["**Countdown**: Show 3...2...1... on screen.", "**Two Button**: Hold A+B to reset."]
    })

    # 0687: Alarm
    projects.append({
        "id": "0687",
        "title": "Counting Machine Alarm System",
        "objective": "Capacity Monitor: If the count exceeds 10 persons, Trigger Alarm (Buzzer).",
        "concepts": ["Limit Monitoring", "Occupancy Safety", "Threshold Triggers", "Compliance Logic"],
        "hardware": ["Pico", "Button", "Buzzer"],
        "interface": "| **Button** | GP14 | Enter |\n| **Buzzer** | GP16 | Alarm |",
        "blocks": ["*   **from Logic, drag `if_compare`**", "*   **from Actuators, drag `pwm_tone`**"],
        "vars": ["**people**: Int"],
        "guide": """**A. Loop**:
1.  **Count**:
  *   If Btn: `people` += 1.
2.  **Check**:
  *   If `people` > 10:
      *   Buzzer On.
      *   Print "OVER CAPACITY".
  *   Else:
      *   Buzzer Off.
  *   **Snap** into `pico_forever`.""",
        "flow": "Used in elevators, clubs, and buses where weight/safety limits exist.",
        "code": """import machine, time
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
buz = machine.PWM(machine.Pin(16))
people = 0

while True:
    if btn.value():
        people += 1
        print(f"Occupancy: {people}")
        while btn.value(): time.sleep(0.01)
        
    if people > 10:
        buz.freq(1000); buz.duty_u16(32768)
    else:
        buz.duty_u16(0)
    time.sleep(0.01)""",
        "mistakes": ["**Stuck Alarm**: How to stop it? Must decrement (`people -= 1`) or reset.", "**Tone**: Continuous tone is annoying. Pulse it?"],
        "next": ["**Decrement**: Add Exit button to reduce count.", "**Warning**: Yellow light at 8 people."]
    })

    # 0688: Game
    projects.append({
        "id": "0688",
        "title": "The Counting Machine Game",
        "objective": "Estimation Challenge: The screen says 'GO'. Close your eyes and click the button exactly 50 times. The system verifies your accuracy.",
        "concepts": ["Mental Counting", "Focus", "Accuracy vs Speed", "Blind Testing"],
        "hardware": ["Pico", "Button"],
        "interface": "| **Button** | GP14 | Click |",
        "blocks": ["*   **from Logic, drag `if_compare`**", "*   **from Text, drag `print`**"],
        "vars": ["None"],
        "guide": """**A. Loop**:
1.  **Wait**: Press to Start.
2.  **Run**:
  *   `count` = 0.
  *   Loop while `time` < 30s (Limit):
      *   If Btn: `count` += 1.
  *   Print "Time Up".
  *   Print "Your Count: " + `count`.
  *   **Snap** into `pico_forever`.""",
        "flow": "Most people lose count around 20 or speed up unconsciously.",
        "code": """import machine, time
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    print("Press to Start...")
    while not btn.value(): pass
    while btn.value(): pass
    
    print("GO! (Press Button to Stop)")
    count = 0
    start = time.ticks_ms()
    
    # We need a stop condition. Let's say holding button for 2s stops.
    # Or just a fixed duration? Let's do: Keep clicking until you think you hit 50.
    # Then hold to finish.
    
    finished = False
    while not finished:
        if btn.value():
            # Check for long press to finish
            p_start = time.ticks_ms()
            while btn.value():
                if time.ticks_diff(time.ticks_ms(), p_start) > 2000:
                    finished = True
                    break
            if not finished: count += 1
            time.sleep(0.05) 
            
    print(f"Real Count: {count}")
    print(f"Error: {abs(50 - count)}")
    time.sleep(5)""",
        "mistakes": ["**Inputs**: Using the same button for 'Count' and 'Stop' is tricky. Better to have a separate Stop button.", "**Double Clicks**: Mechanical switches bounce causing extra counts."],
        "next": ["**Time Estimate**: Click once every 1.0 seconds for 10 seconds.", "**Rhythm**: Match a metronome beat."]
    })

    # 0689: Automated
    projects.append({
        "id": "0689",
        "title": "Automated Counting Machine",
        "objective": "Optical Counter: Use a flashlight and LDR. Every time the beam is broken (dark), increment count. (Production Line Counter).",
        "concepts": ["Beam Break", "Industrial Automation", "Sensor Calibration", "Edge Detection"],
        "hardware": ["Pico", "LDR", "Light Source"],
        "interface": "| **LDR** | GP26 | Detector |",
        "blocks": ["*   **from Smart IO, drag `pico_analog_read`**", "*   **from Logic, drag `if_compare`**"],
        "vars": ["**broken**: Bool"],
        "guide": """**A. Init**: `count` = 0.
**B. Loop**:
1.  **Read**: `val` = ADC.
2.  **Logic**:
  *   If `val` < 5000 (Beam Blocked) AND `broken` == False:
      *   `count` += 1.
      *   `broken` = True.
      *   Print `count`.
  *   If `val` > 10000 (Beam Clear):
      *   `broken` = False.
  *   **Snap** into `pico_forever`.""",
        "flow": "Standard method for counting bottles, boxes, or people passing through a gate.",
        "code": """import machine, time
ldr = machine.ADC(26)
count = 0
broken = False

# Assumption: Light on LDR = High Val? No, Usually Low Voltage (Dark=High Res).
# Adjust based on wiring. Let's assume Dark = High Val (>40000).

while True:
    val = ldr.read_u16()
    
    if val > 40000 and not broken: # Beam Broken (Dark)
        count += 1
        print(f"Item #{count}")
        broken = True
    
    if val < 20000: # Beam Restored (Light)
        broken = False
        
    time.sleep(0.01)""",
        "mistakes": ["**Alignment**: LDR must be inside a tube to block ambient light.", "**Speed**: ADC is slow? No, Python loop is the bottleneck for fast items."],
        "next": ["**Rate**: Calculate Items Per Minute.", "**Total**: Stop when 100 items reached."]
    })

    # 0690: Mastering
    projects.append({
        "id": "0690",
        "title": "Mastering Counting Machine",
        "objective": "7-Segment Display: Drive a single digit LED display using 7 GPIO pins. Create a 'Font' mapping numbers to segments.",
        "concepts": ["Look-Up Tables (LUT)", "Segment Mapping", "Multiplexing", "Display Drivers"],
        "hardware": ["Pico", "7-Seg Display"],
        "interface": "| **Seg Loop (A-G)** | GP10-16 | |",
        "blocks": ["*   **from Variables, drag `create_list`**", "*   **from Functions, drag `define_function`**"],
        "vars": ["**font**: List"],
        "guide": """**A. Init**:
  *   `font` = [
       [1,1,1,1,1,1,0], (0)
       [0,1,1,0,0,0,0], (1) ...
      ]
**B. Function `show(n)`**:
  *   Loop `i` 0 to 6:
      *   Set Pin `10+i` to `font[n][i]`.
**C. Loop**:
  *   Count 0 to 9:
      *   Call `show(count)`.
      *   Wait 1s.
  *   **Snap** into `pico_forever`.""",
        "flow": "Instead of `if n==0... if n==1...`, we use data to drive logic. This is cleaner and faster.",
        "code": """import machine, time
segs = [machine.Pin(i, machine.Pin.OUT) for i in range(10, 17)] # A-G

# 0: A,B,C,D,E,F (No G)
# 1: B,C
font = [
    [1,1,1,1,1,1,0], # 0
    [0,1,1,0,0,0,0], # 1
    [1,1,0,1,1,0,1], # 2
    [1,1,1,1,0,0,1], # 3
    [0,1,1,0,0,1,1], # 4
    [1,0,1,1,0,1,1], # 5
    [1,0,1,1,1,1,1], # 6
    [1,1,1,0,0,0,0], # 7
    [1,1,1,1,1,1,1], # 8
    [1,1,1,1,0,1,1]  # 9
]

def show(n):
    for i in range(7):
        segs[i].value(font[n][i])

while True:
    for i in range(10):
        show(i)
        time.sleep(1)""",
        "mistakes": ["**Common Anode/Cathode**: If Anode, 0=On. Logic must be inverted (`1 - font[n][i]`).", "**Resistors**: Need 7 resistors, one per segment. Not one shared on common pin (brightness varies)."],
        "next": ["**Countdown**: 9 down to 0.", "**Alphabet**: Display A, b, C, d..."]
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
    generate_batch_69_part2()
