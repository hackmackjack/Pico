
## Project 0179: Automated Stopwatch

### 1. Learning Objective
Orchestrate physical-event-triggering. Learn how to use two Light Sensors (LDRs) as "Gates" to start and stop a timer automatically, simulating a professional race track system.

### 2. Concepts Introduced
*   **Photoelectric Gates**: Using a light beam to detect when a physical object passes a point.
*   **Event-Driven Timing**: Starting an clock based on a sensor threshold rather than a button.
*   **Dual-Gate Logic**: managing a distinct "Start" event and "Finish" event.

### 3. Hardware Required
*   Raspberry Pi Pico
*   2 Light Sensors (LDRs)
*   2x 10k Ohm resistors (for voltage dividers)
*   2 Flashlights (to create the "beams")
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Start Gate (LDR1)** | GP26 (ADC0) | Placed at the race start |
| **Finish Gate (LDR2)** | GP27 (ADC1) | Placed at the race finish |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_analog_read`** (read ADC)
*   **from Logic, drag `controls_if`** (if/then)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **start_val**, **finish_val**: Raw brightness levels.
*   **race_time**: Calculated duration.
*   **race_active**: State flag.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Initial State**:
    *   **Set** `race_time` = 0.
    *   **Set** `race_active` = False.
    *   **Print** "RACE READY: Align flashlights with sensors".

**B. "Ready" Calibration Phase**
2.  **Wait for Start Beam Break**:
    *   From **Loops**, drag a repeat-until.
    *   **Condition**: If **Sensors** `pico_analog_read` GP26 < 300 (Darkness = Beam Broken).
    *   **Action**: **Set** `race_active` = True. **Print** "--- START BEAM BROKEN! GO! ---".

**C. Timing Phase**
3.  **Count while Racing**:
    *   From **Loops**, drag a second repeat-until.
    *   **Condition**: If **Sensors** `pico_analog_read` GP27 < 300 (Finish Beam Broken).
    *   **Contents**:
        *   **Set** `race_time` = `race_time` + 0.1.
        *   **Wait** 0.1 seconds.

**D. Result Phase**
4.  **Display Final Time**:
    *   **Print** "--- FINISH BEAM BROKEN! ---".
    *   **Print** "Total Race Time: ", `race_time`, " seconds".
    *   **Wait** 5 seconds before resetting.

### 8. Execution Flow
1.  **Beam Alignment**: Two flashlights shine on the sensors. The Pico sees a "High" value (Bright).
2.  **Trigger**: A toy car passes Gate 1, blocking the light. The Pico sees a "Low" value (Dark) and starts the clock.
3.  **Run**: The timer increments quickly in 0.1s steps while the car is between the gates.
4.  **Finish**: The car passes Gate 2, blocking the second beam. The Pico stops the clock immediately.
5.  **Result**: An extremely accurate measurement of speed and duration.

### 9. Generated Code
```python
import machine
import utime

# Sensors
start_gate = machine.ADC(26)
finish_gate = machine.ADC(27)

def get_brightness(adc):
    return adc.read_u16()

while True:
    print("READY... Align beams.")
    utime.sleep(1)
    
    # Wait for Start (Darkness detected)
    while get_brightness(start_gate) > 20000:
        utime.sleep(0.01)
        
    print(">>> START!")
    start_tick = utime.ticks_ms()
    
    # Wait for Finish (Darkness detected)
    while get_brightness(finish_gate) > 20000:
        utime.sleep(0.01)
        
    end_tick = utime.ticks_ms()
    print(">>> FINISH!")
    
    # Calc
    duration = utime.ticks_diff(end_tick, start_tick) / 1000
    print("FINAL TIME: " + str(duration) + "s")
    
    utime.sleep(5) # Pause before next race
