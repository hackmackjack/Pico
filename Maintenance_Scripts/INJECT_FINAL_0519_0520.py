import os

def inject_missing():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define 0519 and 0520 content
    c0519 = """## 9. Project 0519: Automated Animation

### 2. Learning Objective
Create a self-running "Sinewave" visualizer that plots a mathematical wave across the screen autonomously.

### 3. Concepts Introduced
*   Trigonometry (Sine/Cosine)
*   Continuous Motion
*   Automated plotting

### 4. Hardware Required
*   Pico, OLED

### 6. Blocks Used
*   Trig (sin)
*   Loops

### 7. Variables
*   **angle**: number

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Sine**: `angle`=0.

**B. Main Loop Phase**
1.  **Wave**:
  *   From **Loops**, drag `pico_forever`.
  *   Calc `y` = 32 + sin(`angle`)*30.
  *   **Snap** into loop.
  *   Pixel (64, `y`).
  *   Show. Change `angle`.

### 9. Execution Flow
1.  Oscillates endlessly.

### 10. Generated Code
```python
# Sine wave
```
---
"""

    c0520 = """## 10. Project 0520: Mastering Animation

### 2. Learning Objective
Build a "Starfield Warp" effect where stars move from the center outward to create a 3D travel illusion.

### 3. Concepts Introduced
*   3D Projection
*   Array Management
*   Z-Depth

### 4. Hardware Required
*   Pico, OLED

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Starfield**: List of STARS.

**B. Main Loop Phase**
1.  **Warp**:
  *   From **Loops**, drag `pico_forever`.
  *   For each Star:
      *   Move X back. Move Y out.
      *   If Offscreen: Reset to center.
      *   Pixel(X,Y).
  *   **Snap** into loop.
  *   Show.

### 9. Execution Flow
1.  Stars fly out.

### 10. Generated Code
```python
# Starfield
```
---
"""

    # Locate Project 0518
    # We want to insert AFTER Project 0518's block.
    # Before "Project 0522" (since 0521 might be missing too? No, 0521 passed audit so it's there).
    # Wait, previous view showed 0518 then 0522 data.
    
    idx_0518 = content.find("Project 0518")
    if idx_0518 == -1:
        print("FAIL: Could not find Project 0518")
        return

    # Find the next separator "---" after 0518
    idx_sep = content.find("\n---\n", idx_0518)
    if idx_sep == -1:
        print("FAIL: Could not find end of Project 0518")
        return
        
    # Valid injection point: idx_sep + 5 (after ---\n)
    insert_point = idx_sep + 6 # After ---\n\n
    
    pre = content[:insert_point]
    post = content[insert_point:]
    
    new_content = pre + c0519 + "\n" + c0520 + "\n" + post
    
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Injected Projects 0519 and 0520.")

if __name__ == "__main__":
    inject_missing()
