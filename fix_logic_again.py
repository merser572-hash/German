import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix 1: initDerDieDas sets flex instead of grid
js = js.replace(
    "document.getElementById('ddd-buttons-container').style.display = 'flex';",
    "document.getElementById('ddd-buttons-container').style.display = 'grid';"
)

# Fix 2: rewrite checkArticle completely to use local fox & DDDExtra properly
new_checkArticle = '''function checkArticle(guess) {
    if(!appState.dddWord) return;
    
    const correctArticle = appState.dddWord.article.toLowerCase();
    
    if(guess === correctArticle) {
        // Correct answer! Disable all buttons to prevent double tap
        document.querySelectorAll('.ddd-controls .btn-3d').forEach(b => {
            b.disabled = true;
            b.classList.add('btn-disabled');
        });
        const correctBtn = document.querySelector(`.btn-${correctArticle}`);
        if(correctBtn) correctBtn.classList.remove('btn-disabled');

        if (!appState.failedCurrentWord) {
            appState.xp += 10;
            updateStats();
        }

        playSound('success');
        triggerVibrate(40);
        
        // Hide fox
        const foxCont = document.getElementById('ddd-local-fox');
        if (foxCont) foxCont.style.display = 'none';
        
        showDDDExtra();
    } else {
        // Wrong answer!
        appState.failedCurrentWord = true;
        appState.lives = Math.max(0, appState.lives - 1);
        updateStats();
        playSound('error');
        triggerVibrate([40, 40, 40]);
        
        const wrongBtn = document.querySelector(`.btn-${guess}`);
        if(wrongBtn) wrongBtn.classList.add('btn-disabled');
        
        // Show local angry fox
        const foxCont = document.getElementById('ddd-local-fox');
        const foxMsg = document.getElementById('ddd-local-fox-msg');
        if (foxCont) {
            foxCont.style.display = 'flex';
            foxMsg.innerText = TRANSLATIONS[appState.settings.language]['msg_ohno'] || "Xato! Qaytadan urinib ko'ring.";
        }
    }
}'''

js = re.sub(r'function checkArticle\(guess\) \{.*?(?=function initDerDieDas)', new_checkArticle + '\n\n', js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('Fixed logic!')
