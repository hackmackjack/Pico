import os

REFACTOR_FILE = r"d:\MFF\Pico\refactor_task.md"
TASKS_FILE = r"d:\MFF\Pico\final_tasks.txt"

with open(REFACTOR_FILE, 'r', encoding='utf-8') as f:
    lines = f.readlines()

header = lines[:349]

with open(TASKS_FILE, 'r', encoding='utf-8') as f:
    tasks = f.read()

content = "".join(header) + tasks

with open(REFACTOR_FILE, 'w', encoding='utf-8') as f:
    f.write(content)
