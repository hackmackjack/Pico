
import os
import re

dir_path = r'd:\MFF\Pico\Documentation'
files = [f for f in os.listdir(dir_path) if f.startswith('Docs_') and f.endswith('.md')]

# Mapping of old/incorrect category names to new/correct ones
category_map = {
    r'Outputs': 'Smart IO',
    r'Pin Access': 'Smart IO',
    r'Timing': 'Smart IO',
    r'Sensors': 'Smart Sensors',
    r'Motors': 'Motion & Motors',
    r'Actuators': 'Motion & Motors',
    r'Display': 'Smart Display',
    r'Network': 'Network & IoT',
    r'System': 'System & Storage',
    r'File': 'System & Storage',
    r'Time': 'Smart IO',
}

# Mapping of block descriptions/names to the actual Blockly V2 block names
block_map = {
    r'Setup PWM pin:\[N\]': 'pico_pwm',
    r'PWM Write pin:\[N\] freq:\[F\] duty:\[D\]': 'pico_pwm',
    r'sleep \[N\] seconds': 'pico_wait',
    r'Setup ADC pin:\[\d+/ \d+/ \d+\]': 'pico_sensor_read',
    r'read Analog pin \[N\]': 'pico_sensor_read',
    r'Setup Temperature Sensor pin:\[\d+\]': 'pico_sensor_read',
    r'read temperature sensor pin:\[\d+\]': 'pico_sensor_read',
}

def deep_fix(content):
    new_content = content
    
    # 1. Fix Category: Output/Timing/Sensors lines
    for old, new in category_map.items():
        # Specifically match "* **Category:** " pattern
        new_content = re.sub(fr'\*   \*\*Category:\*\* {old}', f'*   **Category:** {new}', new_content)
        # Match "From **Category**," pattern
        new_content = re.sub(fr'From \*\*{old}\*\*,', f'From **{new}**,', new_content)
        # Match "**from Category, drag...**" pattern
        new_content = re.sub(fr'\*\*from {old}, drag', f'**from {new}, drag', new_content)

    # 2. Fix block names in description
    for old, new in block_map.items():
        new_content = re.sub(old, f'`{new}`', new_content)
    
    # 3. Structural: Remove redundant Initialization Phases for simple GPIO/PWM
    # This pattern matches "Initialization Phase" followed by "Configure Outputs" using old setup blocks.
    # We'll just target the block names directly to make them more accurate.
    
    # 4. Global replacements for common non-macho terms
    new_content = re.sub(r'drag `Setup PWM pin:\[N\]`', 'drag `pico_pwm` (PWM)', new_content)
    new_content = re.sub(r'drag `PWM Write pin:\[N\]`', 'drag `pico_pwm` (PWM)', new_content)
    new_content = re.sub(r'drag `read Analog pin \[N\]`', 'drag `pico_sensor_read` (Analog)', new_content)
    
    return new_content

for filename in files:
    file_path = os.path.join(dir_path, filename)
    print(f"Processing {filename}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = deep_fix(content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Deep Updated {filename}")
    else:
        print(f"No changes in {filename}")

print("Deep update complete.")
