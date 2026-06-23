import os
import re

directory = r'c:\Users\prajw\Documents\Dhiraj skykyn - Copy'
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for file in html_files:
    path = os.path.join(directory, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The logo <a ...> has class="flex min-w-0 shrink-0 items-center gap-2"
    # We want to make sure its href is ./index.html
    
    content = re.sub(
        r'<a href="[^"]*" class="flex min-w-0 shrink-0 items-center gap-2">',
        r'<a href="./index.html" class="flex min-w-0 shrink-0 items-center gap-2">',
        content
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Logo hrefs fixed in all files.')
