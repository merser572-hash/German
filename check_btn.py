import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the button HTML inside checkSatzbau -> error box injection
# Actually, wait, checkSatzbau doesn't INJECT the button, it just un-hides the existing box!
# The box is in index.html!
