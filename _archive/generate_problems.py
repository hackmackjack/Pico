import re
import json

TITLES_FILE = "PICO_2500_TITLES.md"
INDEX_FILE = "PICO_2500_INDEX.md"
PROMPT_FILE = "C:\\Users\\LocalAdmin\\.gemini\\antigravity\\brain\\cb0952c1-2c91-456d-a19a-36d44aa8a62d\\PROJECT_GENERATION_PROMPT.md"
OUTPUT_PROMPTS_FILE = "PHASE3_PROMPTS.jsonl"

def load_system_prompt():
    with open(PROMPT_FILE, 'r', encoding='utf-8') as f:
        return f.read()

def parse_titles():
    batches = {}
    current_batch = None
    
    with open(TITLES_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for line in lines:
        # Match Batch Header: ## Batch 1: LED Patterns 1 (3-5 (Elementary))
        # Responsive Regex Fix: Handles nested () in grade band
        batch_match = re.search(r'## Batch (\d+): (.*?) \((.+?)\)\s*$', line)
        if batch_match:
            b_id = int(batch_match.group(1))
            current_batch = {
                "id": b_id,
                "theme": batch_match.group(2),
                "grade": batch_match.group(3),
                "titles": []
            }
            batches[b_id] = current_batch
            continue
            
        # Match Project Title: *   **Project 0001**: Introduction to LED Patterns
        proj_match = re.search(r'\*\s+\*\*Project (\d+)\*\*: (.*)', line)
        if proj_match and current_batch:
            current_batch["titles"].append({
                "id": proj_match.group(1), # Keep as string "0001"
                "title": proj_match.group(2)
            })
            
    return batches

def generate_prompts_file():
    system_prompt = load_system_prompt()
    batches = parse_titles()
    
    print(f"Loaded {len(batches)} batches.")
    
    with open(OUTPUT_PROMPTS_FILE, 'w', encoding='utf-8') as f:
        for b_id in sorted(batches.keys()):
            batch = batches[b_id]
            
            # Construct User Message
            titles_text = "\n".join([f"- Project {t['id']}: {t['title']}" for t in batch['titles']])
            
            user_message = f"""
Batch Definition:
- Batch ID: {batch['id']}
- Grade Band: {batch['grade']}
- Theme: {batch['theme']}

LOCKED TITLES (You must generate problems for these exact 10):
{titles_text}
"""
            
            # Create JSONL entry
            entry = {
                "batch_id": b_id,
                "system_prompt": system_prompt,
                "user_message": user_message
            }
            f.write(json.dumps(entry) + "\n")
            
    print(f"Generated {OUTPUT_PROMPTS_FILE}")

if __name__ == "__main__":
    generate_prompts_file()
