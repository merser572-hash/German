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
        if (checkBtn) checkBtn.style.display = 'none';
        
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
        
        // Shake animation
        dropzone.style.transition = 'transform 0.05s';
        dropzone.style.transform = 'translateX(5px)';
        setTimeout(() => dropzone.style.transform = 'translateX(-5px)', 50);
        setTimeout(() => dropzone.style.transform = 'translateX(5px)', 100);
        setTimeout(() => dropzone.style.transform = 'translateX(-5px)', 150);
        setTimeout(() => dropzone.style.transform = 'translateX(0)', 200);
        
        // Show the error box
        if (checkBtn) checkBtn.style.display = 'none';
        if (errorBox) {
            errorBox.style.display = 'block';
            document.getElementById('satzbau-correct-text').innerText = appState.currentSentence.de;
            if (appState.currentSentence.explanation) {
                document.getElementById('satzbau-explanation').innerText = appState.currentSentence.explanation;
            } else {
                document.getElementById('satzbau-explanation').innerText = "Nemis tilida darak gaplarda fe'l 2-o'rinda keladi.";
            }
        }
    }
}'''

# Replace from `function checkSatzbau()` until `// --- GRAMMAR TAB LOGIC ---`
js = re.sub(r'function checkSatzbau\(\) \{.*?(?=// --- GRAMMAR TAB LOGIC ---)', new_checkSatzbau + '\n\n', js, flags=re.DOTALL)

# And fix startSatzbauRound to hide the error box if it exists
old_startSatz = "document.getElementById('satz-check-btn').style.display = 'none';"
new_startSatz = '''document.getElementById('satz-check-btn').style.display = 'none';
    const eb = document.getElementById('satzbau-error-box');
    if(eb) eb.style.display = 'none';
    document.getElementById('satz-dropzone').style.borderColor = '#ccc';
    document.getElementById('satz-dropzone').style.backgroundColor = '#f7f7f7';'''
js = js.replace(old_startSatz, new_startSatz)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('Satzbau logic REALLY fixed this time!')
