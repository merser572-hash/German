import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix checkArticle to provide explanation on correct answer as well
new_checkArticle = '''function checkArticle(guess) {
    if(!appState.dddWord) return;
    
    const correctArticle = appState.dddWord.article.toLowerCase();
    const correctMsg = TRANSLATIONS[appState.settings.language]['msg_correct'];
    const wrongMsg = TRANSLATIONS[appState.settings.language]['msg_ohno'];

    const explanation = typeof getGrammarExplanation === 'function' ? getGrammarExplanation(appState.dddWord, appState.settings.language) : '';

    if(guess === correctArticle) {
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
        
        // Hide local fox
        const foxCont = document.getElementById('ddd-local-fox');
        if (foxCont) foxCont.style.display = 'none';
        
        // Show global fox with tip!
        showMascot(`${correctMsg} 🎉<br><span style="font-size:14px; opacity:0.9; margin-top:5px; display:block; font-weight:normal;">${explanation}</span>`, 2500);
        
        showDDDExtra();
    } else {
        appState.failedCurrentWord = true;
        appState.lives = Math.max(0, appState.lives - 1);
        updateStats();
        playSound('error');
        triggerVibrate([40, 40, 40]);
        
        const wrongBtn = document.querySelector(`.btn-${guess}`);
        if(wrongBtn) wrongBtn.classList.add('btn-disabled');
        
        // Show global fox with tip!
        showMascot(`${wrongMsg} "${appState.dddWord.article} ${appState.dddWord.word}".<br><span style="font-size:14px; opacity:0.9; margin-top:5px; display:block; font-weight:normal;">${explanation}</span>`, 3000);
        
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
print('Fixed checkArticle tips')
