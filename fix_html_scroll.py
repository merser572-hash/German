import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    '<div id="dict-categories" style="display:flex; overflow-x:auto; gap:8px; padding-bottom:10px; margin-bottom:8px; scrollbar-width:none; -webkit-overflow-scrolling:touch;">',
    '<div id="dict-categories" class="horizontal-scroll" style="padding-bottom:10px; margin-bottom:8px;">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated index.html")
