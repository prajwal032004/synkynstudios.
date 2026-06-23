import os
import re

directory = r'c:\Users\prajw\Documents\Dhiraj skykyn - Copy'
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

logo_html = '''<a href="./index.html" class="flex min-w-0 shrink-0 items-center gap-2">
                    <!-- Desktop logo -->
                    <figure class="m-0 hidden lg:block lg:max-w-[112px]">
                        <img src="./images/logo.png" alt="Synkyn Studios" class="w-[80px] h-auto object-contain" />
                    </figure>
                    <!-- Mobile logo -->
                    <figure class="m-0 flex max-w-[52px] shrink-0 lg:hidden">
                        <img src="./images/logo.png" alt="Synkyn Studios" class="w-full h-auto object-contain" />
                    </figure>
                </a>'''

# Regex to find the logo a tag
logo_regex = re.compile(r'<a href="\./index\.html" class="flex min-w-0 shrink-0 items-center gap-2">.*?</figure>\s*</a>', re.DOTALL)

for file in html_files:
    path = os.path.join(directory, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. replace waitlist text
    content = re.sub(r'<span>Join the Waitlist</span>', '<span>Connect</span>', content, flags=re.IGNORECASE)
    content = re.sub(r'<span>80\+ properties joined the waitlist</span>', '<span>80+ properties connected</span>', content, flags=re.IGNORECASE)
    content = re.sub(r'>Join the Waitlist<', '>Connect<', content, flags=re.IGNORECASE)
    
    # 2. replace the href specifically for these tags. 
    def replace_href(m):
        a_tag = m.group(1)
        inner = m.group(2)
        new_a_tag = re.sub(r'href="[^"]*"', 'href="./contact.html"', a_tag)
        return new_a_tag + inner + '</a>'
        
    content = re.sub(r'(<a [^>]*>)([^<]*<span>Connect</span>[^<]*)</a>', replace_href, content, flags=re.IGNORECASE)
    content = re.sub(r'(<a [^>]*>)([^<]*Connect[^<]*)</a>', replace_href, content, flags=re.IGNORECASE)

    # 3. For terms and privacy, fix the logo
    if file in ['terms.html', 'privacy.html']:
        content = logo_regex.sub(logo_html, content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated files.')
