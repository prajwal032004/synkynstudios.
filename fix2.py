import os
import re

directory = r'c:\Users\prajw\Documents\Dhiraj skykyn - Copy'
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

# Regex to find multi-line waitlist
waitlist_regex = re.compile(r'Join\s+the\s+Waitlist', re.IGNORECASE)

for file in html_files:
    path = os.path.join(directory, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # replace multi-line waitlist text
    content = waitlist_regex.sub('Connect', content)
    
    # ensure hrefs are correct for these specific a tags. We look for <a href="..."> ... Connect ... </a>
    # Let's use a simpler approach: finding <a href="#" ...> and changing to ./contact.html if the a tag contains Connect
    def replace_href_multiline(m):
        a_tag = m.group(1)
        inner = m.group(2)
        new_a_tag = re.sub(r'href="[^"]*"', 'href="./contact.html"', a_tag)
        return new_a_tag + inner + '</a>'
        
    content = re.sub(r'(<a [^>]*>)([^<]*Connect[^<]*)</a>', replace_href_multiline, content, flags=re.IGNORECASE)
    # also for tags with nested spans
    content = re.sub(r'(<a [^>]*>)(.*?Connect.*?)</a>', replace_href_multiline, content, flags=re.IGNORECASE | re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated files again.')
