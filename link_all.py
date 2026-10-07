import codecs
import re

files = [
    'c:/Users/Admin/Documents/asci html/ASCI (3).html',
    'c:/Users/Admin/Documents/asci html/about-us.html',
    'c:/Users/Admin/Documents/asci html/history-key-milestones.html'
]

for filepath in files:
    with codecs.open(filepath, 'r', 'utf-8') as f:
        text = f.read()

    # Link logo to ASCI (3).html
    text = text.replace('href="#" class="header-logo-link"', 'href="ASCI (3).html" class="header-logo-link"')
    text = text.replace('href="https://www.ascionline.in/" class="header-logo-link"', 'href="ASCI (3).html" class="header-logo-link"')
    text = text.replace('href="https://www.ascionline.in/"', 'href="ASCI (3).html"')

    # Fix history links
    text = text.replace('href="https://www.ascionline.in/history-key-milestones/"', 'href="history-key-milestones.html"')
    
    # Fix about links
    text = text.replace('href="https://www.ascionline.in/about-us/"', 'href="about-us.html"')
    
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(text)

print('Done linking pages to each other')
