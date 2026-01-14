# 📘 Pico 2500: Batch 28 - Reaction Game 2 (Projects 0271-0280)

**Grade Level:** 3-5 (Elementary)  
**Bloom's Level:** Remember/Understand  
**Theme:** Advanced Game Logic & Interaction

---

## 1️⃣ Project 0271: Multi-Player Reaction

### 2️⃣ Learning Objective
Build a game where 2-4 players compete to press their button first when a light turns on. Introduces "First-to-Lock" logic.

### 3️⃣ Concepts Introduced
*   Multi-Input Polling
*   Race Conditions
*   Locking Variables
*   Fairness Algorithms

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   4 Pushbuttons (P1-P4)
*   4 LEDs (P1-P4 Indicators)
*   1 Master LED (Signal)

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **P1 Button** | GP10 |
| **P2 Button** | GP11 |
| **Signal LED** | GP15 |
| **P1 Win LED** | GP12 |
| **P2 Win LED** | GP13 |

### 6️⃣ Blocks Used
🔹 **Loop Until** - Wait for input
🔹 **Break** - Exit loop on winner

### 10️⃣ Generated Code
```python
from machine import Pin
import time
import random

p1_btn = Pin(10, Pin.IN, Pin.PULL_DOWN)
p2_btn = Pin(11, Pin.IN, Pin.PULL_DOWN)
signal = Pin(15, Pin.OUT)
p1_led = Pin(12, Pin.OUT)
p2_led = Pin(13, Pin.OUT)

while True:
    # Reset
    signal.value(0); p1_led.value(0); p2_led.value(0)
    time.sleep(random.uniform(2, 5))
    
    # GO!
    signal.value(1)
    
    winner = None
    while winner is None:
        if p1_btn.value(): winner = 1
        elif p2_btn.value(): winner = 2
    
    # Display Result
    if winner == 1: p1_led.value(1)
    else: p2_led.value(1)
    
    print(f"Player {winner} Wins!")
    time.sleep(3)
```

---

## 1️⃣ Project 0272: Sequence Memory (Simon)

### 2️⃣ Learning Objective
Recreate the classic "Simon Says" memory game. The system plays a pattern of lights; the user must repeat it.

### 3️⃣ Concepts Introduced
*   Arrays / Lists (Growth)
*   Sequence Generation
*   Input Validation
*   Game Loops

### 4️⃣ Hardware
*   4 LEDs (R, G, B, Y)
*   4 Buttons

### 8️⃣ Step-by-Step Guide
**Logic:**
1. `sequence = []`
2. Add random color to `sequence`.
3. Play sequence to user.
4. Wait for user input.
5. If user input == `sequence`:
   - Score + 1, Repeat step 2.
6. Else:
   - Game Over (Buzz).

### 10️⃣ Generated Code
```python
sequence = []
# ... Setup Pins ...

def play_sequence():
    for color in sequence:
        light_led(color)
        time.sleep(0.5)

def get_user_input():
    # Wait for button press matching sequence length
    pass 

while True:
    # Add new step
    sequence.append(random.randint(0, 3))
    play_sequence()
    if not get_user_input():
        print("Game Over")
        break
    time.sleep(1)
```

---

## 1️⃣ Project 0273: Reflex Training (Stats)

### 2️⃣ Learning Objective
Measure the exact reaction time in milliseconds and calculate the "Average" over 5 attempts.

### 3️⃣ Concepts Introduced
*   Time Delta (`ticks_ms`)
*   Averaging Math
*   Statistics
*   Filtering Outliers

### 10️⃣ Generated Code
```python
times = []

for i in range(5):
    time.sleep(random.uniform(1,3))
    led.on()
    start = time.ticks_ms()
    
    while not btn.value(): pass # Wait
    
    end = time.ticks_ms()
    diff = time.ticks_diff(end, start)
    times.append(diff)
    print(f"Reaction: {diff}ms")
    led.off()

avg = sum(times) / len(times)
print(f"Average: {avg}ms")
```

---

## 1️⃣ Project 0274: Audio Reaction Game

### 2️⃣ Learning Objective
React to a SOUND (Beep) instead of a Light. Biologically, auditory reaction time is often faster than visual!

