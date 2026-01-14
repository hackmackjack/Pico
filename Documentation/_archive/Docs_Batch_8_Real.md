
# 🏁 Batch 8: Reaction Game 1

## 1️⃣ Project 0071: Introduction to Reaction Game
### 2️⃣ Learning Objective
The "Wait" Game. Turn on the Red LED ("Wait"). After 3 seconds, turn on the Green LED ("GO!"). The player must press the button only after Green appears.

### 3️⃣ Concepts Introduced
*   **Sequential Logic**: Wait -> Signal -> Listen.
*   **State Management**: Valid vs Invalid input times.

### 4️⃣ Hardware Required
*   **Pico**
*   **Red LED, Green LED**
*   **Button**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |
| **Red LED** | GP14 |
| **Green LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **Wait**
🔹 **Set Pin**

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   Red ON, Green OFF.
    *   Wait 3s.
    *   Red OFF, Green ON.
    *   Wait Until Button Pressed.
    *   Celebrate (Flash Green).

### 9️⃣ Execution Flow (Plain English)
The user stares at the Red light. It turns Green. They mash the button. The system confirms the press.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
red = machine.Pin(14, machine.Pin.OUT)
green = machine.Pin(15, machine.Pin.OUT)
while True:
    red.value(1); green.value(0)
    time.sleep(3)
    red.value(0); green.value(1)
    
    # Wait for input
    while not btn.value():
        time.sleep(0.01)
        
    # Celebrate
    for i in range(5):
        green.toggle()
        time.sleep(0.1)
