import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix appState initialization for lives
js = js.replace("lives: parseInt(localStorage.getItem('wunder_lives') || 5)", "lives: parseInt(localStorage.getItem('wunder_lives') || 20)")

# Fix regen logic (5 -> 20)
js = js.replace("if (mins >= 30 && appState.lives < 5)", "if (mins >= 30 && appState.lives < 20)")
js = js.replace("appState.lives = Math.min(5, appState.lives + heartsToAdd)", "appState.lives = Math.min(20, appState.lives + heartsToAdd)")

# Fix syncUserData
js = js.replace("appState.hearts = data.hearts;", "appState.lives = data.hearts;")
js = js.replace("document.getElementById('lives').innerText = appState.hearts === 9999 ? '∞' : appState.hearts;", "document.getElementById('lives').innerText = appState.lives === 9999 ? '∞' : appState.lives;")

# Fix saveUserDataToCloud
js = js.replace("hearts: appState.hearts,", "hearts: appState.lives,")


# Add Modal functions
modal_funcs = '''
let heartTimerInterval;

function openHeartModal() {
    playSound('tap');
    document.getElementById('heart-modal').style.display = 'flex';
    document.getElementById('heart-modal-count').innerText = appState.isAdmin ? '∞' : appState.lives;
    
    updateHeartCountdown();
    heartTimerInterval = setInterval(updateHeartCountdown, 1000);
}

function closeHeartModal() {
    playSound('tap');
    document.getElementById('heart-modal').style.display = 'none';
    clearInterval(heartTimerInterval);
}

function updateHeartCountdown() {
    if (appState.isAdmin || appState.lives >= 20) {
        document.getElementById('heart-countdown').innerText = "Full!";
        return;
    }
    
    const now = Date.now();
    const diff = now - appState.lastHeartRegen;
    const remainingMs = (30 * 60000) - (diff % (30 * 60000));
    
    const mins = Math.floor(remainingMs / 60000);
    const secs = Math.floor((remainingMs % 60000) / 1000);
    
    document.getElementById('heart-countdown').innerText = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
}
'''
js += '\n' + modal_funcs

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated app.js with 20 hearts limit and modal logic")
