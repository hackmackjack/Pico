import os
import re

def fix_batch_59_60():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'

    # --- BATCH 59: KITCHEN TIMER 3 (0581-0590) ---

    # 0581: Intro
    g0581 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Start Print**:
  *   Print "Timer Started...".
  *   Set `ticks` = 0.

**B. Main Loop Phase**
1.  **Count Seconds**:
  *   From **Loops**, drag `pico_forever`.
  *   Change `ticks` by 1.
2.  **Format**:
  *   If (`ticks` % 10) == 0:
      *   Print " [10s Marks]".
  *   Else:
      *   Print "." (No newline).
  *   Wait 1.0s."""

    # 0582: Blinking
    g0582 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Vars**: `timer` = 15.

**B. Main Loop Phase**
1.  **Urgency Check**:
  *   If `timer` > 10: `wait` = 0.5 (Slow).
  *   Else If `timer` > 0: `wait` = 0.1 (Fast).
  *   Else: LED On (Done). Break.
2.  **Blink**:
  *   LED On. Wait `wait`.
  *   LED Off. Wait `wait`.
  *   `timer` = `timer` - (2 * wait)."""

    # 0583: Manual
    g0583 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Select**:
  *   Repeat Until Button Pressed:
      *   `m` = Map `pico_adc_read` to 1-60.
      *   Display "SET: `m` MINS".
2.  **Run**:
  *   `s` = m * 60.
  *   Repeat while `s` > 0:
      *   Display Time.
      *   Wait 1s. `s` -= 1.
  *   Display "DONE"."""

    # 0584: Sequences
    g0584 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Green (16), Blue (17).

**B. Main Loop Phase**
1.  **Pomodoro**:
  *   Repeat 4 times:
      *   **Focus**: Green On, Blue Off. Wait 1500s.
      *   **Break**: Green Off, Blue On. Wait 300s.
2.  **End**:
  *   All Off."""

    # 0585: Interactive
    g0585 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Mode**: `type` = 0.

**B. Select Phase**
1.  **Cycle**:
  *   Repeat Until Button Released.
  *   If Button Click: `type` = (`type` + 1) % 3.
  *   If 0: "Small (3m)".
  *   If 1: "Medium (4m)".
  *   If 2: "Large (5m)".
  *   Wait 0.1s."""

    # 0586: Smart Switch
    g0586 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **IO**: Lock (14), Start (15).

**B. Main Loop Phase**
1.  **Permission**:
  *   If Button (15) AND Lock (14):
      *   Print "GRANTED".
  *   Else If Button (15) AND NOT Lock (14):
      *   Print "LOCKED".
  *   Wait 0.01s."""

    # 0587: Alarm
    g0587 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Anchor**: `finish` = `pico_milliseconds`.

**B. Main Loop Phase**
1.  **Escalate**:
  *   `over` = `pico_milliseconds` - `finish`.
  *   If `over` < 10000:
      *   Beep Slow.
  *   Else If `over` < 30000:
      *   Beep Fast.
  *   Else:
      *   Beep Continuous."""

    # 0588: Game
    g0588 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Wires**: Defuse(14), Trap(15,16) PULL_UP.
2.  **State**: `time`=20, `spd`=1.0.

**B. Main Loop Phase**
1.  **Check**:
  *   If Defuse High: "WIN". Break.
  *   If Trap High: "FAIL". `spd`=0.2.
2.  **Tick**:
  *   Print `time`.
  *   Wait `spd`.
  *   `time` -= 1."""

    # 0589: Automated
    g0589 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Vars**: `deadline` = 0.

**B. Main Loop Phase**
1.  **Motion**:
  *   If PIR High:
      *   LED On.
      *   `deadline` = `now` + 10000.
2.  **Expiry**:
  *   If `now` > `deadline`:
      *   LED Off."""

    # 0590: Mastering
    g0590 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **RTC**: Set to (2025, 12, 31, 16, 59, 50).

**B. Main Loop Phase**
1.  **Watch**:
  *   Get (Hr, Min, Sec).
  *   If Hr==17 AND Min==0:
      *   Alarm On.
      *   Wait 60s (Skip minute).
  *   Wait 1s."""

    # --- BATCH 60: METRONOME 3 (0591-0600) ---

    # 0591: Intro
    g0591 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Screen**: "BPM: 60".

