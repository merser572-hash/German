import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace syncUserData to use real-time onSnapshot
new_sync_logic = '''
let unsubscribeSnapshot = null;

async function syncUserData(uid) {
    const userRef = db.collection('users').doc(uid);
    
    // Unsubscribe from previous listener if exists
    if (unsubscribeSnapshot) unsubscribeSnapshot();
    
    unsubscribeSnapshot = userRef.onSnapshot((doc) => {
        if (doc.exists) {
            const data = doc.data();
            // Load cloud state into local appState
            if (data.xp !== undefined) {
                appState.xp = data.xp;
                document.getElementById('xp').innerText = appState.xp;
            }
            if (data.streak !== undefined) {
                appState.streak = data.streak;
                document.getElementById('streak').innerText = appState.streak;
            }
            if (data.hearts !== undefined) {
                appState.hearts = data.hearts;
                document.getElementById('lives').innerText = appState.hearts === 9999 ? '∞' : appState.hearts;
            }
            if (data.lastStreakDate) appState.lastStreakDate = data.lastStreakDate;
            if (data.lastHeartUpdate) appState.lastHeartUpdate = data.lastHeartUpdate;
            if (data.progress !== undefined) appState.progress = data.progress;
            if (data.flashcardQueue) appState.flashcardQueue = data.flashcardQueue;
            if (data.currentLevel) appState.currentLevel = data.currentLevel;
            
            // Save to local storage just in case they go offline
            localStorage.setItem('wunderdeutsch_state', JSON.stringify(appState));
        } else {
            // New user, save initial local state to cloud
            saveUserDataToCloud();
        }
    }, (error) => {
        console.error("Error listening to real-time data:", error);
    });
}
'''

js = re.sub(r'async function syncUserData\(uid\) \{.*?(?=\nasync function saveUserDataToCloud)', new_sync_logic, js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Added real-time Firestore sync")
