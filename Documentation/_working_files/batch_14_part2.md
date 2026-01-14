
## Project 0133: Manual Temperature Alarm Control

### 1. Learning Objective
Learn how to store and use baseline data. Understand the concept of "Relative Measurement" by comparing current sensor values to a user-defined reference point.

### 2. Concepts Introduced
*   **Variable Baseline**: Capturing a state in time to use as a future comparator.
*   **Delta Calculation**: Finding the mathematical difference between two values (Current - Normal).
*   **Event-Driven Storage**: Using a button press to trigger data capture.

### 3. Hardware Required
*   Raspberry Pi Pico
*   1 Button
*   10k Ohm pull-down resistor
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP14 | Connect with pull-down resistor |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_read_temp`** (read temperature)
*   **from Smart IO, drag `pico_gpio_read`** (read Pin)
*   **from Variables, drag `variables_set`** (set variable to)
*   **from Math, drag `math_arithmetic`** (subtraction)
*   **from Time, drag `pico_wait`** (wait)
*   **from Text, drag `text_print`** (print to console)

### 6. Variables
*   **baseline_temp**: The stored "Normal" temperature.
*   **current_temp**: Current live reading.
*   **temp_diff**: The calculated difference (Current - Baseline).

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Initial Baseline**:
    *   From **Variables**, drag `variables_set`. **Set** `baseline_temp` to the value of `pico_read_temp`.
    *   From **Text**, drag `text_print`. **Print** "Initial Baseline Set: ", `baseline_temp`.

**B. Monitoring Phase**
2.  **Create Forever Loop**:
    *   From **Loops**, drag `pico_forever` and snap it below initialization.
3.  **Read live data**:
    *   From **Variables**, drag `variables_set`. **Set** `current_temp` to `pico_read_temp`.

**C. Interaction and Storage Phase**
4.  **Detect Reset Button**:
    *   From **Logic**, drag `controls_if`. Snap it inside the loop.
    *   **Condition**: If **Smart IO** `pico_gpio_read` GP14 is True.
    *   **Inside If (then)**:
        *   From **Variables**, drag `variables_set`. **Set** `baseline_temp` = `current_temp`.
        *   From **Text**, drag `text_print`. **Print** "--- Baseline Reset to Current ---".

**D. Comparison Phase**
5.  **Calculate Difference**:
    *   From **Variables**, drag `variables_set`. **Set** `temp_diff` = (`current_temp` - `baseline_temp`).
6.  **Output Logs**:
    *   From **Text**, drag `text_print`. **Print** "Current: ", `current_temp`, " Diff: ", `temp_diff`.
7.  **Add Delay**:
    *   From **Time**, drag `pico_wait` -> 1 second.

### 8. Execution Flow
1.  **Start**: Program reads the temperature once and stores it as the first baseline.
2.  **Loop**: Program continuously checks the current temperature.
3.  **Comparison**: It subtracts the stored baseline from the current reading to find the change.
4.  **Update**: If the user presses the button, the current temperature becomes the new "Normal" baseline.
5.  **Output**: User sees the live change (e.g., +2.5 degrees if it gets warmer).

### 9. Generated Code
```python
from machine import Pin, ADC
import time

# Setup sensor and button
temp_sensor = ADC(4)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
conversion_factor = 3.3 / 65535

# Set initial baseline
def read_celsius():
    reading = temp_sensor.read_u16() * conversion_factor
    return 27 - (reading - 0.706) / 0.001721

baseline_temp = read_celsius()
print("Initial Baseline Set: " + str(baseline_temp))

while True:
    current_temp = read_celsius()
    
    # Store new baseline on button press
    if button.value():
        baseline_temp = current_temp
        print("--- Baseline Reset to Current ---")
        time.sleep(0.3) # Debounce
        
    # Calculate difference
    temp_diff = current_temp - baseline_temp
    
    print("Current: " + str(current_temp) + " Diff: " + str(temp_diff))
    time.sleep(1)
