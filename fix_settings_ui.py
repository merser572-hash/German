import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The profile card to insert right after <header class="top-bar"> inside #view-settings
profile_card = '''
            <div class="card" style="display:flex; align-items:center; gap:16px;">
                <div style="width:56px; height:56px; border-radius:28px; background:var(--primary-btn); color:white; display:flex; justify-content:center; align-items:center; font-size:24px; font-weight:800;" id="settings-avatar">
                    U
                </div>
                <div style="flex: 1; overflow: hidden;">
                    <h3 style="margin:0; font-size:18px; font-weight:800; color:var(--text-dark); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" id="settings-name">User</h3>
                    <p style="margin:0; color:var(--text-muted); font-size:14px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" id="settings-email">user@email.com</p>
                </div>
            </div>
'''

html = re.sub(r'(<div id="view-settings".*?</header>)', r'\1\n' + profile_card, html, flags=re.DOTALL)


# The logout button to insert at the end of the view-settings, before App version
logout_btn = '''
            <div class="card" style="background:var(--red-btn); color:white; text-align:center; cursor:pointer;" onclick="signOut()">
                <div style="font-weight:800; font-size:16px; display:flex; justify-content:center; align-items:center; gap:8px;">
                    <i data-lucide="log-out" style="width:20px;"></i> Sign Out
                </div>
            </div>
'''

html = re.sub(r'(<p style="text-align: center; color: var\(--text-muted\); margin-top: 24px; font-size: 12px; font-weight: 700;">\s*App version: v)', logout_btn + r'\1', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Injected properly")
