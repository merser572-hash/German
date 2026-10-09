import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the plain text AUTH variables and login logic
old_login_setup = '''function setupAuth() {
    if (localStorage.getItem('wunderdeutsch_auth') === 'true') {
        document.getElementById('login-overlay').style.display = 'none';
        document.getElementById('app-container').style.display = 'block';
    } else {
        document.getElementById('login-overlay').style.display = 'flex';
        document.getElementById('app-container').style.display = 'none';
    }

    document.getElementById('login-btn').addEventListener('click', () => {
        if (document.getElementById('login-email').value === AUTH_EMAIL && document.getElementById('login-password').value === AUTH_PASS) {
            localStorage.setItem('wunderdeutsch_auth', 'true');
            document.getElementById('login-overlay').style.display = 'none';
            document.getElementById('app-container').style.display = 'block';
            lucide.createIcons();
        } else {
            document.getElementById('login-error').style.display = 'block';
            setTimeout(() => { document.getElementById('login-error').style.display = 'none'; }, 3000);
        }
    });
}'''

new_login_setup = '''
const AUTH_EMAIL = 'merser572@gmail.com';
const AUTH_HASH = '6453ba4d214e588984f5cb12790af9dff617a43f835a429e67b8b69166c58532';

async function hashPassword(password) {
    const encoder = new TextEncoder();
    const data = encoder.encode(password);
    const hashBuffer = await crypto.subtle.digest('SHA-256', data);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}

function setupAuth() {
    if (localStorage.getItem('wunderdeutsch_auth') === 'true') {
        document.getElementById('login-overlay').style.display = 'none';
        document.getElementById('app-container').style.display = 'block';
    } else {
        document.getElementById('login-overlay').style.display = 'flex';
        document.getElementById('app-container').style.display = 'none';
    }

    document.getElementById('login-btn').addEventListener('click', async () => {
        const emailInput = document.getElementById('login-email').value.trim().toLowerCase();
        const passInput = document.getElementById('login-password').value;
        const hashedInput = await hashPassword(passInput);
        
        if (emailInput === AUTH_EMAIL && hashedInput === AUTH_HASH) {
            localStorage.setItem('wunderdeutsch_auth', 'true');
            document.getElementById('login-overlay').style.display = 'none';
            document.getElementById('app-container').style.display = 'block';
            lucide.createIcons();
        } else {
            document.getElementById('login-error').style.display = 'block';
            setTimeout(() => { document.getElementById('login-error').style.display = 'none'; }, 3000);
        }
    });
}'''

# We also need to remove the top-level AUTH_EMAIL and AUTH_PASS declarations
js = re.sub(r"const AUTH_EMAIL = 'merser572@gmail.com';\s*const AUTH_PASS = 'Hasanboy0412';", "", js)

# Replace setupAuth
js = re.sub(r'function setupAuth\(\) \{.*?(?=\n\}\n\nfunction setupModals)', new_login_setup + '\n', js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Encrypted login setup complete.")
