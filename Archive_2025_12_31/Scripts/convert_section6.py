#!/usr/bin/env python3
"""
Elite Standard Section 6 Template Converter
Uses templates to convert common block patterns to Elite Standard format
"""

import re

# Block mapping templates - common patterns to Elite Standard format
BLOCK_TEMPLATES = {
    # Pin Access / Smart IO
    "Digital Read": "*   **from Smart IO, drag `pico_gpio_read`** (read digital pin state)",
    "Digital Write": "*   **from Smart IO, drag `pico_gpio_write`** (set digital pin HIGH/LOW)",
    "Digital Read (×2)": "*   **from Smart IO, drag `pico_gpio_read`** (read multiple button states)",
    "Digital Read (×3)": "*   **from Smart IO, drag `pico_gpio_read`** (read multiple button states)",
    "Digital Write (×2)": "*   **from Smart IO, drag `pico_gpio_write`** (control multiple LEDs)",
    "Digital Write (×4)": "*   **from Smart IO, drag `pico_gpio_write`** (control multiple outputs)",
    "Digital Write (×5)": "*   **from Smart IO, drag `pico_gpio_write`** (control multiple outputs)",
    "Digital Write (×8)": "*   **from Smart IO, drag `pico_gpio_write`** (control LED array)",
    "Read Analog Pin": "*   **from Smart IO, drag `pico_analog_read`** (read ADC value)",
    "PWM Control": "*   **from Smart IO, drag `pico_pwm_write`** (set PWM duty cycle)",
    "PWM Duty Cycle": "*   **from Smart IO, drag `pico_pwm_write`** (set PWM duty cycle)",
    "Digital Read/Write": "*   **from Smart IO, drag `pico_gpio_read`** (read inputs)\n*   **from Smart IO, drag `pico_gpio_write`** (write outputs)",
    "Pin Mode Control": "*   **from Smart IO, drag `pico_pin_mode`** (configure pin as INPUT/OUTPUT)",
    "LED Control": "*   **from Smart IO, drag `pico_gpio_write`** (control LED state)",
    
    # Logic
    "Logic NOT": "*   **from Logic, drag `not_operator`** (invert boolean value)",
    "Logic OR": "*   **from Logic, drag `or_operator`** (A OR B logic gate)",
    "Logic AND": "*   **from Logic, drag `and_operator`** (A AND B logic gate)",
    "Logic XOR": "*   **from Logic, drag `xor_operator`** (exclusive OR logic)",
    "List Comparison": "*   **from Logic, drag `list_equals`** (compare two lists)",
    "Edge Detection": "*   **from Logic, drag `if_compare`** (detect rising/falling edge)",
    
    # Timing
    "Sleep": "*   **from Time, drag `pico_wait`** (delay/pause execution)",
    "Time Tracking": "*   **from Time, drag `time_ticks_ms`** (get current timestamp)",
    "Timestamp Logic": "*   **from Time, drag `time_ticks_ms`** (track elapsed time)",
    "Variable Sleep": "*   **from Time, drag `pico_wait`** (dynamic delay based on variable)",
    
    # Loops
    "Repeat Loop": "*   **from Loops, drag `pico_repeat`** (repeat N times)",
    "For Loop": "*   **from Loops, drag `for_in_range`** (iterate over range)",
    "Forever Loop": "*   **from Loops, drag `pico_forever`** (infinite loop)",
    
    # Variables
    "Toggle Variable": "*   **from Variables, drag `set_variable`** (toggle boolean state)",
    "State Variable": "*   **from Variables, drag `set_variable`** (track system state)",
    "State Variables": "*   **from Variables, drag `set_variable`** (track multiple states)",
    "Counter Variables": "*   **from Variables, drag `set_variable`** (count events)",
    "Score Tracking": "*   **from Variables, drag `set_variable`** (track game score)",
    "List Append": "*   **from Variables, drag `list_append`** (add item to list)",
    "Sequence List": "*   **from Variables, drag `create_list`** (store sequence pattern)",
    
    # Math
    "Random Number": "*   **from Math, drag `random_int`** (generate random value)",
    "Random Choice": "*   **from Math, drag `random_choice`** (pick random item from list)",
    "Modulo Operator": "*   **from Math, drag `modulo`** (remainder operation)",
    "Map Range": "*   **from Math, drag `map_range`** (scale value from one range to another)",
    "Map Range (Inverted)": "*   **from Math, drag `map_range`** (inverse mapping)",
    
    # Actuators/Sound
    "PWM Frequency Control": "*   **from Actuators, drag `pwm_freq`** (set PWM frequency for tone)",
    "PWM Tone": "*   **from Actuators, drag `pwm_tone`** (generate audio frequency)",
    
    # Advanced
    "Interrupt Setup": "*   **from Advanced, drag `pin_irq`** (configure hardware interrupt)",
    "Callback Function": "*   **from Functions, drag `define_function`** (create interrupt handler)",
}


def convert_section6_block(block_name):
    """Convert a block name to Elite Standard format using templates"""
    # Clean the block name
    block_name = block_name.strip()
    
    # Try exact match first
    if block_name in BLOCK_TEMPLATES:
        return BLOCK_TEMPLATES[block_name]
    
    # Try partial matches for variations
    for template_key, template_value in BLOCK_TEMPLATES.items():
        if template_key.lower() in block_name.lower():
            return template_value
    
    # Fallback: return a generic Elite format
    return f"*   **from [Category], drag `{block_name.lower().replace(' ', '_')}`** (description needed)"


def process_section6_content(content):
    """
    Process Section 6 content and convert to Elite Standard format
    Returns: (fixed_content, changes_count)
    """
    changes = 0
    lines = content.split('\n')
    result_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if we're in a Section 6
        if line.strip() == '### 6. Blocks Used':
            result_lines.append(line)
            i += 1
            
            # Skip blank line
            if i < len(lines) and lines[i].strip() == '':
                result_lines.append(lines[i])
                i += 1
            
            # Process block entries
            while i < len(lines):
                current_line = lines[i]
                
                # Stop at next section or end
                if current_line.strip().startswith('###'):
                    break
                
                # Check for block pattern: *   **BlockName**
                match = re.match(r'\*\s+\*\*([^*]+)\*\*', current_line.strip())
                if match:
                    block_name = match.group(1).strip()
                    
                    # Skip the next line (Category line)
                    if i + 1 < len(lines) and '*   **Category:**' in lines[i + 1]:
                        # Convert this block using template
                        elite_format = convert_section6_block(block_name)
                        result_lines.append(elite_format)
                        changes += 1
                        i += 2  # Skip both the block name and category line
                        
                        # Skip blank line after category if present
                        if i < len(lines) and lines[i].strip() == '':
                            i += 1
                        continue
                
                # Keep other lines as-is
                result_lines.append(current_line)
                i += 1
        else:
            result_lines.append(line)
            i += 1
    
    return '\n'.join(result_lines), changes


def main():
    """Main execution"""
    input_file = r'd:\MFF\Pico\Documentation\Docs_0401_0500.md'
    
    print("🔧 Elite Standard Section 6 Template Converter")
    print("=" * 60)
    
    # Read file
    print(f"📖 Reading: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Process Section 6
    print("🔨 Converting Section 6 blocks using templates...")
    fixed_content, changes = process_section6_content(content)
    
    # Write back
    print(f"💾 Writing changes...")
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    # Summary
    print("=" * 60)
    print(f"✅ Complete!")
    print(f"📊 Blocks converted: {changes}")
    print(f"📁 File updated: {input_file}")
    
    return 0


if __name__ == "__main__":
    main()
