import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

logout_btn = '''
            <div class="card" style="background:var(--red-btn); color:white; text-align:center; cursor:pointer;" onclick="signOut()">
                <div style="font-weight:800; font-size:16px; display:flex; justify-content:center; align-items:center; gap:8px;">
                    <i data-lucide="log-out" style="width:20px;"></i> Sign Out
                </div>
            </div>
'''

html = re.sub(r'(<div style="text-align:center; margin-top:20px; font-size:12px; color:var\(--text-muted\); font-weight:700;">\s*App version: v)', logout_btn + r'\n            \1', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Injected logout button")
