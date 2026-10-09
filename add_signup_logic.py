import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

auth_logic_new = '''
function setupAuth() {
    if (localStorage.getItem('wunderdeutsch_auth') === 'true') {
        document.getElementById('login-overlay').style.display = 'none';
        document.getElementById('app-container').style.display = 'block';
    } else {
        document.getElementById('login-overlay').style.display = 'flex';
        document.getElementById('app-container').style.display = 'none';
    }
    
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

    document.getElementById('login-btn').addEventListener('click', async () => {
        const emailInput = document.getElementById('login-email').value.trim().toLowerCase();
        const passInput = document.getElementById('login-password').value.trim();
        const hashedInput = await hashPassword(passInput);
        
        if (emailInput === AUTH_EMAIL && hashedInput === AUTH_HASH) {
            localStorage.setItem('wunderdeutsch_auth', 'true');
            document.getElementById('login-overlay').style.display = 'none';
            document.getElementById('app-container').style.display = 'block';
            lucide.createIcons();
        } else {
            document.getElementById('login-error').innerText = "Incorrect credentials.";
            document.getElementById('login-error').style.display = 'block';
            setTimeout(() => { document.getElementById('login-error').style.display = 'none'; }, 3000);
        }
    });
    
    document.getElementById('signup-btn').addEventListener('click', () => {
        // Mock Signup for frontend demonstration
        const emailInput = document.getElementById('login-email').value.trim();
        const passInput = document.getElementById('login-password').value.trim();
        
        if (emailInput.length < 5 || passInput.length < 6) {
            document.getElementById('login-error').innerText = "Email or password too short.";
            document.getElementById('login-error').style.display = 'block';
            setTimeout(() => { document.getElementById('login-error').style.display = 'none'; }, 3000);
            return;
        }
        
        alert("Success! Your account is created locally. In Phase 5, this will save to the Firebase database!");
        localStorage.setItem('wunderdeutsch_auth', 'true');
        appState.isAdmin = false; // New users are not admins!
        updateStats();
        
        document.getElementById('login-overlay').style.display = 'none';
        document.getElementById('app-container').style.display = 'block';
        lucide.createIcons();
    });
}
'''

js = re.sub(r'function setupAuth\(\) \{.*?(?=\n\}\n\nfunction setupModals)', auth_logic_new + '\n', js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated auth logic in app.js")
