import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r'<script>\s*if \(\'serviceWorker\' in navigator\).*?</script>', '', text, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

app_js = app_js.replace(
    'updateStats();',
    'updateStats();\n    updateOfflineMode(); // conditionally register SW on startup'
)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("Done")
