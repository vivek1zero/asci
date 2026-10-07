import codecs
import re

for filename in ['c:/Users/Admin/Documents/asci html/about-us.html', 'c:/Users/Admin/Documents/asci html/history-key-milestones.html']:
    with codecs.open(filename, 'r', 'utf-8') as f:
        text = f.read()

    # The custom style block starts at <style>\n    :root { and ends at Action Icon Styling
    # Actually let's just regex replace the specific parts
    
    # Remove the :root block inside the injected style
    text = re.sub(r':root\s*\{[^\}]+\}', '', text, count=1)
    
    # Remove the body block inside the injected style
    text = re.sub(r'body\s*\{\s*margin:[^\}]+\}', '', text, count=1)

    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(text)

print('Removed custom :root and body styles')
