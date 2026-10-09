import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace der diedas subtraction
js = js.replace(
    '''appState.failedCurrentWord = true;
        appState.lives = Math.max(0, appState.lives - 1);
        updateStats();''',
    '''appState.failedCurrentWord = true;
        if (!loseHeart()) return;'''
)

# Replace satzbau init reset
js = js.replace(
    '''appState.satzLives = 5;
    document.getElementById('satz-lives').textContent = appState.satzLives;''',
    '''// appState.satzLives is deprecated; we use global lives now
    updateStats();'''
)

# Replace satzbau subtraction
js = js.replace(
    '''appState.satzLives = Math.max(0, appState.satzLives - 1);
        document.getElementById('satz-lives').textContent = appState.satzLives;''',
    '''if (!loseHeart()) return;'''
)

# Replace alert in loseHeart with custom modal logic
old_lose_heart = '''function loseHeart() {
    if (appState.isAdmin) return true; // Admin never loses hearts
    
    if (appState.lives > 0) {
        appState.lives--;
        appState.lastHeartRegen = Date.now(); // Reset timer if they weren't regenerating
        saveGamificationState();
        updateStats();
        return true;
    } else {
        alert("Sizda yuraklar qolmadi! 30 daqiqa kuting."); // Placeholder for Out of Hearts
        return false;
    }
}'''

new_lose_heart = '''function loseHeart() {
    if (appState.isAdmin) return true; // Admin never loses hearts
    
    if (appState.lives > 0) {
        appState.lives--;
        appState.lastHeartRegen = Date.now(); // Reset timer if they weren't regenerating
        saveGamificationState();
        updateStats();
        
        if (appState.lives === 0) {
            showNoHeartsModal();
            return false;
        }
        return true;
    } else {
        showNoHeartsModal();
        return false;
    }
}

function showNoHeartsModal() {
    const m = document.getElementById('no-hearts-modal');
    if(m) m.style.display = 'flex';
}
function closeNoHeartsModal() {
    const m = document.getElementById('no-hearts-modal');
    if(m) m.style.display = 'none';
    switchView('home'); // Send them home so they don't get stuck in a broken game loop
}
'''
js = js.replace(old_lose_heart, new_lose_heart)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated loseHeart logic")
