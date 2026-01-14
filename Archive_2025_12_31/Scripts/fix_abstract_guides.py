
import re

DOC_FILE = r"d:\MFF\Pico\Documentation\Docs_0001_0100.md"

def improve_guides():
    with open(DOC_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to find the section
    # We look for "### 8️⃣ Step-by-Step Guide" followed by lines containing "A. Initialization Phase"
    
    # Heuristic Replacements within the guide body:
    # "A. Initialization Phase" -> "1. Setup"
    # "B. Main Loop Phase" -> "2. Main Loop"
    # "C. Event / Condition Handling" -> Remove or change to "3. Events"
    # "**Action X**:" -> "" (Remove Action label)
    # "Turn Pin X ON" -> "From Pin Access, set Pin X to HIGH."
    # "Wait for X Seconds" -> "From Timing, wait X seconds."
    
    def replacement_logic(match):
        header = match.group(1) # ### 8...
        text = match.group(2)   # Body
        
        # Header replacements
        text = text.replace("*   **A. Initialization Phase**", "*   **1. Setup**")
        text = text.replace("*   **B. Main Loop Phase**", "*   **2. Main Loop**")
        text = text.replace("*   **C. Event / Condition Handling**", "") # Typically empty in these docs, valid to remove if None
        text = text.replace("    *   None.", "")
        
        # Action replacements
        text = re.sub(r'\*   \*\*Action \d+\*\*:', '*  ', text) # Remove Action Label
        
        # Content improvements (Simple Heuristics)
        text = re.sub(r'Turn Pin (\d+) ON.*', r'From **Pin Access**, drag `set Pin \1 to HIGH`.', text, flags=re.IGNORECASE)
        text = re.sub(r'Turn Pin (\d+) OFF.*', r'From **Pin Access**, drag `set Pin \1 to LOW`.', text, flags=re.IGNORECASE)
        
        # New: Handle "Turn LED ON", "Turn LED OFF"
        text = re.sub(r'Turn LED ON', r'From **Smart IO**, drag `Turn LED [GP25] [ON]`.', text, flags=re.IGNORECASE)
        text = re.sub(r'Turn LED OFF', r'From **Smart IO**, drag `Turn LED [GP25] [OFF]`.', text, flags=re.IGNORECASE)
        
        # New: Handle Waits
        text = re.sub(r'Wait (?:for |)(\d+(?:\.\d+)?) ?s(?:econds)?', r'From **Timing**, drag `sleep \1 seconds`.', text, flags=re.IGNORECASE)
        
        # New: Split comma separated actions if they look like instructions
        # e.g. "Action A, Action B" -> "Action A.\n    *   Action B"
        # We only do this if the line contains "From **" to avoid splitting unrelated text
        if "From **" in text or "sleep" in text:
             text = text.replace(", ", ".\n    *   ")
        
        return header + text

    # Apply to all Step-by-Step Guide sections
    pattern = r'(### 8️⃣ Step-by-Step Guide\n)(.*?)(?=\n### 9️⃣)'
    
    new_content = re.sub(pattern, replacement_logic, content, flags=re.DOTALL)
    
    with open(DOC_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Refactored guides in document.")

if __name__ == "__main__":
    improve_guides()
