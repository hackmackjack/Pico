
import re

DOC_FILE = r"d:\MFF\Pico\Documentation\Docs_0001_0100.md"

def update_section_headers():
    with open(DOC_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find "### 8️⃣ Block Logic"
    # We replace it with "### 8️⃣ Step-by-Step Guide"
    
    # We can do a global replace since this header string is standard across all projects in this file.
    new_content = content.replace("### 8️⃣ Block Logic", "### 8️⃣ Step-by-Step Guide")
    
    # Verify how many were changed
    count = content.count("### 8️⃣ Block Logic")
    
    with open(DOC_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Updated {count} projects to use 'Step-by-Step Guide'.")

if __name__ == "__main__":
    update_section_headers()
