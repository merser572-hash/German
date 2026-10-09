import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace('    }\n}\n}\n\nfunction addXP(amount)', '    }\n}\n\nfunction addXP(amount)')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Removed extra brace")
