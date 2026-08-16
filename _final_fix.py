with open('public/app.js', encoding='utf-8') as f:
    content = f.read()

# Fix zh-CN section:
# Line 6 has "WeChat donation QR" but should be "微信收款码"
# Lines 7-8 are English adapter strings that shouldn't be in zh-CN
# Lines 9-10 are correct Chinese adapter strings

# Replace the incorrect qrAlt in zh-CN
content = content.replace(
    '"sponsor.qrAlt": "WeChat donation QR",\n    "sponsor.adapterLabel": "Adapter donation",\n    "sponsor.adapterQrAlt": "Adapter donation QR",\n    "sponsor.adapterLabel": "改编者打赏"',
    '"sponsor.qrAlt": "微信收款码",\n    "sponsor.adapterLabel": "改编者打赏"'
)

with open('public/app.js', 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
with open('public/app.js', encoding='utf-8') as f:
    content = f.read()
idx = content.find('WeChat donation QR')
if idx >= 0:
    print('ERROR: WeChat donation QR still found at', idx)
else:
    print('Fixed: WeChat donation QR removed from zh-CN')

idx2 = content.find('微信收款码')
if idx2 >= 0:
    out = content[max(0,idx2-100):idx2+300]
    with open('C:/Users/Administrator/Documents/Default Project/flyingmouse-format/final_check.txt', 'w', encoding='utf-8') as f:
        f.write(out)
    print('Fixed: 微信收款码 found')
else:
    print('ERROR: 微信收款码 not found')
