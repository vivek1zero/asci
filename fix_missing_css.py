import codecs

with codecs.open('c:/Users/Admin/Documents/asci html/root_block.txt', 'r', 'utf-8') as f:
    root_block = f.read()

body_block = '''
    body {
      font-family: var(--font-sans);
      color: var(--color-text-main);
      background-color: var(--color-bg);
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      overflow-x: hidden;
    }
'''

injection = root_block + "\n" + body_block + "\n"

for filename in ['c:/Users/Admin/Documents/asci html/about-us.html', 'c:/Users/Admin/Documents/asci html/history-key-milestones.html']:
    with codecs.open(filename, 'r', 'utf-8') as f:
        text = f.read()

    # insert after the first <style> tag
    text = text.replace('<style>', '<style>\n' + injection, 1)

    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(text)

print('Restored missing root and body css')
