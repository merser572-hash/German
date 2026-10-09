import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

toggles_html = '''
                <div class="setting-item" style="display:flex; justify-content:space-between; align-items:center;">
                    <span><i data-lucide="bell" style="width:16px; margin-right:8px; vertical-align:middle;"></i> <span data-i18n="settings_notif">Notifications</span></span>
                    <label class="toggle-switch">
                        <input type="checkbox" id="setting-notif" checked onchange="toggleNotif(this)">
                        <span class="slider"></span>
                    </label>
                </div>
                
                <div class="setting-item" style="display:flex; justify-content:space-between; align-items:center;">
                    <span><i data-lucide="calendar-clock" style="width:16px; margin-right:8px; vertical-align:middle;"></i> <span data-i18n="settings_reminder">Daily Reminders</span></span>
                    <label class="toggle-switch">
                        <input type="checkbox" id="setting-reminder" checked onchange="toggleReminder(this)">
                        <span class="slider"></span>
                    </label>
                </div>
'''

if 'id="setting-notif"' not in html:
    html = html.replace('<div class="setting-item" style="display:flex; justify-content:space-between; align-items:center;">\n                    <span><i data-lucide="wifi-off"', toggles_html + '<div class="setting-item" style="display:flex; justify-content:space-between; align-items:center;">\n                    <span><i data-lucide="wifi-off"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added toggles to settings")
