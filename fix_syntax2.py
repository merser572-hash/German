import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Remove the extra brace
js = js.replace(
'''    livesElements.forEach(el => el.textContent = displayLives);
}
}

function switchView(viewId) {''',
'''    livesElements.forEach(el => el.textContent = displayLives);
}

function switchView(viewId) {'''
)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Fixed syntax error 2!")
