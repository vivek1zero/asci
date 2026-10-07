import codecs
import re

filename = 'c:/Users/Admin/Documents/asci html/history-key-milestones.html'
with codecs.open(filename, 'r', 'utf-8') as f:
    text = f.read()

# Increase padding for timeline column body
text = re.sub(r'padding: 24px 20px;', 'padding: 32px 24px;', text)

# Increase margin below header
text = re.sub(r'margin-bottom: 24px;\s+position: relative;', 'margin-bottom: 32px;\n      position: relative;', text)

# Increase gap between milestone items
text = re.sub(r'gap: 18px;', 'gap: 24px;', text)

# Increase gap in facts strip
text = re.sub(r'gap: 16px;\s+margin-top: 32px;', 'gap: 24px;\n      margin-top: 40px;', text)

# Fix any stray font-family duplicate syntax I might have created
text = re.sub(r'color: var\(--color-text-muted\); font-family: var\(--font-sans\);', 'color: var(--color-text-muted);', text)

with codecs.open(filename, 'w', 'utf-8') as f:
    f.write(text)

print('Spacing improved')
