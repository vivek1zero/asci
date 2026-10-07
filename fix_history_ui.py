import codecs

with codecs.open('c:/Users/Admin/Documents/asci html/history-key-milestones.html', 'r', 'utf-8') as f:
    text = f.read()

replacements = {
    'color: #0f172a;': 'color: var(--color-text-main);',
    'color: #0d0d0d;': 'color: var(--color-text-main);',
    'color: #1e293b;': 'color: var(--color-text-main);',
    'color: #d90c29;': 'color: var(--color-asci-teal);',
    'color: #d92128;': 'color: var(--color-asci-teal);',
    'background: #f8fafc;': 'background: #f4f5f6;',
    'background: #fafafa;': 'background: #f4f5f6;',
    'background-color: #f8fafc;': 'background-color: #f4f5f6;',
    'background-color: #fafafa;': 'background-color: #f4f5f6;',
    'border: 1px solid #e2e8f0;': 'border: 1px solid var(--color-card-border);',
    'border: 1.2px solid #e2e8f0;': 'border: 1.2px solid var(--color-card-border);',
    'border-color: #d90c29;': 'border-color: var(--color-asci-teal);',
    'border-color: #d92128;': 'border-color: var(--color-asci-teal);',
    'color: #475569;': 'color: var(--color-text-muted);',
    'color: #64748b;': 'color: var(--color-text-light);',
    'color: #555b66;': 'color: var(--color-text-muted);',
    "font-family: 'Inter'": "font-family: var(--font-sans)",
    "font-family: 'Bricolage Grotesque'": "font-family: var(--font-sans)",
    "font-family: 'Domine'": "font-family: var(--font-serif)"
}

for old, new in replacements.items():
    text = text.replace(old, new)

with codecs.open('c:/Users/Admin/Documents/asci html/history-key-milestones.html', 'w', 'utf-8') as f:
    f.write(text)

print('Fixed history UI colors and fonts')
