import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_btn = '''<button class="action-btn" style="width:100%; background:#FFEAA7; color:#2D3436; box-shadow:0 4px 0 #FDCB6E; border:2px solid #2D3436;" onclick="startSatzbauRound()">Tushundim, keyingisi &#8594;</button>'''

new_btn = '''<button class="action-btn primary-btn" style="width:100%; margin-top: 10px; display:flex; align-items:center; justify-content:center; gap:8px;" onclick="startSatzbauRound()">Tushundim, keyingisi <i data-lucide="arrow-right"></i></button>'''

html = html.replace(old_btn, new_btn)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated button in index.html")
