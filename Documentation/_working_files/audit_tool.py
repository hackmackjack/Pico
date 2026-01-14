import re
import os

files = [
    r"d:\MFF\Pico\Documentation\Docs_0001_0100.md",
    r"d:\MFF\Pico\Documentation\Docs_0101_0200.md",
    r"d:\MFF\Pico\Documentation\Docs_0201_0300.md"
]

required_sections = [
    "Learning Objective",
    "Concepts Introduced",
    "Hardware Required",
    "Wiring",
    "Blocks Used",
    "Variables",
    "Step-by-Step Guide",
    "Execution Flow",
    "Generated Code",
    "Common Mistakes",
    "Try This Next"
]

with open("FULL_AUDIT_REPORT.md", "w", encoding="utf-8") as out:
    out.write("| Project | Title | Sections | Status |\n")
    out.write("| :--- | :--- | :--- | :--- |\n")

    count = 0
    for file_path in files:
        if not os.path.exists(file_path):
            out.write(f"| ERROR | File not found: {file_path} | | |\n")
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Robust Logic: Find all start indices
        # Handles "## 1️⃣ Project", "## Project", etc.
        pattern = r"## .*Project (\d{4}): (.+)"
        matches = list(re.finditer(pattern, content))
        
        for i, match in enumerate(matches):
            pid = match.group(1)
            title = match.group(2).strip()
            
            # Determine content range for this project
            start = match.start()
            if i + 1 < len(matches):
                end = matches[i+1].start()
                project_text = content[start:end]
            else:
                project_text = content[start:]
            
            # Check sections within this range
            missing = []
            for sec in required_sections:
                if sec not in project_text:
                    # Loose check: try partial match or case insensitive if needed
                    # But our standard is strict.
                    missing.append(sec)
            
            status = "PASS" if not missing else f"FAIL Missing: {len(missing)}"
            sections_score = f"{len(required_sections) - len(missing)}/11"
            
            out.write(f"| {pid} | {title} | {sections_score} | {status} |\n")
            count += 1
            
    out.write(f"\n**Total Projects Audited: {count}**\n")