### 3️⃣ Concepts Introduced
*   Auditory Stimulus
*   Sensory Processing
*   Tone Generation

### 10️⃣ Generated Code
```python
buzzer = PWM(Pin(15))

time.sleep(random.uniform(2,5))

# Sound Stimulus
buzzer.freq(1000)
buzzer.duty_u16(32768)
start = time.ticks_ms()

while not btn.value(): pass

buzzer.duty_u16(0)
print(f"Time: {time.ticks_diff(time.ticks_ms(), start)}ms")
```

---

## 1️⃣ Project 0275: Progressive Difficulty

### 2️⃣ Learning Objective
Make the game harder as the player succeeds. Reduce the "Window of Opportunity" to press the button.

### 3️⃣ Concepts Introduced
*   Difficulty Curves
*   Timeouts
*   Level Progression

### 10️⃣ Generated Code
```python
timeout = 1000 # Start with 1.0s window
level = 1

while True:
    print(f"Level {level}")
    
    # Wait... Go!
    led.on()
    start = time.ticks_ms()
    
    pressed = False
    while time.ticks_diff(time.ticks_ms(), start) < timeout:
        if btn.value():
            pressed = True
            break
            
    led.off()
    
    if pressed:
        print("Success!")
        timeout -= 100 # Make it harder (faster)
        level += 1
    else:
        print("Too Slow! Game Over")
        break
```

---

## 1️⃣ Project 0276: Reaction Time Display (TM1637)

### 2️⃣ Learning Objective
Display the reaction time instantly on a 4-digit 7-segment display for immediate feedback.

### 3️⃣ Concepts Introduced
*   External Displays
*   Number Formatting
*   I2C / Bit-Bang drivers

### 10️⃣ Generated Code
```python
import tm1637
display = tm1637.TM1637(clk=Pin(2), dio=Pin(3))

# ... calculate diff ...
diff = 245 # example
display.number(diff)
```

---

## 1️⃣ Project 0277: Tournament Mode (Best of 3)

### 2️⃣ Learning Objective
Track scores between two players over multiple rounds. First to 3 wins.

### 3️⃣ Concepts Introduced
*   Scorekeeping Variables
*   Winning Condition
*   Reset Logic

### 10️⃣ Generated Code
```python
p1_score = 0
p2_score = 0

while p1_score < 3 and p2_score < 3:
    winner = play_round() # Returns 1 or 2
    if winner == 1: p1_score += 1
    else: p2_score += 1
    print(f"Score: {p1_score} - {p2_score}")

print("Tournament Winner Decided!")
```

---

## 1️⃣ Project 0278: Calibration System (Fairness)

### 2️⃣ Learning Objective
Ensure buttons are working correctly. Measure "Latency" of the button press itself or prevent "False Starts" (Holding button before light).

### 3️⃣ Concepts Introduced
*   Cheat Detection
*   Input Validation
*   Anti-Cheat Logic

### 10️⃣ Generated Code
```python
time.sleep(2)

# Anti-Cheat: Check if button is ALREADY held
if btn.value() == 1:
    print("FOUL! You were holding the button!")
    buzzer.beep()
    # Restart round...
else:
    led.on() # Go!
```

---

## 1️⃣ Project 0279: Wireless Multiplayer

### 2️⃣ Learning Objective
Two players on TWO different Picos. Use UART or Radio logic to sync the "GO" signal.

### 3️⃣ Concepts Introduced
*   Synchronization
*   Latency Compensation
*   Networked Gaming

### 10️⃣ Generated Code
```python
uart.write('GO')
led.on()
start = time.ticks_ms()
```

---

## 1️⃣ Project 0280: Championship Reaction System

### 2️⃣ Learning Objective
Combine everything: Visual + Audio modes, Multiplayer, Scoring, Display, and Anti-Cheat.

### 3️⃣ Features
1. **Mode Select:** 1-Player (Time) or 2-Player (Race).
2. **Display:** Shows score or time.
3. **Sound:** Win/Loss effects.
4. **Fairness:** Foul detection.

### 10️⃣ Code Strategy
State machine handling `MENU`, `COUNTDOWN`, `GAME`, `RESULT`.

---

**Batch 28 Complete & Fixed.**