```

### 10. Common Mistakes
*   **Floating Pins**: Forgetting the pull-down resistor on the button will cause random baseline resets.
*   **Missing Print**: If you don't print the difference, you won't see the benefit of the baseline.

### 11. Try This Next
*   **Visual Diff**: Blink a Red LED if diff > 2.0 (Hotter) and a Blue LED if diff < -2.0 (Colder).
*   **Long-Term Tracking**: Try to see how much the temperature drifts over 10 minutes.

---

## Project 0134: Temperature Alarm Sequences

### 1. Learning Objective
Learn how to implement multi-zone logic (Range Checking). Understand how to use nested conditions or multiple IF blocks to categorize data into different states (Cool, Normal, Hot).

### 2. Concepts Introduced
*   **Range Monitoring**: Checking if a value falls between two specific numbers.
*   **Multi-Output Control**: Managing several indicators (LEDs) based on a single sensor input.
*   **Status Indicators**: Mapping environmental data to established color standards (Red/Yellow/Green).

### 3. Hardware Required
*   Raspberry Pi Pico
*   3 LEDs (Red, Yellow, Green)
*   3x 220-330 Ohm resistors
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Green LED** | GP14 | Cool status (< 20C) |
| **Yellow LED** | GP13 | Normal status (20C - 28C) |
| **Red LED** | GP12 | Hot status (> 28C) |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_read_temp`** (read temperature)
*   **from Logic, drag `controls_if`** (if/else if/else)
*   **from Logic, drag `logic_operation`** (AND)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **t**: The temperature read from the sensor.

### 7. Step-by-Step Guide

**A. Setup Phase**
1.  **Initialize all LEDs to OFF**:
    *   From **Smart IO**, drag `pico_gpio_write` blocks for GP14, GP13, and GP12 -> LOW.

**B. Monitoring Phase**
2.  **Create Forever Loop**:
    *   From **Loops**, drag `pico_forever`.
3.  **Read Temp**:
    *   **Set** `t` = `pico_read_temp`.

**C. Logic Branching Phase**
4.  **Categorize Temperature**:
    *   From **Logic**, drag a `controls_if` block. Use the gear icon to add two **else if** slots and one **else** slot.
5.  **Cool Zone (If t < 20)**:
    *   Inside the first **If** slot (t < 20):
    *   **Set** GP14 (Green) -> HIGH.
    *   **Set** GP13 (Yellow) -> LOW.
    *   **Set** GP12 (Red) -> LOW.
6.  **Normal Zone (Else If t >= 20 AND t <= 28)**:
    *   Inside the first **Else If** slot (t >= 20 and t <= 28):
    *   **Set** GP14 (Green) -> LOW.
    *   **Set** GP13 (Yellow) -> HIGH.
    *   **Set** GP12 (Red) -> LOW.
7.  **Hot Zone (Else)**:
    *   Inside the **Else** slot (covers all cases > 28):
    *   **Set** GP14 (Green) -> LOW.
    *   **Set** GP13 (Yellow) -> LOW.
    *   **Set** GP12 (Red) -> HIGH.

**D. Timing Phase**
8.  **Add Delay**:
    *   From **Time**, drag `pico_wait` -> 1 second.

### 8. Execution Flow
1.  **Read**: Get the temperature value.
2.  **Compare Cool**: If below 20C, turn on ONLY Green LED.
3.  **Compare Normal**: If between 20C and 28C, turn on ONLY Yellow LED.
4.  **Compare Hot**: If above 28C, turn on ONLY Red LED.
5.  **Output**: Visual indicators provide instant environmental feedback.

### 9. Generated Code
```python
from machine import Pin, ADC
import time

# Configure LEDs
led_green = Pin(14, Pin.OUT)
led_yellow = Pin(13, Pin.OUT)
led_red = Pin(12, Pin.OUT)
sensor = ADC(4)
conv = 3.3 / 65535

while True:
    read = sensor.read_u16() * conv
    t = 27 - (read - 0.706) / 0.001721
    
    if t < 20:
        led_green.value(1)
        led_yellow.value(0)
        led_red.value(0)
    elif t >= 20 and t <= 28:
        led_green.value(0)
        led_yellow.value(1)
        led_red.value(0)
    else:
        led_green.value(0)
        led_yellow.value(0)
        led_red.value(1)
        
    time.sleep(1)
```

