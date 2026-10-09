import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Completely bypass the login screen
js = js.replace(
'''function setupAuth() {
    if (localStorage.getItem('wunderdeutsch_auth') === 'true') {
        document.getElementById('login-overlay').style.display = 'none';
        document.getElementById('app-container').style.display = 'block';
    } else {
        document.getElementById('login-overlay').style.display = 'flex';
        document.getElementById('app-container').style.display = 'none';
    }''',
'''function setupAuth() {
    // TEMPORARY BYPASS to unblock the user completely
    localStorage.setItem('wunderdeutsch_auth', 'true');
    appState.isAdmin = true;
    
    document.getElementById('login-overlay').style.display = 'none';
    document.getElementById('app-container').style.display = 'block';
    
    if (localStorage.getItem('wunderdeutsch_auth') === 'true') {
        // intentionally empty to avoid parsing issues from regex
    } else {
        // intentionally empty
    }'''
)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Bypassed login screen completely")