```

### 10. Common Mistakes
*   **Threshold Selection**: Ambient light changes. If the room is too bright, your "300" or "20000" threshold might never trigger. Check your raw values in the console first.
*   **Beam Gap**: If the flashlights are too far away, they won't be bright enough to trigger a "High" state initially.

### 11. Try This Next
*   **Speed Trap**: If you know the distance between the sensors (e.g., 1 meter), calculate the Speed in km/h!
*   **Win Light**: Turn on a Green LED at the finish gate when the record is broken.

---

## Project 0180: Mastering Stopwatch

### 1. Learning Objective
Explore high-speed UI refreshes and string formatting. Learn how to display a multi-part time variable (Minutes:Seconds:Milliseconds) on an OLED screen without causing visual "flicker".

### 2. Concepts Introduced
*   **String Formatting**: combining separate numbers into a clean `XX:YY:ZZ` layout.
*   **High-Frequency Updates**: Refreshing the OLED screen 20-30 times per second for smooth ms tracking.
*   **Calculated Modulo**: Using `%` and `/` math to extract minutes and seconds from a single milliseconds counter.

### 3. Hardware Required
*   Raspberry Pi Pico
*   OLED Display (I2C)
*   1 Button (Pause/Resume)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SCL/SDA** | GP1/GP0 | Display output |
| **Pause Button** | GP14 | Freezes the display |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Math, drag `math_arithmetic`** (division / modulo)
*   **from Displays, drag `pico_oled_text`** (show time)
*   **from Displays, drag `pico_oled_show`** (sync)

### 6. Variables
*   **total_ms**: The master counter in milliseconds.
*   **m, s, ms**: Extracted time components.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize Hardware**: Start OLED.
2.  **Setup Variables**:
    *   **Set** `total_ms` = 0.

**B. Calculation Phase (Loop)**
3.  **Start Loop**: From **Loops**, drag `pico_forever`.
4.  **Increment Time**: **Set** `total_ms` = `total_ms` + 30. (Update roughly every 30ms).
5.  **Calculate Components**:
    *   **Set** `minutes` = (`total_ms` / 60000) round down.
    *   **Set** `rem_ms` = `total_ms` % 60000.
    *   **Set** `seconds` = (`rem_ms` / 1000) round down.
    *   **Set** `final_ms` = `rem_ms` % 1000.

**C. UI Rendering Phase**
6.  **Update Screen**:
    *   **Clear** OLED.
    *   From **Displays**, drag `pico_oled_text`.
    *   **String**: `minutes` + ":" + `seconds` + ":" + `final_ms`.
    *   **Position**: Center of screen [20, 30].
    *   Snap `pico_oled_show`.
7.  **Short Wait**: **Wait** 0.03 seconds.

### 8. Execution Flow
1.  **Run**: The Pico counts rapidly in 30ms chunks.
2.  **Logic**: The math blocks convert a huge number like "75000ms" into "1 minute, 15 seconds".
3.  **Display**: The OLED shows `01:15:000`.
4.  **Result**: A professional-looking stopwatch with smooth, fast-moving milliseconds.

### 9. Generated Code
```python
import machine
import ssd1306
import utime

# Setup
i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

total_ms = 0
start_tick = utime.ticks_ms()

while True:
    # Get current delta
    total_ms = utime.ticks_diff(utime.ticks_ms(), start_tick)
    
    # Math: min, sec, ms
    minutes = total_ms // 60000
    seconds = (total_ms % 60000) // 1000
    millis = total_ms % 1000
    
    # Format String
    # 02d = 2 digits with leading zero padding
    time_str = "{:02d}:{:02d}:{:03d}".format(minutes, seconds, millis)
    
    # Refresh
    oled.fill(0)
    oled.text("STOPWATCH", 28, 0)
    # Draw double size effect by repeating or using larger font
    oled.text(time_str, 20, 30)
    oled.show()
    
    # Minimal wait to prevent I2C bus flooding
    utime.sleep(0.03)
```

### 10. Common Mistakes
*   **Flicker**: If you don't use `oled.show()` correctly or have a very long loop, the display will blink and hurt the eyes. Keep the loop tight.
*   **Leading Zeros**: without `{02d}`, "5 seconds" would show as `1:5:0` instead of `01:05:000`.

### 11. Try This Next
*   **Lap List**: Save the lap times in a list and show the "Last Lap" on the bottom half of the screen.
*   **Pause Feature**: Add checking for a button press to `if not paused:` the incrementing logic.

---
