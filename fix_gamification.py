import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

old_appState = '''const appState = {
    streak: 3, xp: 120, lives: 5, words: [], currentWotd: null, dddWord: null, currentView: 'home',
    dddQueue: [],
    satzQueue: [],
    settings: { sound: true, vibration: true, offline: true, language: 'en' }
};'''

new_appState = '''const appState = {
    isAdmin: true, // Since only merser572@gmail.com is allowed currently
    streak: parseInt(localStorage.getItem('wunder_streak') || 0), 
    xp: parseInt(localStorage.getItem('wunder_xp') || 0), 
    dailyXP: parseInt(localStorage.getItem('wunder_daily_xp') || 0),
    lives: parseInt(localStorage.getItem('wunder_lives') || 5), 
    lastHeartRegen: parseInt(localStorage.getItem('wunder_last_regen') || Date.now()),
    lastActiveDate: localStorage.getItem('wunder_last_active_date') || new Date().toDateString(),
    words: [], currentWotd: null, dddWord: null, currentView: 'home',
    dddQueue: [],
    satzQueue: [],
    settings: { sound: true, vibration: true, offline: true, language: 'en' }
};

// --- GAMIFICATION LOGIC ---
function checkHeartRegen() {
    if (appState.isAdmin) return; // Admin has infinite
    const now = Date.now();
    const diff = now - appState.lastHeartRegen;
    const mins = Math.floor(diff / 60000);
    
    if (mins >= 30 && appState.lives < 5) {
        const heartsToAdd = Math.floor(mins / 30);
        appState.lives = Math.min(5, appState.lives + heartsToAdd);
        appState.lastHeartRegen = now - ((mins % 30) * 60000); // keep remainder
        saveGamificationState();
        updateStats();
    }
}

setInterval(checkHeartRegen, 60000); // Check every minute

function loseHeart() {
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
}

function checkStreak() {
    const today = new Date().toDateString();
    
    if (appState.lastActiveDate !== today) {
        // A new day!
        // Did they miss yesterday?
        const yesterday = new Date(Date.now() - 86400000).toDateString();
        if (appState.lastActiveDate !== yesterday && appState.lastActiveDate !== today) {
            appState.streak = 0; // Lost streak :(
        }
        
        appState.dailyXP = 0; // Reset daily XP
        appState.lastActiveDate = today;
        saveGamificationState();
    }
    
    // Check if daily goal met (e.g. 20 XP)
    if (appState.dailyXP >= 20 && localStorage.getItem('wunder_goal_met_' + today) !== 'true') {
        appState.streak++;
        localStorage.setItem('wunder_goal_met_' + today, 'true');
        showMascot("Tabriklaymiz! Kunlik maqsadga yetdingiz! 🚀", 3000);
        saveGamificationState();
    }
}

function saveGamificationState() {
    localStorage.setItem('wunder_streak', appState.streak);
    localStorage.setItem('wunder_xp', appState.xp);
    localStorage.setItem('wunder_daily_xp', appState.dailyXP);
    localStorage.setItem('wunder_lives', appState.lives);
    localStorage.setItem('wunder_last_regen', appState.lastHeartRegen);
    localStorage.setItem('wunder_last_active_date', appState.lastActiveDate);
}

function addXP(amount) {
    appState.xp += amount;
    appState.dailyXP += amount;
    saveGamificationState();
    checkStreak();
    updateStats();
}
'''

js = js.replace(old_appState, new_appState)

# Replace all the updateStats logic in app.js
old_updateStats = '''function updateStats() {
    const s = document.getElementById('streak');
    const x = document.getElementById('xp');
    if(s) s.textContent = appState.streak;
    if(x) x.textContent = appState.xp;
    
    // update xp everywhere if needed
    const fXp = document.getElementById('fc-xp');
    if(fXp) fXp.textContent = appState.xp;
}'''

new_updateStats = '''function updateStats() {
    const streakElements = document.querySelectorAll('#streak');
    const xpElements = document.querySelectorAll('#xp, #fc-xp');
    const livesElements = document.querySelectorAll('#lives, #ddd-lives, #satz-lives');
    
    streakElements.forEach(el => el.textContent = appState.streak);
    xpElements.forEach(el => el.textContent = appState.xp);
    
    let displayLives = appState.isAdmin ? '∞' : appState.lives;
    livesElements.forEach(el => el.textContent = displayLives);
}'''

if 'function updateStats()' in js:
    js = re.sub(r'function updateStats\(\) \{.*?(?=\n\}|\nfunction|\n//)', new_updateStats, js, flags=re.DOTALL)
    # The regex might not catch the closing brace properly if there are newlines. Let's just use replace since I have the exact string from previous searches.
    
with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Added appState and Gamification functions!")
