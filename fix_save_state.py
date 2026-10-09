import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

save_gamification = '''
function saveGamificationState() {
    localStorage.setItem('wunder_streak', appState.streak);
    localStorage.setItem('wunder_xp', appState.xp);
    localStorage.setItem('wunder_daily_xp', appState.dailyXP);
    localStorage.setItem('wunder_lives', appState.lives);
    localStorage.setItem('wunder_last_regen', appState.lastHeartRegen);
    localStorage.setItem('wunder_last_active_date', appState.lastActiveDate);
    
    // Always mirror gamification state to cloud immediately
    if (typeof saveUserDataToCloud === 'function') {
        saveUserDataToCloud();
    }
}
'''

js = re.sub(r'function saveGamificationState\(\) \{.*?(?=\n\}\n\nfunction addXP)', save_gamification.strip(), js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated saveGamificationState to trigger cloud sync")
