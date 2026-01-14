import re
import os

def verify_docs():
    file_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    if not os.path.exists(file_path):
        print("File not found.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all project headers
    projects = re.findall(r'## \d+\. Project (\d+):', content)
    unique_projects = sorted(list(set(projects)))
    
    print(f"Total Projects Found: {len(unique_projects)}")
    
    # Check for missing projects
    expected = [f"{i:04d}" for i in range(501, 601)]
    missing = [p for p in expected if p not in unique_projects]
    
    if missing:
        print(f"Missing {len(missing)} projects: {missing[:5]}...{missing[-5:] if len(missing)>5 else ''}")
    else:
        print("All projects 0501-0600 are present.")

    # detailed check for a few samples
    # Check typical section headers count
    sections = [
        "### 2. Learning Objective",
        "### 3. Concepts Introduced",
        "### 4. Hardware Required",
        "### 5. Wiring / Interfaces",
        "### 6. Blocks Used",
        "### 7. Variables",
        "### 8. Step-by-Step Guide",
        "### 9. Execution Flow",
        "### 10. Generated Code",
        "### 11. Common Mistakes",
        "### 12. Try This Next"
    ]
    
    for sec in sections:
        count = content.count(sec)
        print(f"Section '{sec}' count: {count}")

    # Check for placeholders
    if "TODO" in content or "pass" in content:
        print("Warning: 'TODO' or 'pass' found in text.")

    # Check total lines
    print(f"Total lines: {len(content.splitlines())}")

if __name__ == "__main__":
    verify_docs()
