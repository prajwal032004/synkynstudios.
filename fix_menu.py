import glob, re

for f in glob.glob('*.html'):
    c = open(f, encoding='utf8').read()
    
    # Replace <a href="./about-us.html" ... data-menu="company" with <a href="javascript:void(0)"
    def replacer(match):
        return match.group(0).replace('./about-us.html', 'javascript:void(0)')
    
    c2 = re.sub(r'<a[^>]+href="\./about-us\.html"[^>]+data-menu="company"[^>]*>', replacer, c, flags=re.DOTALL)
    
    if c != c2:
        open(f, 'w', encoding='utf8').write(c2)
        print('fixed', f)
