import re

INDEX_FILE = "PICO_2500_INDEX.md"
OUTPUT_FILE = "PICO_2500_TITLES.md"

# --- ARCHETYPES PER GRADE BAND ---
# We use these to suffix/prefix the Batch Theme to create distinct projects

ELEM_PATTERNS = [
    "Introduction to {theme}",
    "Blinking {theme}",
    "Manual {theme} Control",
    "{theme} Sequences",
    "Interactive {theme}",
    "Smart {theme} Switch",
    "{theme} Alarm System",
    "The {theme} Game",
    "Automated {theme}",
    "Mastering {theme}"
]

MID_PATTERNS = [
    "{theme} Sensor Setup",
    "{theme} Data Reader",
    "{theme} Threshold Logic",
    "{theme} Status Monitor",
    "Automated {theme} Controller",
    "{theme} Safety Trigger",
    "{theme} Data Logger",
    "Smart {theme} System",
    "{theme} Calibration Tool",
    "Advanced {theme} Prototype"
]

HIGH_PATTERNS = [
    "{theme} Driver Implementation",
    "Asynchronous {theme} Handler",
    "Object-Oriented {theme} Class",
    "Robust {theme} Controller",
    "{theme} with Error Handling",
    "Optimized {theme} Algorithm",
    "{theme} Data Pipeline",
    "Secure {theme} Interface",
    "Multi-Threaded {theme}",
    "Industrial {theme} Soluton"
]

def clean_theme(full_theme):
    # Remove "1", "2", etc from end of theme "LED Patterns 1" -> "LED Patterns"
    return re.sub(r'\s+\d+$', '', full_theme)

def get_titles(grade_band, theme):
    clean = clean_theme(theme)
    titles = []
    
    if "Elementary" in grade_band:
        patterns = ELEM_PATTERNS
    elif "Middle" in grade_band:
        patterns = MID_PATTERNS
    else:
        patterns = HIGH_PATTERNS
        
    for p in patterns:
        titles.append(p.format(theme=clean))
        
    return titles

def generate_titles():
    print(f"Reading {INDEX_FILE}...")
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    output = "# 📚 Pico 2500: Complete Project List\n\n"
    
    # Parse Index Table (Skip headers)
    for line in lines:
        if not line.startswith("| **"): continue
        
        # Format: | **1** | 3-5 (Elementary) | Remember/Understand | `0001-0010` | LED Patterns 1 |
        parts = [p.strip() for p in line.split('|')]
        if len(parts) < 6: continue
        
        batch_id = int(parts[1].replace("**", ""))
        grade = parts[2]
        r_range = parts[4].replace("`", "")
        theme = parts[5]
        
        titles = get_titles(grade, theme)
        
        output += f"## Batch {batch_id}: {theme} ({grade})\n"
        
        start_num = (batch_id - 1) * 10 + 1
        
        for i, title in enumerate(titles):
            proj_num = start_num + i
            output += f"*   **Project {proj_num:04d}**: {title}\n"
        
        output += "\n"

    print(f"Writing {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(output)
    print("Done.")

if __name__ == "__main__":
    generate_titles()
