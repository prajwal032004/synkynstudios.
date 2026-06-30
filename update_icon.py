import os
import re

svg_replacement = '''<svg fill="none" height="20" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg">
                                                        <path class="stroke-secondary dark:stroke-accent {=$class}" d="M2.5 14.166l7.5 3.334 7.5-3.334M2.5 9.166l7.5 3.334 7.5-3.334M10 2.5L2.5 5.833l7.5 3.334 7.5-3.334L10 2.5z" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                                    </svg>'''

for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Regex to find the <a ... href="./prints.html"> and replace the FIRST <svg ...>...</svg> inside it.
        # Since it's a bit complex, we can find the block.
        def replace_svg(match):
            prefix = match.group(1)
            return prefix + svg_replacement

        # The pattern looks for href="./prints.html" up to <svg ... </svg>
        pattern = re.compile(r'(href="\./prints\.html".*?)<svg.*?</svg>', re.DOTALL)
        content = pattern.sub(replace_svg, content)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
