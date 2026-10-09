import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace('// Save to local storage just in case they go offline\n just in case they go offline', '// Save to local storage just in case they go offline')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Fixed syntax error")
