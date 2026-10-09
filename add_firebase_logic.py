import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace setupAuth
new_setup_auth = '''
const firebaseConfig = {
  apiKey: "AIzaSyBOkp-2BM9eZRiyd7SfLF7R4yGnBjGeOXc",
  authDomain: "wunder-deutsch.firebaseapp.com",
  projectId: "wunder-deutsch",
  storageBucket: "wunder-deutsch.firebasestorage.app",
  messagingSenderId: "493733820448",
  appId: "1:493733820448:web:af2f19e8cafbcd6aa22445"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.firestore();

// Global user state
let currentUser = null;

function setupAuth() {
    let isLoginMode = true;

    document.getElementById('auth-switch-link').addEventListener('click', (e) => {
        e.preventDefault();
        isLoginMode = !isLoginMode;
        
        if (isLoginMode) {
            document.getElementById('auth-title').innerText = "Welcome back!";
            document.getElementById('login-btn').style.display = 'block';
            document.getElementById('signup-btn').style.display = 'none';
            document.getElementById('auth-switch-text').innerText = "Don't have an account?";
            document.getElementById('auth-switch-link').innerText = "Sign up";
        } else {
            document.getElementById('auth-title').innerText = "Create a new account";
            document.getElementById('login-btn').style.display = 'none';
            document.getElementById('signup-btn').style.display = 'block';
            document.getElementById('auth-switch-text').innerText = "Already have an account?";
            document.getElementById('auth-switch-link').innerText = "Login";
        }
    });
    
    function showError(msg) {
        document.getElementById('login-error').innerText = msg;
        document.getElementById('login-error').style.display = 'block';
        setTimeout(() => { document.getElementById('login-error').style.display = 'none'; }, 5000);
    }

    // Login with Email
    document.getElementById('login-btn').addEventListener('click', async () => {
        const email = document.getElementById('login-email').value.trim();
        const pass = document.getElementById('login-password').value.trim();
        if (!email || !pass) return showError("Please enter email and password");
        
        try {
            document.getElementById('login-btn').innerText = "Logging in...";
            await auth.signInWithEmailAndPassword(email, pass);
        } catch (error) {
            document.getElementById('login-btn').innerText = "Login";
            showError(error.message);
        }
    });
    
    // Sign Up with Email
    document.getElementById('signup-btn').addEventListener('click', async () => {
        const email = document.getElementById('login-email').value.trim();
        const pass = document.getElementById('login-password').value.trim();
        if (!email || !pass) return showError("Please enter email and password");
        if (pass.length < 6) return showError("Password must be at least 6 characters");
        
        try {
            document.getElementById('signup-btn').innerText = "Creating account...";
            await auth.createUserWithEmailAndPassword(email, pass);
        } catch (error) {
            document.getElementById('signup-btn').innerText = "Create Account";
            showError(error.message);
        }
    });

    // Google Sign-In
    document.getElementById('google-login-btn').addEventListener('click', async () => {
        const provider = new firebase.auth.GoogleAuthProvider();
        try {
            await auth.signInWithPopup(provider);
        } catch (error) {
            showError(error.message);
        }
    });

    // Auth State Observer
    auth.onAuthStateChanged(async (user) => {
        if (user) {
            currentUser = user;
            document.getElementById('login-overlay').style.display = 'none';
            document.getElementById('app-container').style.display = 'block';
            
            // Check if admin
            appState.isAdmin = (user.email === 'merser572@gmail.com');
            
            // Sync data with Firestore
            await syncUserData(user.uid);
            
            lucide.createIcons();
            updateStats();
        } else {
            currentUser = null;
            document.getElementById('login-overlay').style.display = 'flex';
            document.getElementById('app-container').style.display = 'none';
            document.getElementById('login-btn').innerText = "Login";
            document.getElementById('signup-btn').innerText = "Create Account";
        }
    });
}

function signOut() {
    auth.signOut();
}

async function syncUserData(uid) {
    const userRef = db.collection('users').doc(uid);
    try {
        const doc = await userRef.get();
        if (doc.exists) {
            const data = doc.data();
            // Load cloud state into local appState
            if (data.xp !== undefined) appState.xp = data.xp;
            if (data.streak !== undefined) appState.streak = data.streak;
            if (data.hearts !== undefined) appState.hearts = data.hearts;
            if (data.lastStreakDate) appState.lastStreakDate = data.lastStreakDate;
            if (data.lastHeartUpdate) appState.lastHeartUpdate = data.lastHeartUpdate;
            if (data.flashcardQueue) appState.flashcardQueue = data.flashcardQueue;
            if (data.currentLevel) appState.currentLevel = data.currentLevel;
        } else {
            // New user, save initial local state to cloud
            await saveUserDataToCloud();
        }
    } catch (e) {
        console.error("Error syncing data:", e);
    }
}

async function saveUserDataToCloud() {
    if (!currentUser) return;
    try {
        await db.collection('users').doc(currentUser.uid).set({
            xp: appState.xp,
            streak: appState.streak,
            hearts: appState.hearts,
            lastStreakDate: appState.lastStreakDate,
            lastHeartUpdate: appState.lastHeartUpdate,
            flashcardQueue: appState.flashcardQueue,
            currentLevel: appState.currentLevel,
            lastActive: firebase.firestore.FieldValue.serverTimestamp()
        }, { merge: true });
    } catch (e) {
        console.error("Error saving data:", e);
    }
}
'''

# Use regex to replace the bypassed setupAuth
js = re.sub(r'function setupAuth\(\) \{.*?(?=\n\}\n\nfunction setupModals)', new_setup_auth + '\n', js, flags=re.DOTALL)

# Add saveUserDataToCloud() calls to important state updates
js = js.replace('appState.xp += amount;', 'appState.xp += amount;\n    saveUserDataToCloud();')
js = js.replace('appState.hearts--;', 'appState.hearts--;\n        saveUserDataToCloud();')
js = js.replace('appState.streak++;', 'appState.streak++;\n        saveUserDataToCloud();')
js = js.replace('appState.streak = 1;', 'appState.streak = 1;\n        saveUserDataToCloud();')
js = js.replace('appState.hearts++;\n                appState.lastHeartUpdate', 'appState.hearts++;\n                appState.lastHeartUpdate')
js = js.replace('localStorage.setItem(\'wunderdeutsch_state\', JSON.stringify(appState));', 'localStorage.setItem(\'wunderdeutsch_state\', JSON.stringify(appState));\n    saveUserDataToCloud();')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Added Firebase logic to app.js")
