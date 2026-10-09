import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_login_html = '''
    <div id="login-overlay" style="display:flex; position:fixed; top:0; left:0; width:100%; height:100%; background:var(--bg-color); z-index:9999; justify-content:center; align-items:center; padding:20px;">
        <div style="background:white; padding:32px; border-radius:24px; box-shadow:0 8px 0 #DFE6E9; width:100%; max-width:400px; text-align:center;">
            <h2 style="margin-bottom:8px; font-size:24px; font-weight:800;">WunderDeutsch</h2>
            <p style="color:var(--text-muted); margin-bottom:24px;" id="auth-title">Welcome back!</p>
            
            <input type="email" id="login-email" placeholder="Email" style="width:100%; padding:14px; border-radius:12px; border:2px solid #DFE6E9; margin-bottom:12px; font-size:16px;">
            <input type="password" id="login-password" placeholder="Password" style="width:100%; padding:14px; border-radius:12px; border:2px solid #DFE6E9; margin-bottom:24px; font-size:16px;">
            
            <p id="login-error" style="color:var(--red-btn); font-weight:700; margin-bottom:12px; display:none;">Incorrect credentials.</p>
            
            <button id="login-btn" class="action-btn primary-btn" style="width:100%; margin-bottom: 16px;">Login</button>
            <button id="signup-btn" class="action-btn" style="width:100%; background:var(--blue-btn); box-shadow: 0 4px 0 var(--blue-shadow); color:white; display:none;">Create Account</button>
            
            <p style="font-size: 14px; color: var(--text-muted); margin-top: 16px;">
                <span id="auth-switch-text">Don't have an account?</span> 
                <a href="#" id="auth-switch-link" style="color:var(--primary-btn); font-weight:700;">Sign up</a>
            </p>
        </div>
    </div>
'''

html = re.sub(r'<div id="login-overlay".*?</p>\s*</div>\s*</div>', new_login_html, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated login overlay UI")
