import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_login_html = '''
    <div id="login-overlay" style="display:flex; position:fixed; top:0; left:0; width:100%; height:100%; background:var(--bg-color); z-index:9999; justify-content:center; align-items:center; padding:20px;">
        <div style="background:white; padding:32px; border-radius:24px; box-shadow:0 8px 0 #DFE6E9; width:100%; max-width:400px; text-align:center;">
            <h2 style="margin-bottom:8px; font-size:24px; font-weight:800;">WunderDeutsch</h2>
            <p style="color:var(--text-muted); margin-bottom:24px;" id="auth-title">Welcome back!</p>
            
            <button id="google-login-btn" class="action-btn" style="width:100%; margin-bottom:16px; background:white; color:#333; border:2px solid #DFE6E9; box-shadow:0 4px 0 #DFE6E9; display:flex; justify-content:center; align-items:center; gap:8px;">
                <svg width="24" height="24" viewBox="0 0 48 48"><path fill="#FFC107" d="M43.611,20.083H42V20H24v8h11.303c-1.649,4.657-6.08,8-11.303,8c-6.627,0-12-5.373-12-12c0-6.627,5.373-12,12-12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C12.955,4,4,12.955,4,24c0,11.045,8.955,20,20,20c11.045,0,20-8.955,20-20C44,22.659,43.862,21.35,43.611,20.083z"/><path fill="#FF3D00" d="M6.306,14.691l6.571,4.819C14.655,15.108,18.961,12,24,12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C16.318,4,9.656,8.337,6.306,14.691z"/><path fill="#4CAF50" d="M24,44c5.166,0,9.86-1.977,13.409-5.192l-6.19-5.238C29.211,35.091,26.715,36,24,36c-5.202,0-9.619-3.317-11.283-7.946l-6.522,5.025C9.505,39.556,16.227,44,24,44z"/><path fill="#1976D2" d="M43.611,20.083H42V20H24v8h11.303c-0.792,2.237-2.231,4.166-4.087,5.571c0.001-0.001,0.002-0.001,0.003-0.002l6.19,5.238C36.971,39.205,44,34,44,24C44,22.659,43.862,21.35,43.611,20.083z"/></svg>
                Continue with Google
            </button>
            
            <div style="display:flex; align-items:center; margin-bottom:16px;">
                <div style="flex:1; height:1px; background:#DFE6E9;"></div>
                <span style="padding:0 12px; color:var(--text-muted); font-size:14px; font-weight:700;">OR</span>
                <div style="flex:1; height:1px; background:#DFE6E9;"></div>
            </div>
            
            <input type="email" id="login-email" placeholder="Email" style="width:100%; padding:14px; border-radius:12px; border:2px solid #DFE6E9; margin-bottom:12px; font-size:16px;">
            <input type="password" id="login-password" placeholder="Password" style="width:100%; padding:14px; border-radius:12px; border:2px solid #DFE6E9; margin-bottom:24px; font-size:16px;">
            
            <p id="login-error" style="color:var(--red-btn); font-weight:700; margin-bottom:12px; display:none;">Error goes here</p>
            
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

# Add logout button in settings
logout_btn = '''
                <div style="height: 1px; background: #DFE6E9; margin: 24px 0;"></div>
                <button class="action-btn" onclick="signOut()" style="width: 100%; background: var(--red-btn); color: white; box-shadow: 0 4px 0 var(--red-shadow);">
                    <i data-lucide="log-out"></i> Sign Out
                </button>
'''
if 'onclick="signOut()"' not in html:
    html = html.replace('</div>\n            </div>\n        </div>\n    </div>\n\n    <!-- Level Selector Modal -->', logout_btn + '\n            </div>\n        </div>\n    </div>\n\n    <!-- Level Selector Modal -->')


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html with new Auth UI")
