import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add Telegram globals
tg_init = '''
let tg = window.Telegram ? window.Telegram.WebApp : null;
let isTMA = tg && tg.initDataUnsafe && tg.initDataUnsafe.user;
'''
js = js.replace('let db;\nlet auth;', 'let db;\nlet auth;\n' + tg_init)

# Modify initApp to branch for TMA
tma_init_logic = '''
async function initApp() {
    if (isTMA) {
        tg.expand();
        tg.ready();
        document.getElementById('login-overlay').style.display = 'none';
        document.getElementById('app-container').style.display = 'flex';
        
        currentUser = { 
            uid: String(tg.initDataUnsafe.user.id), 
            email: (tg.initDataUnsafe.user.username || 'tg_user') + '@telegram.org', 
            displayName: tg.initDataUnsafe.user.first_name 
        };
        
        appState.isAdmin = (currentUser.uid === '132644287' || currentUser.email === 'merser572@gmail.com');
        
        let dName = currentUser.displayName || "Student";
        const settingsName = document.getElementById('settings-name');
        const settingsEmail = document.getElementById('settings-email');
        const settingsAvatar = document.getElementById('settings-avatar');
        if (settingsName) settingsName.innerText = dName;
        if (settingsEmail) settingsEmail.innerText = currentUser.email || "";
        if (settingsAvatar) settingsAvatar.innerText = dName.charAt(0).toUpperCase();

        tg.CloudStorage.getItem('wunder_state', (err, value) => {
            if (!err && value) {
                try {
                    let cloudState = JSON.parse(value);
                    if ((cloudState.xp || 0) >= (appState.xp || 0)) {
                        Object.assign(appState, cloudState);
                    }
                } catch(e){}
            }
            isCloudSynced = true;
            lucide.createIcons();
            updateStats();
            updateHomeUIForLevel();
            loadVocabulary();
        });
        
    } else {
        setupAuth();
        updateHomeUIForLevel();
        await loadVocabulary();
    }
'''
js = re.sub(r'async function initApp\(\) \{.*?(?=    document\.getElementById\(\'level-picker-btn\'\))', tma_init_logic, js, flags=re.DOTALL)

# Modify saveUserDataToCloud
tma_save = '''
async function saveUserDataToCloud() {
    if (!currentUser || !isCloudSynced) return;
    
    if (isTMA) {
        tg.CloudStorage.setItem('wunder_state', JSON.stringify(appState), (err) => {
            if (err) console.error("CloudStorage error", err);
        });
        return;
    }
'''
js = js.replace('async function saveUserDataToCloud() {\n    if (!currentUser || !isCloudSynced) return;', tma_save)


# Premium Modal Logic
premium_logic = '''
function openPremiumModal() {
    playSound('tap');
    document.getElementById('premium-modal').style.display = 'flex';
}

function closePremiumModal() {
    playSound('tap');
    document.getElementById('premium-modal').style.display = 'none';
}

function buyPro(provider) {
    playSound('tap');
    if (!isTMA) {
        showToast("Faqat Telegram bot orqali ishlaydi!");
        return;
    }
    
    tg.sendData(JSON.stringify({
        action: "buy_subscription",
        plan: "monthly_49000",
        provider: provider
    }));
    
    closePremiumModal();
    showToast("To'lov oynasi ochilmoqda...");
}
'''
js += '\n' + premium_logic

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Added TMA logic to app.js")
