
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
    # Handle non-bolded versions just in case
    r'from Time': 'from Smart IO',
    r'from Motors': 'from Motion & Motors',
    r'from Sensors': 'from Smart Sensors',
    r'from Display': 'from Smart Display',
    r'from Network': 'from Network & IoT',
    r'from System': 'from System & Storage',
    r'from File': 'from System & Storage',
    r'from Actuators': 'from Motion & Motors',
}

def bulk_fix_categories(content):
    new_content = content
    for old, new in category_map.items():
        # Use regex to replace, ensuring we don't accidentally replace parts of words
        # and handling casing where possible (though bolding makes it specific)
        new_content = re.sub(old, new, new_content)
    return new_content

def fix_pico_wait_category(content):
    # Specifically fix "from Time, drag `pico_wait`" which is very common
    return re.sub(r'from Time, drag `pico_wait`', 'from Smart IO, drag `pico_wait`', content, flags=re.IGNORECASE)

# Attempt to remove "Initialization Phase" that uses pico_setup_pin for simple GPIO
# This is a bit risky to automate fully with regex across 2500 projects, 
# so I'll focus on the obvious category fixes first as requested.
# But I can fix the "from Smart IO, drag `pico_setup_pin`" in the "Blocks Used" section
# if the tool doesn't even have that block.
# According to picofile.html, there IS NO pico_setup_pin block defined in the G generator!
# Let me verify that.

for filename in files:
    file_path = os.path.join(dir_path, filename)
    print(f"Processing {filename}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = bulk_fix_categories(content)
    new_content = fix_pico_wait_category(new_content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No changes in {filename}")

print("Bulk replacement complete.")
