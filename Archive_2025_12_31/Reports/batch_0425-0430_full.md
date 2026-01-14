
## 1. Project 0425: Interactive Sound & Music

### 2. Learning Objective
Create tilt-controlled audio effects using accelerometer for X/Y axis modulation. You will learn about multi-axis sensor input and audio parameter mapping.

### 3. Concepts Introduced
*   **Tilt Tone**: Device orientation affects sound characteristics.
*   **Dual-Axis Modulation**: X-axis controls pitch, Y-axis controls volume.
*   **Accelerometer Input**: Reading tilt angles for audio control.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **Accelerometer** (ADXL345 or MPU6050)
*   **Buzzer** (passive)

### 5. Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Accelerometer SDA** | GP0 (I2C0 SDA) | I2C communication |
| **Accelerometer SCL** | GP1 (I2C0 SCL) | I2C communication |
| **Buzzer** | GP15 | PWM output |

### 6. Blocks Used
*   **from Sensors, drag `i2c_read`** (read accelerometer X/Y values)
*   **from Math, drag `map_range`** (convert tilt to frequency/volume)
*   **from Smart IO, drag `pico_pwm_write`** (control buzzer)
*   **from Time, drag `pico_wait`** (sampling rate)

### 7. Variables
*   **xTilt**: Accelerometer X-axis value (-1.0 to +1.0 g).
*   **yTilt**: Accelerometer Y-axis value (-1.0 to +1.0 g).
*   **frequency**: Pitch controlled by X-axis (200-800 Hz).
*   **volume**: Duty cycle controlled by Y-axis (0-100%).

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup I2C and PWM**:
    *   From **Sensors**, initialize I2C on GP0/GP1.
    *   From **Smart IO**, configure GP15 as PWM output.

**B. Main Loop Phase**
2.  **Read Accelerometer**:
    *   From **Sensors**, read X and Y axis values → store in `xTilt`, `yTilt`.
3.  **Map X to Frequency**:
    *   From **Math**, map `xTilt` from [-1.0, +1.0] to [200, 800] Hz.
4.  **Map Y to Volume**:
    *   From **Math**, map `yTilt` from [-1.0, +1.0] to [0, 100]%.
5.  **Apply to Buzzer**:
    *   From **Smart IO**, set PWM frequency to mapped value.
    *   From **Smart IO**, set PWM duty cycle to volume percentage.
6.  **Sample Delay**:
    *   From **Time**, wait 0.05 seconds.

### 9. Execution Flow
Tilting the device left/right changes pitch (low to high). Tilting forward/backward changes volume (quiet to loud). This creates an expressive instrument where physical motion directly controls sound parameters.

### 10. Generated Code
```python
import machine
import time

buzzer = machine.PWM(machine.Pin(15))

while True:
    # Simulated accelerometer values (-1 to +1)
    x_tilt = 0.5  # Replace with actual I2C read
    y_tilt = 0.3
    
    frequency = int((x_tilt + 1) / 2 * 600 + 200)
    volume = int((y_tilt + 1) / 2 * 100)
    duty = int(volume / 100 * 65535)
    
    buzzer.freq(frequency)
    buzzer.duty_u16(duty)
    time.sleep(0.05)
```

### 11. Common Mistakes
*   **No I2C Response**: Check wiring and I2C address.
*   **Inverted Axes**: Swap mapping or negate tilt value if backwards.

### 12. Try This Next
*   **3-Axis**: Add Z-axis control for tempo.
*   **Gestures**: Detect shake or tap to trigger sounds.

---

[Content continues with Projects 0426-0430... saved to separate file due to length]
