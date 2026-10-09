import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Update setupAuth to toggle new fields
auth_toggle = '''
    document.getElementById('auth-switch-link').addEventListener('click', (e) => {
        e.preventDefault();
        isLoginMode = !isLoginMode;
        
        if (isLoginMode) {
            document.getElementById('auth-title').innerText = "Welcome back!";
            document.getElementById('login-btn').style.display = 'block';
            document.getElementById('signup-btn').style.display = 'none';
            document.getElementById('auth-switch-text').innerText = "Don't have an account?";
            document.getElementById('auth-switch-link').innerText = "Sign up";
            
            document.getElementById('signup-name').style.display = 'none';
            document.getElementById('signup-password-confirm').style.display = 'none';
            document.getElementById('login-password').style.marginBottom = '24px';
        } else {
            document.getElementById('auth-title').innerText = "Create a new account";
            document.getElementById('login-btn').style.display = 'none';
            document.getElementById('signup-btn').style.display = 'block';
            document.getElementById('auth-switch-text').innerText = "Already have an account?";
            document.getElementById('auth-switch-link').innerText = "Login";
            
            document.getElementById('signup-name').style.display = 'block';
            document.getElementById('signup-password-confirm').style.display = 'block';
            document.getElementById('login-password').style.marginBottom = '12px';
        }
    });
'''
js = re.sub(r"document\.getElementById\('auth-switch-link'\)\.addEventListener\('click', \(e\) => \{.*?\}\);", auth_toggle, js, flags=re.DOTALL)


# Update Signup logic to use name and confirm password
signup_logic = '''
    // Sign Up with Email
    document.getElementById('signup-btn').addEventListener('click', async () => {
        const name = document.getElementById('signup-name').value.trim();
        const email = document.getElementById('login-email').value.trim();
        const pass = document.getElementById('login-password').value.trim();
        const confirmPass = document.getElementById('signup-password-confirm').value.trim();
        
        if (!name) return showError("Please enter your name");
        if (!email || !pass) return showError("Please enter email and password");
        if (pass.length < 6) return showError("Password must be at least 6 characters");
        if (pass !== confirmPass) return showError("Passwords do not match");
        
        try {
            document.getElementById('signup-btn').innerText = "Creating account...";
            const userCredential = await auth.createUserWithEmailAndPassword(email, pass);
            await userCredential.user.updateProfile({
                displayName: name
            });
            // Force reload to get updated profile in onAuthStateChanged
            window.location.reload();
        } catch (error) {
            document.getElementById('signup-btn').innerText = "Create Account";
            showError(error.message);
        }
    });
'''
js = re.sub(r"// Sign Up with Email.*?\}\);", signup_logic, js, flags=re.DOTALL)


# Update Mascot text
mascot_logic = '''
function updateHomeUIForLevel() {
    const isMed = appState.currentLevel === 'Medizin';
    
    // Update Mascot text
    const mascotTitle = document.querySelector('.mascot-section .speech-bubble .large');
    const mascotSub = document.querySelector('.mascot-section .speech-bubble .small');
    
    let userName = currentUser && currentUser.displayName ? currentUser.displayName.split(' ')[0] : '';
    
    if (mascotTitle) {
        if (appState.settings.language === 'uz') mascotTitle.innerText = userName ? `Salom ${userName}! Men Fritsman.` : `Salom! Men Fritsman.`;
        else if (appState.settings.language === 'en') mascotTitle.innerText = userName ? `Hello ${userName}! I'm Fritz.` : `Hello! I'm Fritz.`;
        else mascotTitle.innerText = userName ? `Hallo ${userName}! Ich bin Fritz.` : `Hallo! Ich bin Fritz.`;
    }
    
    if (mascotSub) {
        if (isMed) {
            if (appState.settings.language === 'uz') mascotSub.innerText = "Salom doktor! Tibbiy nemis tilini o'rganamiz!";
            else if (appState.settings.language === 'en') mascotSub.innerText = "Hello doctor! Let's learn Medical German!";
            else mascotSub.innerText = "Hallo Herr Doktor! Lass uns medizinisches Deutsch lernen!";
        } else {
            mascotSub.innerText = TRANSLATIONS[appState.settings.language]['mascot_sub'];
        }
    }
'''
js = re.sub(r"function updateHomeUIForLevel\(\) \{.*?(?=    // Update Menu Titles)", mascot_logic, js, flags=re.DOTALL)


# Also need to call updateHomeUIForLevel() when auth state changes so name appears immediately
auth_state = '''
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
            updateHomeUIForLevel();
        } else {
'''
js = re.sub(r"// Auth State Observer.*?\} else \{", auth_state, js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated app.js with new signup and mascot logic")
