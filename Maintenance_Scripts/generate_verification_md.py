import re
import os

source_path = r"d:\MFF\Pico\Documentation\Docs_0101_0200.md"
report_path = r"d:\MFF\Pico\Documentation\Verification_Report_0101_0200.md"

def generate_report():
    if not os.path.exists(source_path):
        print("Source file not found.")
        return

    with open(source_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    project_starts = []
    for i, line in enumerate(lines):
        # Match "## 1. Project" OR "## Project" to catch all variants
        if re.match(r"^## (1\. )?Project", line.strip()):
            project_starts.append(i)
    
    project_starts.append(len(lines))
    
    # Dictionary to store result per Project ID
    # Format: "0101": {"status": "PASS", "missing": []}
    # We prefer PASS over FAIL if duplicates exist.
    results = {}

    for i in range(len(project_starts) - 1):
        start_line = project_starts[i]
        end_line = project_starts[i+1]
        
        chunk = "".join(lines[start_line:end_line])
        header = lines[start_line].strip()
        
        # Extract ID
        match = re.search(r'Project (\d+)', header)
        if not match: continue
        
        pid = match.group(1)
        
        # Check Sections 2-12
        missing = []
        for sec in range(2, 13):
            # Look for "### 2." etc
            if not re.search(rf'^### {sec}\.', chunk, re.MULTILINE):
                missing.append(sec)
        
        status = "PASS" if not missing else "FAIL"
        
        # Init if new
        if pid not in results:
            results[pid] = {"status": status, "missing": missing, "header": header}
        else:
            # Update if current is PASS and stored is FAIL
            if status == "PASS" and results[pid]["status"] == "FAIL":
                results[pid] = {"status": status, "missing": missing, "header": header}
            # Keep existing if it's PASS, or if both are FAIL (maybe check which is better?)

    # Write Markdown Report
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Verification Verdict: Docs_0101_0200.md\n")
        f.write("## Standard: Enhanced Detail v2.0 (12 Sections)\n\n")
        f.write("| Project ID | Status | Missing Sections | 12-Stage Validation |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        
        sorted_ids = sorted(results.keys())
        pass_count = 0
        total_count = len(sorted_ids)
        
        for pid in sorted_ids:
            data = results[pid]
            stat = data["status"]
            miss = data["missing"]
            
            if stat == "PASS":
                pass_count += 1
                miss_str = "None"
                valid_icon = "✅ Verified"
            else:
                miss_str = ", ".join(map(str, miss))
                valid_icon = "❌ Failed"
            
            f.write(f"| **{pid}** | **{stat}** | {miss_str} | {valid_icon} |\n")
            
        f.write("\n## Summary\n")
        f.write(f"- **Total Projects Tested**: {total_count}\n")
        f.write(f"- **Passed**: {pass_count}\n")
        f.write(f"- **Failed**: {total_count - pass_count}\n")

    print(f"Report Generated at {report_path}")
    print(f"Stats: {pass_count}/{total_count} Passing.")

if __name__ == "__main__":
    generate_report()
