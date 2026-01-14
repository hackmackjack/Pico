import os
import re

def assemble_docs():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    base_dir = r'd:\MFF\Pico'
    
    # Map batch numbers to their source files
    batch_map = {
        51: "REGENERATE_BATCH_51.py",
        52: "REGENERATE_BATCH_52.py", # Check if this is the best one.
        53: "BUILD_BATCH53.py",
        54: "BUILD_BATCH54.py",
        55: "BUILD_BATCH55_V2.py",
        56: "BUILD_BATCH56_V2.py",
        57: "BUILD_BATCH57_V2.py",
        58: "BUILD_BATCH58_V2.py",
        59: "BUILD_BATCH59_V2.py",
        60: "BUILD_BATCH60_V2.py"
    }
    
    # Store all projects 501-600
    all_projects = {} 
    
    # Regex to extract project blocks like p0501 = """..."""
    # We must allow for p0501 = '''...''' as well if used.
    # And handle potential spaces like p0501= """
    pattern = re.compile(r'p(\d{4})\s*=\s*"""(.*?)"""', re.DOTALL)
    
    print("Extracting content from build scripts...")
    for batch_num in range(51, 61):
        filename = batch_map[batch_num]
        path = os.path.join(base_dir, filename)
        
        if not os.path.exists(path):
            print(f"CRITICAL ERROR: Missing script {filename}")
            # Fallback logic could go here, but for now we assume existance based on `ls`
            continue
            
        with open(path, 'r', encoding='utf-8') as f:
            script_content = f.read()
            
        matches = pattern.findall(script_content)
        print(f"  Batch {batch_num} ({filename}): Found {len(matches)} projects.")
        
        for pid, content in matches:
            all_projects[int(pid)] = content

    # Assemble final text
    final_text = "#  Pico 2500: Documentation (Projects 0501-0600)\n\n"
    
    batch_titles = {
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

    print("Assembling and Indexing...")
    for batch_num in range(51, 61):
        batch_title = batch_titles.get(batch_num, "Unknown")
        final_text += f"---\n\n#  Batch {batch_num}: {batch_title}\n\n"
        
        start_id = (batch_num - 51) * 10 + 501
        end_id = start_id + 10
        
        for pid in range(start_id, end_id):
            if pid not in all_projects:
                print(f"  WARNING: Project {pid} missing from extraction. Creating placeholder.")
                content = create_placeholder(pid)
            else:
                content = all_projects[pid]
            
            # CLEANUP AND FIX
            content = fix_content(content, pid)
            
            final_text += content + "\n\n"

    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(final_text)
        
    print("Assembly Complete.")

def fix_content(text, pid):
    """Applies Elite Standard repairs to the text block."""
    
    # 1. Fix Project Header Numbering: ## X. Project 05YY
    # We want ## 1. Project 0501 (relative to batch)
    # The PID math: relative_index = (pid - 501) % 10 + 1
    rel_index = (pid - 501) % 10 + 1
    
    # Regex to replace existing header
    # Matches ## <anything>. Project <PID>
    header_regex = re.compile(rf'##\s*\d+\.\s*Project\s*{pid}', re.IGNORECASE)
    new_header = f"## {rel_index}. Project {pid}"
    
    if header_regex.search(text):
        text = header_regex.sub(new_header, text)
    else:
        # If header not found in the block, prepend it (rare case)
        # But usually snippets contain the header.
        pass

    # 2. Fix List Indentation (4 spaces -> 2 spaces)
    # Target lines starting with 4 spaces and a bullet/number
    # We process line by line
    lines = text.split('\n')
    new_lines = []
    
    # We primarily target the "Step-by-Step Guide" section
    in_guide = False
    
    for line in lines:
        if "Step-by-Step Guide" in line:
            in_guide = True
        if "Execution Flow" in line:
            in_guide = False
            
        if in_guide:
            # Replace 4-space indent with 2-space
            # Specific pattern: "    * " -> "  * "
            # Specific pattern: "    1. " -> "  1. " (Though numbered lists shouldn't be indented usually unless nested)
            if line.startswith("    *"):
                new_lines.append(line.replace("    *", "  *", 1))
            elif line.startswith("    1."):
                new_lines.append(line.replace("    1.", "  1.", 1))
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
            
    text = '\n'.join(new_lines)
    
    return text.strip()

def create_placeholder(pid):
    return f"""## {(pid-501)%10+1}. Project {pid}: Missing Content
### 2. Learning Objective
Placeholder for missing project.
"""

if __name__ == "__main__":
    assemble_docs()
