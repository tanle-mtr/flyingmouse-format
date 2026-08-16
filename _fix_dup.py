with open('public/app.js', encoding='utf-8') as f:
    content = f.read()

# The zh-CN section has duplicate adapterLabel/adapterQrAlt lines (added twice by regex)
# We need to remove the first duplicate pair (lines 7-9 in the output above)
# Pattern: adapter donation" followed by another adapter donation" before 改编者打赏

import re
# Remove the duplicate "Adapter donation" pair that appears before the Chinese version
# The pattern is: adapterLabel/adapterQrAlt appearing twice, then the Chinese version
pattern = r'("sponsor\.adapterLabel": "Adapter donation",\n    "sponsor\.adapterQrAlt": "Adapter donation QR",)\n    \1'
content = re.sub(pattern, r'\1', content)

with open('public/app.js', 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
with open('public/app.js', encoding='utf-8') as f:
    content = f.read()
idx = content.find('sponsor.adapterLabel')
out = content[max(0,idx-200):idx+400]
with open('C:/Users/Administrator/Documents/Default Project/flyingmouse-format/sponsor_verify.txt', 'w', encoding='utf-8') as f:
    f.write(out)
print('done')
