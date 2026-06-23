import os
import re
import glob

# The directory with HTML files
target_dir = r"c:\Users\prajw\Documents\Dhiraj skykyn - Copy"

html_files = glob.glob(os.path.join(target_dir, "*.html"))

pattern = re.compile(r'\s*<style id="synkyn-fx-css">.*?</style>', re.DOTALL)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = pattern.sub('', content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned {file}")
    else:
        print(f"No match in {file}")
