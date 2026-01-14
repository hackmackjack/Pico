import os

def rebuild_project_0501():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    # 1. Define the Perfect Content for Project 0501
    # Note: Using 2 spaces for list indentation to prevent 'code block' rendering in some editors.
    new_content = """#  Pico 2500: Documentation (Projects 0501-0600)

---

#  Batch 51: Digital Art 3

## 1. Project 0501: Introduction to Digital Art

### 2. Learning Objective
Create a visual strobe effect by flashing White light (Red + Green + Blue) for 0.05 seconds and turning it off for 0.1 seconds to understand rapid switching and the Persistence of Vision.

### 3. Concepts Introduced
*   Strobe Effect (Persistence of Vision)
*   RGB Color Mixing (White = R+G+B)
*   Precise Millisecond Timing
*   Simultaneous Pin Control

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED (Common Cathode)
*   3x 220Ω Resistors
*   Jumper Wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red Anode** | GP16 | via 220Ω Resistor |
| **Green Anode** | GP17 | via 220Ω Resistor |
| **Blue Anode** | GP18 | via 220Ω Resistor |
| **Cathode** | GND | Ground |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_write`** (Set pin state)
*   **from Loops, drag `pico_forever`** (Repeat logic)
*   **from Time, drag `pico_wait`** (Control duration)

### 7. Variables
*   **None**: Direct pin control project.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Output**:
  *   From **Smart IO**, drag `pico_gpio_write` blocks for GP16, GP17, and GP18.
  *   **Snap** into `start` block.
  *   Set all to **LOW**.

**B. Main Loop Phase**
1.  **Create Loop**:
  *   From **Loops**, drag `pico_forever`.
  *   **Snap** below initialization.
2.  **Turn ON (White)**:
  *   From **Smart IO**, drag `pico_gpio_write` (GP16, 17, 18).
  *   **Snap** into loop.
  *   Set all to **HIGH**.
3.  **Hold Flash**:
  *   From **Time**, drag `pico_wait`.
  *   **Snap** below writes.
  *   Set value to 0.05 seconds.
4.  **Turn OFF**:
  *   From **Smart IO**, drag `pico_gpio_write` (GP16, 17, 18).
  *   **Snap** below wait.
  *   Set all to **LOW**.
5.  **Hold Darkness**:
  *   From **Time**, drag `pico_wait`.
  *   **Snap** below writes.
  *   Set value to 0.1 seconds.

### 9. Execution Flow
1.  **Start**: The Pico configures pins 16, 17, and 18 as digital outputs.
2.  **Output**: All three channels turn on simultaneously, producing White light.
3.  **Delay**: The system pauses for 50ms, allowing the eye to register the flash.
4.  **Output**: All channels turn off.
5.  **Delay**: System pauses for 100ms for contrast.
6.  **Repeat**: The process repeats, creating a high-speed strobe effect.

### 10. Generated Code
```python
import machine, time
r = machine.Pin(16, machine.Pin.OUT)
g = machine.Pin(17, machine.Pin.OUT)
b = machine.Pin(18, machine.Pin.OUT)

while True:
    # White
    r.on(); g.on(); b.on()
    time.sleep(0.05)
    # Off
    r.off(); g.off(); b.off()
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Missing Resistors**: Connecting LEDs directly to 3.3V can burn them out.
*   **Photosensitivity**: This project creates flashing lights—avoid if sensitive.

### 12. Try This Next
*   **Color Chaser**: Strobe only Red, then only Green, then only Blue.

---
"""

    # 2. Read existing file
    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 3. Find boundaries to replace
    # We want to replace everything from the start of the file up to "## 2. Project 0502"
    # Or more specifically, from "#  Batch 51" down to the start of 0502.
    # But since 0501 is the FIRST project, we can just find where 0502 starts.
    
    splitter = "## 2. Project 0502: Blinking Digital Art"
    
    parts = content.split(splitter)
    
    if len(parts) < 2:
        print("Error: Could not find Project 0502 boundary.")
        return

    # 4. Construct final content
    # parts[0] is the old 0501. We replace it with new_content.
    # We need to make sure we don't duplicate the file header if it's already in new_content.
    # new_content includes formatting from Line 1.
    
    final_data = new_content + "\n" + splitter + parts[1]
    
    # 5. Write back
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(final_data)
    
    print("Successfully rebuilt Project 0501.")

if __name__ == "__main__":
    rebuild_project_0501()
