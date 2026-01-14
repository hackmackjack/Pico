
import os

def generate_batch_61():
    header = """
# 🏁 Batch 61: LED Patterns 4

---
"""
    projects = [
        {
            "id": "0601",
            "title": "Introduction to LED Patterns",
            "objective": "Create a function `blink_fast()` and `blink_slow()`. Call them in a loop: Fast, Fast, Slow.",
            "concepts": ["Code Modularity", "Functions", "Sequencing", "Loop Patterns"],
            "hardware": ["Pico", "LED"],
            "interface": "| **LED** | GP16 | Signal Output |",
            "blocks": [
                "*   **from Functions, drag `define_function`**",
                "*   **from Loops, drag `pico_forever`**",
                "*   **from Functions, drag `call_function`**",
                "*   **from Smart IO, drag `pico_gpio_write`**"
            ],
            "vars": ["None (Control Flow only)"],
            "guide": """**A. Initialization Phase**
1.  **Define Functions**:
  *   From **Functions**, drag `define function [blink_fast]`.
  *   Inside:
      *   From **Smart IO**, drag `digital write pin:[16] to 1`.
      *   From **Time**, drag `sleep [0.1]s`.
      *   From **Smart IO**, drag `digital write pin:[16] to 0`.
      *   From **Time**, drag `sleep [0.1]s`.
  *   **Snap** into workspace (detached).
2.  **Define Slow Function**:
  *   From **Functions**, drag `define function [blink_slow]`.
  *   Inside:
      *   From **Smart IO**, drag `digital write pin:[16] to 1`.
      *   From **Time**, drag `sleep [0.5]s`.
      *   From **Smart IO**, drag `digital write pin:[16] to 0`.
      *   From **Time**, drag `sleep [0.5]s`.
  *   **Snap** into workspace.

**B. Main Loop Phase**
1.  **Sequence**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Functions**, drag `call [blink_fast]`.
  *   From **Functions**, drag `call [blink_fast]`.
  *   From **Functions**, drag `call [blink_slow]`.
  *   **Snap** into loop.""",
            "flow": "The system defines reusable blocks of code for flashing the LED. The main loop directs the orchestra: Fast, Fast, Slow. This introduces the concept of subroutines.",
            "code": """import machine
import time

led = machine.Pin(16, machine.Pin.OUT)

def blink_fast():
    led.value(1)
    time.sleep(0.1)
    led.value(0)
    time.sleep(0.1)

def blink_slow():
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)

while True:
    blink_fast()
    blink_fast()
    blink_slow()""",
            "mistakes": ["**Indentation**: Ensure function content is indented.", "**Name Collision**: Function definitions must happen before they are called."],
            "next": ["**SOS**: modify to 3 fast, 3 slow, 3 fast.", "**Variable Speed**: Pass a delay argument to the function."]
        }
        # ... logic repeats for 0602...0610
        # For brevity in this tool call, I will generate 0601 full and placeholders for others, 
        # then expand them if space permits or in next steps?
        # No, I should generate them properly.
    ]
    
    # Adding 0602
    projects.append({
        "id": "0602",
        "title": "Blinking LED Patterns",
        "objective": "Simulate a heartbeat using two rapid flashes followed by a long pause.",
        "concepts": ["Rhythmic Timing", "Asymmetric Duty Cycles", "Biological Simulation", "Gap Timing"],
        "hardware": ["Pico", "Red LED"],
        "interface": "| **LED** | GP16 | Heartbeat Signal |",
        "blocks": ["*   **from Loops, drag `pico_forever`**", "*   **from Smart IO, drag `pico_gpio_write`**", "*   **from Time, drag `pico_wait`**"],
        "vars": ["None"],
        "guide": """**A. Initialization Phase**
1.  **Setup**:
  *   From **Smart IO**, drag `pico_gpio_setup` (GP16, Output).
  *   **Snap** into setup block.

**B. Main Loop Phase**
1.  **Lub-Dub**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Smart IO**, turn LED ON. Wait 0.1s.
  *   From **Smart IO**, turn LED OFF. Wait 0.1s.
  *   From **Smart IO**, turn LED ON. Wait 0.1s.
  *   From **Smart IO**, turn LED OFF. Wait 1.0s.
  *   **Snap** into loop.""",
        "flow": "The LED flashes ON-OFF-ON widely, then rests. This 1.3s cycle mimics a resting heart rate of ~46 BPM.",
        "code": """import machine
import time

led = machine.Pin(16, machine.Pin.OUT)

while True:
    led.on(); time.sleep(0.1)
    led.off(); time.sleep(0.1)
    led.on(); time.sleep(0.1)
    led.off(); time.sleep(1.0)""",
        "mistakes": ["**Timing**: Making the gap too short makes it look like a strobe.", "**Color**: Red LEDs invoke the biological metaphor better."],
        "next": ["**Tachycardia**: Reduce the rest to 0.5s.", "**Arrhythmia**: Add random jitter to the rest period."]
    })
    
    # Adding 0603
    projects.append({
        "id": "0603",
        "title": "Manual LED Patterns Control",
        "objective": "Swap the state of two LEDs with a button press (A=On/B=Off -> A=Off/B=On).",
        "concepts": ["State Inversion", "Toggle Logic", "Boolean Not", "Complementary Outputs"],
        "hardware": ["Pico", "Button", "2 LEDs"],
        "interface": "| **Button** | GP14 | Input |\n| **LED A** | GP15 | Output |\n| **LED B** | GP16 | Output |",
        "blocks": ["*   **from Logic, drag `if_do`**", "*   **from Variables, drag `set_variable`**", "*   **from Smart IO, drag `pico_gpio_write`**"],
        "vars": ["**state**: Boolean (True/False)"],
        "guide": """**A. Initialization Phase**
1.  **Vars**:
  *   From **Variables**, set `state` to True.
  *   **Snap** into setup.

**B. Main Loop Phase**
1.  **Check**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Smart IO**, read Button. If Pressed:
      *   From **Variables**, set `state` to `not state`.
      *   Wait 0.2s (Debounce).
  *   **Snap** into loop.
2.  **Output**:
  *   From **Smart IO**, write LED A to `state`.
  *   From **Smart IO**, write LED B to `not state`.
  *   **Snap** below check.""",
        "flow": "The `state` variable tracks the system. LED A follows `state`, LED B follows the opposite. Pressing the button flips the boolean, instantly swapping the lights.",
        "code": """import machine, time
ledA = machine.Pin(15, machine.Pin.OUT)
ledB = machine.Pin(16, machine.Pin.OUT)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
state = True

while True:
    if btn.value():
        state = not state
        time.sleep(0.2)
    ledA.value(state)
    ledB.value(not state)""",
        "mistakes": ["**No XOR**: Trying to use two variables instead of one generic state for complementary pairs.", "**Holding**: Button toggles repeatedly if not debounced/waited."],
        "next": ["**Tri-State**: Add a 3rd state where both are OFF.", "**Blink Mode**: Swap blinking patterns instead of static logic."]
    })

    # Adding 0604
    projects.append({
        "id": "0604",
        "title": "LED Patterns Sequences",
        "objective": "Create a 'Stacker' effect where LEDs light up accumulatively (1, 1+2, 1+2+3, All, Off).",
        "concepts": ["Accumulator Logic", "Incremental Display", "Bar Graph", "Loops"],
        "hardware": ["Pico", "4 LEDs"],
        "interface": "| **LEDs** | GP16-19 | Bargraph |",
        "blocks": ["*   **from Loops, drag `count_with`**", "*   **from Smart IO, drag `pico_gpio_write`**"],
        "vars": ["**i**: Loop Index"],
        "guide": """**A. Initialization Phase**
1.  **Setup**:
  *   Config GP16-19 as Output.

**B. Main Loop Phase**
1.  **Fill**:
  *   From **Loops**, loop `i` from 16 to 19.
      *   From **Smart IO**, turn Pin `i` ON.
      *   Wait 0.2s.
  *   **Snap** into `pico_forever`.
2.  **Clear**:
  *   From **Smart IO**, turn GP16-19 OFF.
  *   Wait 0.5s.
  *   **Snap** after loop.""",
        "flow": "The inner loop lights LEDs one by one without turning the previous ones off. Once the loop finishes (bar full), the external command wipes them all.",
        "code": """import machine, time
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(16, 20)]

while True:
    for led in leds:
        led.on()
        time.sleep(0.2)
    for led in leds: led.off()
    time.sleep(0.5)""",
        "mistakes": ["**Turning Off Inside**: If you turn the LED off inside the loop, it becomes a 'Running Light', not a 'Stacker'.", "**Index Range**: Python range(16,20) covers 16,17,18,19."],
        "next": ["**Unstack**: Create a loop that turns them off one by one (reverse order) instead of all at once.", "**Bounce**: Stack up then unstack down."]
    })

    # ... I will stop here for this file write and append the rest in part 2 to avoid tool limits.
    # Actually I can write a loop.
    
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
    generate_batch_61()
