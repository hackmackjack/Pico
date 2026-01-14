import os

def inject_final():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Content to inject
    new_projects = """
---

## 9. Project 0519: Automated Animation

### 2. Learning Objective
Create a self-running "Sinewave" visualizer that plots a mathematical wave across the screen autonomously.

### 3. Concepts Introduced
*   Trigonometry (Sine/Cosine)
*   Continuous Motion
*   Automated plotting

### 4. Hardware Required
*   Pico, OLED

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

## 10. Project 0520: Mastering Animation

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
"""

    # Locate insertion point
    # Find "Project 0518"
    idx_0518 = content.find("Project 0518")
    if idx_0518 == -1:
        # Fallback: Find 0517
        idx_0518 = content.find("Project 0517")
        print("Warning: Used 0517 anchor")

    # Find the Code block for 0518/0517
    # Look for "### 10. Generated Code" after the project start
    idx_code = content.find("### 10. Generated Code", idx_0518)
    
    # Find the next header "## " after that code block
    # This denotes the start of the next project (which might be 0522 or 0523)
    idx_next = content.find("## ", idx_code + 20)
    
    if idx_next == -1:
        print("FAIL: Could not find next project header")
        return

    # Insert before idx_next
    pre = content[:idx_next]
    post = content[idx_next:]
    
    new_content = pre + new_projects + "\n" + post
    
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("Successfully injected 0519 and 0520!")

if __name__ == "__main__":
    inject_final()
