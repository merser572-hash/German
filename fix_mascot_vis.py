with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace("if (mascot) mascot.style.display = 'none';", "if (mascot) mascot.classList.remove('show');")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('Fixed mascot visibility reset')
