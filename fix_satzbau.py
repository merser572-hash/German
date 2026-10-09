import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_checkSatzbau = '''function checkSatzbau() {
    const target = appState.currentSentence.de.replace(/[.!?]/g, '').toLowerCase().trim();
    
    const dropzone = document.getElementById('satz-dropzone');
    const currentWords = [];
    dropzone.querySelectorAll('.satz-tile').forEach(btn => {
        currentWords.push(btn.textContent);
    });
    const current = currentWords.join(' ').toLowerCase().trim();
    const checkBtn = document.getElementById('satz-check-btn');
    const errorBox = document.getElementById('satzbau-error-box');
    
    if (current === target) {
        playSound('success');
        appState.xp += 15;
        updateStats();
        dropzone.style.borderColor = 'var(--green-btn)';
        dropzone.style.backgroundColor = '#e8fce8';
        checkBtn.style.display = 'none';
        
        // Show correct mascot!
        const correctMsg = TRANSLATIONS[appState.settings.language]['msg_correct'];
        showMascot(correctMsg, 1500);
        
        setTimeout(() => {
            dropzone.style.borderColor = '#ccc';
            dropzone.style.backgroundColor = '#f7f7f7';
            startSatzbauRound();
        }, 1500);
    } else {
        playSound('error');
        appState.satzLives = Math.max(0, appState.satzLives - 1);
        document.getElementById('satz-lives').textContent = appState.satzLives;
        
        dropzone.style.borderColor = 'var(--red-btn)';
        dropzone.style.backgroundColor = '#ffebeb';
        
        // Show the error box
        checkBtn.style.display = 'none';
        errorBox.style.display = 'block';
        document.getElementById('satzbau-correct-text').innerText = appState.currentSentence.de;
        if (appState.currentSentence.explanation) {
            document.getElementById('satzbau-explanation').innerText = appState.currentSentence.explanation;
        } else {
            document.getElementById('satzbau-explanation').innerText = "Gapdagi fe'l doimo 2-o'rinda kelishi kerak (darak gaplarda).";
        }
    }
}'''

js = re.sub(r'function checkSatzbau\(\) \{.*?(?=function startSatzbauRound)', new_checkSatzbau + '\n\n', js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('Satzbau check logic fixed')