### 10. Common Mistakes
*   **Overlapping Ranges**: If you checked `t < 25` and then `t < 20`, order matters or it will trigger the wrong LED.
*   **Leaving Multiples ON**: Forgetting to turn OFF the other LEDs in each branch will result in all LEDs being ON eventually.

### 11. Try This Next
*   **Dynamic Thresholds**: Use a potentiometer to adjust the 'Normal' window.
*   **Blinking Red**: Make the Red LED blink if it reaches a 'Danger' level (e.g., > 35C).

---

## Project 0135: Interactive Temperature Alarm

### 1. Learning Objective
Learn how to perform mathematical unit conversion. Understand how user input (button hold) can dynamically change how data is processed and displayed.

### 2. Concepts Introduced
*   **Unit Conversion Formula**: Implementing standard equations (C to F).
*   **State-Dependent Output**: Changing display mode based on button state.
*   **Input-Output Mapping**: Using digital input to switch between calculation models.

### 3. Hardware Required
*   Raspberry Pi Pico
*   1 Button
*   10k Ohm pull-down resistor
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP14 | Press and hold to view Fahrenheit |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_read_temp`** (read temperature)
*   **from Logic, drag `controls_if`** (if/else)
*   **from Math, drag `math_arithmetic`** (multiplication, addition)
*   **from Smart IO, drag `pico_gpio_read`** (read Pin)
*   **from Text, drag `text_print`** (print to console)

### 6. Variables
*   **temp_c**: Celsius value.
*   **temp_f**: Calculated Fahrenheit value.

### 7. Step-by-Step Guide

**A. Data Acquisition Phase**
1.  **Start Main Loop**:
    *   From **Loops**, drag `pico_forever`.
2.  **Read Baseline Temperature**:
    *   From **Variables**, **Set** `temp_c` = `pico_read_temp`.

**B. Calculation and Choice Phase**
3.  **Check Button State**:
    *   From **Logic**, drag `controls_if` with **else**.
    *   **Condition**: If **Smart IO** `pico_gpio_read` GP14 is True (held down).
4.  **Branch 1: Fahrenheit (Button Pressed)**:
    *   Inside the **If** slot:
    *   From **Variables**, **Set** `temp_f` = (`temp_c` * 1.8) + 32.
    *   From **Text**, **Print** "Temp in Fahrenheit: ", `temp_f`.
5.  **Branch 2: Celsius (Button Released)**:
    *   Inside the **Else** slot:
    *   From **Text**, **Print** "Temp in Celsius: ", `temp_c`.

**C. Timing Phase**
6.  **Add Delay**:
    *   **Wait** 0.5 seconds.

### 8. Execution Flow
1.  **Read**: Temperature is acquired in Celsius.
2.  **Check**: The program checks if GP14 (button) is active.
3.  **Path A (Hold)**: If held, math is performed to convert C to F before printing.
4.  **Path B (Normal)**: If not held, the original C value is printed.
5.  **Repeat**: Data updates twice per second.

### 9. Generated Code
```python
from machine import Pin, ADC
import time

# Hardware setup
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
temp_adc = ADC(4)
c_factor = 3.3 / 65535

while True:
    read = temp_adc.read_u16() * c_factor
    temp_c = 27 - (read - 0.706) / 0.001721
    
    if button.value() == 1:
        # Convert C to F
        temp_f = (temp_c * 1.8) + 32
        print("Temp in Fahrenheit: " + str(temp_f) + " F")
    else:
        print("Temp in Celsius: " + str(temp_c) + " C")
        
    time.sleep(0.5)
