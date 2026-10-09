import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

toast_logic = '''
let toastTimeout;
function showComingSoonToast() {
    playSound('tap');
    const toast = document.getElementById('toast-notification');
    if (!toast) return;
    
    let msg = "Tez orada! (Coming soon)";
    if (appState.settings.language === 'en') msg = "Coming soon!";
    if (appState.settings.language === 'de') msg = "Kommt bald!";
    
    document.getElementById('toast-message').innerText = msg;
    
    toast.style.bottom = '40px';
    
    clearTimeout(toastTimeout);
    toastTimeout = setTimeout(() => {
        toast.style.bottom = '-100px';
    }, 3000);
}
'''

if 'function showComingSoonToast' not in js:
    js += '\n' + toast_logic

# Enhance selectLevel to change UI text dynamically
level_enhance = '''
function updateHomeUIForLevel() {
    const isMed = appState.currentLevel === 'Medizin';
    
    // Update Mascot text
    const mascotSub = document.querySelector('.mascot-section .speech-bubble .small');
    if (mascotSub) {
        if (isMed) {
            if (appState.settings.language === 'uz') mascotSub.innerText = "Salom doktor! Tibbiy nemis tilini o'rganamiz!";
            else if (appState.settings.language === 'en') mascotSub.innerText = "Hello doctor! Let's learn Medical German!";
            else mascotSub.innerText = "Hallo Herr Doktor! Lass uns medizinisches Deutsch lernen!";
        } else {
            mascotSub.innerText = TRANSLATIONS[appState.settings.language]['mascot_sub'];
        }
    }
    
    // Update Menu Titles
    const btnDDD = document.querySelector('.menu-card.blue h3');
    const btnSatz = document.querySelector('.menu-card.green h3');
    const btnDict = document.querySelector('.menu-card.yellow h3');
    
    if (btnDDD && btnSatz && btnDict) {
        if (isMed) {
            btnDDD.innerText = "Tibbiyot: Der Die Das";
            btnSatz.innerText = "Klinik Gaplar";
            btnDict.innerText = "Tibbiy Lug'at";
        } else {
            btnDDD.innerText = TRANSLATIONS[appState.settings.language]['title_ddd'];
            btnSatz.innerText = TRANSLATIONS[appState.settings.language]['title_satzbau'];
            btnDict.innerText = TRANSLATIONS[appState.settings.language]['title_dict'];
        }
    }
}
'''

if 'function updateHomeUIForLevel' not in js:
    js += '\n' + level_enhance

# Call it in selectLevel and initApp
js = js.replace('''    renderCategories();
    closeLevelModal();''', '''    renderCategories();
    closeLevelModal();
    updateHomeUIForLevel();''')

js = js.replace('''    let display = appState.currentLevel === 'A1' ? 'Level: A1' : 'Medizin B2 🩺';
    const lvlDisp = document.getElementById('current-level-display');
    if (lvlDisp) lvlDisp.innerText = display;
    
    await loadVocabulary();''', '''    let display = appState.currentLevel === 'A1' ? 'Level: A1' : 'Medizin B2 🩺';
    const lvlDisp = document.getElementById('current-level-display');
    if (lvlDisp) lvlDisp.innerText = display;
    
    updateHomeUIForLevel();
    
    await loadVocabulary();''')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Added Toast logic and dynamic menu text")
