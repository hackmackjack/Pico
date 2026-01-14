
import os

def generate_batch_62_part1():
    header = """
# 🏁 Batch 62: Button Logic 4

---
"""
    projects = []

    # 0611: Turbo Button
    projects.append({
        "id": "0611",
        "title": "Introduction to Button Logic",
        "objective": "Create a 'Turbo' button that reduces the sleep delay in a blinking loop, making the LED blink faster while held.",
        "concepts": ["Variable Delay", "Input-Modulated Timing", "Dynamic Control", "State Check"],
        "hardware": ["Pico", "Button", "LED"],
        "interface": "| **Button** | GP14 | Turbo Input |\n| **LED** | GP16 | Output |",
        "blocks": ["*   **from Variables, drag `set_variable`**", "*   **from Logic, drag `if_else`**", "*   **from Time, drag `pico_wait`**"],
        "vars": ["**delay**: Floar (seconds)"],
        "guide": """**A. Initialization Phase**
1.  **Vars**:
  *   From **Variables**, set `delay` to 0.5.
  *   **Snap** into setup.

**B. Main Loop Phase**
1.  **Check Input**:
  *   From **Loops**, drag `pico_forever`.
  *   If Button (GP14) pressed:
      *   Set `delay` to 0.1.
  *   Else:
      *   Set `delay` to 0.5.
  *   **Snap** into loop.
2.  **Blink**:
  *   Toggle LED (GP16).
  *   Wait `delay`s.
  *   **Snap** below check.""",
        "flow": "Standard Input -> Process -> Output loop. The Input (Button) changes a Variable (delay). The Process uses that variable to control the Output timing.",
        "code": """import machine, time
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(16, machine.Pin.OUT)
delay = 0.5

while True:
    if btn.value():
        delay = 0.1
    else:
        delay = 0.5
    
    led.toggle()
    time.sleep(delay)""",
        "mistakes": ["**Responsiveness**: If delay is 0.5, you have to wait up to 0.5s for the button to register. Reduce base delay or use polling.", "**Debounce**: Not critical here as we are just checking state."],
        "next": ["**Hyper Turbo**: Add a second button for 0.05s delay.", "**Smoothing**: Ramp the speed down instead of instant jump."]
    })

    # 0612: Dead Man's Switch
    projects.append({
        "id": "0612",
        "title": "Blinking Button Logic",
        "objective": "Implement a safety switch where the LED stays ON only while the button is actively held down. Releasing it turns it OFF immediately.",
        "concepts": ["Momentary Switch", "Active Engagement", "Fail-Safe", "Direct Mapping"],
        "hardware": ["Pico", "Button", "LED"],
        "interface": "| **Button** | GP14 | Safety Switch |\n| **LED** | GP16 | Active Indicator |",
        "blocks": ["*   **from Smart IO, drag `pico_gpio_read`**", "*   **from Smart IO, drag `pico_gpio_write`**"],
        "vars": ["**safe**: Boolean"],
        "guide": """**A. Init**: Setup IOs.
**B. Loop**:
1.  **Direct Map**:
  *   From **Loops**, drag `pico_forever`.
  *   Set `safe` to Read Button (GP14).
  *   Write LED (GP16) to `safe`.
  *   **Snap** into loop.""",
        "flow": "The simplest form of logic: Output = Input. If the human operator becomes incapacitated (releases button), the machine stops (LED Off).",
        "code": """import machine, time
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(16, machine.Pin.OUT)

while True:
    led.value(btn.value())
    time.sleep(0.01)""",
        "mistakes": ["**Latched Button**: Using a click-on/click-off button defeats the purpose of a dead man's switch.", "**Lag**: Adding large sleep delays makes the stop unsafe."],
        "next": ["**Time Delay**: Allow 1s of release before stopping (grace period).", "**Dual Hand**: Require two buttons held to run."]
    })

    # 0613: XOR Gate
    projects.append({
        "id": "0613",
        "title": "Manual Button Logic Control",
        "objective": "Implement an XOR (Exclusive OR) gate: LED is ON if Button A OR Button B is pressed, but NOT both.",
        "concepts": ["XOR Logic", "Boolean Algebra", "Truth Tables", "Complex Conditionals"],
        "hardware": ["Pico", "2 Buttons", "LED"],
        "interface": "| **Btn A** | GP14 | Input A |\n| **Btn B** | GP15 | Input B |\n| **LED** | GP16 | Output Q |",
        "blocks": ["*   **from Logic, drag `if_else`**", "*   **from Logic, drag `not_operator`**"],
        "vars": ["**a**: Boolean", "**b**: Boolean"],
        "guide": """**A. Init**: Setup IOs.
**B. Loop**:
1.  **Read**:
  *   From **Loops**, drag `pico_forever`.
  *   Read Btn A -> `a`. Read Btn B -> `b`.
2.  **Logic**:
  *   If (`a` AND NOT `b`) OR (`b` AND NOT `a`):
      *   Turn LED On.
  *   Else:
      *   Turn LED Off.
  *   **Snap** into loop.""",
        "flow": "XOR Truth Table:\n0,0 -> 0\n0,1 -> 1\n1,0 -> 1\n1,1 -> 0\nThis logic is common in stairwell light switches (2-way switching).",
        "code": """import machine, time
btnA = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnB = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(16, machine.Pin.OUT)

while True:
    a = btnA.value()
    b = btnB.value()
    if (a and not b) or (b and not a):
        led.on()
    else:
        led.off()
    time.sleep(0.05)""",
        "mistakes": ["**OR vs XOR**: Standard OR stays on if both are pressed.", "**Wiring**: Ensure both buttons have common ground/pull-down."],
        "next": ["**XNOR**: Inverted XOR (On if both same).", "**Half Adder**: Use XOR for Sum and AND for Carry."]
    })

    # 0614: Button Logic Sequences (Double Tap)
    projects.append({
        "id": "0614",
        "title": "Button Logic Sequences",
        "objective": "Detect a 'Double Tap' gesture (two presses within 0.5s) to toggle an LED. Single taps should be ignored.",
        "concepts": ["Gesture Recognition", "Timeout Logic", "State Machine", "Timing Windows"],
        "hardware": ["Pico", "Button", "LED"],
        "interface": "| **Button** | GP14 | Gesture Input |\n| **LED** | GP16 | Mode Indicator |",
        "blocks": ["*   **from Time, drag `time_ticks_ms`**", "*   **from Logic, drag `break_loop`**"],
        "vars": ["**taps**: Integer", "**start**: Timestamp"],
        "guide": """**A. Init**: `mode`=False.
**B. Loop**:
1.  **Wait 1st Tap**:
  *   Wait for Button Press.
  *   Wait for Button Release.
  *   Set `start` = `current_time`.
2.  **Window**:
  *   Loop while `current_time` - `start` < 500:
      *   If Button Press:
           *   Toggle `mode`.
           *   Write `mode` to LED.
           *   Wait until Release.
           *   Break loop.
  *   **Snap** into `pico_forever`.""",
        "flow": "We listen for the first rising edge. Once found, we open a 500ms window. If a second rising edge appears in that window, it's a Double Tap.",
        "code": """import machine, time
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(16, machine.Pin.OUT)
mode = False

while True:
    # Wait for 1st press
    while not btn.value(): time.sleep(0.01)
    while btn.value(): time.sleep(0.01) # Wait release
    
    start = time.ticks_ms()
    
    # Check window
    while time.ticks_diff(time.ticks_ms(), start) < 500:
        if btn.value():
            # 2nd press detected
            mode = not mode
            led.value(mode)
            while btn.value(): time.sleep(0.01) # Wait release
            break
        time.sleep(0.01)""",
        "mistakes": ["**Blocking**: Standard `sleep` blocks the window check. Use `ticks_diff`.", "**Triple Tap**: Currently registers as Double + Single."],
        "next": ["**Long Press toggle**: Short=On, Long=Off.", "**Triple Click**: Add counter for N clicks."]
    })

    # 0615: Interactive Vote
    projects.append({
        "id": "0615",
        "title": "Interactive Button Logic",
        "objective": "Create a voting system where 3 buttons increment counters for A, B, or C. After 10s, display the winner.",
        "concepts": ["Data Aggregation", "Comparison Sorting", "Tallying", "Time Limits"],
        "hardware": ["Pico", "3 Buttons"],
        "interface": "| **Btn A** | GP14 | Option A |\n| **Btn B** | GP15 | Option B |\n| **Btn C** | GP16 | Option C |",
        "blocks": ["*   **from Variables, drag `change_variable`**", "*   **from Logic, drag `if_compare`**"],
        "vars": ["**a**: Int", "**b**: Int", "**c**: Int"],
        "guide": """**A. Init**: Set a=0, b=0, c=0.
**B. Voting Phase**:
1.  **Start Timer**: `start` = `time`.
2.  **Poll**:
  *   Loop while `elapsed` < 10000:
      *   If Btn A Press -> Indent `a`. Wait Release.
      *   If Btn B Press -> Indent `b`. Wait Release.
      *   If Btn C Press -> Indent `c`. Wait Release.
  *   **Snap** below Setup.
3.  **Result**:
  *   Print `a`, `b`, `c`.
  *   If `a` > `b` and `a` > `c`: Print "A Wins".
  *   ... (rest of logic).
  *   **Snap** below loop.""",
        "flow": "A temporal gathering phase followed by a logic analysis phase. This mirrors real-world batch processing.",
        "code": """import machine, time
btns = [machine.Pin(i, machine.Pin.IN, machine.Pin.PULL_DOWN) for i in range(14, 17)]
counts = [0, 0, 0]
start = time.ticks_ms()

print("VOTE NOW! (10s)")
while time.ticks_diff(time.ticks_ms(), start) < 10000:
    for i in range(3):
        if btns[i].value():
            counts[i] += 1
            print(f"Vote cast for {chr(65+i)}")
            while btns[i].value(): time.sleep(0.01)

print(f"Results: A={counts[0]}, B={counts[1]}, C={counts[2]}")
winner_idx = counts.index(max(counts))
print(f"WINNER: {chr(65+winner_idx)}")""",
        "mistakes": ["**Tie**: Use `>=` comparisons or specifically check for ties.", "**Spamming**: Add a delay after vote to prevent one person voting 50 times."],
        "next": ["**LED Graph**: Show bar graph of votes on LEDs.", "**Secret Ballot**: Don't print votes until end."]
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
    generate_batch_62_part1()
