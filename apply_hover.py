import codecs

for filename in ['c:/Users/Admin/Documents/asci html/about-us.html', 'c:/Users/Admin/Documents/asci html/history-key-milestones.html']:
    with codecs.open(filename, 'r', 'utf-8') as f:
        text = f.read()

    text = text.replace('border-color: #d90c29;', 'border-color: var(--color-asci-teal);')

    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(text)

print('Updated hover theme')
