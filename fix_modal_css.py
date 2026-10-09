import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix Modal background
html = html.replace('background:var(--card-bg);', 'background:white;')
html = html.replace('background:var(--bg-color);', 'background:#F7F9FA;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed Modal CSS")
