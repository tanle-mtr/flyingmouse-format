with open('public/app.js', encoding='utf-8') as f:
    content = f.read()

# The en-US section has duplicate adapterLabel and adapterQrAlt lines.
# We need to keep only one set. Let's find the en-US block and fix it.
import re

# Find the section between "en-US": { and the next top-level key
# The structure is: "zh-CN": { ... }, "en-US": { ... }
# Let's find the sponsor block in en-US and deduplicate

lines = content.split('\n')
result = []
in_en_us = False
sponsor_lines_in_en = []
sponsor_start_idx = -1
sponsor_end_idx = -1
brace_depth = 0

for i, line in enumerate(lines):
    if '"en-US"' in line and '{' in line:
        in_en_us = True
        brace_depth = line.count('{') - line.count('}')
    elif in_en_us:
        brace_depth += line.count('{') - line.count('}')
        if brace_depth == 0:
            in_en_us = False
    
    # Track sponsor lines in en-US
    if in_en_us and ('sponsor.adapterLabel' in line or 'sponsor.adapterQrAlt' in line):
        if sponsor_start_idx == -1:
            sponsor_start_idx = i
        sponsor_end_idx = i
        sponsor_lines_in_en.append((i, line))

# Remove duplicate sponsor lines in en-US (keep first occurrence of each key)
if len(sponsor_lines_in_en) > 2:
    seen = set()
    for i, line in sponsor_lines_in_en:
        # Extract key
        m = re.search(r'"(\w+)":', line)
        if m:
            key = m.group(1)
            if key in seen:
                lines[i] = None  # mark for removal
            else:
                seen.add(key)

# Build final content
final_lines = [l for l in lines if l is not None]
content = '\n'.join(final_lines)

with open('public/app.js', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Removed {len(lines) - len(final_lines)} duplicate lines')
