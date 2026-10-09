import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace('"settings_lang": "Language",', '"settings_lang": "Language", "settings_notif": "Notifications", "settings_reminder": "Daily Reminders",')
js = js.replace('"settings_lang": "Sprache",', '"settings_lang": "Sprache", "settings_notif": "Benachrichtigungen", "settings_reminder": "Tägliche Erinnerungen",')
js = js.replace('"settings_lang": "Til",', '"settings_lang": "Til", "settings_notif": "Bildirishnomalar", "settings_reminder": "Kunlik eslatmalar",')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Added translations for toggles")
