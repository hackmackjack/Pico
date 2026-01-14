#!/usr/bin/env python3
"""
Enhanced Elite Standard v2.0 Documentation Generator
Produces DETAILED Section 8 step-by-step guides with "From [Category], drag" format
"""

import re

PROJECT_DETAILS = {
    # Detailed templates for Section 8 guides
    '0425': {
        'title': 'Interactive Sound & Music',
        'hw': 'Pico, Accelerometer, Buzzer',
        'concept': 'Tilt-controlled audio',
        'section8': '''**A. Initialization Phase**
1.  **Setup I2C and PWM**:
    *   From **Sensors**, drag I2C initialization block.
        *   **Snap** into setup section.
        *   Configure for GP0 (SDA) and GP1 (SCL).
    *   From **Smart IO**, drag PWM setup block.
        *   **Snap** below.
        *   Configure GP15 as PWM output for buzzer.

**B. Main Loop Phase**
2.  **Read Accelerometer Data**:
    *   From **Sensors**, drag `i2c_read` block.
        *   **Snap** into main loop.
        *   Read X and Y axis values.
        *   Store in `xTilt` and `yTilt` variables.
3.  **Map X-Axis to Frequency**:
    *   From **Math**, drag `map_range` block.
        *   **Snap** below.
        *   Input: `xTilt` (range -1.0 to +1.0)
        *   Output: frequency (range 200 to 800 Hz)
4.  **Map Y-Axis to Volume**:
    *   From **Math**, drag `map_range` block.
        *   **Snap** below.
        *   Input: `yTilt` (range -1.0 to +1.0)
        *   Output: volume (range 0 to 100%)
5.  **Apply to Buzzer**:
    *   From **Smart IO**, drag `pico_pwm_write` block.
        *   **Snap** below.
        *   Set frequency to mapped value.
        *   Set duty cycle based on volume percentage.
6.  **Sampling Delay**:
    *   From **Time**, drag `pico_wait` block.
        *   **Snap** below.
        *   Set delay to 0.05 seconds (50ms sampling rate).'''
    },
    # Add more detailed templates for other key projects
}

# Default detailed template for remaining projects
DEFAULT_DETAILED_SECTION8 = '''**A. Initialization Phase**
1.  **Configure Hardware**:
    *   From **Smart IO**, drag pin configuration blocks.
        *   **Snap** into setup section.
        *   Set up all required pins (digital, PWM, or analog).
    *   From **Variables**, drag variable initialization blocks.
        *   **Snap** below.
        *   Initialize state variables and thresholds.

**B. Main Loop Phase**
2.  **Read Input Sensors**:
    *   From **Smart IO**, drag appropriate read blocks (digital, analog, or I2C).
        *   **Snap** into main loop.
        *   Read all sensor inputs and store in variables.
3.  **Process Data**:
    *   From **Logic**, drag conditional blocks.
        *   **Snap** below.
        *   Implement decision logic based on sensor readings.
    *   From **Math**, drag calculation blocks if needed.
        *   **Snap** within logic blocks.
        *   Perform any required computations (mapping, thresholds, etc.).
4.  **Update Outputs**:
    *   From **Smart IO**, drag output control blocks.
        *   **Snap** below logic.
        *   Update LEDs, motors, buzzers, or other actuators.
5.  **Timing Control**:
    *   From **Time**, drag `pico_wait` block.
        *   **Snap** at end of loop.
        *   Set appropriate delay for update rate.'''


def generate_detailed_project(proj_num, title, hw, concept, section8=None):
    """Generate project with DETAILED Section 8"""
    
    if section8 is None:
        section8 = DEFAULT_DETAILED_SECTION8
    
    return f"""
## 1. Project {proj_num}: {title}

### 2. Learning Objective
Master {concept} using Raspberry Pi Pico with detailed implementation guidance.

### 3. Concepts Introduced
*   **Core Concept**: {concept}
*   **Hardware Integration**: {hw}
*   **Programming Skills**: Sensor reading, data processing, output control

### 4. Hardware Required
{hw}

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Primary Output** | GP15 | Main control signal |
| **Sensor Input** | GP26 | Analog/digital sensor |
| **Additional** | GP16-17 | As needed for project |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_write`** (control digital outputs)
*   **from Smart IO, drag `pico_analog_read`** (read analog sensors)
*   **from Smart IO, drag `pico_pwm_write`** (PWM control for motors/LEDs)
*   **from Time, drag `pico_wait`** (timing and delays)
*   **from Logic, drag `if_compare`** (conditional logic)
*   **from Math, drag `map_range`** (value mapping and scaling)

### 7. Variables
*   **state**: Current system state (boolean or enumeration)
*   **sensorValue**: Raw sensor reading
*   **processedValue**: Calculated/mapped value
*   **threshold**: Decision threshold for logic

### 8. Step-by-Step Guide

{section8}

### 9. Execution Flow
System initializes all hardware components and enters the main control loop. Each iteration reads sensor inputs, processes the data according to the project's logic ({concept}), updates outputs accordingly, and maintains timing through controlled delays. This creates a responsive, real-time control system.

### 10. Generated Code
```python
import machine, time

# Pin configuration
output_pin = machine.Pin(15, machine.Pin.OUT)
sensor_pin = machine.ADC(26)  # or Pin for digital

# Variables
state = False
threshold = 30000  # Adjust based on sensor

# Main loop
while True:
    # Read sensor
    sensor_value = sensor_pin.read_u16()
    
    # Process logic
    if sensor_value > threshold:
        state = True
        output_pin.on()
    else:
        state = False
        output_pin.off()
    
    # Delay
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Incorrect Pin Configuration**: Verify all pins match wiring diagram
*   **Missing Pull-up/Pull-down**: Add resistors for button inputs
*   **Timing Issues**: Adjust delays if system feels unresponsive
*   **Threshold Calibration**: Test sensor values and adjust thresholds accordingly

### 12. Try This Next
*   **Enhanced Features**: Add LCD display for real-time monitoring
*   **Multi-sensor**: Combine multiple sensors for complex logic
*   **Wireless Control**: Add WiFi/Bluetooth for remote operation
*   **Data Logging**: Store sensor readings to file for analysis

---
"""

# Generate for key projects with custom Section 8
print("Generating detailed documentation...")
print("Note: Run full generation to create all 73 projects with detailed Section 8")
