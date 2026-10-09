import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Trim password
js = js.replace(
    '''const passInput = document.getElementById('login-password').value;''',
    '''const passInput = document.getElementById('login-password').value.trim();'''
)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Trimmed password in app.js")
