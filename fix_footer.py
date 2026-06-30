import os
import re

svg_replacement = '''<svg fill="none" height="20" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg">
                                                        <path class="stroke-secondary dark:stroke-accent" d="M10 2.5c-3.1 0-5.6 2.5-5.6 5.6 0 4.7 5.6 10.6 5.6 10.6s5.6-5.9 5.6-10.6c0-3.1-2.5-5.6-5.6-5.6z" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                                        <circle class="stroke-secondary dark:stroke-accent" cx="10" cy="8.1" r="2.5" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                                    </svg>'''

for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace the svg inside footer-copy--location
        pattern = re.compile(r'(<p class="footer-copy footer-copy--location">)\s*<svg.*?</svg>', re.DOTALL)
        content = pattern.sub(r'\1' + svg_replacement, content)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
