import re

# Read file
with open('Docs_0001_0100.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix emoji formatting
content = content.replace('### 🔟 Generated Code (Reference Only)', '### 10️⃣ Generated Code')
content = content.replace('### 1️⃣1️⃣ Common Mistakes & Debug Tips', '### 11️⃣ Common Mistakes')  
content = content.replace('### 1️⃣2️⃣ Try This Next', '### 12️⃣ Try This Next')
content = content.replace('### 9️⃣ Execution Flow (Plain English)', '### 9️⃣ Execution Flow')
content = content.replace('### 7️⃣ Variables & State', '### 7️⃣ Variables')

# Write back
with open('Docs_0001_0100.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed emoji formatting issues")
