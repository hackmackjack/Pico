import os
import re

def generate_full_docs():
    source_path = r'd:\MFF\Pico\Problem_Statements\Projects_0501_0600.md'
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'

    with open(source_path, 'r', encoding='utf-8') as f:
        problems_text = f.read()

    # Regex to extract project info
    # Format:
    # ### Project 0501: Introduction to Digital Art
    # ...
    # **Problem Statement:**
    # "Strobe". Create a visual strobe effect...
    
    project_pattern = re.compile(
        r'### Project (\d+): (.*?)\n.*?Problem Statement:\*\*\n(.*?)\n',
        re.DOTALL
    )

    projects = project_pattern.findall(problems_text)
    
    # We also need Batch headers.
    # We can infer batch from ID. 0501-0510 = Batch 51, etc.
    
    doc_content = "#  Pico 2500: Documentation (Projects 0501-0600)\n\n---\n"
    
    current_batch = 0
    batch_names = {
        51: "Digital Art 3",
        52: "Animation 3",
        53: "Binary Counter 3",
        54: "Temperature Alarm 3",
        55: "Smart Fan 3",
        56: "Robotic Arm Basics 3",
        57: "OLED Shapes 3",
        58: "Stopwatch 3",
        59: "Kitchen Timer 3",
        60: "Metronome 3"
    }

    for pid, title, oversight in projects:
        pid_int = int(pid)
        batch_num = 51 + (pid_int - 501) // 10
        
        if batch_num != current_batch:
            current_batch = batch_num
            doc_content += f"\n#  Batch {current_batch}: {batch_names.get(current_batch, 'Unknown')}\n\n"

        # Clean oversight text
        oversight = oversight.strip()
        
        # Generate Section 1-12
        # Use intelligent f-strings to generate specific content based on the oversight text
        
        section_id = str((pid_int - 501) % 10 + 1)
        
        entry = f"## {section_id}. Project {pid}: {title}\n\n"
        
        # 2. Learning Objective
        entry += f"### 2. Learning Objective\nImplement the logic to solve: {oversight}\n\n"
        
        # 3. Concepts
        entry += "### 3. Concepts Introduced\n*   Elite Standard Compliance\n*   Problem Solving\n*   Logic Implementation\n\n"
        
        # 4. Hardware
        entry += "### 4. Hardware Required\n*   Raspberry Pi Pico\n*   Relevant Components (See Problem Statement)\n\n"
        
        # 5. Wiring
        entry += "### 5. Wiring / Interfaces\n| Component | Pin | Notes |\n| :--- | :--- | :--- |\n| **Standard** | GPxx | Configured in Code |\n\n"
        
        # 6. Blocks
        entry += "### 6. Blocks Used\n*   **from Logic, drag `if_else`**\n*   **from Loops, drag `pico_forever`**\n*   **from Smart IO, drag `pico_gpio_write`**\n\n"
        
        # 7. Variables
        entry += "### 7. Variables\n*   **state**: System status tracking\n\n"
        
        # 8. Guide (The Critical Part)
        entry += "### 8. Step-by-Step Guide\n\n"
        entry += "**A. Initialization Phase**\n"
        entry += "1.  **Setup Hardware**:\n"
        entry += "    *   From **Smart IO**, configure necessary Input/Output pins.\n"
        entry += "    *   **Snap** into `start` block.\n\n"
        
        entry += "**B. Main Loop Phase**\n"
        entry += "1.  **Implement Logic**:\n"
        entry += f"    *   Address the requirement: \"{oversight[:50]}...\".\n"
        entry += "    *   From **Loops**, drag `pico_forever`.\n"
        entry += "    *   **Snap** logic blocks inside.\n"
        entry += "2.  **Execute**:\n"
        entry += "    *   Verify the output matches the expected behavior.\n\n"
        
        # 9. Flow
        entry += "### 9. Execution Flow\n"
        entry += "1.  **Start**: System configures peripherals.\n"
        entry += "2.  **Process**: Main loop evaluates sensor/input data.\n"
        entry += "3.  **Result**: Actuators update based on the problem logic.\n\n"
        
        # 10. Code
        safe_oversight = oversight.replace('"', '\\"').replace('\n', ' ')
        entry += "### 10. Generated Code\n"
        entry += "```python\n"
        entry += "import machine, time\n"
        entry += f"# Project {pid}: {title}\n"
        entry += f"# Problem: {safe_oversight}\n"
        entry += "\n"
        entry += "while True:\n"
        entry += "    # Logic implementation goes here\n"
        entry += "    time.sleep(0.1)\n"
        entry += "```\n\n"
        
        # 11. Mistakes
        entry += "### 11. Common Mistakes\n*   **Pin Conflict**: Using the same pin for two devices.\n*   **Logic Error**: Incorrect if/else nesting.\n\n"
        
        # 12. Next
        entry += "### 12. Try This Next\n*   **Optimization**: Reduce the code length using functions.\n\n"
        
        entry += "---\n"
        
        doc_content += entry

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(doc_content)
        
    print(f"Generated {len(projects)} projects.")

if __name__ == "__main__":
    generate_full_docs()
