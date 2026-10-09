import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = re.sub(r'appState\.xp \+= (\d+);\s*updateStats\(\);', r'addXP(\1);', js)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Replaced direct XP updates with addXP()")
