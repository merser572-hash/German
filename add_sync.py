import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Make toast generic
toast_logic = '''
function showToast(customMsg) {
    playSound('tap');
    const toast = document.getElementById('toast-notification');
    if (!toast) return;
    
    let msg = customMsg;
    if (!msg) {
        msg = "Tez orada! (Coming soon)";
        if (appState.settings.language === 'en') msg = "Coming soon!";
        if (appState.settings.language === 'de') msg = "Kommt bald!";
    }
    
    document.getElementById('toast-message').innerText = msg;
'''
js = re.sub(r"function showComingSoonToast\(\) \{.*?(?=    document\.getElementById\('toast-message'\)\.innerText = msg;)", toast_logic, js, flags=re.DOTALL)

# Add forceCloudSync
sync_func = '''
async function forceCloudSync() {
    if (!currentUser) return;
    const btn = document.getElementById('sync-btn');
    const icon = btn.querySelector('i');
    
    if (btn) btn.style.opacity = '0.5';
    if (icon) icon.classList.add('lucide-spin'); // Optional if we add css animation
    
    try {
        await saveUserDataToCloud();
        // syncUserData sets up the snapshot listener, so it will pull the latest automatically
        
        let msg = "Bulut bilan sinxronlandi! ☁️";
        if (appState.settings.language === 'en') msg = "Cloud Synced! ☁️";
        if (appState.settings.language === 'de') msg = "Cloud synchronisiert! ☁️";
        
        showToast(msg);
    } catch (e) {
        showToast("Sync Error!");
    }
    
    if (btn) btn.style.opacity = '1';
    if (icon) icon.classList.remove('lucide-spin');
}
'''
js += '\n' + sync_func

# Replace any old calls
js = js.replace('showComingSoonToast()', 'showToast()')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Added forceCloudSync and updated Toast")