**B. Main Loop Phase**
1.  **Pulse**:
  *   Invert Screen (White).
  *   Wait 0.05s.
  *   Invert Screen (Black).
  *   Wait 0.95s."""

    # 0592: Blinking
    g0592 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Count-In**:
  *   Repeat 4 times:
      *   Flash LED (Silent).
      *   Wait 1s.

**B. Main Loop Phase**
1.  **Live**:
  *   LED On.
  *   Click Buzzer.
  *   Wait 1s interval."""

    # 0593: Manual
    g0593 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Tap Detect**:
  *   Wait for Tap 1 -> `t1`.
  *   Wait for Tap 2 -> `t2`.
  *   `gap` = t2 - t1.

**B. Main Loop Phase**
1.  **Playback**:
  *   Click Buzzer.
  *   Wait `gap` seconds."""

    # 0594: Sequences
    g0594 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Pattern**: List [0.4, 0.4, 0.4, 0.2, 0.4].

**B. Main Loop Phase**
1.  **Groove**:
  *   For each `item` in List:
      *   Click Buzzer.
      *   Wait `item` seconds."""

    # 0595: Interactive
    g0595 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Beat**: 1.

**B. Main Loop Phase**
1.  **Accent**:
  *   If `beat` == 1 AND Btn A: Tone = Loud.
  *   Else: Tone = Normal.
2.  **Triplet**:
  *   If Btn B: Play 3 clicks in 1s.
  *   Else: Play 1 click in 1s.
3.  **Count**:
  *   `beat` = `beat` + 1 (Mod 4)."""

    # 0596: Smart Switch
    g0596 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Pins**: Switch(14), Audio(15), Haptic(16).

**B. Main Loop Phase**
1.  **Route**:
  *   If Switch On (Silent):
      *   Pulse Haptic.
  *   Else:
      *   Pulse Audio.
  *   Wait 1s."""

    # 0597: Alarm
    g0597 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Mic**: GP26.

**B. Main Loop Phase**
1.  **Level**:
  *   Scan 100 samples -> Find Max.
2.  **Threshold**:
  *   If Max > 40000:
      *   Flash Red LED. "Too Loud".
  *   else:
      *   LED Off."""

    # 0598: Game
    g0598 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Sync**: `start` = `now`.

**B. Main Loop Phase**
1.  **Polyrhythm**:
  *   `t` = `now` - `start`.
  *   If (`t` % 400) == 0: Click B1 (3/4 time).
  *   If (`t` % 300) == 0: Click B2 (4/4 time).
  *   If `t` > 1200: Reset `start`."""

    # 0599: Automated
    g0599 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Tempo**: `gap` = 1.0s.

**B. Main Loop Phase**
1.  **Accelerate**:
  *   Repeat 4 times (Bar):
      *   Click. Wait `gap`.
  *   `gap` = `gap` * 0.95 (Speed up 5%).
  *   Print "FASTER..."."""

    # 0600: Mastering
    g0600 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **UI**: Draw Metronome arm.

**B. Main Loop Phase**
1.  **Swing**:
  *   `angle` = sin(`now` * speed) * 45.
  *   Draw Line from Center at `angle`.
  *   If `angle` crosses 0: Click Buzzer.
  *   Refresh OLED."""

    replacements = {
        "0581": g0581, "0582": g0582, "0583": g0583, "0584": g0584, "0585": g0585,
        "0586": g0586, "0587": g0587, "0588": g0588, "0589": g0589, "0590": g0590,
        "0591": g0591, "0592": g0592, "0593": g0593, "0594": g0594, "0595": g0595,
        "0596": g0596, "0597": g0597, "0598": g0598, "0599": g0599, "0600": g0600
    }

    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for pid, new_text in replacements.items():
        pattern = rf"(## \d+\. Project {pid}.*?)(### 8\. Step-by-Step Guide.*?)(### 9\. Execution Flow)"
        match = re.search(pattern, content, re.DOTALL)
        if match:
            full_match = match.group(0)
            header = match.group(1)
            footer = match.group(3)
            new_block = header + new_text + "\n\n" + footer
            content = content.replace(full_match, new_block)
        else:
            print(f"Project {pid} Not Found for Regex")

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Fixed Batches 59 & 60 (0581-0600).")

if __name__ == "__main__":
    fix_batch_59_60()
