import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_inputs = '''
            <input type="text" id="signup-name" placeholder="Your Name" style="width:100%; padding:14px; border-radius:12px; border:2px solid #DFE6E9; margin-bottom:12px; font-size:16px; display:none;">
            <input type="email" id="login-email" placeholder="Email" style="width:100%; padding:14px; border-radius:12px; border:2px solid #DFE6E9; margin-bottom:12px; font-size:16px;">
            <input type="password" id="login-password" placeholder="Password" style="width:100%; padding:14px; border-radius:12px; border:2px solid #DFE6E9; margin-bottom:12px; font-size:16px;">
            <input type="password" id="signup-password-confirm" placeholder="Confirm Password" style="width:100%; padding:14px; border-radius:12px; border:2px solid #DFE6E9; margin-bottom:24px; font-size:16px; display:none;">
'''

# Replace the old inputs
html = re.sub(r'<input type="email" id="login-email".*?<input type="password" id="login-password".*?>', new_inputs, html, flags=re.DOTALL)

# Fix the button styling
html = html.replace(
    '<button id="signup-btn" class="action-btn" style="width:100%; background:var(--blue-btn); box-shadow: 0 4px 0 var(--blue-shadow); color:white; display:none;">Create Account</button>',
    '<button id="signup-btn" class="action-btn" style="width:100%; padding:16px; font-size:18px; font-weight:800; background:var(--blue-btn); box-shadow: 0 4px 0 var(--blue-shadow); color:white; display:none;">Create Account</button>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html inputs and buttons")
