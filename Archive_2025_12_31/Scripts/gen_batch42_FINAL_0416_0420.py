# Complete Batch 42: Projects 0416-0420 (Final 5)

target_file = r'd:\MFF\Pico\Documentation\Docs_0401_0500.md'

batch42_part2 = r'''
## 1️⃣ Project 0416: Smart Button Logic Switch

### 2️⃣ Learning Objective
Implement a three-button stopwatch controller with start, stop, and reset functionality. You will learn about state machine design and multi-button coordination.

### 3️⃣ Concepts Introduced
*   **Start/Stop/Reset**: Three-state control system.
*   **Stopwatch Controller**: Managing timer state with buttons.
*   **State Machine**: Running, stopped, and reset states.

### 4️⃣ Hardware Required
*   **Pico**
*   **3× Buttons** (Start, Stop, Reset)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Start Button** | GP12 | PULL_DOWN |
| **Stop Button** | GP13 | PULL_DOWN |
| **Reset Button** | GP14 | PULL_DOWN |

### 6️⃣ Blocks Used

🔹 **Digital Read (×3)**
*   **Category:** Pin Access

🔹 **Time Tracking**
*   **Category:** Timing

🔹 **State Variables**
*   **Category:** Variables

### 7️⃣ Variables & State
*   **isRunning**: Boolean, timer currently counting.
*   **elapsedTime**: Accumulated time in seconds.
*   **startTime**: Timestamp when timer started.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Inputs**, drag `Setup Button pin:[12,13,14] as PULL_DOWN`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [isRunning] to [False]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [elapsedTime] to [0]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Start Button**:
        *   From **Logic**, drag `if [digital read pin 12] AND not [isRunning] then`.
            *   **Snap** into loop.
            *   Inside:
                *   From **Variables**, drag `set [isRunning] to [True]`.
                    *   **Snap** inside.
                *   From **Timing**, drag `set [startTime] to [time()]`.
                    *   **Snap** below.
                *   From **Console**, drag `print [STARTED]`.
                    *   **Snap** below.
    *   **Stop Button**:
        *   From **Logic**, drag `if [digital read pin 13] AND [isRunning] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Variables**, drag `set [isRunning] to [False]`.
                *   From **Timing**, drag `change [elapsedTime] by [time() - startTime]`.
                *   From **Console**, drag `print [STOPPED at {elapsedTime}s]`.
    *   **Reset Button**:
        *   From **Logic**, drag `if [digital read pin 14] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Variables**, drag `set [isRunning] to [False]`.
                *   From **Variables**, drag `set [elapsedTime] to [0]`.
                *   From **Console**, drag `print [RESET]`.
    *   **Display Current Time**:
        *   From **Logic**, drag `if [isRunning] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Timing**, drag `set [currentTime] to [elapsedTime + (time() - startTime)]`.
                *   From **Console**, drag `print [Time: {currentTime:.2f}s]`.
        *   From **Logic**, drag `else`.
            *   Inside: `print [Time: {elapsedTime:.2f}s (STOPPED)]`.
    *   From **Timing**, drag `sleep [0.1] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

Press Start to begin counting. The timer accumulates seconds. Press Stop to freeze it at the current value. Press Start again to resume from where it stopped (lap timer behavior). Press Reset at any time to zero the timer. This mimics a physical stopwatch with three distinct buttons.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

start_btn = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
stop_btn = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
reset_btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

is_running = False
elapsed_time = 0
start_time = 0

while True:
    # Start
    if start_btn.value() and not is_running:
        is_running = True
        start_time = time.time()
        print("STARTED")
        time.sleep(0.3)
    
    # Stop
    if stop_btn.value() and is_running:
        is_running = False
        elapsed_time += time.time() - start_time
        print(f"STOPPED at {elapsed_time:.2f}s")
        time.sleep(0.3)
    
    # Reset
    if reset_btn.value():
        is_running = False
        elapsed_time = 0
        print("RESET")
        time.sleep(0.3)
    
    # Display
    if is_running:
        current_time = elapsed_time + (time.time() - start_time)
        print(f"Time: {current_time:.2f}s", end='\r')
    else:
        print(f"Time: {elapsed_time:.2f}s (STOPPED)", end='\r')
    
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Time Jumps on Resume**: Ensure you capture `startTime` fresh each time Start is pressed.
*   **Reset While Running**: Decide if reset should auto-stop or if it requires stop first.

### 1️⃣2️⃣ Try This Next

*   **Lap Times**: Add 4th button to record lap times without stopping main timer.
*   **Display Integration**: Show time on 7-segment display or OLED.

---

## 1️⃣ Project 0417: Button Logic Alarm System

### 2️⃣ Learning Objective
Implement a silent hold-up alarm triggered by sustained button press. You will learn about time-delay triggers and safety-critical input detection.

### 3️⃣ Concepts Introduced
*   **Hold-up Alarm**: Hidden button for emergency signaling.
*   **Time-Delay Trigger**: Action occurs only after prolonged press.
*   **Silent Alarm**: Visual alert without audio (stealth mode).

### 4️⃣ Hardware Required
*   **Pico**
*   **Button** (hidden under counter)
*   **LED** (silent alarm indicator)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Alarm Button** | GP14 | PULL_DOWN |
| **Alert LED** | GP16 | Flashes silently |

### 6️⃣ Blocks Used

🔹 **Digital Read**
*   **Category:** Pin Access

🔹 **Time Tracking**
*   **Category:** Timing

🔹 **LED Control**
*   **Category:** Pin Access

### 7️⃣ Variables & State
*   **buttonPressStart**: Timestamp when button first pressed.
*   **alarmTriggered**: Boolean flag for alarm state.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Inputs**, drag `Setup Button pin:[14] as PULL_DOWN`.
        *   **Snap** into setup block.
    *   From **Pin Access**, drag `Setup Pin:[16] as OUTPUT`.
        *   **Snap** below.
    *   From **Variables**, drag `set [buttonPressStart] to [0]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [alarmTriggered] to [False]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Button Press Detection**:
        *   From **Logic**, drag `if [digital read pin 14] then`.
            *   **Snap** into loop.
            *   Inside:
                *   From **Logic**, drag `if [buttonPressStart] = [0] then`.
                    *   **Snap** inside.
                    *   Inside: From **Timing**, drag `set [buttonPressStart] to [time()]`.
                *   From **Logic**, drag `if [time() - buttonPressStart] > [5] then`.
                    *   **Snap** below.
                    *   Inside:
                        *   From **Variables**, drag `set [alarmTriggered] to [True]`.
                        *   From **Console**, drag `print [SILENT ALARM ACTIVATED]`.
        *   From **Logic**, drag `else`.
            *   **Snap** below.
            *   Inside: From **Variables**, drag `set [buttonPressStart] to [0]`.
    *   **Silent Alarm Flash**:
        *   From **Logic**, drag `if [alarmTriggered] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Pin Access**, drag `digital write pin:[16] value:[HIGH]`.
                *   From **Timing**, drag `sleep [0.1] seconds`.
                *   From **Pin Access**, drag `digital write pin:[16] value:[LOW]`.
                *   From **Timing**, drag `sleep [0.1] seconds`.

### 9️⃣ Execution Flow (Plain English)

When the hidden button is pressed and held for 5 continuous seconds, a silent alarm activates. The LED begins flashing rapidly (0.1s on, 0.1s off) to alert security personnel without making sound. If the button is released before 5 seconds, the timer resets and no alarm triggers. This mimics a retail panic button scenario.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(16, machine.Pin.OUT)

button_press_start = 0
alarm_triggered = False

while True:
    if button.value():
        if button_press_start == 0:
            button_press_start = time.time()
        
        # Check if held for 5 seconds
        if time.time() - button_press_start > 5 and not alarm_triggered:
            alarm_triggered = True
            print("SILENT ALARM ACTIVATED!")
    else:
        button_press_start = 0
    
    # Flash LED if alarm triggered
    if alarm_triggered:
        led.on()
        time.sleep(0.1)
        led.off()
        time.sleep(0.1)
    else:
        time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Alarm Never Triggers**: Ensure button stays pressed continuously for full 5 seconds.
*   **No Reset**: Add a reset code (e.g., 3 rapid button taps) to deactivate alarm.

### 1️⃣2️⃣ Try This Next

*   **Network Alert**: Send MQTT or HTTP POST when alarm triggers (Wi-Fi integration).
*   **Dual Confirmation**: Require two different buttons held simultaneously.

---

## 1️⃣ Project 0418: The Button Logic Game

### 2️⃣ Learning Objective
Create a Simon Says memory game with expanding sequences. You will learn about dynamic list growth and pattern recall testing.

### 3️⃣ Concepts Introduced
*   **Simon Says**: Classic memory replication game.
*   **Memory Expansion Loop**: Pattern grows by one element each round.
*   **Pattern Recall**: User must reproduce exact sequence.

### 4️⃣ Hardware Required
*   **Pico**
*   **4× LEDs** (different colors)
*   **4× Buttons** (matching colors)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED A** | GP16 | Red |
| **LED B** | GP17 | Green |
| **LED C** | GP18 | Blue |
| **LED D** | GP19 | Yellow |
| **Button A** | GP12 | Red button |
| **Button B** | GP13 | Green button |
| **Button C** | GP14 | Blue button |
| **Button D** | GP15 | Yellow button |

### 6️⃣ Blocks Used

🔹 **Random Choice**
*   **Category:** Math

🔹 **List Append**
*   **Category:** Variables

🔹 **List Comparison**
*   **Category:** Logic

### 7️⃣ Variables & State
*   **sequence**: Growing list of LED indexes.
*   **userInput**: Player's button presses.
*   **round**: Current difficulty level.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Inputs**, drag `Setup Button pin:[12-15] as PULL_DOWN`.
        *   **Snap** into setup block.
    *   From **Pin Access**, drag `Setup Pin:[16-19] as OUTPUT`.
        *   **Snap** below.
    *   From **Variables**, drag `set [sequence] to [[]]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [round] to [1]`.
        *   **Snap** below.

*   **B. Main Loop Phase (Game Round)**
    *   **Add New Step**:
        *   From **Math**, drag `set [newLED] to [random(0,3)]`.
            *   **Snap** into loop.
        *   From **Variables**, drag `append [newLED] to [sequence]`.
            *   **Snap** below.
    *   **Play Sequence**:
        *   From **Console**, drag `print [Round {round}: Watch...]`.
        *   From **Loops**, drag `for [led] in [sequence]`.
            *   **Snap** below.
            *   Inside:
                *   From **Pin Access**, drag `digital write pin:[16 + led] value:[HIGH]`.
     *   From **Timing**, drag `sleep [0.5] seconds`.
                *   From **Pin Access**, drag `digital write pin:[16 + led] value:[LOW]`.
                *   From **Timing**, drag `sleep [0.3] seconds`.
    *   **Collect User Input**:
        *   From **Variables**, drag `set [userInput] to [[]]`.
        *   From **Loops**, drag `repeat [length of sequence] times`.
            *   Inside: Wait for any button, append to userInput.
    *   **Check Correctness**:
        *   From **Logic**, drag `if [userInput] = [sequence] then`.
            *   Inside: `print [CORRECT!]` and `change [round] by [1]`.
        *   From **Logic**, drag `else`.
            *   Inside: `print [GAME OVER at round {round}]` and break.

### 9️⃣ Execution Flow (Plain English)

Round 1: System flashes LED A. User presses button A → correct. Round 2: System flashes A, then B. User presses A, then B → correct. Round 3: A, B, C... The sequence grows by one random LED each round. If the user misses any step, game ends and final round is announced.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
import random

leds = [machine.Pin(16+i, machine.Pin.OUT) for i in range(4)]
buttons = [machine.Pin(12+i, machine.Pin.IN, machine.Pin.PULL_DOWN) for i in range(4)]

sequence = []
round_num = 1

while True:
    # Add new random LED
    sequence.append(random.randint(0, 3))
    
    # Play sequence
    print(f"Round {round_num}: Watch...")
    for led_idx in sequence:
        leds[led_idx].on()
        time.sleep(0.5)
        leds[led_idx].off()
        time.sleep(0.3)
    
    # Collect user input
    user_input = []
    print("Your turn!")
    for _ in range(len(sequence)):
        while not any(btn.value() for btn in buttons):
            time.sleep(0.05)
        for i, btn in enumerate(buttons):
            if btn.value():
                user_input.append(i)
                leds[i].on()
                time.sleep(0.2)
                leds[i].off()
                while btn.value():  # Wait for release
                    time.sleep(0.05)
                break
    
    # Check
    if user_input == sequence:
        print("CORRECT!")
        round_num += 1
        time.sleep(1)
    else:
        print(f"GAME OVER at round {round_num}")
        break
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Sequence Too Fast**: Increase LED-on time to 0.8s for easier gameplay.
*   **Button Bounce**: User input might register twice without proper debouncing.

### 1️⃣2️⃣ Try This Next

*   **High Score**: Save best round to file, display on startup.
*   **Speed Mode**: Decrease flash time as rounds increase.

---

## 1️⃣ Project 0419: Automated Button Logic

### 2️⃣ Learning Objective
Analyze button debounce by comparing raw edge counts to properly debounced clicks. You will learn about signal noise and debounce effectiveness.

### 3️⃣ Concepts Introduced
*   **Debounce Studio**: Visualizing button bounce.
*   **Signal Noise Analysis**: Counting spurious edges.
*   **Raw vs Filtered**: Comparing unfiltered and filtered signals.

### 4️⃣ Hardware Required
*   **Pico**
*   **Cheap Button** (intentionally bouncy)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP14 | PULL_DOWN |

### 6️⃣ Blocks Used

🔹 **Edge Detection**
*   **Category:** Logic

🔹 **Timestamp Logic**
*   **Category:** Timing

🔹 **Counter Variables**
*   **Category:** Variables

### 7️⃣ Variables & State
*   **rawEdgeCount**: Total rising edges (including bounce).
*   **debouncedClickCount**: Properly filtered clicks.
*   **lastEdgeTime**: Timestamp of last raw edge.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Inputs**, drag `Setup Button pin:[14] as PULL_DOWN`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [rawEdgeCount] to [0]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [debouncedClickCount] to [0]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [lastEdgeTime] to [0]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [lastButton] to [False]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Raw Edge Count**:
        *   From **Pin Access**, drag `set [currentButton] to [digital read pin 14]`.
            *   **Snap** into loop.
        *   From **Logic**, drag `if [currentButton] AND not [lastButton] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Variables**, drag `change [rawEdgeCount] by [1]`.
                *   From **Timing**, drag `set [lastEdgeTime] to [time()]`.
    *   **Debounced Click Count**:
        *   From **Logic**, drag `if [currentButton] AND not [lastButton] AND [time() - lastEdgeTime] > [0.05] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Variables**, drag `change [debouncedClickCount] by [1]`.
    *   **Display Difference**:
        *   From **Console**, drag `print [Raw Edges: {rawEdgeCount} | Debounced Clicks: {debouncedClickCount} | Noise: {rawEdgeCount - debouncedClickCount}]`.
            *   **Snap** below.
    *   From **Variables**, drag `set [lastButton] to [currentButton]`.
        *   **Snap** below.
    *   From **Timing**, drag `sleep [0.001] seconds`.
        *   **Snap** below (1ms polling for raw edges).

### 9️⃣ Execution Flow (Plain English)

Every button press creates multiple electrical edges (bounce). The raw counter counts ALL edges. The debounced counter only counts edges separated by >50ms. After 10 button presses, raw might show 47 edges while debounced shows 10. The difference (37) is the noise eliminated by debouncing.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

raw_edge_count = 0
debounced_click_count = 0
last_edge_time = 0
last_button = False

while True:
    current_button = button.value()
    current_time = time.time()
    
    # Raw edge detection
    if current_button and not last_button:
        raw_edge_count += 1
        
        # Debounced detection (50ms minimum between clicks)
        if current_time - last_edge_time > 0.05:
            debounced_click_count += 1
        
        last_edge_time = current_time
    
    last_button = current_button
    
    # Display
    noise = raw_edge_count - debounced_click_count
    print(f"Raw: {raw_edge_count} | Debounced: {debounced_click_count} | Noise: {noise}", end='\r')
    
    time.sleep(0.001)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **No Difference**: Quality buttons might not bounce. Use intentionally cheap/old switch.
*   **Missed Bounces**: Polling faster than 1ms might be needed for very fast bounce.

### 1️⃣2️⃣ Try This Next

*   **Oscilloscope View**: Plot button voltage over time to visualize bounce waveform.
*   **RC Filter**: Add hardware capacitor to compare hardware vs software debounce.

---

## 1️⃣ Project 0420: Mastering Button Logic

### 2️⃣ Learning Objective
Implement interrupt-driven button handling to catch presses during blocking code. You will learn about asynchronous event handling and IRQ configuration.

### 3️⃣ Concepts Introduced
*   **Interrupts (IRQ)**: Hardware-triggered code execution.
*   **Asynchronous Events**: Responding immediately regardless of main code.
*   **Sleep Interruption**: Catching button during `sleep(10)` call.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **LED**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP14 | PULL_DOWN with IRQ |
| **LED** | GP16 | Interrupt indicator |

### 6️⃣ Blocks Used

🔹 **Interrupt Setup**
*   **Category:** Advanced (Pin Access)

🔹 **Callback Function**
*   **Category:** Functions

🔹 **Digital Write**
*   **Category:** Pin Access

### 7️⃣ Variables & State
*   **buttonPressed**: Global flag set by interrupt.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Variables**, drag `set [buttonPressed] to [False]`.
        *   **Snap** into setup block (global variable).
    *   **Define Interrupt Handler**:
        *   From **Functions**, drag `def button_callback(pin):`.
            *   **Snap** below.
            *   Inside:
                *   From **Variables**, drag `set [global buttonPressed] to [True]`.
                *   From **Console**, drag `print [INTERRUPT! Button pressed]`.
    *   From **Inputs**, drag `Setup Button pin:[14] as PULL_DOWN`.
        *   **Snap** below.
    *   From **Advanced**, drag `pin[14].irq(trigger=Pin.IRQ_RISING, handler=button_callback)`.
        *   **Snap** below.
    *   From **Pin Access**, drag `Setup Pin:[16] as OUTPUT`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Blocking Code**:
        *   From **Console**, drag `print [Sleeping for 10 seconds (try pressing button)...]`.
            *   **Snap** into loop.
        *   From **Timing**, drag `sleep [10] seconds`.
            *   **Snap** below.
    *   **Check Interrupt Flag**:
        *   From **Logic**, drag `if [buttonPressed] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Pin Access**, drag `digital write pin:[16] value:[HIGH]`.
                *   From **Timing**, drag `sleep [1] seconds`.
                *   From **Pin Access**, drag `digital write pin:[16] value:[LOW]`.
                *   From **Variables**, drag `set [buttonPressed] to [False]`.
        *   From **Console**, drag `print [Main loop resumed]`.

### 9️⃣ Execution Flow (Plain English)

The main loop sleeps for 10 seconds (simulating slow blocking code). Normally, button presses during sleep would be missed. But with IRQ enabled, pressing the button immediately calls `button_callback()`, which sets a global flag. When sleep finishes, the main code checks the flag and flashes the LED, proving the press was caught despite the blocking sleep.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

button_pressed = False

def button_callback(pin):
    global button_pressed
    button_pressed = True
    print("INTERRUPT! Button pressed during sleep")

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_callback)
led = machine.Pin(16, machine.Pin.OUT)

while True:
    print("Sleeping for 10 seconds (try pressing button)...")
    time.sleep(10)
    
    if button_pressed:
        print("Button was pressed during sleep!")
        led.on()
        time.sleep(1)
        led.off()
        button_pressed = False
    
    print("Main loop resumed")
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Interrupt Doesn't Fire**: Ensure IRQ trigger is set to RISING, not FALLING or BOTH.
*   **Multiple Triggers**: Button bounce can fire IRQ multiple times. Add debounce in callback.

### 1️⃣2️⃣ Try This Next

*   **Wake from Deep Sleep**: Use IRQ to wake Pico from low-power sleep mode.
*   **Priority Queue**: Use IRQ to add events to a queue processed by main loop.

---

✅ **BATCH 42 COMPLETE: Projects 0411-0420 (Button Logic 3)**

---
'''

with open(target_file, 'a', encoding='utf-8') as f:
    f.write(batch42_part2)

print("✅ BATCH 42 COMPLETE: Projects 0411-0420 (Button Logic 3)")
print("📊 Progress: 20/100 projects documented")
print("📋 Next: Batch 43 (Sound & Music 3, Projects 0421-0430)...")
