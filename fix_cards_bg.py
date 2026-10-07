import codecs

for filename in ['c:/Users/Admin/Documents/asci html/about-us.html', 'c:/Users/Admin/Documents/asci html/history-key-milestones.html']:
    with codecs.open(filename, 'r', 'utf-8') as f:
        text = f.read()

    # Change the page-content section background to #f4f5f6
    text = text.replace('<section class="page-content" style="padding: 80px 0; background: var(--color-bg);">', '<section class="page-content" style="padding: 80px 0; background: #f4f5f6;">')
    
    # Change card borders to use home page variables
    text = text.replace('border: 1px solid #e2e8f0;', 'border: 1px solid var(--color-card-border);')

    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(text)

print('Fixed cards background and borders')
