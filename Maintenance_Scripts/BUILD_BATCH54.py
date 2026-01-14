import os

def build_batch54():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    p0531 = """
---

# Batch 54: Temperature Alarm 3

## 1. Project 0531: Introduction to Temperature Alarm

### 2. Learning Objective
Read the internal temperature of the Pico and perform unit conversion from Celsius to Fahrenheit using standard mathematical operators.

### 3. Concepts Introduced
*   Analog Input (Internal Sensor)
*   Unit Conversion Math
*   Float Arithmetic
*   Terminal Output Formatting

### 4. Hardware Required
*   Raspberry Pi Pico (On-board internal sensor)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Internal Sensor** | ADC 4 | Built into the RP2040 chip |

### 6. Blocks Used
*   **from Sensors, drag `pico_internal_temp`** (Read Celsius)
*   **from Math, drag `arithmetic`** (C * 9/5 + 32)
*   **from Text, drag `print`** (Show result)

### 7. Variables
*   **temp_c**: Float (Temperature in Celsius)
*   **temp_f**: Float (Temperature in Fahrenheit)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Start Program**: No special hardware setup needed for internal sensor.

**B. Main Loop Phase**
2.  **Read Temperature**:
    *   From **Sensors**, set `temp_c` to `pico_internal_temp`.
3.  **Calculate Fahrenheit**:
    *   From **Variables**, set `temp_f` to:
        *   (`temp_c` * 1.8) + 32.
4.  **Print Results**:
    *   From **Text**, drag `print`.
    *   Show "Celsius: [temp_c], Fahrenheit: [temp_f]".
5.  **Wait**:
    *   From **Time**, wait 1 second.

### 9. Execution Flow
1.  **Start**: Pico begins monitoring its internal temperature sensor.
2.  **Process**: The code captures the current Celsius value.
3.  **Math**: It applies the conversion formula ($F = C \times \frac{9}{5} + 32$).
4.  **Output**: The converted values are sent to the terminal for the user to see.
5.  **Repeat**: The process repeats every second to track changes.

### 10. Generated Code
```python
import machine
import time

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    # The internal sensor has its own conversion logic
    temp_c = 27 - (reading - 0.706)/0.001721
    
    # Calculate Fahrenheit
    temp_f = (temp_c * 9/5) + 32
    
    print(f"Celsius: {temp_c:.2f}C, Fahrenheit: {temp_f:.2f}F")
    time.sleep(1)
```

### 11. Common Mistakes
*   **Floating Point Pruning**: Forgetting that `9/5` in some languages can result in `1` (integer) instead of `1.8`. In Python 3, this is handled automatically, but be mindful in block logic.
*   **Decimal Precision**: Printing 10 decimal places makes the data hard to read. Use rounding or formatted strings.

### 12. Try This Next
*   **Kelvin**: Add a second conversion for Kelvin ($C + 273.15$).
"""

    p0532 = """
---

## 1. Project 0532: Blinking Temperature Alarm

### 2. Learning Objective
Create a low-temperature "Freeze Warning" system that triggers a fast-blinking Blue LED when the temperature drops to or below $0^{\circ}C$.

### 3. Concepts Introduced
*   Critical Threshold Detect
*   Conditional Alerts
*   Thermal Monitoring
*   Frequency Scaling for Warnings

### 4. Hardware Required
*   Raspberry Pi Pico
*   External Temp Sensor (DS18B20 or similar) or Internal
*   Blue LED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Blue LED** | GP16 | Connected via 220Ω resistor |

### 6. Blocks Used
*   **from Logic, drag `less_than_equal`** (Compare to 0)
*   **from Smart IO, drag `pico_gpio_write`** (Flash LED)
*   **from Sensors, drag `pico_internal_temp`**

### 7. Variables
*   **temp**: Float (Current Celsius reading)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Output**: Set GP16 (Blue LED) as Output.

**B. Main Loop Phase**
2.  **Check Environment**:
    *   Set `temp` to current internal temperature.
3.  **Determine Logic**:
    *   From **Logic**, drag `if_else`.
    *   Condition: `temp` <= 0.
4.  **Activate "Ice Mode" (If True)**:
    *   From **Smart IO**, set GP16 HIGH.
    *   Wait 0.1s.
    *   From **Smart IO**, set GP16 LOW.
    *   Wait 0.1s.
5.  **Steady Mode (Else)**:
    *   From **Smart IO**, set GP16 LOW (All safe).

### 9. Execution Flow
1.  **Monitor**: The system constantly reads the temperature.
2.  **Judge**: It checks if the current reading is $0^{\circ}C$ or lower.
3.  **Action**: If the freeze condition is met, the LED flashes rapidly to get attention.
4.  **Idle**: If the temperature is safe, the LED stays dark.

### 10. Generated Code
```python
import machine
import time

led = machine.Pin(16, machine.Pin.OUT)
sensor_temp = machine.ADC(4)
v_to_c = 3.3/65535

while True:
    reading = sensor_temp.read_u16() * v_to_c
    c = 27 - (reading - 0.706)/0.001721
    
    if c <= 0:
        # Rapid flash warning
        led.on(); time.sleep(0.1)
        led.off(); time.sleep(0.1)
    else:
        led.off()
        time.sleep(1)
```

### 11. Common Mistakes
*   **Internal Temp Heat**: The internal sensor measures the CHIP temperature, not the air. It might show $30^{\circ}C$ even in a room that feels like $22^{\circ}C$. For freezer testing, use an external probe.
*   **Block Overlap**: Not using `else` might leave the LED stuck ON when the temp rises back above zero.

### 12. Try This Next
*   **Heat Alarm**: Add a Red LED that flashes if temp goes above $40^{\circ}C$.
"""

    p0533 = """
---

## 1. Project 0533: Manual Temperature Alarm Control

### 2. Learning Objective
Build a "Test Harness" that allows manual override of temperature readings via a button to verify if alarm systems are functioning correctly.

### 3. Concepts Introduced
*   Simulation Logic
*   Artificial State Injection
*   System Validation
*   Conditional Incrementation

### 4. Hardware Required
*   Raspberry Pi Pico
*   1x Push Button
*   Buzzer (Alarm)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Test Button** | GP14 | Manual Heat Injector |
| **Buzzer** | GP15 | Alarm Output |

### 6. Blocks Used
*   **from Logic, drag `if_do`** (Check button)
*   **from Variables, drag `change_variable`** (+1 to temp)
*   **from Time, drag `pico_wait`** (Sampling/Wait rate)

### 7. Variables
*   **sim_temp**: Integer (The "fake" temperature value)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure IO**: GP14 (Input), GP15 (Output).
2.  **Init Sim**: Set `sim_temp` to 25.

**B. Main Loop Phase**
3.  **Check "Heat" Button**:
    *   If GP14 is HIGH:
        *   Increment `sim_temp` by 1.
        *   Wait 0.5s.
4.  **Simulate Cooling**:
    *   Wait 2s.
    *   Decrement `sim_temp` by 1 (Minimum 25).
5.  **Evaluate Alarm**:
    *   If `sim_temp` > 35:
        *   Beep Buzzer.
6.  **Report**:
    *   Print current "Simulated Temp": `sim_temp`.

### 9. Execution Flow
1.  **Start**: The system assumes a baseline room temperature of $25^{\circ}C$.
2.  **Input**: Pressing the button simulates "heating" the sensor artificially.
3.  **Logic**: The code reacts to the fake value exactly as it would to a real sensor.
4.  **Output**: If the user "overheats" the system with enough presses, the alarm triggers.
5.  **Cooling**: When the button is released, the simulation slowly "cools" back to room temperature.

### 10. Generated Code
```python
from machine import Pin
import time

btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(15, Pin.OUT)

sim_temp = 25

while True:
    if btn.value():
        sim_temp += 1
        print(f"Applying Heat... ({sim_temp})")
        time.sleep(0.5)
    
    if sim_temp > 35:
        buzzer.on(); time.sleep(0.1); buzzer.off()
        
    # Natural cooling
    if sim_temp > 25:
        sim_temp -= 0.1 # Slow cool
        
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Infinite Temp**: Not adding a "cooling" logic means the alarm will stay on forever after the first test.
*   **Print Flood**: Printing every 0.1s will clog the terminal; only print when values change.

### 12. Try This Next
*   **Cooling Button**: Add a second button that simulated ICE (subtracts temperature).
"""

    p0534 = """
---

## 1. Project 0534: Temperature Alarm Sequences

### 2. Learning Objective
Implement a persistence-tracking algorithm to record and display the minimum and maximum temperatures detected since the device was powered on.

### 3. Concepts Introduced
*   Extrema Tracking (Min/Max)
*   Value Comparison
*   Data Persistence (Runtime)
*   Multi-variable Reporting

### 4. Hardware Required
*   Raspberry Pi Pico

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Internal Sensor** | ADC 4 | Standard Pico temp |

### 6. Blocks Used
*   **from Logic, drag `greater_than`** (Check Max)
*   **from Logic, drag `less_than`** (Check Min)
*   **from Variables, drag `set_variable`**

### 7. Variables
*   **current**: Float (Latest reading)
*   **min_temp**: Float (Lowest recorded)
*   **max_temp**: Float (Highest recorded)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Initial Records**:
    *   Read current temp into `current`.
    *   Set both `min_temp` and `max_temp` to `current`. (If you set them to 0, min will stay at 0 forever).

**B. Main Loop Phase**
2.  **Read Temp**:
    *   Set `current` to new sensor value.
3.  **Track Extremes**:
    *   **Max Check**: If `current` > `max_temp`: Update `max_temp` to `current`.
    *   **Min Check**: If `current` < `min_temp`: Update `min_temp` to `current`.
4.  **Display Status**:
    *   Print "Current: [current], Min: [min_temp], Max: [max_temp]".
5.  **Wait**: 2 seconds.

### 9. Execution Flow
1.  **Initialize**: The system takes its first reading to establish a baseline.
2.  **Scan**: Every 2 seconds, a new temperature is measured.
3.  **Compare**: The CPU checks if the new number "beats" the existing records.
4.  **Update**: If a new extreme is found, the old record is discarded.
5.  **Show**: The terminal displays the full history of the session's temperature range.

### 10. Generated Code
```python
import machine
import time

sensor = machine.ADC(4)

def get_temp():
    v = sensor.read_u16() * (3.3 / 65535)
    return 27 - (v - 0.706)/0.001721

# Initial state
current = get_temp()
mx = current
mn = current

while True:
    current = get_temp()
    
    if current > mx: mx = current
    if current < mn: mn = current
    
    print(f"Now: {current:.1f} | Min: {mn:.1f} | Max: {mx:.1f}")
    time.sleep(2)
```

### 11. Common Mistakes
*   **Starting at Zero**: Initializing `min_temp` to 0. Unless your room is $0^{\circ}C$, the current temperature (e.g., $25^{\circ}C$) will never be "less than 0", so the Min value will never update.
*   **Too much precision**: Use rounding (`round(temp, 1)`) to avoid numbers like 24.1287346 in your terminal.

### 12. Try This Next
*   **Manual Reset**: Add a button that resets both Min and Max to the current value.
"""

    p0535 = """
---

## 1. Project 0535: Interactive Temperature Alarm

### 2. Learning Objective
Create a "Comfort Zone" monitor using a dual-LED system to indicate if the current environment is within a specific safe range ($20^{\circ}C$ to $25^{\circ}C$).

### 3. Concepts Introduced
*   Window Comparators (Range logic)
*   Logical AND (Condition pooling)
*   Bio-Feedback Systems
*   Visual Indicator States

### 4. Hardware Required
*   Raspberry Pi Pico
*   Red LED (Alert)
*   Green LED (Comfort)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red LED** | GP16 | Out of range |
| **Green LED** | GP17 | Inside range |

### 6. Blocks Used
*   **from Logic, drag `and_operation`** (Check both bounds)
*   **from Logic, drag `greater_than`** and **`less_than`**
*   **from Smart IO, drag `pico_gpio_write`**

### 7. Variables
*   **t**: Float (Current Temperature)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **GPIO Init**: Set GP16/17 to Outputs.

**B. Main Loop Phase**
2.  **Sense**: Read temp into `t`.
3.  **The Comparison Window**:
    *   From **Logic**, drag `if_else`.
    *   Condition: (`t` >= 20) **AND** (`t` <= 25).
4.  **Safe State (If True)**:
    *   Set Green HIGH, Red LOW.
5.  **Danger State (Else)**:
    *   Set Green LOW, Red HIGH.
6.  **Wait**: 1s.

### 9. Execution Flow
1.  **Read**: Temperature is measured.
2.  **Logic**: The system checks two boundaries simultaneously.
    *   Too cold? (<20) $\Rightarrow$ Condition FAILS.
    *   Too hot? (>25) $\Rightarrow$ Condition FAILS.
    *   Just right? (20-25) $\Rightarrow$ Condition PASSES.
3.  **Display**: Only one LED can be on at a time, providing a clear Green (Good) or Red (Warning) signal.

### 10. Generated Code
```python
import machine
import time

red = machine.Pin(16, machine.Pin.OUT)
green = machine.Pin(17, machine.Pin.OUT)
sensor = machine.ADC(4)

while True:
    v = sensor.read_u16() * (3.3/65535)
    t = 27 - (v - 0.706)/0.001721
    
    if 20 <= t <= 25:
        # Comfort Zone
        green.on()
        red.off()
    else:
        # Outside comfort
        green.off()
        red.on()
        
    print(f"Status: {'COMFORT' if 20 <= t <= 25 else 'OUTSIDE'} ({t:.1f}C)")
    time.sleep(1)
```

### 11. Common Mistakes
*   **Exclusive OR**: Forgetting to turn off the "Safe" LED when entering the "Danger" state results in both LEDs being lit.
*   **Hard Boundaries**: If your room is exactly $25.0^{\circ}C$, the LEDs might flicker if the sensor noise jumps between 24.9 and 25.1. (Solution: Hysteresis).

### 12. Try This Next
*   **Buzzer Warning**: Beep the buzzer briefly only if entering the Red state from the Green state.
"""

    p0536 = """
---

## 1. Project 0536: Smart Temperature Alarm Switch

### 2. Learning Objective
Implement "Hysteresis" logic to prevent rapid, unnecessary rapid-fire switching of a fan or heater near the target temperature threshold.

### 3. Concepts Introduced
*   Hysteresis (Lag logic)
*   Chatter Prevention
*   Schmitt Trigger Concept
*   Upper/Lower Trigger Points

### 4. Hardware Required
*   Raspberry Pi Pico
*   Relay or Fan (Simulated with LED)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Cooling Fan** | GP16 | Simulated using LED |

### 6. Blocks Used
*   **from Logic, drag `greater_than`** (Upper threshold)
*   **from Logic, drag `less_than`** (Lower threshold)
*   **from Variables, drag `set_variable`** (State tracking)

### 7. Variables
*   **temp**: Float (Current reading)
*   **fan_on**: Boolean (Current fan state)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **GPIO Setup**: Set GP16 to Output.
2.  **State Init**: `fan_on = FALSE`.

**B. Main Loop Phase**
3.  **Sample Environment**: Read temp into `temp`.
4.  **Check High Limit (Trigger ON)**:
    *   If `temp` > 30:
        *   Set GP16 to **HIGH**.
        *   `fan_on = TRUE`.
5.  **Check Low Limit (Trigger OFF)**:
    *   If `temp` < 28:
        *   Set GP16 to **LOW**.
        *   `fan_on = FALSE`.
6.  **The Gap**: If the temperature is 29, the code does nothing—it keeps whatever state the fan was already in.

### 9. Execution Flow
1.  **Rising Heat**: As temperature hits $29^{\circ}C$, nothing happens. At $30.1^{\circ}C$, the fan kicks in.
2.  **Cooling**: The fan lowers the temperature. As it drops back to $29.5^{\circ}C$, the fan **stays on** (preventing rapid ON/OFF).
3.  **Shutoff**: Only when the system is safely "Cool" ($27.9^{\circ}C$) does the fan turn off.
4.  **Purpose**: This "Slack" prevents the relay from clicking/chattering 100 times per minute.

### 10. Generated Code
```python
import machine
import time

fan = machine.Pin(16, machine.Pin.OUT)
sensor = machine.ADC(4)

def get_temp():
    v = sensor.read_u16() * (3.3/65535)
    return 27 - (v - 0.706)/0.001721

while True:
    t = get_temp()
    
    if t > 30.0:
        fan.on()
        print("Cooling Activated")
    elif t < 28.0:
        fan.off()
        print("Eco Mode (Safe Temp)")
        
    time.sleep(1)
```

### 11. Common Mistakes
*   **Narrow Gap**: If your OFF point is 29.9 and ON is 30.0, you still have chattering. Make the "comfort gap" at least 1-2 degrees.
*   **Condition Clash**: Using `if (temp > 30)` followed immediately by `else { fan.off() }`. This IS NOT hysteresis. It must be `if/elif` or two separate `if` checks with different numbers.

### 12. Try This Next
*   **Visual Gap**: use an OLED to show the "Target" range and the current value.
"""

    p0537 = """
---

## 1. Project 0537: Temperature Alarm Alarm System

### 2. Learning Objective
Build a "Fire Detection" algorithm based on the **Rate of Change** (the derivative) of temperature rather than just the raw absolute temperature value.

### 3. Concepts Introduced
*   Change over Time ($\Delta T / \Delta t$)
*   Delta Tracking
*   Historical State comparison
*   Fast-response Logic

### 4. Hardware Required
*   Raspberry Pi Pico
*   Buzzer

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buzzer** | GP15 | Safety Alarm |

### 6. Blocks Used
*   **from Math, drag `arithmetic`** (Subtraction for Delta)
*   **from Variables, drag `set_variable`**
*   **from Time, drag `pico_wait`** (Sampling window)

### 7. Variables
*   **old_temp**: Float (Temp 10 seconds ago)
*   **new_temp**: Float (Current temp)
*   **rise**: Float (The difference)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Alarm**: Set GP15 as Buzzer Output.
2.  **Seed History**: Read current temp into `old_temp`.

**B. Main Loop Phase**
3.  **Sample Window**: Wait 10 seconds.
4.  **Check Current**: Read current temp into `new_temp`.
5.  **Calculate Velocity**:
    *   `rise = new_temp - old_temp`.
6.  **Evaluate Logic**:
    *   If `rise` > 5:
        *   **ALARM**: Pulse Buzzer rapidly.
        *   Print: "FIRE ALERT: RAPID RISE DETECTED!".
7.  **Shift History**:
    *   Set `old_temp` to the `new_temp` value (prepare for next check).

### 9. Execution Flow
1.  **Observe**: System sleeps for 10 seconds.
2.  **Compare**: It looks at the difference between "then" and "now".
3.  **Logic**: If the temp is $60^{\circ}C$ but hasn't changed, no alarm (it's an oven). If the temp only $35^{\circ}C$ but it was $20^{\circ}C$ ten seconds ago, trigger alarm (something is burning).
4.  **Repeat**: Always updates its reference point to keep tracking the most recent trend.

### 10. Generated Code
```python
from machine import Pin, ADC
import time

buzzer = Pin(15, Pin.OUT)
sensor = ADC(4)

def get_t():
    v = sensor.read_u16() * (3.3/65535)
    return 27 - (v - 0.706)/0.001721

old_t = get_t()

while True:
    time.sleep(10) # 10 second window
    new_t = get_t()
    
    rise = new_t - old_t
    print(f"Window Change: {rise:.2f}C")
    
    if rise > 5.0:
        print("!!! RAPID RISE DISCOVERED !!!")
        for _ in range(10):
            buzzer.on(); time.sleep(0.1); buzzer.off(); time.sleep(0.1)
            
    old_t = new_t
```

### 11. Common Mistakes
*   **Too Short Window**: If you check every 0.1s, the temp might only rise 0.01 degrees, which is too small to distinguish from sensor noise. Check over 5-10 seconds.
*   **Negatives**: If you use a freezer, the "rise" might be -10. Make sure the logic check for `> 5` specifically.

### 12. Try This Next
*   **Variable Sensitivity**: Add a button that lets you cycle between "High Sensitivity" (Rise > 2) and "Low Sensitivity" (Rise > 10).
"""

    p0538 = """
---

## 1. Project 0538: The Temperature Alarm Game

### 2. Learning Objective
Create a gamified "Body Heat" challenge where users hold the sensor and see who can reach a target temperature $30^{\circ}C$ in the shortest amount of time.

### 3. Concepts Introduced
*   Thermal Inertia
*   Timers and Stopwatches
*   Game States (Ready, Go, Win)
*   Value Thresholds

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP8 | I2C Data |
| **OLED SCL** | GP9 | I2C Clock |

### 6. Blocks Used
*   **from Time, drag `pico_milliseconds`** (Get timestamp)
*   **from Logic, drag `repeat_while`** (Running the game)
*   **from Display, drag `pico_oled_text`**

### 7. Variables
*   **start_time**: Integer (Ticks at start)
*   **current_temp**: Float

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Prep Display**: Init OLED. Show "Hold Sensor to START!".

**B. Wait Phase**
2.  **Detect Touch**:
    *   Loop until `internal_temp` > 28.
3.  **Start Clock**:
    *   Set `start_time` to current milliseconds.

**C. Active Phase**
4.  **Race**:
    *   While `internal_temp` < 32:
        *   Update OLED with "Temp: [current]" and "Time: [ms - start]".
5.  **Calculate Finale**:
    *   Record `final_score` = (`pico_ms` - `start_time`) / 1000.
    *   Print to OLED: "FINISHED! TIME: [score] s".

### 9. Execution Flow
1.  **Ready**: System waits for the sensor to detect a human hand (rise above room temp).
2.  **Go**: Once triggered, a timer starts running.
3.  **Active**: The user squeezes the chip to transfer body heat.
4.  **Win**: As soon as the goal is reached, the clock stops.
5.  **Score**: The screen freezes on the duration, allowing for a competitive "high score" comparison.

### 10. Generated Code
```python
import machine, ssd1306, time

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
adc = machine.ADC(4)

def get_t():
    v = adc.read_u16() * (3.3/65535)
    return 27 - (v - 0.706)/0.001721

while True:
    oled.fill(0); oled.text("READY...", 30, 25); oled.show()
    
    # Wait for hand
    while get_t() < 28: time.sleep(0.1)
    
    start = time.ticks_ms()
    t = get_t()
    
    while t < 31: # Goal
        t = get_t()
        now = time.ticks_diff(time.ticks_ms(), start) / 1000
        oled.fill(0)
        oled.text(f"TEMP: {t:.1f}C", 10, 10)
        oled.text(f"TIME: {now:.1f}s", 10, 30)
        oled.show()
        
    # Result
    oled.fill(0); oled.text("WIN!", 40, 10); oled.text(f"SCORE: {now}s", 10, 30); oled.show()
    time.sleep(5) # Delay before next game
```

### 11. Common Mistakes
*   **Inverted Cooling**: If the room is already $31^{\circ}C$, the game will finish instantly. Ensure the goal is at least $2-3^{\circ}C$ above ambient.
*   **Squeeze too hard**: Remind users not to crush the Pico; body heat transfer through the board takes a few seconds anyway.

### 12. Try This Next
*   **Cooldown Phase**: Add a mandatory cooldown period where the temp must drop below $27^{\circ}C$ before another person can play.
"""

    p0539 = """
---

## 1. Project 0539: Automated Temperature Alarm

### 2. Learning Objective
Implement a "Moving Average Filter" that averages 10 sequential readings to eliminate flickering data spikes and create a smooth, reliable temperature signal.

### 3. Concepts Introduced
*   Signal Processing (Low-pass filtering)
*   Circular Buffers / Summing Lists
*   Noise Reduction
*   Integer/Float Precision

### 4. Hardware Required
*   Raspberry Pi Pico

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Internal Sensor** | ADC 4 | Standard Pico temp |

### 6. Blocks Used
*   **from Loops, drag `count_with`** (Loop 10 times)
*   **from Variables, drag `change_variable`** (Summing results)
*   **from Math, drag `division`** (Final Average)

### 7. Variables
*   **sum_total**: Float (Accumulator)
*   **smoothed_val**: Float (Final result)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Prep Program**: No hardware init required.

**B. Main Loop Phase**
2.  **Clear Samples**:
    *   Set `sum_total` to 0.
3.  **Collect Data**:
    *   From **Loops**, `count_with` variable `i` from 1 to 10.
        *   Inside loop: Read temp and **ADD** it to `sum_total`.
        *   Wait 0.05s between reads.
4.  **Calculate Smooth Value**:
    *   `smoothed_val = sum_total / 10`.
5.  **Report**:
    *   Print: "Filtered Data: [smoothed_val]".
6.  **Wait**: 1s.

### 9. Execution Flow
1.  **Sample**: In less than a second, the Pico takes 10 snapshots of the temperature.
2.  **Flatten**: If the sensor jumped to $28^{\circ}C$ for one microsecond due to electrical static, that one spike ($1/10th$ weight) is swallowed by the 9 other good readings.
3.  **Result**: The output "floats" smoothly rather than jumping erratically.
4.  **Benefit**: Prevents "false alarms" in systems that trigger fans or buzzers.

### 10. Generated Code
```python
import machine
import time

adc = machine.ADC(4)

def get_raw():
    v = adc.read_u16() * (3.3/65535)
    return 27 - (v - 0.706)/0.001721

while True:
    total = 0
    for _ in range(10):
        total += get_raw()
        time.sleep(0.05)
    
    avg = total / 10
    print(f"Noise-Reduced Temp: {avg:.3f}C")
    time.sleep(1)
```

### 11. Common Mistakes
*   **Sampling too slow**: If you wait 2 seconds between samples, your "average" is actually a report on what happened 20 seconds ago—the data is too "laggy".
*   **Zeroing**: Forgetting to reset the `total` back to 0 at the start of the loop will cause the number to grow to infinity.

### 12. Try This Next
*   **Dynamic Window**: Add a button to switch between a 10-sample average (fast) and a 100-sample average (extremely smooth but slow).
"""

    p0540 = """
---

## 1. Project 0540: Mastering Temperature Alarm

### 2. Learning Objective
Introduce the fundamentals of Closed-Loop Control by building a Proportional Fan Controller. The fan speed is calculated dynamically based on how "far" the temperature is from the target.

### 3. Concepts Introduced
*   Closed Loop Control
*   Error Signal ($Target - Current$)
*   Proportional Gain ($Kp$)
*   Linear Modulation

### 4. Hardware Required
*   Raspberry Pi Pico
*   Motor Driver and Fan (Simulated with PWM LED)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Cooling Fan** | GP16 | PWM Speed Control |

### 6. Blocks Used
*   **from Math, drag `arithmetic`** (Subtraction and Multiplication)
*   **from Smart IO, drag `pico_pwm_write`** (Set speed)
*   **from Logic, drag `if_else`** (Clip bounds)

### 7. Variables
*   **current**: Float (Sensor temp)
*   **target**: Float (Desired temp, e.g., 28)
*   **error**: Float (The difference)
*   **power**: Integer (0-65535 PWM)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init PWM**: Set GP16 at 1000Hz.
2.  **Goals**: Set `target` to 28.0 and `gain` to 5000.

**B. Main Loop Phase**
3.  **Calculate Error**:
    *   `error = current - target`.
4.  **Determine Power**:
    *   If `error` > 0:
        *   `power = error * gain`.
    *   Else:
        *   `power = 0`.
5.  **Safety Clip**:
    *   If `power` > 65535: `power = 65535`.
6.  **Apply Logic**:
    *   From **Smart IO**, set GP16 (PWM) to `power`.
7.  **Report**:
    *   Print: "Distance from target: [error], Fan Power: [power]".

### 9. Execution Flow
1.  **Sense**: Temperature is $27^{\circ}C$. Error is negative. Fan power is 0 (Off).
2.  **Heat**: Temperature rises to $28.5^{\circ}C$. Error is $0.5$. $0.5 \times 5000 = 2500$ power. Fan spins very slowly.
3.  **Critical**: Temperature hits $35^{\circ}C$. Error is $7$. $7 \times 5000 = 35000$. Fan is now at half-speed.
4.  **Response**: The system doesn't just turn ON/OFF; it adjusts its efforts to match the severity of the problem.

### 10. Generated Code
```python
import machine
import time

fan = machine.PWM(machine.Pin(16))
fan.freq(1000)
adc = machine.ADC(4)

target = 28.0
kp = 6000 # Gain factor

while True:
    v = adc.read_u16() * (3.3/65535)
    t = 27 - (v - 0.706)/0.001721
    
    error = t - target
    
    if error > 0:
        power = int(error * kp)
        if power > 65000: power = 65000
    else:
        power = 0
        
    fan.duty_u16(power)
    print(f"Temp: {t:.1f} | Error: {error:.1f} | PWM: {power}")
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Gain too high**: Setting `gain` to 1,000,000 means even a $0.001$ margin will kick the fan to full speed. This makes it act like a simple switch, losing the benefit of proportional control.
*   **Integer Conversion**: PWM values must be whole numbers. Ensure you use `int()` in the calculation.

### 12. Try This Next
*   **User Target**: Connect a Potentiometer to adjust the `target` value in real-time.
"""
    
    with open(target_file, 'a', encoding='utf-8') as f:
        f.write(p0531 + p0532 + p0533 + p0534 + p0535 + p0536 + p0537 + p0538 + p0539 + p0540)
    
    print("Batch 54 (0531-0540) appended with Elite Standard v2.0.")

if __name__ == "__main__":
    build_batch54()