```

### 🔟 Common Mistakes & Debug Tips
*   **Cheating**: This simple code doesn't check if you pressed *early*.

### 1️⃣2️⃣ Try This Next
*   **Random**: Make the wait time random (2-5s).

---

## 1️⃣ Project 0072: Blinking Reaction Game (Catch the Light)
### 2️⃣ Learning Objective
Timing accuracy. An LED blinks fast (0.1s ON, 0.5s OFF). Try to press the button exactly while the light is ON.

### 3️⃣ Concepts Introduced
*   **Time Window**: An opportunity that opens and closes.
*   **Coincidence Detection**: Input Time == Event Time.

### 4️⃣ Hardware Required
*   **Pico**
*   **LED**
*   **Button**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |
| **LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **If**

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   LED ON.
    *   Wait 0.1s (Game Window).
    *   IF Button Pressed: YOU WIN (Solid On).
    *   LED OFF.
    *   Wait 0.5s.

### 9️⃣ Execution Flow (Plain English)
The light flashes. You try to catch it. If you press while it's dark, nothing happens. If you catch it, it stays on to congratulate you.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)
while True:
    led.value(1)
    # Check during the ON window (crude)
    start = time.ticks_ms()
    caught = False
    while time.ticks_diff(time.ticks_ms(), start) < 100:
        if btn.value():
            caught = True
            break
            
    if caught:
        # Win State
        time.sleep(2)
    else:
        led.value(0)
        time.sleep(0.5)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Polling**: If you use `time.sleep(0.1)`, you can't check the button *during* the sleep. You need a loop or checking before/after.

### 1️⃣2️⃣ Try This Next
*   **Speed Up**: Make the window smaller (0.05s).

---

## 1️⃣ Project 0073: Manual Reaction Game Control (Button Masher)
### 2️⃣ Learning Objective
Count presses in a fixed time. Start timer on first press, see how many you can get in 10s.

### 3️⃣ Concepts Introduced
*   **Rate Measurement**: Events per Time.
*   **Timeout**: Ending a loop after duration.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |

### 6️⃣ Blocks Used
🔹 **Timer**

### 7️⃣ Variables & State
*   **count**
*   **start_time**

### 8️⃣ Block Logic
*   **Loop**:
    *   Wait for First Press.
    *   `start_time` = Now.
    *   `count` = 0.
    *   WHILE (Now - `start_time`) < 10s:
        *   IF Pressed: `count` += 1. Wait for Release.
    *   Print `count`.

### 9️⃣ Execution Flow (Plain English)
Ready? GO! Clickclickclickclick. Stop! Score: 42.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
while True:
    print("Press to Start...")
    while not btn.value(): pass
    
    print("GO!")
    start = time.ticks_ms()
    count = 0
    while time.ticks_diff(time.ticks_ms(), start) < 10000:
        if btn.value():
            count += 1
            while btn.value(): pass # Debounce/Release
            
    print("Score:", count)
    time.sleep(2)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Cheating**: Without the "Wait for Release" line, holding the button counts as millions of presses.

### 1️⃣2️⃣ Try This Next
*   **High Score**: Save the best score to a variable.

---

## 1️⃣ Project 0074: Reaction Game Sequences (Whack-a-Mole)
### 2️⃣ Learning Objective
Spatial mapping. 3 LEDs, 3 Buttons. Random LED lights up, press matching button.

### 3️⃣ Concepts Introduced
*   **Mapping**: Input A -> Output A.
*   **Indices**: Managing arrays of inputs/outputs.

### 4️⃣ Hardware Required
*   **Pico**
*   **3x LEDs** (Left, Mid, Right)
*   **3x Buttons**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Btn L** | GP10 |
| **Btn M** | GP11 |
| **Btn R** | GP12 |
| **LED L** | GP13 |
| **LED M** | GP14 |
| **LED R** | GP15 |

### 6️⃣ Blocks Used
🔹 **Random**
🔹 **List** (Advanced) or multiple IFs.

### 7️⃣ Variables & State
*   **target** (0, 1, or 2)

### 8️⃣ Block Logic
*   **Loop**:
    *   `target` = Random(0, 2).
    *   Turn ON LED[`target`].
    *   Wait for Input.
    *   IF Correct Button: Score++.
    *   Turn OFF.

### 9️⃣ Execution Flow (Plain English)
Left light! Hit Left button. Middle light! Hit Middle. Speed increases.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
import random

# Lists for easy handling
leds = [machine.Pin(13, machine.Pin.OUT), machine.Pin(14, machine.Pin.OUT), machine.Pin(15, machine.Pin.OUT)]
btns = [machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN), 
        machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN), 
        machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)]

score = 0
while True:
    target = random.randint(0, 2)
    leds[target].value(1)
    
    pressed = -1
    while pressed == -1:
        for i in range(3):
            if btns[i].value():
                pressed = i
                while btns[i].value(): pass # Release
                
    leds[target].value(0)
    
    if pressed == target:
        score += 1
        print("Score:", score)
    else:
        print("Miss! Game Over.")
        score = 0
        time.sleep(1)
    time.sleep(0.2)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Wiring Mess**: 6 wires plus grounds. Use a breadboard carefully.

### 1️⃣2️⃣ Try This Next
*   **Timeout**: Lose if you don't press within 1 second.

---

## 1️⃣ Project 0075: Interactive Reaction Game (Hot Potato)
### 2️⃣ Learning Objective
Tempo control. Buzzer ticks faster and faster. If it stops (Long Beep) while you hold the button, you lose.

### 3️⃣ Concepts Introduced
*   **Acceleration**: Decreasing delay over time.
*   **Game State**: Active vs Exploded.

### 4️⃣ Hardware Required
*   **Pico**
*   **Buzzer**
*   **Button** (The "Potato")

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |
| **Buzzer** | GP15 |

### 6️⃣ Blocks Used
🔹 **Variable**

### 7️⃣ Variables & State
*   **delay_time**

### 8️⃣ Block Logic
*   **Loop**:
    *   Tick (Beep).
    *   Wait `delay_time`.
    *   `delay_time` = `delay_time` * 0.9 (Get faster).
    *   IF `delay_time` < 0.05: BOOM.

### 9️⃣ Execution Flow (Plain English)
Tick... Tick... Tick..Tick.TickTickTickBOOM!

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
import random
buzz = machine.Pin(15, machine.Pin.OUT)
btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if btn.value(): # Start Game
        dt = 1.0
        while dt > 0.05:
            buzz.value(1); time.sleep(0.05); buzz.value(0)
            time.sleep(dt)
            dt = dt * 0.9
        
        # BOOM
        buzz.value(1); time.sleep(2); buzz.value(0)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Math**: Multiplying by 0.9 shrinks the number. 1.0 -> 0.9 -> 0.81 ...

### 1️⃣2️⃣ Try This Next
*   **Random Fuse**: Explode at a random time instead of just speed.

---

## 1️⃣ Project 0076: Smart Reaction Game (False Start)
### 2️⃣ Learning Objective
Negative constraints. If you press too early, you lose.

### 3️⃣ Concepts Introduced
*   **Prohibited Action**: Detecting input when none is allowed.
*   **Foul State**: Special error mode.

### 4️⃣ Hardware Required
*   **Pico**
*   **Red/Green LEDs**
*   **Button**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |
| **Red LED** | GP14 |
| **Green LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **Break Loop**

### 7️⃣ Variables & State
*   **foul**

### 8️⃣ Block Logic
*   **Loop**:
    *   Red ON.
    *   Wait Random(2, 5)s.
        *   (Check button constantly during wait - if pressed, FOUL).
    *   IF Not Foul: Green ON.
    *   Measure reaction.

### 9️⃣ Execution Flow (Plain English)
Wait... Wait... (Buffer checks button)... Green! If you pressed during Wait, Red flashes angrily.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
import random
btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
red = machine.Pin(14, machine.Pin.OUT)
green = machine.Pin(15, machine.Pin.OUT)

while True:
    red.value(1); green.value(0)
    wait_time = random.uniform(2, 5)
    start_wait = time.ticks_ms()
    foul = False
    
    # Wait Loop
    while time.ticks_diff(time.ticks_ms(), start_wait) < (wait_time * 1000):
        if btn.value():
            foul = True
            break
            
    if foul:
        for i in range(10): 
            red.toggle(); time.sleep(0.05)
    else:
        red.value(0); green.value(1)
        # Wait for press logic here
        while not btn.value(): pass
        time.sleep(1) # Win display
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Loop Blocking**: You can't use `time.sleep(5)` because you need to check the button *during* the wait.

### 1️⃣2️⃣ Try This Next
*   **Disqualification**: Lock the game for 5 seconds on a foul.

---

## 1️⃣ Project 0077: Reaction Game Alarm (Defuse)
### 2️⃣ Learning Objective
Logic under pressure. 3 wires (buttons). Only one is safe.

### 3️⃣ Concepts Introduced
*   **Boolean Logic**: (A OR B) = Boom. (C) = Safe.
*   **Countdown**: Visual or Auditory pressure.

### 4️⃣ Hardware Required
*   **Pico**
*   **3 Buttons**
*   **Buzzer**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Btn 1** | GP10 |
| **Btn 2** | GP11 |
| **Btn 3** | GP12 |
| **Buzzer** | GP15 |

### 6️⃣ Blocks Used
🔹 **If / Else If**

### 7️⃣ Variables & State
*   **safe_wire**

### 8️⃣ Block Logic
*   **Loop**:
    *   `safe_wire` = Random(1, 3).
    *   Loop until button pressed.
    *   IF Pressed == `safe_wire`: "Defused!".
    *   ELSE: "BOOM!".

### 9️⃣ Execution Flow (Plain English)
Which wire? Red? Blue? Green? *Click*... BOOM.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
import random
btns = [machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN),
        machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN),
        machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)]
buzz = machine.Pin(15, machine.Pin.OUT)

while True:
    safe = random.randint(0, 2)
    print("Code set. Cut a wire!")
    
    cut = -1
    while cut == -1:
        for i in range(3):
            if btns[i].value(): cut = i
            
    if cut == safe:
        print("Defused.")
        time.sleep(2)
    else:
        print("BOOM")
        buzz.value(1); time.sleep(1); buzz.value(0)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Floating Pins**: Ensure buttons verify 0 when not pressed (Pull Down).

### 1️⃣2️⃣ Try This Next
*   **Timer**: Add a 10s countdown that explodes if no wire is cut.

---

## 1️⃣ Project 0078: The Reaction Game Game (Simon)
### 2️⃣ Learning Objective
Memory. Flash sequence, record input, compare.

### 3️⃣ Concepts Introduced
*   **Arrays/Lists**: Storing a sequence.
*   **Appending**: Adding to the end of a list.

### 4️⃣ Hardware Required
*   **Pico**
*   **RGB LED (or 3 LEDs)**
*   **3 Buttons**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **LEDs** | GP13, 14, 15 |
| **Buttons** | GP10, 11, 12 |

### 6️⃣ Blocks Used
🔹 **List**

### 7️⃣ Variables & State
*   **sequence[]**

### 8️⃣ Block Logic
*   **Loop**:
    *   Add Random Color to `sequence`.
    *   Play `sequence` (Flash LEDs).
    *   Wait for User Input sequence.
    *   IF Wrong: Game Over.
    *   IF Correct: Output "Level Up".

### 9️⃣ Execution Flow (Plain English)
Red. (Red). Red-Green. (Red-Green). Red-Green-Blue. (Red-Green-Blue).

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
import random

leds = [machine.Pin(13, machine.Pin.OUT), machine.Pin(14, machine.Pin.OUT), machine.Pin(15, machine.Pin.OUT)]
btns = [machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN), 
        machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN), 
        machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)]

sequence = []

while True:
    # Add step
    sequence.append(random.randint(0, 2))
    
    # Play
    for s in sequence:
        leds[s].value(1); time.sleep(0.5); leds[s].value(0); time.sleep(0.2)
        
    # Read
    for s in sequence:
        pressed = -1
        while pressed == -1:
            for i in range(3):
                if btns[i].value():
                    pressed = i
                    while btns[i].value(): pass # Release
        
        if pressed != s:
            print("Fail!"); sequence = []; time.sleep(2); break
    
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Memory**: Pico has plenty of RAM for this.
*   **Boring?**: Add sound tones for each color.

### 1️⃣2️⃣ Try This Next
*   **Speed Up**: Make the playback faster each level.

---

## 1️⃣ Project 0079: Automated Reaction Game (Ninja)
### 2️⃣ Learning Objective
Physical speed. Wave hand past sensor when light flashes.

### 3️⃣ Concepts Introduced
*   **Motion Detection**: Using PIR or Ultrasonic.
*   **Reflex**: Human physical movement time.

### 4️⃣ Hardware Required
*   **Pico**
*   **Ultrasonic Sensor**
*   **LED**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Trig** | GP16 |
| **Echo** | GP17 |
| **LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **Distance**
🔹 **Timer**

### 7️⃣ Variables & State
*   **reaction_ms**

### 8️⃣ Block Logic
*   **Loop**:
    *   Wait Random Time.
    *   LED ON (Go!).
    *   Start Timer.
    *   Wait until Distance < 20cm.
    *   Stop Timer. Print Result.

### 9️⃣ Execution Flow (Plain English)
Stand back. Light turns on. SWIPE! "You took 240ms".

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
import random
trig = machine.Pin(16, machine.Pin.OUT)
echo = machine.Pin(17, machine.Pin.IN)
led = machine.Pin(15, machine.Pin.OUT)

def get_dist():
    trig.low(); time.sleep_us(2)
    trig.high(); time.sleep_us(10); trig.low()
    while echo.value() == 0: pass
    start = time.ticks_us()
    while echo.value() == 1: pass
    return (time.ticks_diff(time.ticks_us(), start)) * 0.0343 / 2

while True:
    led.value(0)
    time.sleep(random.uniform(2, 5))
    led.value(1)
    
    start = time.ticks_ms()
    while get_dist() > 20: pass
    end = time.ticks_ms()
    
    print("Time:", time.ticks_diff(end, start), "ms")
    led.value(0)
    time.sleep(2)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Sensor Lag**: Ultrasonic sensors take ~10-20ms to ping. It's not instant, but close enough for humans.

### 1️⃣2️⃣ Try This Next
*   **PIR**: Use a PIR sensor (slower, but covers wider area).

---

## 1️⃣ Project 0080: Mastering Reaction Game (Binary)
### 2️⃣ Learning Objective
Cognitive load. It's not just "press button", it's "process info then press".
Flashes count = Button presses required.

### 3️⃣ Concepts Introduced
*   **Input Validation**: Confirming X events happened.
*   **Cognitive Delay**: Thinking time vs acting time.

### 4️⃣ Hardware Required
*   **Pico**
*   **LED**
*   **Button**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |
| **LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **Repeat**

### 7️⃣ Variables & State
*   **flash_count**
*   **press_count**

### 8️⃣ Block Logic
*   **Loop**:
    *   `flash_count` = Random(1, 3).
    *   Flash LED `flash_count` times.
    *   Wait for user to press `flash_count` times.
    *   IF Correct: Win.

### 9️⃣ Execution Flow (Plain English)
Blink-Blink. (User thinks "Two"). Click-Click. Win.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
import random

btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)

while True:
    count = random.randint(1, 4)
    # Display
    for i in range(count):
        led.value(1); time.sleep(0.2); led.value(0); time.sleep(0.2)
        
    # Input
    presses = 0
    start = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start) < 3000: # 3s window
        if btn.value():
            presses += 1
            while btn.value(): pass
            
    if presses == count:
        print("Correct!")
    else:
        print("Wrong count.")
    time.sleep(2)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Counting**: Users often miss one blink if it's too fast. 0.2s is aggressive.

### 1️⃣2️⃣ Try This Next
*   **Math**: Flash 2 times, then pause, flash 3 times. User must press 5 times.

---
