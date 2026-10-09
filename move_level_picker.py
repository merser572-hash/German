import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<div style="padding: 16px 16px 0 16px;">', '<div style="padding: 0 16px 12px 16px; margin-top: -16px; display:flex; justify-content:center;">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Moved level picker higher")
