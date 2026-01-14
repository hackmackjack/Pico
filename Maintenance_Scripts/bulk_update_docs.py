
import os
import re

dir_path = r'd:\MFF\Pico\Documentation'
files = [f for f in os.listdir(dir_path) if f.startswith('Docs_') and f.endswith('.md')]

# Mapping of old/incorrect category names to new/correct ones
category_map = {
    r'\*\*Time\*\*': '**Smart IO**',
    r'\*\*Motors\*\*': '**Motion & Motors**',
    r'\*\*Sensors\*\*': '**Smart Sensors**',
    r'\*\*Display\*\*': '**Smart Display**',
    r'\*\*Network\*\*': '**Network & IoT**',
    r'\*\*System\*\*': '**System & Storage**',
    r'\*\*File\*\*': '**System & Storage**',
    r'\*\*Actuators\*\*': '**Motion & Motors**',
    r'\*\*Outputs\*\*': '**Smart IO**',
    r'\*\*Pin Access\*\*': '**Smart IO**',
    r'\*\*Timing\*\*': '**Smart IO**',
}

def fix_categories(content):
    new_content = content
    for old, new in category_map.items():
        new_content = re.sub(old, new, new_content)
    
    # Non-bolded versions
    new_content = re.sub(r'from Time', 'from Smart IO', new_content)
    new_content = re.sub(r'from Motors', 'from Motion & Motors', new_content)
    new_content = re.sub(r'from Sensors', 'from Smart Sensors', new_content)
    new_content = re.sub(r'from Display', 'from Smart Display', new_content)
    new_content = re.sub(r'from Network', 'from Network & IoT', new_content)
    new_content = re.sub(r'from System', 'from System & Storage', new_content)
    new_content = re.sub(r'from File', 'from System & Storage', new_content)
    new_content = re.sub(r'from Actuators', 'from Motion & Motors', new_content)
    new_content = re.sub(r'from Outputs', 'from Smart IO', new_content)
    new_content = re.sub(r'from Pin Access', 'from Smart IO', new_content)
    new_content = re.sub(r'from Timing', 'from Smart IO', new_content)
    
    return new_content

def fix_block_names(content):
    # pico_wait fixes
    content = re.sub(r'drag `sleep \[N\] seconds`', 'drag `pico_wait` (wait)', content)
    content = re.sub(r'drag `sleep` block', 'drag `pico_wait` (wait)', content)
    # pico_gpio_write fixes
    content = re.sub(r'drag `PWM Write pin:\[N\] freq:\[F\] duty:\[D\]`', 'drag `pico_gpio_write` (set Pin)', content)
    return content

def remove_setup_pin_and_variables(content):
    # This specifically targets the "Initialization Phase" that uses pico_setup_pin to set variables.
    # It's better to do this in two stages:
    # 1. Broad cleanup of the "Initialization Phase" sections if they contain pico_setup_pin.
    # 2. Replacing variable names (led, btn) with pin numbers in the guide.
    
    # We'll focus on the most common pattern found in the first batch first.
    
    # Pattern 1: Step-by-Step with Initialization Phase
    # This is a complex multi-line regex.
    pattern = r'\*\*A\. Initialization Phase\*\*\n1\.\s+\*\*Define Output\*\*:\n\s+\*\s+From \*\*Smart IO\*\*, drag `pico_setup_pin`\..+?GP(\d+).+?assign to variable `(\w+)`\.\n\s+\*\s+\*\*Snap\*\* into `start`\.'
    
    # Instead of deleting, it's easier to just run specific project-level fixes for the first 10 projects
    # and then use a more general cleaner for the rest if they use pico_setup_pin.
    
    # Let's do a simpler replacement for pico_setup_pin in the "Blocks Used" list.
    content = re.sub(r'\*\s+\*\*from Smart IO, drag `pico_setup_pin`\*\* \(setup Pin\)\n?', '', content)
    
    return content

for filename in files:
    file_path = os.path.join(dir_path, filename)
    print(f"Processing {filename}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = fix_categories(content)
    new_content = fix_block_names(new_content)
    new_content = remove_setup_pin_and_variables(new_content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No changes in {filename}")

print("Bulk update complete.")
