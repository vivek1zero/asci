import codecs
import re

for filename in ['c:/Users/Admin/Documents/asci html/ASCI (3).html', 'c:/Users/Admin/Documents/asci html/about-us.html', 'c:/Users/Admin/Documents/asci html/history-key-milestones.html']:
    with codecs.open(filename, 'r', 'utf-8') as f:
        text = f.read()

    # Fix History & key milestones link
    text = text.replace('href="/history-key-milestones"', 'href="history-key-milestones.html"')
    # Or in case it is something else
    text = re.sub(r'href="[^"]*"\s*(>[^<]*<span>History &amp; key milestones</span>)', r'href="history-key-milestones.html"\1', text)

    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(text)

print('Fixed megamenu history link')
