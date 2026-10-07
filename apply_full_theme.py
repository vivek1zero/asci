import codecs
import re

for filename in ['c:/Users/Admin/Documents/asci html/history-key-milestones.html', 'c:/Users/Admin/Documents/asci html/about-us.html']:
    with codecs.open(filename, 'r', 'utf-8') as f:
        text = f.read()

    # Red/Orange shades to Teal/Orange
    text = re.sub(r'#d90c29', 'var(--color-asci-teal)', text, flags=re.IGNORECASE)
    text = re.sub(r'#d92128', 'var(--color-asci-teal)', text, flags=re.IGNORECASE)
    text = re.sub(r'#d91b42', 'var(--color-asci-teal)', text, flags=re.IGNORECASE)
    text = re.sub(r'#d97706', 'var(--color-accent-orange)', text, flags=re.IGNORECASE)

    # Slate/Gray shades to Text/Border vars
    text = re.sub(r'#0f172a', 'var(--color-text-main)', text, flags=re.IGNORECASE)
    text = re.sub(r'#0d0d0d', 'var(--color-text-main)', text, flags=re.IGNORECASE)
    text = re.sub(r'#1e293b', 'var(--color-text-main)', text, flags=re.IGNORECASE)
    
    text = re.sub(r'#475569', 'var(--color-text-muted)', text, flags=re.IGNORECASE)
    text = re.sub(r'#64748b', 'var(--color-text-light)', text, flags=re.IGNORECASE)
    text = re.sub(r'#555b66', 'var(--color-text-muted)', text, flags=re.IGNORECASE)
    
    text = re.sub(r'#e2e8f0', 'var(--color-card-border)', text, flags=re.IGNORECASE)
    text = re.sub(r'#cbd5e1', 'var(--color-card-hover-border)', text, flags=re.IGNORECASE)

    # Light backgrounds
    text = re.sub(r'#f8fafc', '#f4f5f6', text, flags=re.IGNORECASE)
    text = re.sub(r'#fafafa', '#f4f5f6', text, flags=re.IGNORECASE)

    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(text)

print('Full theme applied to all files')
