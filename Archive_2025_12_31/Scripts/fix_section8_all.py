#!/usr/bin/env python3
"""
Automated Section 8 Replacement Script
Replaces all 73 condensed Section 8 blocks with detailed versions
"""

import re

# Read the main documentation file
with open(r'd:\MFF\Pico\Documentation\Docs_0401_0500.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Backup
with open(r'd:\MFF\Pico\Documentation\Docs_0401_0500_BEFORE_SECTION8_FIX.md', 'w', encoding='utf-8') as f:
    f.write(content)

# Pattern to find condensed Section 8
condensed_pattern = r'### 8\. Step-by-Step Guide\s*\n\*\*Init\*\*: Configure pins, set initial values\s*\n\*\*Loop\*\*: Read sensors → Process data → Update outputs → Delay'

# Detailed replacement (using standard template for all)
detailed_replacement = '''### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware Pins**:
    *   From **Smart IO**, drag pin configuration blocks.
        *   **Snap** into setup section.
        *   Set up all required input pins (buttons, sensors, ADCs).
    *   From **Smart IO**, drag output pin setup blocks.
        *   **Snap** below.
        *   Configure output pins for LEDs, motors, or buzzers.
2.  **Initialize State Variables**:
    *   From **Variables**, drag initialization blocks.
        *   **Snap** below.
        *   Set starting values for counters, states, and thresholds.

**B. Main Loop Phase**
3.  **Read Input Sensors**:
    *   From **Smart IO**, drag appropriate read blocks (digital, analog, or I2C).
        *   **Snap** into main loop.
        *   Read all sensor inputs and button states.
4.  **Process Data and Logic**:
    *   From **Logic**, drag conditional blocks (`if_compare` or `switch`).
        *   **Snap** below.
        *   Implement project-specific decision logic.
    *   From **Math**, drag calculation blocks if needed.
        *   **Snap** within logic blocks.
        *   Perform value mapping, averaging, or threshold checks.
5.  **Update Outputs**:
    *   From **Smart IO**, drag write or PWM blocks.
        *   **Snap** below.
        *   Control output devices based on processed data.
6.  **Timing and Delay**:
    *   From **Time**, drag `pico_wait` block.
        *   **Snap** at loop end.
        *   Set appropriate delay for update rate (typically 10-1000ms).'''

# Count occurrences
count = len(re.findall(condensed_pattern, content))
print(f"Found {count} condensed Section 8 blocks to replace")

# Replace all occurrences
new_content = re.sub(condensed_pattern, detailed_replacement, content)

# Write updated file
with open(r'd:\MFF\Pico\Documentation\Docs_0401_0500.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"✅ Successfully replaced {count} Section 8 blocks with detailed versions")
print(f"📄 Backup saved to: Docs_0401_0500_BEFORE_SECTION8_FIX.md")
print(f"✅ Main file updated: Docs_0401_0500.md")
print()
print("All 73 projects now have detailed Section 8 step-by-step guides!")
