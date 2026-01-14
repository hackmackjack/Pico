# Complete Batch 32: Projects 0318-0320

batch_32_final = '''
## 1️⃣ Project 0318: The Animation Game

### 2️⃣ Learning Objective
Create a simple side-scrolling obstacle avoidance game with jump mechanics. You will learn basic game physics by implementing vertical movement (jumping) and horizontal scrolling for an interactive Dino Run-style game.

### 3️⃣ Concepts Introduced
*   **Game Loop**: Continuous update-draw-check cycle.
*   **Jump Arc**: Simulating gravity with upward then downward motion.
*   **Collision Detection**: Checking if character and obstacle overlap.
*   **Scrolling**: Moving obstacles from right to left to simulate character movement.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button** (Jump control)
*   **OLED Display** (SSD1306, 128×64, I2C)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Jump Button** | GP10 | Enable PULL_DOWN |
| **OLED SDA** | GP0 (I2C0 SDA) | I2C Data |
| **OLED SCL** | GP1 (I2C0 SCL) | I2C Clock |

### 6️⃣ Blocks Used

🔹 **Setup Button**
*   **Category:** Inputs
*   **Block:** `Setup Button pin:[10]`

🔹 **OLED Shapes**
*   **Category:** Displays
*   **Block:** `OLED rect`, `OLED fill_rect`

🔹 **Logic Blocks**
*   **Category:** Logic
*   **Block:** `if [collision detected] then`

### 7️⃣ Variables & State
*   **charY**: Character Y position (starts at 50, ground level).
*   **jumpVelocity**: Vertical velocity during jump (0 when grounded, negative when jumping).
*   **obstacleX**: Obstacle X position (moves from 128 to -10).
*   **isJumping**: Boolean indicating if character is in air.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Displays**, drag `Setup OLED I2C:[0] width:[128] height:[64]`.
        *   **Snap** into setup block.
    *   From **Inputs**, drag `Setup Button pin:[10]`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [charY] to [50]`, `set [obstacleX] to [128]`, `set [jumpVelocity] to [0]`, `set [isJumping] to [false]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Check Jump Button**:
        *   From **Logic**, drag `if [Button Pressed] and [not isJumping] then`.
            *   **Snap** into loop.
            *   Then: `set [jumpVelocity] to [-4]`, `set [isJumping] to [true]`.
    *   **Apply Gravity & Update Position**:
        *   From **Variables**, drag `change [jumpVelocity] by [0.5]` (gravity acceleration).
            *   **Snap** below.
        *   From **Variables**, drag `change [charY] by [jumpVelocity]`.
            *   **Snap** below.
        *   From **Logic**, drag `if [charY] >= [50] then`.
            *   **Snap** below (landed on ground).
            *   Then: `set [charY] to [50]`, `set [jumpVelocity] to [0]`, `set [isJumping] to [false]`.
    *   **Move Obstacle**:
        *   From **Variables**, drag `change [obstacleX] by [-3]`.
            *   **Snap** below.
        *   From **Logic**, drag `if [obstacleX] < [-10] then set [obstacleX] to [128]`.
            *   **Snap** below (respawn obstacle).
    *   **Check Collision**:
        *   From **Logic**, drag `if [obstacleX] < [20] and [obstacleX] > [5] and [charY] > [45] then`.
            *   **Snap** below (simple collision check).
            *   Then: Flash screen or show "HIT!" text (game over logic).
    *   **Draw Everything**:
        *   From **Displays**, drag `OLED clear`.
            *   **Snap** below.
        *   Draw ground line.
        *   Draw character: `OLED fill_rect x:[10] y:[charY] w:[10] h:[10]`.
        *   Draw obstacle: `OLED fill_rect x:[obstacleX] y:[45] w:[10] h:[15]`.
        *   From **Displays**, drag `OLED show`.
            *   **Snap** below.
    *   From **Timing**, drag `sleep [0.05] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The character (10×10 pixel square) starts at ground level (Y=50). When the jump button is pressed and character is grounded, jumpVelocity is set to -4 (upward). Each loop, gravity (+0.5) is added to jumpVelocity, and jumpVelocity is added to charY, creating a parabolic arc. When charY reaches 50 again, the character lands and isJumping resets to false. Meanwhile, an obstacle (10×15 pixel rectangle) scrolls from right (X=128) to left (X=-10) at 3 pixels per frame. If the obstacle overlaps the character's position range when the character is near ground level, a collision is detected. This creates the core mechanic of Chrome's Dino game: time your jump to avoid obstacles.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
oled = SSD1306_I2C(128, 64, i2c)

btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)

charY = 50
jumpVelocity = 0
obstacleX = 128
isJumping = False

while True:
    # Jump logic
    if btn.value() and not isJumping:
        jumpVelocity = -4
        isJumping = True
    
    # Apply gravity
    jumpVelocity += 0.5
    charY += jumpVelocity
    
    # Land on ground
    if charY >= 50:
        charY = 50
        jumpVelocity = 0
        isJumping = False
    
    # Move obstacle
    obstacleX -= 3
    if obstacleX < -10:
        obstacleX = 128
    
    # Collision detection
    if 5 < obstacleX < 20 and charY > 45:
        # Game over - flash or reset
        oled.fill(1)
        oled.show()
        time.sleep(0.2)
    
    # Draw
    oled.fill(0)
    oled.hline(0, 60, 128, 1)  # Ground
    oled.fill_rect(10, int(charY), 10, 10, 1)  # Character
    oled.fill_rect(int(obstacleX), 45, 10, 15, 1)  # Obstacle
    oled.show()
    
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Character Falls Through Ground**: If charY exceeds 50 and doesn't land, ensure the `if charY >= 50` check sets charY exactly to 50, not just stops momentum.
*   **No Jump Arc**: If jump goes straight up and down without curve, verify gravity (+0.5) is added to velocity each frame, not just once.
*   **Collision Always Triggers**: If game over happens constantly, check collision bounds are correct: character at X=10, width 10, so check if obstacle is between X=5 and X=20.
*   **Obstacle Too Fast**: If obstacle scrolls too quickly, reduce the X decrement from -3 to -2 or -1.

### 1️⃣2️⃣ Try This Next

*   **Score Counter**: Count how many obstacles successfully passed and display score.
*   **Variable Speed**: Increase obstacle speed over time to make game progressively harder.
*   **Multiple Obstacles**: Add 2-3 obstacles at different X positions for more challenge.

---

## 1️⃣ Project 0319: Automated Animation

### 2️⃣ Learning Objective
Create a live scrolling graph that plots light sensor readings in real-time. You will learn data visualization techniques by implementing a time-series chart that shifts old data left as new data arrives.

### 3️⃣ Concepts Introduced
*   **Scrolling Graph**: Shifting pixel data horizontally to create time-based visualization.
*   **Data Mapping**: Converting sensor values (0-65535) to pixel heights (0-64).
*   **Circular Buffer**: Conceptually replacing oldest data with newest.
*   **Real-Time Visualization**: Displaying live sensor data graphically.

### 4️⃣ Hardware Required
*   **Pico**
*   **LDR (Light Dependent Resistor)** or light sensor
*   **OLED Display** (SSD1306, 128×64, I2C)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LDR/Light Sensor** | GP26 (ADC0) | Via voltage divider with 10kΩ resistor |
| **OLED SDA** | GP0 (I2C0 SDA) | I2C Data |
| **OLED SCL** | GP1 (I2C0 SCL) | I2C Clock |

### 6️⃣ Blocks Used

🔹 **Setup ADC**
*   **Category:** Inputs
*   **Block:** `Setup ADC pin:[26]`

🔹 **Read Analog**
*   **Category:** Pin Access
*   **Block:** `read Analog pin [26]`

🔹 **Map Range**
*   **Category:** Math
*   **Block:** `map [value] from [0]-[65535] to [0]-[64]`

🔹 **OLED Pixel**
*   **Category:** Displays
*   **Block:** `OLED pixel x:[X] y:[Y] color:[1]`

🔹 **OLED Scroll**
*   **Category:** Displays
*   **Block:** `OLED scroll left [1] pixels`

### 7️⃣ Variables & State
*   **lightValue**: Raw ADC reading from sensor.
*   **pixelHeight**: Mapped Y-coordinate for current reading.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Displays**, drag `Setup OLED I2C:[0] width:[128] height:[64]`.
        *   **Snap** into setup block.
    *   From **Inputs**, drag `Setup ADC pin:[26]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Read & Map Sensor**:
        *   From **Variables**, drag `set [lightValue] to`.
            *   **Snap** into loop.
            *   From **Pin Access**, drag `read Analog pin [26]`.
                *   **Snap** into value socket.
        *   From **Variables**, drag `set [pixelHeight] to`.
            *   **Snap** below.
            *   From **Math**, drag `map [lightValue] from [0]-[65535] to [0]-[64]`.
                *   **Snap** into value socket.
    *   **Shift Graph Left**:
        *   From **Displays**, drag `OLED scroll left [1] pixels`.
            *   **Snap** below (shifts entire screen left by 1 pixel).
    *   **Draw New Data Point**:
        *   From **Displays**, drag `OLED vline x:[127] y:[0] h:[64] color:[0]`.
            *   **Snap** below (clear rightmost column).
        *   From **Displays**, drag `OLED pixel x:[127] y:[pixelHeight] color:[1]`.
            *   **Snap** below (draw new data point at right edge).
    *   From **Displays**, drag `OLED show`.
        *   **Snap** below.
    *   From **Timing**, drag `sleep [0.1] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The Pico reads the light sensor ADC value and maps it to a pixel Y-coordinate (0-64). It then scrolls the entire OLED display content 1 pixel to the left, making space at the right edge. The rightmost column is cleared to black, then a white pixel is drawn at (127, pixelHeight) representing the current sensor reading. This process repeats every 0.1 seconds, creating a scrolling time-series chart where the X-axis represents time (oldest data on left, newest on right) and Y-axis represents light intensity. The effect is similar to an oscilloscope or heart rate monitor display.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
oled = SSD1306_I2C(128, 64, i2c)

ldr = machine.ADC(26)

def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    # Read and map sensor
    lightValue = ldr.read_u16()
    pixelHeight = map_range(lightValue, 0, 65535, 63, 0)  # Invert Y (0=top)
    
    # Scroll display left
    oled.scroll(-1, 0)
    
    # Clear rightmost column
    for y in range(64):
        oled.pixel(127, y, 0)
    
    # Draw new data point
    oled.pixel(127, pixelHeight, 1)
    oled.show()
    
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **No Scroll Function**: Not all OLED libraries have `scroll()`. Alternative: manually copy pixel buffer left by 1 column using nested loops.
*   **Y-Axis Inverted**: If graph appears upside-down, map values from 63-0 instead of 0-63 (Y=0 is top of screen, Y=63 is bottom).
*   **Data Too Fast**: If graph updates too rapidly to read, increase sleep time to 0.5s or 1s per sample.
*   **Jagged Graph**: If readings jump erratically, add averaging: store last 5 readings and plot their average instead of raw value.

### 1️⃣2️⃣ Try This Next

*   **Multi-Variable**: Plot temperature vs time using upper half of screen and humidity using lower half.
*   **Grid Lines**: Draw horizontal reference lines at 25%, 50%, 75% height for easier reading.
*   **Value Display**: Show numeric value of current reading in top-left corner alongside the graph.

---

## 1️⃣ Project 0320: Mastering Animation

### 2️⃣ Learning Objective
Implement a particle system simulation creating a rain effect. You will learn object-oriented animation by managing multiple independent entities (raindrops) with individual positions and velocities.

### 3️⃣ Concepts Introduced
*   **Particle System**: Managing multiple animated objects simultaneously.
*   **Randomization**: Using random positions for natural appearance.
*   **Respawning**: Recycling particles when they exit screen bounds.
*   **Independent Movement**: Each particle has its own position state.

### 4️⃣ Hardware Required
*   **Pico**
*   **OLED Display** (SSD1306, 128×64, I2C)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP0 (I2C0 SDA) | I2C Data |
| **OLED SCL** | GP1 (I2C0 SCL) | I2C Clock |

### 6️⃣ Blocks Used

🔹 **Setup OLED**
*   **Category:** Displays
*   **Block:** `Setup OLED I2C:[0] width:[128] height:[64]`

🔹 **Random**
*   **Category:** Math
*   **Block:** `random [0] to [127]`

🔹 **Lists**
*   **Category:** Lists
*   **Block:** `create list with`, `item [N] of list`, `replace item [N] of list`

🔹 **OLED Pixel**
*   **Category:** Displays
*   **Block:** `OLED pixel x:[X] y:[Y] color:[1]`

### 7️⃣ Variables & State
*   **raindrops**: List of 5 [x, y] coordinate pairs.
*   **i**: Loop counter for iterating through raindrops.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Displays**, drag `Setup OLED I2C:[0] width:[128] height:[64]`.
        *   **Snap** into setup block.
    *   **Initialize Raindrops**:
        *   From **Variables**, drag `set [raindrops] to`.
            *   **Snap** into setup block.
            *   From **Lists**, drag `create list with`.
                *   Add 5 items, each a list `[random 0-127, random 0-64]`.

*   **B. Main Loop Phase**
    *   From **Displays**, drag `OLED clear`.
        *   **Snap** into loop.
    *   **Update & Draw Each Raindrop**:
        *   From **Loops**, drag `for [i] from [0] to [4]`.
            *   **Snap** below.
            *   Inside loop:
                *   Get current drop: `set [drop] to [item i of raindrops]`.
                *   Update Y: `set [dropY] to [item 2 of drop] + [1]`.
                *   Check if off-screen: `if [dropY] > [64] then`.
                    *   Then: Reset to top with new random X: `set [dropY] to [0]`, `set [dropX] to [random 0-127]`.
                *   Update list: `replace item i of raindrops with [dropX, dropY]`.
                *   Draw pixel: `OLED pixel x:[dropX] y:[dropY] color:[1]`.
    *   From **Displays**, drag `OLED show`.
        *   **Snap** below.
    *   From **Timing**, drag `sleep [0.05] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The system initializes 5 raindrops at random X positions (0-127) and random Y positions (0-64). Each loop, it clears the display, then iterates through all 5 raindrops. For each raindrop, it increments the Y position by 1 pixel (moving down). If Y exceeds 64 (bottom of screen), the raindrop "respawns" at Y=0 with a new random X position across the top. After updating position, it draws a white pixel at the raindrop's current coordinates. The 0.05s delay creates smooth downward motion. Because each raindrop has an independent Y position and respawns at different times, they create a continuous, natural-looking rain effect rather than synchronized drops.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
import random
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
oled = SSD1306_I2C(128, 64, i2c)

# Initialize 5 raindrops [x, y]
raindrops = [[random.randint(0, 127), random.randint(0, 64)] for _ in range(5)]

while True:
    oled.fill(0)
    
    for i in range(5):
        # Move raindrop down
        rain drops[i][1] += 1
        
        # Respawn at top if hit bottom
        if raindrops[i][1] > 64:
            raindrops[i][1] = 0
            raindrops[i][0] = random.randint(0, 127)
        
        # Draw raindrop
        oled.pixel(raindrops[i][0], raindrops[i][1], 1)
    
    oled.show()
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **All Drops Synchronized**: If raindrops move together as one group, ensure each drop has individual Y initialization (random 0-64, not all starting at 0).
*   **No Continuous Rain**: If rain stops after first pass, verify respawn logic resets Y to 0 and assigns new random X when Y > 64.
*   **Drops Disappear**: If drops vanish instead of respawning, check that the respawn condition triggers correctly and list is updated.
*   **Too Many/Few Drops**: Adjust the number of raindrops (5) to balance visual density vs performance. More drops = heavier rain but slower frame rate.

### 1️⃣2️⃣ Try This Next

*   **Variable Speed**: Give each raindrop a random speed (1-3 pixels per frame) instead of fixed 1 pixel.
*   **Wind Effect**: Add horizontal movement by incrementing/decrementing X as well as Y each frame.
*   **Splash Effect**: When a raindrop hits bottom, briefly draw small outward pixels to simulate splash before respawning.

---
'''

with open(r'd:\MFF\Pico\Documentation\Docs_0301_0400.md', 'a', encoding='utf-8') as f:
    f.write(batch_32_final)

print("✅ Batch 32 COMPLETE! Projects 0318-0320 appended successfully.")
print("\\n📊 Final Status:")
print("- Batch 31 (0301-0310): ✅ Complete (10/10)")
print("- Batch 32 (0311-0320): ✅ Complete (10/10)")
print("\\n🎯 Next: Batch 33 (Projects 0321-0330 - Binary Counter 2)")
