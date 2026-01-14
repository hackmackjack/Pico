import sys, os, re

# Paths
TITLES_FILE = r"d:\MFF\Pico\Reference_Bible_Standards\PICO_2500_TITLES.md"
PROBLEM_FILES = [
    r"d:\MFF\Pico\Problem_Statements\Projects_1401_1500.md",
    r"d:\MFF\Pico\Problem_Statements\Projects_1501_1600.md",
    r"d:\MFF\Pico\Problem_Statements\Projects_1601_1700.md",
    r"d:\MFF\Pico\Problem_Statements\Projects_1701_1800.md",
    r"d:\MFF\Pico\Problem_Statements\Projects_1801_1900.md",
    r"d:\MFF\Pico\Problem_Statements\Projects_1901_2000.md",
    r"d:\MFF\Pico\Problem_Statements\Projects_2001_2100.md",
    r"d:\MFF\Pico\Problem_Statements\Projects_2101_2200.md",
    r"d:\MFF\Pico\Problem_Statements\Projects_2201_2300.md",
    r"d:\MFF\Pico\Problem_Statements\Projects_2301_2400.md",
    r"d:\MFF\Pico\Problem_Statements\Projects_2401_2500.md"
]

# 1. Parse Identity Truth (Titles)
pid_to_title = {}
batch_to_topic = {}
if os.path.exists(TITLES_FILE):
    with open(TITLES_FILE, 'r', encoding='utf-8') as f:
        titles_content = f.read()
    
    # Get Project Titles
    matches = re.finditer(r"\*\s+\*\*Project (\d+)\*\*:\s*(.*)", titles_content)
    for match in matches:
        pid = match.group(1)
        title = match.group(2).strip()
        pid_to_title[pid] = title
        
    # Get Batch Topics
    b_matches = re.finditer(r"## Batch (\d+):\s*(.*)", titles_content)
    for b_match in b_matches:
        b_num = b_match.group(1)
        b_topic_line = b_match.group(2).strip()
        # Clean: "Advanced Radar Screen 4 (6-8 (Middle))" -> "Advanced Radar Screen"
        # Logic: stop before the first " Number (" or digit + "("
        b_topic = re.split(r"\s+\d+\s*\(", b_topic_line)[0].strip()
        batch_to_topic[b_num] = b_topic

# 2. Parse Functional Truth (Goals)
pid_to_goal = {}
for f_path in PROBLEM_FILES:
    if not os.path.exists(f_path):
        continue
    with open(f_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    projects = re.split(r"### Project (\d+):", content)
    for i in range(1, len(projects), 2):
        pid = projects[i]
        details = projects[i+1]
        
        goal_match = re.search(r"problem statement:\*\*\s*\n?\s*\"(.*?)\"\.\s*(.*?)(\n|$)", details, re.IGNORECASE)
        if goal_match:
            niche = goal_match.group(1).strip()
            summary = goal_match.group(2).strip().split('.')[0].strip()
            if len(summary) > 100: summary = summary[:97] + "..."
            pid_to_goal[pid] = f'**Goal**: "{niche}" ({summary})'
        else:
            pid_to_goal[pid] = '**Goal**: "TBD" (TBD)'

# 3. Generate Dashboard
dashboard = []
for batch_num in range(141, 251):
    b_str = str(batch_num)
    topic = batch_to_topic.get(b_str, "TBD")
    r_start = batch_num * 10 - 9
    r_end = batch_num * 10
    dashboard.append(f"| **{batch_num}** | {r_start}-{r_end} | {topic} | `[----------]` 0% | 🔄 PENDING |")

# 4. Generate Task List
tasks = []
for batch_num in range(141, 251):
    b_str = str(batch_num)
    topic = batch_to_topic.get(b_str, "TBD")
    r_start = batch_num * 10 - 9
    r_end = batch_num * 10
    tasks.append(f"### **Batch {batch_num}: {topic} ({r_start}-{r_end})**")
    for pid_val in range(r_start, r_end + 1):
        pid_str = str(pid_val)
        title = pid_to_title.get(pid_str, f"Project {pid_str}")
        goal = pid_to_goal.get(pid_str, '**Goal**: "TBD" (TBD)')
        tasks.append(f"- [ ] **{pid_str}**: {title} | {goal}")
    tasks.append("")

# Output
with open(r"d:\MFF\Pico\final_dashboard.txt", 'w', encoding='utf-8') as f:
    f.write("\n".join(dashboard))

with open(r"d:\MFF\Pico\final_tasks.txt", 'w', encoding='utf-8') as f:
    f.write("\n".join(tasks))
