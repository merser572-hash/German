import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

profile_card = '''
        <div class="settings-list">
            
            <div style="background:var(--card-bg); padding:16px; border-radius:16px; margin-bottom:24px; display:flex; align-items:center; gap:16px; box-shadow:0 4px 0 rgba(0,0,0,0.05);">
                <div style="width:56px; height:56px; border-radius:28px; background:var(--primary-btn); color:white; display:flex; justify-content:center; align-items:center; font-size:24px; font-weight:800;" id="settings-avatar">
                    U
                </div>
                <div style="flex: 1; overflow: hidden;">
                    <h3 style="margin:0; font-size:18px; font-weight:800; color:var(--text-dark); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" id="settings-name">User</h3>
                    <p style="margin:0; color:var(--text-muted); font-size:14px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" id="settings-email">user@email.com</p>
                </div>
            </div>
            
            <div class="settings-item">
'''

html = html.replace('<div class="settings-list">\n            <div class="settings-item">', profile_card)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added profile card to settings")
