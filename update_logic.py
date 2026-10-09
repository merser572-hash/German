import re

with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Add TRANSLATION KEYS
app_js = app_js.replace(
    '"listen": "Listen",',
    '"settings_offline": "Offline Mode", "settings_clear_cache": "Clear Cache & Reload", "listen": "Listen",'
)
app_js = app_js.replace(
    '"listen": "Aussprache hören",',
    '"settings_offline": "Offline-Modus", "settings_clear_cache": "Cache leeren & neuladen", "listen": "Aussprache hören",'
)
app_js = app_js.replace(
    '"listen": "Talaffuzni eshitish",',
    '"settings_offline": "Offlayn rejim", "settings_clear_cache": "Keshni tozalash va yangilash", "listen": "Talaffuzni eshitish",'
)

app_js = app_js.replace(
    'sound: true, vibration: true, language: \'en\'',
    'sound: true, vibration: true, offline: true, language: \'en\''
)

init_settings_replacement = '''document.getElementById('toggle-sound').checked = appState.settings.sound;
    document.getElementById('toggle-vibration').checked = appState.settings.vibration;
    document.getElementById('toggle-offline').checked = appState.settings.offline;'''

app_js = app_js.replace(
    '''document.getElementById('toggle-sound').checked = appState.settings.sound;
    document.getElementById('toggle-vibration').checked = appState.settings.vibration;''',
    init_settings_replacement
)

new_functions = '''
function clearAllCaches() {
    triggerVibrate(50);
    playSound('tap');
    if ('caches' in window) {
        caches.keys().then(names => {
            return Promise.all(names.map(name => caches.delete(name)));
        }).then(() => {
            window.location.reload(true);
        });
    } else {
        window.location.reload(true);
    }
}

function updateOfflineMode() {
    if (appState.settings.offline) {
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register('sw.js?v=24');
        }
    } else {
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.getRegistrations().then(function(registrations) {
                for(let registration of registrations) {
                    registration.unregister();
                }
            });
            // also clear caches so offline doesn't work next time
            if ('caches' in window) {
                caches.keys().then(names => Promise.all(names.map(name => caches.delete(name))));
            }
        }
    }
}
'''

app_js = app_js.replace(
    'function toggleSetting(key) {',
    new_functions + '\nfunction toggleSetting(key) {'
)

app_js = app_js.replace(
    "if (appState.settings.vibration && key === 'vibration') triggerVibrate(50);",
    "if (appState.settings.vibration && key === 'vibration') triggerVibrate(50);\n    if (key === 'offline') updateOfflineMode();"
)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)
print('Logic updated!')
