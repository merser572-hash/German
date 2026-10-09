import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add refresh button next to settings
html = html.replace(
    '''<button class="icon-btn" onclick="switchView('settings')"><i data-lucide="settings"></i></button>''',
    '''<div style="display:flex; gap:8px;">
                    <button class="icon-btn" onclick="clearAllCaches()"><i data-lucide="refresh-cw"></i></button>
                    <button class="icon-btn" onclick="switchView('settings')"><i data-lucide="settings"></i></button>
                </div>'''
)

# 2. Add offline mode toggle
offline_toggle = '''<div class="setting-row">
                    <span><i data-lucide="download-cloud"></i> <span data-i18n="settings_offline">Offline Mode</span></span>
                    <label class="switch">
                        <input type="checkbox" id="toggle-offline" onchange="toggleSetting('offline')">
                        <span class="slider"></span>
                    </label>
                </div>'''

html = html.replace(
    '''<div class="setting-row">
                    <span><i data-lucide="globe"></i> <span data-i18n="settings_lang">Language</span></span>''',
    offline_toggle + '''\n                <div class="setting-row">
                    <span><i data-lucide="globe"></i> <span data-i18n="settings_lang">Language</span></span>'''
)

# 3. Add clear cache button before contact card
clear_cache_btn = '''<div class="card" style="margin-bottom: 16px;">
                <button class="btn-3d" style="background:#FF7675; color:white; width:100%; padding:12px; border:none; border-radius:12px; font-weight:700; box-shadow:0 4px 0 #D63031; display:flex; align-items:center; justify-content:center; gap:8px;" onclick="clearAllCaches()">
                    <i data-lucide="trash-2" style="width:20px;"></i> <span data-i18n="settings_clear_cache">Clear All Caches</span>
                </button>
            </div>\n\n            <div class="card">'''

html = html.replace(
    '''<div class="card">
                <h3 style="margin-bottom:12px;" data-i18n="contact_title">Contact</h3>''',
    clear_cache_btn + '''
                <h3 style="margin-bottom:12px;" data-i18n="contact_title">Contact</h3>'''
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("UI updated!")
