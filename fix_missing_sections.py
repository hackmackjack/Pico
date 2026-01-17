import re

DOC_FILE = "Documentation/Docs_0101_0200.md"

CODE_0161 = """### 9. Execution Flow
1.  **Start**: Initialize OLED.
2.  **Draw**: Triangle.
3.  **Wait**: 1s.
4.  **Draw**: Circle.
5.  **Wait**: 1s.
6.  **Draw**: Rectangle.
7.  **Loop**: Repeat sequence.

### 10. Generated Code
```python
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

while True:
    # Triangle
    oled.fill(0)
    oled.line(64, 10, 34, 54, 1)
    oled.line(34, 54, 94, 54, 1)
    oled.line(94, 54, 64, 10, 1)
    oled.show()
    time.sleep(1)

    # Circle
    oled.fill(0)
    oled.circle(64, 32, 25, 1)
    oled.show()
    time.sleep(1)

    # Rect
    oled.fill(0)
    oled.rect(39, 7, 50, 50, 1)
    oled.show()
    time.sleep(1)
```"""

CODE_0162 = """### 9. Execution Flow
1.  **Start**: Initialize OLED.
2.  **Fill**: Draw filled rectangle.
3.  **Outline**: Draw outline rectangle.
4.  **Loop**: Blink between filled and empty.

### 10. Generated Code
```python
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

while True:
    # Filled
    oled.fill(0)
    oled.fill_rect(10, 10, 100, 40, 1)
    oled.show()
    time.sleep(1)

    # Outline
    oled.fill(0)
    oled.rect(10, 10, 100, 40, 1)
    oled.show()
    time.sleep(1)
```"""

CODE_0163 = """### 9. Execution Flow
1.  **Start**: Init X to 0.
2.  **Loop**: Increment X.
3.  **Draw**: Circle at (X, 32).
4.  **Wrap**: If X > 128, X = 0.

### 10. Generated Code
```python
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

x_pos = 0

while True:
    x_pos += 2
    if x_pos > 128:
        x_pos = 0

    oled.fill(0)
    oled.circle(x_pos, 32, 10, 1)
    oled.show()
    time.sleep(0.05)
```"""

def fix_project(content, pid, code_block):
    # Find end of S8 (before S11)
    # Pattern: End of S8 content... \n\n### 11.

    pattern = rf"(## Project {pid}.*?### 8\. Step-by-Step Guide.*?)\n+(### 11\.)"
    match = re.search(pattern, content, re.DOTALL)

    if match:
        print(f"Fixing {pid}...")
        return content.replace(match.group(0), match.group(1) + "\n\n" + code_block + "\n\n" + match.group(2))
    else:
        print(f"Could not find insertion point for {pid}")
        return content

def main():
    with open(DOC_FILE, 'r') as f: content = f.read()

    content = fix_project(content, "0161", CODE_0161)
    content = fix_project(content, "0162", CODE_0162)
    content = fix_project(content, "0163", CODE_0163)

    with open(DOC_FILE, 'w') as f: f.write(content)
    print("Missing sections injected.")

if __name__ == "__main__":
    main()
