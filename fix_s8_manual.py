import re

DOC_FILE = "Documentation/Docs_0101_0200.md"

S8_0198 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Pins**:
    *   From **Variables**, create variable **`btn`**.
    *   From **Smart IO**, drag **`Pin`** block. Set to **GP14, Pull-Down** (Input).
    *   From **Variables**, create variable **`bz`**.
    *   From **Smart IO**, drag **`Pin`** block. Set to **GP15** (Output).
    *   **Snap** into `start`.

**B. Function Definition (game_round)**
2.  **Define Function**:
    *   From **Functions**, drag **`to function [game_round] do`**.
3.  **Rhythm Playback**:
    *   From **Text**, print "Listen to the rhythm...".
    *   From **Loops**, drag **`repeat [4] times`**.
    *   **Inside Loop**:
        *   Set **`bz`** to **HIGH (1)**. Wait **0.05s**.
        *   Set **`bz`** to **LOW (0)**. Wait **0.95s**.
4.  **Wait for Player**:
    *   From **Text**, print "NOW YOU! Tap on the NEXT beat!".
    *   From **Variables**, set **`perfect_time`** to (`time.ticks_ms()` + 1000).
    *   From **Loops**, drag **`while [btn] == 0`**:
        *   **Check Timeout**: If `time.ticks_ms() > (perfect_time + 1000)`:
            *   Print "TOO LATE!". **Return**.
5.  **Evaluate Tap**:
    *   From **Variables**, set **`user_time`** to `time.ticks_ms()`.
    *   From **Variables**, set **`error`** to absolute difference (`user_time` - `perfect_time`).
    *   **Feedback**:
        *   If `error` < 100: Print "EXCELLENT! Error: " + `error` + "ms".
        *   Else If `error` < 250: Print "NOT BAD. Error: " + `error` + "ms".
        *   Else: Print "OFF BEAT. Error: " + `error` + "ms".

**C. Main Loop Phase**
6.  **Start Loop**:
    *   From **Loops**, drag **`pico_forever`**.
7.  **Run Game**:
    *   From **Functions**, call **`game_round`**.
8.  **Cooldown**:
    *   From **Smart IO**, drag **`pico_wait`**. Set duration to **3** seconds."""

S8_0200 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Pins**:
    *   From **Variables**, create **`led_a`** (GP15, Output).
    *   From **Variables**, create **`led_b`** (GP14, Output).
    *   From **Variables**, set **`timer`** to **0**.
    *   **Snap** into `start`.

**B. Main Loop Phase**
2.  **Start Loop**:
    *   From **Loops**, drag **`pico_forever`**.
3.  **Check Rhythms**:
    *   From **Variables**, set **`a_hit`** to `(timer % 300 == 0)`.
    *   From **Variables**, set **`b_hit`** to `(timer % 200 == 0)`.
4.  **Update LEDs**:
    *   From **Logic**, if **`a_hit`**: Set **`led_a`** to **HIGH**.
    *   From **Logic**, if **`b_hit`**: Set **`led_b`** to **HIGH**.
5.  **Pulse Logic**:
    *   From **Logic**, if **`a_hit`** OR **`b_hit`**:
        *   **Hold**: Wait **0.05s**.
        *   **Reset**: Set **`led_a`** and **`led_b`** to **LOW**.
        *   **Advance**: Change **`timer`** by **50**.
    *   **Else (No Beat)**:
        *   **Advance**: Wait **0.01s**. Change **`timer`** by **10**.
6.  **Reset Measure**:
    *   From **Logic**, if **`timer`** >= **600**:
        *   Set **`timer`** to **0**.
        *   Print "--- Next Measure ---"."""

def manual_fix():
    with open(DOC_FILE, 'r') as f: content = f.read()

    # Fix 0198
    pattern_198 = r"(## Project 0198.*?)### 8\. Step-by-Step Guide.*?(\n\n### 9\.)"
    replacement_198 = r"\1" + S8_0198 + r"\2"
    content = re.sub(pattern_198, replacement_198, content, flags=re.DOTALL)

    # Fix 0200
    pattern_200 = r"(## Project 0200.*?)### 8\. Step-by-Step Guide.*?(\n\n### 9\.)"
    replacement_200 = r"\1" + S8_0200 + r"\2"
    content = re.sub(pattern_200, replacement_200, content, flags=re.DOTALL)

    with open(DOC_FILE, 'w') as f: f.write(content)
    print("Fixed Projects 0198 and 0200.")

if __name__ == "__main__":
    manual_fix()
