def restore_0501():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    # 1. content to restore (Header + Project 0501)
    # Using strict 2-space indentation for lists as requested previously.
    restored_block = """#  Batch 51: Digital Art 3

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

    with open(target_path, 'r', encoding='utf-8') as f:
        existing_content = f.read()

    # Splitter is "## 2. Project 0502"
    splitter = "## 2. Project 0502"
    if splitter not in existing_content:
        print("Could not find Project 0502 to insert before.")
        return

    parts = existing_content.split(splitter)
    
    # Reassemble: File Header -> New 0501 -> Old 0502...
    # The file header is currently:
    # #  Pico 2500: Documentation (Projects 0501-0600)
    # 
    #     ---
    #
    
    # We want to insert AFTER the "---" line preferably, or just replace the beginning up to 0502.
    # Looking at the file dump:
    # Line 1: # Pico 2500...
    # Line 3: ---
    # Line 7: ## 2. Project 0502...
    
    # It seems the previous tool left an indentation on the separator line '    ---'.
    # I should clean that up too.
    
    header = "#  Pico 2500: Documentation (Projects 0501-0600)\n\n---\n\n"
    
    # parts[1] is everything starting from ": Blinking Digital Art..." (because split eats the delimiter)
    # Wait, split(DELIM) -> [Pre, Post]. Pre contains header. Post contains rest.
    
    final_content = header + restored_block + splitter + parts[1]
    
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
        
    print("Restored Project 0501.")

if __name__ == "__main__":
    restore_0501()
