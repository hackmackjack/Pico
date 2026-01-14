
import os

def generate_batch_62_part2():
    projects = []
    
    # 0616: Shift Key
    projects.append({
        "id": "0616",
        "title": "Smart Button Logic Switch",
        "objective": "Implement a 'Shift' modifier: Pressing Button B alone prints 'b', but holding Button A while pressing B prints 'B'.",
        "concepts": ["Chording", "Modifier Keys", "Logic AND", "Keyboard Matrix Logic"],
        "hardware": ["Pico", "Button A (Shift)", "Button B (Char)"],
        "interface": "| **Btn A** | GP14 | Shift |\n| **Btn B** | GP15 | Letter 'b' |",
        "blocks": ["*   **from Logic, drag `if_else`**", "*   **from Smart IO, drag `pico_gpio_read`**", "*   **from Text, drag `print`**"],
        "vars": ["None"],
        "guide": """**A. Loop**:
  *   From **Loops**, drag `pico_forever`.
  *   If Button B Pressed:
      *   If Button A Pressed (Shift Held):
          *   Print "B".
      *   Else:
          *   Print "b".
      *   Wait Until B Release.
  *   **Snap** into loop.""",
        "flow": "Standard keyboard logic. The state of one input changes the interpretation of another input.",
        "code": """import machine, time
shift = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
char_b = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if char_b.value():
        if shift.value():
            print("B", end="")
        else:
            print("b", end="")
        
        while char_b.value(): time.sleep(0.01) # Debounce
    time.sleep(0.01)""",
        "mistakes": ["**Reverse Logic**: Checking B first ensures we only trigger on action press, not modifier press.", "**Debounce**: Missing the 'Wait Until Release' causes bbbbbbbbb."],
        "next": ["**Caps Lock**: Toggle Shift state with a 3rd button.", "**Ctrl+C**: Detect specific combination to break loop."]
    })

    # 0617: Sequence Lock
    projects.append({
        "id": "0617",
        "title": "Button Logic Alarm System",
        "objective": "Create a digital combination lock. To unlock (Green LED), the user must press A, B, A, C in order. Any error resets the sequence (Red LED).",
        "concepts": ["State Machine", "Sequence Detection", "Tuple Matching", "Security Logic"],
        "hardware": ["Pico", "3 Buttons", "R/G LEDs"],
        "interface": "| **Btns** | GP13-15 | Inputs |\n| **Red** | GP16 | Error |\n| **Green** | GP17 | Unlock |",
        "blocks": ["*   **from Loops, drag `repeat_until`**", "*   **from Logic, drag `break_loop`**"],
        "vars": ["**state**: Integer (Current step)"],
        "guide": """**A. Init**: `state`=0.
**B. Loop**:
1.  **Wait Input**:
  *   Wait for ANY button.
2.  **Check Step**:
  *   If `state`==0 AND Btn A: `state`=1.
  *   Else If `state`==1 AND Btn B: `state`=2.
  *   Else If `state`==2 AND Btn A: `state`=3.
  *   Else If `state`==3 AND Btn C:
       *   Unlock (Green). `state`=0.
  *   Else:
       *   Error (Red). `state`=0.
  *   Wait Release.
  *   **Snap** into `pico_forever`.""",
        "flow": "A finite state machine (FSM). We only advance to the next state if the exact correct input occurs. Otherwise, we reset to state 0.",
        "code": """import machine, time
btns = [machine.Pin(i, machine.Pin.IN, machine.Pin.PULL_DOWN) for i in range(13, 16)] # A,B,C
red = machine.Pin(16, machine.Pin.OUT)
green = machine.Pin(17, machine.Pin.OUT)
step = 0

print("LOCKED")
while True:
    # Wait for press
    pressed = -1
    while pressed == -1:
        for i in range(3):
            if btns[i].value(): pressed = i; break
        time.sleep(0.01)
        
    # Logic
    if step == 0 and pressed == 0: step = 1
    elif step == 1 and pressed == 1: step = 2
    elif step == 2 and pressed == 0: step = 3
    elif step == 3 and pressed == 2:
        print("UNLOCK!"); green.on(); red.off(); step = 0; time.sleep(2); green.off()
    else:
        print("RESET"); red.on(); green.off(); step = 0; time.sleep(0.5); red.off()

    while btns[pressed].value(): time.sleep(0.01)""",
        "mistakes": ["**Hard Reset**: Most users forget to reset `step=0` on failure, allowing A-B-(Wrong)-A-C to work.", "**Timeout**: Add a 5s timeout to reset code."],
        "next": ["**Konami Code**: U-U-D-D-L-R-L-R-B-A.", "**Dynamic Code**: Allow user to set new code."]
    })

    # 0618: Mash Game
    projects.append({
        "id": "0618",
        "title": "The Button Logic Game",
        "objective": "Measure 'Clicks Per Second' (CPS). Count how many times the user presses the button in 10 seconds and display the score.",
        "concepts": ["Accumulator", "Time Limits", "Frequency Measurement", "Gaming Metrics"],
        "hardware": ["Pico", "Button"],
        "interface": "| **Button** | GP14 | Mash Input |",
        "blocks": ["*   **from Time, drag `time_ticks_ms`**", "*   **from Variables, drag `change_variable`**"],
        "vars": ["**score**: Integer"],
        "guide": """**A. Init**: `score`=0.
**B. Game**:
1.  **Countdown**: Print "3, 2, 1, GO".
2.  **Measure**:
  *   `start` = `time`.
  *   While `time` - `start` < 10000:
       *   Wait Press -> `score` += 1.
       *   Wait Release.
  *   **Snap** below Init.
3.  **Result**:
  *   Print "Score: " + `score`.
  *   **Snap** below loop.""",
        "flow": "A pure stress test of the switch mechanism and human reflex. The 'Wait Release' is crucial to prevent holding the button down.",
        "code": """import machine, time
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
score = 0

print("GO!")
start = time.ticks_ms()
while time.ticks_diff(time.ticks_ms(), start) < 10000:
    if btn.value():
        score += 1
        while btn.value(): pass # Block until release
        
print(f"TIME UP! Score: {score}")
print(f"CPS: {score/10}")""",
        "mistakes": ["**Cheating**: Using a vibrating massager or electric toothbrush to press.", "**Debounce**: If switch bounces, score will be artificially high."],
        "next": ["**Graph**: Plot CPS over time (fatigue curve).", "**Display**: Show live score on OLED."]
    })

    # 0619: Automated Logic (Long vs Short)
    projects.append({
        "id": "0619",
        "title": "Automated Button Logic",
        "objective": "Distinguish between a 'Tap' (<0.5s) and a 'Hold' (>0.5s) to trigger different actions using a single button.",
        "concepts": ["Duration Measurement", "UX Design", "Input Overloading", "Timer Checks"],
        "hardware": ["Pico", "Button", "2 LEDs"],
        "interface": "| **Button** | GP14 | Input |\n| **LED 1** | GP16 | Tap |\n| **LED 2** | GP17 | Hold |",
        "blocks": ["*   **from Time, drag `time_ticks_ms`**", "*   **from Logic, drag `if_compare`**"],
        "vars": ["**pressTime**: Integer"],
        "guide": """**A. Loop**:
  *   Wait for Press.
  *   `start` = `time`.
  *   Wait for Release.
  *   `duration` = `time` - `start`.
  *   If `duration` > 500:
       *   "HOLD DETECTED". Blink LED 2.
  *   Else:
       *   "TAP DETECTED". Blink LED 1.
  *   **Snap** into `pico_forever`.""",
        "flow": "We measure the width of the pulse (high state). The width determines the command.",
        "code": """import machine, time
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led1 = machine.Pin(16, machine.Pin.OUT)
led2 = machine.Pin(17, machine.Pin.OUT)

while True:
    if btn.value():
        start = time.ticks_ms()
        while btn.value(): time.sleep(0.01)
        duration = time.ticks_diff(time.ticks_ms(), start)
        
        if duration > 500:
            print("HOLD")
            led2.on(); time.sleep(0.1); led2.off()
        else:
            print("TAP")
            led1.on(); time.sleep(0.1); led1.off()""",
        "mistakes": ["**Feedback**: The user doesn't know *when* they have held long enough. Better to light LED 2 *while* holding after 500ms.", "**Rebound**: Very short clicks (<50ms) might be noise."],
        "next": ["**Visual Feedback**: Turn on LED 2 immediately when 500ms passes (before release).", "**Morse**: Decode Long-Short-Long."]
    })

    # 0620: Mastering Logic (Edge Detection)
    projects.append({
        "id": "0620",
        "title": "Mastering Button Logic",
        "objective": "Implement robust RISING EDGE detection manually. Count events only on the transition from LOW to HIGH, separate from the level.",
        "concepts": ["Edge Detection", "State History", "Rising/Falling Front", "Signal Processing"],
        "hardware": ["Pico", "Button"],
        "interface": "| **Button** | GP14 | Signal |",
        "blocks": ["*   **from Logic, drag `if_compare`**", "*   **from Variables, drag `set_variable`**"],
        "vars": ["**current**: Bool", "**last**: Bool", "**count**: Int"],
        "guide": """**A. Init**: `count`=0, `last`=False.
**B. Loop**:
1.  **Sample**:
  *   `current` = Read Button.
2.  **Compare**:
  *   If `current` == True AND `last` == False:
       *   `count` += 1.
       *   Print "RISING EDGE".
3.  **Update**:
  *   `last` = `current`.
  *   Wait 0.01s.
  *   **Snap** into `pico_forever`.""",
        "flow": "The core logic of all digital counters. We look for the specific moment where 0 becomes 1.",
        "code": """import machine, time
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
last = False
count = 0

while True:
    current = btn.value()
    if current and not last:
        count += 1
        print(f"EDGE {count}")
    last = current
    time.sleep(0.01)""",
        "mistakes": ["**Reverse**: `if not current and last` is a FALLING edge (Release).", "**Equality**: `if current == last` means no change."],
        "next": ["**Debounce**: Add time check to Edge Detection.", "**Encoder**: Use two offset signals for Quadrature Encoders."]
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
    generate_batch_62_part2()
