import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Find the stray bracket before setupModals()
js = re.sub(r'\}\s*function setupModals\(\)', 'function setupModals()', js)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Removed stray bracket")
