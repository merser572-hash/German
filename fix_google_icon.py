import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix Google icon squishing and size
html = html.replace('<svg width="24" height="24" viewBox="0 0 48 48">', '<svg width="28" height="28" viewBox="0 0 48 48" style="flex-shrink: 0;">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed Google Icon")
