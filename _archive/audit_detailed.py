import glob
import re

def audit_files():
    files = sorted(glob.glob("Pico_500_Batch_*.md"))
    report = {}
    
    section_headers = {
        "1": "Project Title",
        "2": "Learning Objective",
        "3": "Concepts Introduced",
        "4": "Hardware Required",
        "5": "Wiring / Interfaces",
        "6": "Blocks Used",
        "7": "Variables & State",
        "8": "Block Logic",
        "9": "Execution Flow",
        "10": "Generated Code",
        "11": "Common Mistakes",
        "12": "Try This Next"
    }

    print(f"Auditing {len(files)} files...")
    
    total_files = 0
    failed_files = 0

    for filename in files:
        total_files += 1
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        file_errors = []

        # Check for all sections
        # We look for ## [Emoji] or ### [Emoji] followed by number
        # Regex to match headers like: ## 1️⃣ or ### 1️⃣
        # Note: Some might use different emojis or formats, but standard is specific.
        
        # Split by project
        projects = re.split(r'^## 1️⃣', content, flags=re.MULTILINE)[1:] # Skip preamble
        if not projects:
             file_errors.append("No projects found starting with '## 1️⃣'")
        
        for i, project in enumerate(projects):
            proj_title = project.split('\n')[0].strip()
            # print(f"  Checking {proj_title}...")
            
            # Check Section 6: Blocks Used
            # Needs to contain "Category:" or "🔹"
            # Extract section 6
            sec6_match = re.search(r'### 6️⃣(.*?)(### 7️⃣|$)', project, re.DOTALL)
            if sec6_match:
                sec6_content = sec6_match.group(1)
                if "Category:" not in sec6_content and "🔹" not in sec6_content:
                    file_errors.append(f"Project '{proj_title}': Section 6 (Blocks) formatting incorrect.")
            else:
                 file_errors.append(f"Project '{proj_title}': Section 6 missing.")

            # Check Section 10: Generated Code
            # Needs to contain "import" and not be just comments/placeholder
            sec10_match = re.search(r'### 🔟(.*?)(### 1️⃣|$)', project, re.DOTALL)
            if sec10_match:
                sec10_content = sec10_match.group(1)
                if "```python" not in sec10_content:
                     file_errors.append(f"Project '{proj_title}': Section 10 (Code) missing python block.")
                else:
                    code_block = re.search(r'```python(.*?)```', sec10_content, re.DOTALL)
                    if code_block:
                        code = code_block.group(1).strip()
                        if "import" not in code and "def " not in code and len(code.split('\n')) < 3:
                             file_errors.append(f"Project '{proj_title}': Section 10 (Code) seems incomplete/placeholder.")
                    else:
                         file_errors.append(f"Project '{proj_title}': Section 10 (Code) empty block.")
            else:
                file_errors.append(f"Project '{proj_title}': Section 10 missing.")

        if file_errors:
            failed_files += 1
            print(f"\nIssues in {filename}:")
            for err in file_errors:
                print(f"  - {err}")
            report[filename] = file_errors

    print(f"\nAudit Complete. {failed_files}/{total_files} files need attention.")
    return report

if __name__ == "__main__":
    audit_files()
