# Continue Kitchen Timer 2: Projects 0385-0390

target_file = r'd:\MFF\Pico\Documentation\Docs_0301_0400.md'

kitchen_timer_continued = r'''
## 1️⃣ Project 0385: Interactive Kitchen Timer

### 2️⃣ Learning Objective
Implement gesture-based timer control using a tilt sensor for snooze functionality. You will learn about physical gesture interrupt handling.

### 3️⃣ Concepts Introduced
*   **Shake to Snooze**: Using physical gestures to control timer behavior.
*   **Gesture Interrupt**: Detecting tilt/shake events during alarm.
*   **Snooze Logic**: Adding extra time when alarm is triggered.

### 4️⃣ Hardware Required
*   **Pico**
*   **Tilt Sensor** (SW520D or similar)
*   **Buzzer**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Tilt Sensor** | GP16 | Digital Input |
| **Buzzer** | GP15 | PWM |

### 6️⃣ Blocks Used

🔹 **Digital Read**
*   **Category:** Pin Access

🔹 **Change Variable**
*   **Category:** Variables

🔹 **Buzzer Control**
*   **Category:** Actuators

### 7️⃣ Variables & State
*   **timeLeft**: Countdown timer value.
*   **alarmRinging**: Boolean flag for alarm state.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Inputs**, drag `Setup Pin:[16] as INPUT`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [timeLeft] to [10]`.
        *   **Snap** below (10 seconds for demo).
    *   From **Variables**, drag `set [alarmRinging] to [False]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Normal Countdown**:
        *   From **Logic**, drag `if not [alarmRinging] then`.
            *   **Snap** into loop.
            *   Inside:
                *   From **Variables**, drag `change [timeLeft] by [-1]`.
                    *   **Snap** inside.
                *   From **Logic**, drag `if [timeLeft] <= [0] then`.
                    *   **Snap** below.
                    *   Inside:
                        *   From **Variables**, drag `set [alarmRinging] to [True]`.
                        *   From **Actuators**, drag `Buzzer [15] tone [1000]`.
    *   **Snooze Detection**:
        *   From **Logic**, drag `if [alarmRinging] AND [digital read pin 16] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Console**, drag `print [Shake detected! Adding 5 minutes...]`.
                    *   **Snap** inside.
                *   From **Variables**, drag `change [timeLeft] by [300]`.
                    *   **Snap** below (add 5 minutes).
                *   From **Variables**, drag `set [alarmRinging] to [False]`.
                    *   **Snap** below.
                *   From **Actuators**, drag `Buzzer [15] stop`.
                    *   **Snap** below.
    *   From **Timing**, drag `sleep [1] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The timer counts down normally. When it hits 0, the buzzer sounds continuously. To stop the alarm and add 5 more minutes, the user shakes the Pico. The tilt sensor detects the movement, silences the buzzer, adds 300 seconds to the timer, and resumes the countdown. This mimics a physical alarm clock's snooze button.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

tilt = machine.Pin(16, machine.Pin.IN)
buzzer = machine.PWM(machine.Pin(15))

time_left = 10
alarm_ringing = False

while True:
    if not alarm_ringing:
        time_left -= 1
        print(f"Time left: {time_left}s")
        
        if time_left <= 0:
            alarm_ringing = True
            buzzer.freq(1000)
            buzzer.duty_u16(32768)
    
    # Snooze detection
    if alarm_ringing and tilt.value():
        print("Shake detected! Snoozing for 5 minutes...")
        time_left = 300
        alarm_ringing = False
        buzzer.duty_u16(0)
        time.sleep(1)  # Prevent multiple triggers
    
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Tilt Always Triggered**: Tilt sensors are sensitive. Add a small delay after detecting shake to prevent continuous triggering.
*   **Buzzer Stays On**: Ensure `buzzer.duty_u16(0)` is called to actually silence the buzzer.

### 1️⃣2️⃣ Try This Next

*   **Double Shake**: Require 2 shakes within 2 seconds to snooze (prevent accidental snooze).
*   **Accelerometer**: Replace tilt sensor with MPU6050 for precise shake detection.

---

## 1️⃣ Project 0386: Smart Kitchen Timer Switch

### 2️⃣ Learning Objective
Implement microwave-style door-pause logic where opening a switch pauses the timer. You will learn about safety interlock programming.

### 3️⃣ Concepts Introduced
*   **Door Open Pause**: Timer pauses when switch opens.
*   **Microwave Logic**: Requiring explicit resume action after door closes.
*   **Safety Interlock**: Preventing operation when door is open.

### 4️⃣ Hardware Required
*   **Pico**
*   **Switch** (simulating door sensor)
*   **Start Button**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Door Switch** | GP16 | PULL_UP (closed = LOW, open = HIGH) |
| **Start Button** | GP14 | PULL_DOWN |

### 6️⃣ Blocks Used

🔹 **Digital Read**
*   **Category:** Pin Access

🔹 **Logic States**
*   **Category:** Logic

🔹 **Variables**
*   **Category:** Variables

### 7️⃣ Variables & State
*   **timerRunning**: Boolean, currently counting down.
*   **timeLeft**: Remaining seconds.
*   **paused**: Boolean, true when door opened.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Inputs**, drag `Setup Pin:[16] as INPUT_PULLUP`.
        *   **Snap** into setup block.
    *   From **Inputs**, drag `Setup Button pin:[14] as PULL_DOWN`.
        *   **Snap** below.
    *   From **Variables**, drag `set [timeLeft] to [60]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [timerRunning] to [False]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [paused] to [False]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Door Check**:
        *   From **Logic**, drag `if [digital read pin 16] = HIGH then`.
            *   **Snap** into loop (door is open).
            *   Inside:
                *   From **Logic**, drag `if [timerRunning] then`.
                    *   **Snap** inside.
                    *   Inside:
                        *   From **Console**, drag `print [Door opened! Timer paused]`.
                        *   From **Variables**, drag `set [paused] to [True]`.
                        *   From **Variables**, drag `set [timerRunning] to [False]`.
    *   **Resume Logic**:
        *   From **Logic**, drag `if [paused] AND [digital read pin 16] = LOW AND [digital read pin 14] then`.
            *   **Snap** below (door closed AND start pressed).
            *   Inside:
                *   From **Console**, drag `print [Door closed. Resuming...]`.
                *   From **Variables**, drag `set [timerRunning] to [True]`.
                *   From **Variables**, drag `set [paused] to [False]`.
    *   **Countdown**:
        *   From **Logic**, drag `if [timerRunning] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Variables**, drag `change [timeLeft] by [-1]`.
                *   From **Console**, drag `print [Time: {timeLeft}s]`.
    *   From **Timing**, drag `sleep [1] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

When the timer is running and the door switch opens (e.g., user opens microwave door), the timer immediately pauses and stops counting down. Closing the door is NOT enough to resume—the user must also press the "Start" button. This safety feature prevents the microwave from running with the door open and requires explicit user confirmation to continue.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

door_switch = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
start_btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

time_left = 60
timer_running = False
paused = False

while True:
    # Door open check
    if door_switch.value():  # Door is open
        if timer_running:
            print("Door opened! Timer paused.")
            paused = True
            timer_running = False
    
    # Resume check (door closed AND start pressed)
    if paused and not door_switch.value() and start_btn.value():
        print("Door closed. Resuming timer...")
        timer_running = True
        paused = False
        time.sleep(0.5)  # Debounce
    
    # Countdown
    if timer_running:
        time_left -= 1
        print(f"Time: {time_left}s")
        
        if time_left <= 0:
            print("Timer complete!")
            timer_running = False
    
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Auto-Resume**: If timer resumes when door closes without button press, check the resume logic condition.
*   **Switch Polarity**: PULL_UP switches are LOW when closed, HIGH when open. Verify wiring matches code logic.

### 1️⃣2️⃣ Try This Next

*   **Warning Beep**: Sound a brief beep when door opens to alert user.
*   **Multiple Pauses**: Track how many times the timer was paused and log it.

---

## 1️⃣ Project 0387: Kitchen Timer Alarm System

### 2️⃣ Learning Objective
Implement input validation to detect stuck buttons and prevent infinite increments. You will learn about timeout-based error detection.

### 3️⃣ Concepts Introduced
*   **Stuck Button Detection**: Recognizing when a button is held too long.
*   **Input Validation**: Rejecting unrealistic user inputs.
*   **Error Handling**: Sounding alerts for problematic conditions.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button** (Add Minute)
*   **Buzzer** (Error Alert)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Add Minute Button** | GP14 | PULL_DOWN |
| **Buzzer** | GP15 | PWM |

### 6️⃣ Blocks Used

🔹 **Time Tracking**
*   **Category:** Timing

🔹 **Digital Read**
*   **Category:** Pin Access

🔹 **Buzzer Control**
*   **Category:** Actuators

### 7️⃣ Variables & State
*   **buttonPressStart**: Timestamp when button was first pressed.
*   **totalMinutes**: Accumulated time.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Inputs**, drag `Setup Button pin:[14] as PULL_DOWN`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [totalMinutes] to [0]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [buttonPressStart] to [0]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Button Press Detection**:
        *   From **Logic**, drag `if [digital read pin 14] then`.
            *   **Snap** into loop.
            *   Inside:
                *   From **Logic**, drag `if [buttonPressStart] = [0] then`.
                    *   **Snap** inside.
                    *   Inside:
                        *   From **Timing**, drag `set [buttonPressStart] to [time()]`.
                            *   **Snap** inside.
                *   From **Logic**, drag `if [time() - buttonPressStart] > [10] then`.
                    *   **Snap** below.
                    *   Inside:
                        *   From **Console**, drag `print [ERROR: Button stuck! Ignoring input]`.
                            *   **Snap** inside.
                        *   From **Actuators**, drag `Buzzer [15] tone [500] for [1000]ms`.
                            *   **Snap** below (error tone).
                        *   From **Variables**, drag `set [buttonPressStart] to [0]`.
                            *   **Snap** below.
        *   From **Logic**, drag `else`.
            *   **Snap** below.
            *   Inside:
                *   From **Logic**, drag `if [buttonPressStart] > [0] then`.
                    *   **Snap** inside.
                    *   Inside:
                        *   From **Variables**, drag `change [totalMinutes] by [1]`.
                            *   **Snap** inside.
                        *   From **Console**, drag `print [Added 1 minute. Total: {totalMinutes}]`.
                            *   **Snap** below.
                        *   From **Variables**, drag `set [buttonPressStart] to [0]`.
                            *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

When the user presses the "Add Minute" button, the program records the timestamp. If the button is released within 10 seconds, 1 minute is added to the timer. If the button is held for more than 10 seconds (e.g., book resting on keyboard), the program sounds an error beep and ignores the input, preventing the timer from being set to an unrealistic value like 500 minutes.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.PWM(machine.Pin(15))

total_minutes = 0
button_press_start = 0

while True:
    if button.value():
        if button_press_start == 0:
            button_press_start = time.time()
        
        # Check if held too long
        if time.time() - button_press_start > 10:
            print("ERROR: Button stuck! Ignoring input.")
            buzzer.freq(500)
            buzzer.duty_u16(32768)
            time.sleep(1)
            buzzer.duty_u16(0)
            button_press_start = 0
    else:
        # Button released
        if button_press_start > 0 and time.time() - button_press_start <= 10:
            total_minutes += 1
            print(f"Added 1 minute. Total: {total_minutes} minutes")
        button_press_start = 0
    
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Always Errors**: If every press triggers an error, the 10-second threshold might be too short. Increase to 15 seconds.
*   **Never Registers**: If button presses don't add minutes, check the release detection logic.

### 1️⃣2️⃣ Try This Next

*   **Long Press Feature**: Instead of error, holding for 3 seconds adds 5 minutes at once (intentional long press).
*   **Visual Feedback**: Flash an LED when stuck button is detected.

---

(Continuing with 0388-0390 in next script due to size...)
'''

with open(target_file, 'a', encoding='utf-8') as f:
    f.write(kitchen_timer_continued)

print("✅ Generated Projects 0385-0387 (Kitchen Timer 2)")
print("📋 Final 3 Kitchen Timer projects coming (0388-0390)...")
