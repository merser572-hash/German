import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace alert('Coming soon!') with a function call
html = html.replace("alert('Coming soon!')", "showComingSoonToast()")

# Add the Toast UI at the bottom of the body
toast_html = '''
    <!-- Toast Notification -->
    <div id="toast-notification" style="position:fixed; bottom:-100px; left:50%; transform:translateX(-50%); background:#2D3436; color:white; padding:16px 24px; border-radius:100px; box-shadow:0 8px 16px rgba(0,0,0,0.2); font-weight:700; transition:bottom 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); z-index:9999; display:flex; align-items:center; gap:12px; white-space:nowrap;">
        <i data-lucide="info" style="color:var(--blue-btn);"></i>
        <span id="toast-message">Tez orada! (Coming soon)</span>
    </div>
'''

if 'id="toast-notification"' not in html:
    html = html.replace('</body>', toast_html + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added Toast UI to replace alert")