```

### 10. Common Mistakes
*   **Operator Order**: In math, ensure multiplication happens before addition for the correct F conversion.
*   **Serial Flooding**: Not adding a wait block will make the print statements fly by too fast.

### 11. Try This Next
*   **Toggle Mode**: Instead of holding the button, make it click to switch and stay in that mode until the next click.
*   **Kelvin Mode**: Add another button or calculation path for Kelvin (C + 273.15).

---

## Project 0136: Smart Temperature Alarm Switch

### 1. Learning Objective
Understand the concept of Hysteresis in Control Systems. Learn how to prevent "chatter" or rapid oscillation of a switch by using two different thresholds for turning an output ON and OFF.

### 2. Concepts Introduced
*   **Hysteresis**: A system property where the state depends on the direction of change.
*   **Control Loop Stability**: Preventing rapid on/off switching near a single threshold point.
*   **Actuator Simulation**: Using an LED to simulate a high-power device like a fan or heater.

### 3. Hardware Required
*   Raspberry Pi Pico
*   1 LED (Fan Simulator)
*   1x 220-330 Ohm resistor
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED (Fan)** | GP15 | Turns on at 30C, stays on until 25C |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_read_temp`** (read temperature)
*   **from Logic, drag `controls_if`** (sequential if blocks)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Variables, drag `variables_set`** (set variable to)

### 6. Variables
*   **t**: Live temperature reading.

### 7. Step-by-Step Guide

**A. Monitoring Phase**
1.  **Start Main Loop**:
    *   From **Loops**, drag `pico_forever`.
2.  **Read Temp**:
    *   **Set** `t` = `pico_read_temp`.

**B. Logic Control Phase**
3.  **Turn ON Threshold**:
    *   From **Logic**, drag a `controls_if` block.
    *   **Condition**: If `t` > 30.
    *   **Inside**: **Set** GP15 (Fan) -> HIGH.
    *   **Output**: From **Text**, **Print** "FAN ON (TOO HOT)".

4.  **Turn OFF Threshold**:
    *   From **Logic**, drag a second `controls_if` block (separate from the first).
    *   **Condition**: If `t` < 25.
    *   **Inside**: **Set** GP15 (Fan) -> LOW.
    *   **Output**: From **Text**, **Print** "FAN OFF (COOL ENOUGH)".

**C. Maintenance Phase**
5.  **Steady State Handling**: Note that if `t` is between 25 and 30, **nothing happens to the LED**. It stays in whatever state it was last set to. This is the "Hysteresis Window".

6.  **Add Delay**:
    *   **Wait** 1 second to observe changes slowly.

### 8. Execution Flow
1.  **Rise**: Temperature rises to 30.1C. Fan turns ON.
2.  **Fluctuation**: Temperature drops to 29.5C. Fan STAYS ON (because it's not < 25C).
3.  **Fall**: Temperature drops to 24.9C. Fan turns OFF.
4.  **Rise Again**: Temperature goes back to 26C. Fan STAYS OFF (because it's not > 30C).
5.  **Result**: The motor/fan doesn't wear out from clicking on/off every second at the 30.0C border.

### 9. Generated Code
```python
from machine import Pin, ADC
import time

led_fan = Pin(15, Pin.OUT)
sensor = ADC(4)
factor = 3.3 / 65535

while True:
    read = sensor.read_u16() * factor
    t = 27 - (read - 0.706) / 0.001721
    
    # Upper threshold to turn ON
    if t > 30:
        led_fan.value(1)
        print("FAN ON - Current: " + str(t))
    
    # Lower threshold to turn OFF
    if t < 25:
        led_fan.value(0)
        print("FAN OFF - Current: " + str(t))
        
    time.sleep(1)
```

### 10. Common Mistakes
*   **Using Else**: If you use `if t > 30 / else: led.off()`, you have NO hysteresis. It will flicker at 30.0C.
*   **Wrong Threshold Order**: Ensure the ON threshold is actually higher than the OFF threshold for cooling (or vice-versa for heating).

### 11. Try This Next
*   **Heat Logic**: Reverse the logic for a heater: Turn ON at < 20C, Turn OFF at > 22C.
*   **Visual Windows**: Add a different colored LED that glows only when inside the "Stable/Wait" window (between 25 and 30).

---
