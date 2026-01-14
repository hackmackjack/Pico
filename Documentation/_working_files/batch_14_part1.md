
# BATCH 14: Temperature Alarm 1 (Projects 0131-0140)

## Project 0131: Introduction to Temperature Alarm

### 1. Learning Objective
Learn how to access the internal temperature sensor of the Raspberry Pi Pico. Understand how to convert raw sensor data into meaningful Celsius readings and log them to the console.

### 2. Concepts Introduced
*   **Analog-to-Digital Conversion (ADC)**: Converting physical voltage into a digital number.
*   **Built-in Sensors**: Using the Pico's internal hardware (ADC4) for monitoring.
*   **Data Logging**: Continuously outputting sensor data for observation.

### 3. Hardware Required
*   Raspberry Pi Pico (using internal sensor)

### 4. Wiring / Interfaces
*   **No external wiring required**: This project uses the built-in sensor on the Pico board itself.

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_read_temp`** (read temperature in Celsius)
*   **from Text, drag `text_print`** (print to console)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **temp_c**: Stores the current temperature value in degrees Celsius.

### 7. Step-by-Step Guide

**A. Setup Phase**
1.  **Start the Main Program Structure**:
    *   From **Loops**, drag the `pico_forever` block and snap it into the workspace.

**B. Data Acquisition Phase**
2.  **Read the Internal Sensor**:
    *   From **Variables**, drag the `variables_set` block and snap it inside the `pico_forever` loop.
    *   **Set** the variable name to `temp_c`.
    *   From **Sensors**, drag the `pico_read_temp` block and snap it into the value slot of the set block.
    *   Ensure the dropdown is set to **Celsius**.

**C. Output and Timing Phase**
3.  **Print to Console**:
    *   From **Text**, drag the `text_print` block and snap it below the variable set block.
    *   From **Text**, drag a text string block and snap it into the first slot. **Set** text to "Temperature: ".
    *   From **Variables**, drag the `temp_c` block and snap it into the second slot.
    *   Drag another text string block and **Set** text to " C".

4.  **Add Delay**:
    *   From **Time**, drag the `pico_wait` block and snap it at the end of the loop.
    *   **Set** wait time to 2 seconds.

### 8. Execution Flow
1.  **Start**: The program enters an infinite loop.
2.  **Read**: The Pico reads the voltage from the internal ADC channel 4 (connected to the temperature sensor).
3.  **Convert**: The firmware automatically converts the raw ADC value into a Celsius temperature reading.
4.  **Display**: The calculated value is sent via USB serial to the computer's terminal.
5.  **Wait**: The Pico pauses for 2 seconds before taking the next reading to prevent data flooding.

### 9. Generated Code
```python
import machine
import utime

# Configure the internal temperature sensor (ADC 4)
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    # Read raw ADC value
    reading = sensor_temp.read_u16() * conversion_factor
    
    # Convert voltage to Celsius based on Pico datasheet formula
    # temp = 27 - (voltage - 0.706) / 0.001721
    temperature = 27 - (reading - 0.706) / 0.001721
    
    print("Temperature: " + str(temperature) + " C")
    utime.sleep(2)
```

### 10. Common Mistakes
*   **Confusing C and F**: Ensure the block or formula is set for Celsius.
*   **Reading Too Fast**: Not including a `wait` block can crash the serial console with too much data.
*   **Blocking Sensor**: Touching the chip can heat it up and give inaccurate room temperature readings.

### 11. Try This Next
*   **Change to Fahrenheit**: Use the math block `(C * 1.8) + 32` to convert the reading.
*   **Fast Log**: Reduce the wait time to 0.1s and see how the temperature fluctuates when you blow on the chip.

---

## Project 0132: Blinking Temperature Alarm

### 1. Learning Objective
Apply conditional logic to sensor data. Create a "Freeze Warning" system that alerts the user when the temperature drops below a specific threshold.

### 2. Concepts Introduced
*   **Threshold Triggering**: Activating an output only when a specific value is reached.
*   **Visual Alerting**: Using LED states (Blinking vs. Solid) to convey status.
*   **Environmental Simulation**: Testing code logic using temperature changes.

### 3. Hardware Required
*   Raspberry Pi Pico
*   1 Blue LED
*   1x 220-330 Ohm resistor
*   Breadboard and jumper wires
*   (Optional: Ice cube in a plastic bag to test)

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Blue LED Anode (+)** | GP15 | Connect through resistor |
| **Blue LED Cathode (-)** | GND | Common ground |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_read_temp`** (read temperature)
*   **from Logic, drag `controls_if`** (if/else)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **current_temp**: Stores the Celsius reading from the internal sensor.

### 7. Step-by-Step Guide

**A. Setup Phase**
1.  **Initialize LED**:
    *   From **Smart IO**, drag `pico_gpio_write` and snap it to the start.
    *   **Set** GP15 as OUTPUT -> LOW.

**B. Sensor Reading Phase**
2.  **Create Main Loop**:
    *   From **Loops**, drag `pico_forever` and snap it below setup.
3.  **Read Temperature**:
    *   From **Variables**, drag `variables_set`. **Set** `current_temp` to the value of `pico_read_temp`.

**C. Conditional Alarm Phase**
4.  **Check for "Cold" Condition**:
    *   From **Logic**, drag the `controls_if` block with the **else** extension. Snap it inside the loop.
    *   **Condition**: If `current_temp` < 25.
5.  **Freeze Warning (Blink)**:
    *   Inside the **If** (then) slot:
    *   From **Smart IO**, drag `pico_gpio_write`. **Set** GP15 -> HIGH.
    *   From **Time**, drag `pico_wait` -> 0.2s.
    *   From **Smart IO**, drag `pico_gpio_write`. **Set** GP15 -> LOW.
    *   From **Time**, drag `pico_wait` -> 0.2s.
6.  **Normal Status (Solid)**:
    *   Inside the **Else** slot:
    *   From **Smart IO**, drag `pico_gpio_write`. **Set** GP15 -> HIGH.

### 8. Execution Flow
1.  **Start**: Initialize the Blue LED.
2.  **Monitor**: Continually check the Pico's core temperature.
3.  **Evaluate**: Compare the reading to 25 degrees Celsius.
4.  **Blink**: If temperature is low (below 25C), the LED flashes rapidly.
5.  **Steady**: if temperature is normal (25C or above), the LED stays on solid.

### 9. Generated Code
```python
from machine import Pin, ADC
import time

# Setup hardware
led_blue = Pin(15, Pin.OUT)
temp_sensor = ADC(4)
conversion_factor = 3.3 / 65535

while True:
    # Read temperature
    reading = temp_sensor.read_u16() * conversion_factor
    temp = 27 - (reading - 0.706) / 0.001721
    
    if temp < 25:
        # Blink for cold warning
        led_blue.value(1)
        time.sleep(0.2)
        led_blue.value(0)
        time.sleep(0.2)
    else:
        # Solid for normal temp
        led_blue.value(1)
```

### 10. Common Mistakes
*   **Threshold Too High/Low**: If your room is 26C, a threshold of 25C won't trigger unless you actively cool the sensor.
*   **No Wait in Else**: While the blink has wait blocks, the else part should also be efficient (though not strictly required for logic, it's good practice).

### 11. Try This Next
*   **Dual Alarm**: Add a Red LED that blinks when Temp > 30 (Heat Warning).
*   **Hysteresis**: Try to stop the LED from flickering if the temperature stays exactly at 25C.

---
