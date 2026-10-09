import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

upgrade_btn = '''
            <div class="card" style="background: linear-gradient(135deg, #00AEEF, #007BB5); color:white; text-align:center; cursor:pointer; margin-bottom:24px;" onclick="openPremiumModal()">
                <div style="font-weight:800; font-size:16px; display:flex; justify-content:center; align-items:center; gap:8px;">
                    <i data-lucide="zap" style="width:20px; fill: white;"></i> WunderDeutsch Pro - Upgrade
                </div>
            </div>
            
            <div class="card">
'''

html = html.replace('<div class="card">\n                <h3 style="margin-bottom:16px;" data-i18n="settings_pref">Preferences</h3>', upgrade_btn + '                <h3 style="margin-bottom:16px;" data-i18n="settings_pref">Preferences</h3>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added upgrade button to settings")
