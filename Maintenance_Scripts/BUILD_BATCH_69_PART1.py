
import os

def generate_batch_69_part1():
    header = """
# 🏁 Batch 69: Counting Machine 4

---
"""
    projects = []

    # 0681: Clicker
    projects.append({
        "id": "0681",
        "title": "Introduction to Counting Machine",
        "objective": "Simple Tally Counter: Every time the button is pressed, increment a variable `count` and print it.",
        "concepts": ["Variables (Integer)", "Increment Operation", "State Persistence", "User Input"],
        "hardware": ["Pico", "Button"],
        "interface": "| **Button** | GP14 | Increment |",
        "blocks": ["*   **from Variables, drag `change_variable`**", "*   **from Text, drag `print`**"],
        "vars": ["**count**: Int"],
        "guide": """**A. Init**: `count` = 0.
**B. Loop**:
1.  **Wait**: Press.
2.  **Count**:
  *   Change `count` by 1.
  *   Print `count`.
  *   Wait until Release.
  *   **Snap** into `pico_forever`.""",
        "flow": "The variable holds the state in memory. Without it, the computer forgets what happened a moment ago.",
        "code": """import machine, time
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
count = 0

print("Ready")
while True:
    if btn.value():
        count += 1
        print(count)
        while btn.value(): time.sleep(0.01)
    time.sleep(0.01)""",
        "mistakes": ["**Global Scope**: In Python, modifying a global variable inside a function requires `global count`. (Not issue in main loop).", "**Double Count**: Forgotten debounce/release wait."],
        "next": ["**Reset**: Button B resets count to 0.", "**Limit**: Roll over to 0 after 100."]
    })

    # 0682: Visual Count
    projects.append({
        "id": "0682",
        "title": "Blinking Counting Machine",
        "objective": "Visualizer: Create a variable `count` (e.g., 3). Blink the LED that many times to represent the number.",
        "concepts": ["Data Visualization", "Controlled Loops", "Numerical Representation", "Iterative Output"],
        "hardware": ["Pico", "LED"],
        "interface": "| **LED** | GP16 | Output |",
        "blocks": ["*   **from Loops, drag `repeat`**", "*   **from Smart IO, drag `pico_gpio_toggle`**"],
        "vars": ["**count**: Int"],
        "guide": """**A. Init**: `count` = 5 (or random).
**B. Loop**:
1.  **Display**:
  *   Print `count`.
  *   Loop `count` times:
      *   Toggle LED (On). Wait 0.2s.
      *   Toggle LED (Off). Wait 0.2s.
  *   Wait 2s.
  *   **Snap** into `pico_forever`.""",
        "flow": "This is how simple machines (like error codes on washing machines) communicate numbers without a screen.",
        "code": """import machine, time, random
led = machine.Pin(16, machine.Pin.OUT)

while True:
    count = random.randint(1, 5)
    print(f"Count: {count}")
    
    for _ in range(count):
        led.on(); time.sleep(0.2)
        led.off(); time.sleep(0.2)
        
    time.sleep(2)""",
        "mistakes": ["**Off-by-One**: Looping `range(count)` is correct (0 to count-1), which is `count` iterations.", "**Speed**: Blinking too fast makes it hard to count."],
        "next": ["**Binary**: Display number in binary (1=001, 2=010, etc) using 3 LEDs.", "**Morse**: Blink the digit in Morse."]
    })

    # 0683: Manual (Up/Down)
    projects.append({
        "id": "0683",
        "title": "Manual Counting Machine Control",
        "objective": "Bi-Directional Counter: Button A increments reading. Button B decrements reading. Print value.",
        "concepts": ["Increment/Decrement", "Dual Input Logic", "Bounds Checking", "UI Navigation"],
        "hardware": ["Pico", "2 Buttons"],
        "interface": "| **Btn A** | GP14 | Up |\n| **Btn B** | GP15 | Down |",
        "blocks": ["*   **from Variables, drag `change_variable`**", "*   **from Logic, drag `if_else`**"],
        "vars": ["**val**: Int"],
        "guide": """**A. Init**: `val` = 0.
**B. Loop**:
1.  **Poll A**:
  *   If Btn A: `val` += 1. Wait Release.
2.  **Poll B**:
  *   If Btn B: `val` -= 1. Wait Release.
3.  **Update**:
  *   Print `val`.
  *   **Snap** into `pico_forever`.""",
        "flow": "The standard interface for most digital settings (Volume, Brightness, Thermostat).",
        "code": """import machine, time
up = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
down = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
val = 0

print(val)
while True:
    change = False
    if up.value():
        val += 1; change = True
        while up.value(): time.sleep(0.01)
    
    if down.value():
        val -= 1; change = True
        while down.value(): time.sleep(0.01)
        
    if change: print(val)
    time.sleep(0.01)""",
        "mistakes": ["**Negative Numbers**: If you only want positive counts, check `if val < 0`.", "**Overflow**: Integers on Pico are large, but on 8-bit systems, they roll over at 255."],
        "next": ["**Clamp**: Limit between 0 and 10.", "**Auto-Repeat**: Hold button to scroll fast."]
    })

    # 0684: Sequences (FizzBuzz)
    projects.append({
        "id": "0684",
        "title": "Counting Machine Sequences",
        "objective": "FizzBuzz: Count from 1 to 20. If number is div by 3, print 'Fizz'. If div by 5, 'Buzz'. If both, 'FizzBuzz'.",
        "concepts": ["Modulo Arithmetic", "Conditional Chains", "Algorithms", "Interview Questions"],
        "hardware": ["Pico"],
        "interface": "| **Console** | USB | Output |",
        "blocks": ["*   **from Math, drag `modulo_operator`**", "*   **from Loops, drag `for_in_range`**"],
        "vars": ["**i**: Int"],
        "guide": """**A. Loop**:
1.  **Iterate**:
  *   Loop `i` 1 to 21:
      *   `msg` = "".
      *   If `i` % 3 == 0: `msg` += "Fizz".
      *   If `i` % 5 == 0: `msg` += "Buzz".
      *   If `msg` == "": `msg` = `i`.
      *   Print `msg`.
      *   Wait 0.5s.
  *   **Snap** into `pico_forever`.""",
        "flow": "The classic programming interview test. Verifies understanding of division remainders.",
        "code": """import time
while True:
    for i in range(1, 21):
        output = ""
        if i % 3 == 0: output += "Fizz"
        if i % 5 == 0: output += "Buzz"
        if output == "": output = str(i)
        print(output)
        time.sleep(0.5)
    time.sleep(5)""",
        "mistakes": ["**Order Logic**: Checking 3 then 5 allows 'FizzBuzz' to form naturally interaction. Using `elif` for 5 would break it.", "**Modulo**: `i % 3` returns remainder."],
        "next": ["**Prime**: Print only Prime numbers.", "**Fibonacci**: Print 1, 1, 2, 3, 5, 8..."]
    })

    # 0685: Interactive (Target)
    projects.append({
        "id": "0685",
        "title": "Interactive Counting Machine",
        "objective": "Target Game: The screen says 'Click 7 times'. User clicks. System checks if input == 7.",
        "concepts": ["User Verification", "Comparisons", "Game Loops", "Input Counting"],
        "hardware": ["Pico", "Button", "LED"],
        "interface": "| **Button** | GP14 | Click |\n| **LED** | GP16 | Win/Loss |",
        "blocks": ["*   **from Logic, drag `if_compare`**", "*   **from Loops, drag `repeat_until`**"],
        "vars": ["**target**: Int", "**clicks**: Int"],
        "guide": """**A. Loop**:
1.  **Setup**:
  *   `target` = Random(3, 10).
  *   Print "Click " + `target` + " times!".
  *   `clicks` = 0.
2.  **Input**:
  *   Wait 5s (Accumulate clicks).
  *   Loop while polling:
       *   If Btn Press: `clicks`+=1.
3.  **Check**:
  *   If `clicks` == `target`: Win (LED On).
  *   Else: Fail (Flash).
  *   **Snap** into `pico_forever`.""",
        "flow": "Requires the user to count mentally and sync with the machine.",
        "code": """import machine, time, random
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(16, machine.Pin.OUT)

while True:
    target = random.randint(3, 10)
    print(f"CLICK {target} TIMES IN 5 SECONDS!")
    
    clicks = 0
    start = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start) < 5000:
        if btn.value():
            clicks += 1
            print(clicks)
            while btn.value(): time.sleep(0.01)
        time.sleep(0.01)
        
    print(f"You clicked: {clicks}")
    if clicks == target:
        print("WIN")
        led.on(); time.sleep(2); led.off()
    else:
        print("FAIL")
        for _ in range(5): led.toggle(); time.sleep(0.1)
    time.sleep(1)""",
        "mistakes": ["**Panic**: User clicks too fast and switch bounce misses/doubles counts.", "**Timer**: User might be mid-click when time runs out."],
        "next": ["**Blind**: Don't print the count as they click.", "**Rhythm**: Clicks must be evenly spaced."]
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
    generate_batch_69_part1()
