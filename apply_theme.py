import codecs
import re

with codecs.open('c:/Users/Admin/Documents/asci html/history-key-milestones.html', 'r', 'utf-8') as f:
    text = f.read()

# Replace red color with teal
text = text.replace('#d90c29', 'var(--color-asci-teal)')

# Replace hero background
text = text.replace('background: #f8fafc;', 'background: var(--color-bg);')

# Replace page content background
text = text.replace('background: #fafafa;', 'background: var(--color-bg);')

# Use CSS variables for fonts
text = text.replace('font-size: 3.5rem; font-weight: 800; color: #0f172a;', 'font-size: 3.5rem; font-weight: 800; color: var(--color-text-main); font-family: var(--font-serif);')
text = text.replace('font-size: 1.5rem; font-weight: 700; color: #0f172a;', 'font-size: 1.5rem; font-weight: 700; color: var(--color-text-main); font-family: var(--font-serif);')
text = text.replace('color: #475569;', 'color: var(--color-text-muted); font-family: var(--font-sans);')
text = text.replace('font-family: \'Inter\'', 'font-family: var(--font-sans)')

with codecs.open('c:/Users/Admin/Documents/asci html/history-key-milestones.html', 'w', 'utf-8') as f:
    f.write(text)

print('Updated theme in history page')
