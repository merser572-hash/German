import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace("let displayLives = appState.isAdmin ? '? : appState.lives;", "let displayLives = appState.isAdmin ? '\\u221E' : appState.lives;")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Fixed infinity symbol")
