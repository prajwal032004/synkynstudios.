import glob

html_files = glob.glob("*.html")

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = content.replace('class="w-[82px] h-auto object-contain"', 'class="w-[80px] h-auto object-contain"')
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")
