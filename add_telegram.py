import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_contact = '''<a href="tel:+998333371005" style="color:var(--blue-btn); text-decoration:none; display:flex; align-items:center; gap:8px;"><i data-lucide="phone" style="width:20px;"></i> +998 33 337 10 05</a>'''

new_contact = '''<a href="tel:+998333371005" style="color:var(--blue-btn); text-decoration:none; display:flex; align-items:center; gap:8px;"><i data-lucide="phone" style="width:20px;"></i> +998 33 337 10 05</a>
                    <a href="http://t.me/hasanboy_hoshimjonov" target="_blank" style="color:var(--blue-btn); text-decoration:none; display:flex; align-items:center; gap:8px;"><i data-lucide="send" style="width:20px;"></i> Telegram</a>'''

html = html.replace(old_contact, new_contact)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added telegram")
