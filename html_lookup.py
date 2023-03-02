import os
from translate import translate_file

# Set the root directory path
root_dir = 'C:/PythonFiles/Developer Trial Task'

# Get all the HTML files in the root directory
html_files = [os.path.join(root_dir, f) for f in os.listdir(root_dir) if f.endswith('.html')]

print(len(html_files))
i=0
# Translate each HTML file and save the translated file
for html_file in html_files:
    i+=1
    print(f"Translating {i} out of {len(html_files)}")
    translate_file(html_file)
