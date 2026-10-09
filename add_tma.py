import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Inject Telegram SDK
if '<script src="https://telegram.org/js/telegram-web-app.js"></script>' not in html:
    html = html.replace('<!-- App Scripts -->', '<!-- App Scripts -->\n    <script src="https://telegram.org/js/telegram-web-app.js"></script>')

# Premium Modal
premium_modal = '''
    <!-- Premium Subscription Modal -->
    <div id="premium-modal" class="modal-overlay" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:9999; justify-content:center; align-items:center; padding:20px;">
        <div style="background:var(--card-bg); padding:32px; border-radius:24px; text-align:center; max-width:400px; width:100%; box-shadow:0 8px 0 rgba(0,0,0,0.1);">
            <div style="font-size:48px; margin-bottom:16px;">👑</div>
            <h2 style="font-size:24px; font-weight:800; margin-bottom:8px;">WunderDeutsch Pro</h2>
            <p style="color:var(--text-muted); margin-bottom:24px;">A1-B1 to'liq kurs, tibbiy nemis tili va cheksiz jonlar!</p>
            
            <button class="action-btn" onclick="buyPro('click')" style="width:100%; background:#00AEEF; color:white; box-shadow: 0 4px 0 #007BB5; margin-bottom:16px;">
                <i data-lucide="credit-card"></i> Click orqali to'lash (49,000 UZS)
            </button>
            
            <button class="action-btn" onclick="buyPro('stars')" style="width:100%; background:#FDCB6E; color:var(--text-dark); box-shadow: 0 4px 0 #E1B12C; margin-bottom:24px;">
                <i data-lucide="star"></i> Pay with Telegram Stars
            </button>
            
            <button class="action-btn" onclick="closePremiumModal()" style="width:100%; background:#DFE6E9; color:var(--text-dark); box-shadow: 0 4px 0 #B0BEC5;">Keyinroq</button>
        </div>
    </div>
'''

if 'id="premium-modal"' not in html:
    html = html.replace('<!-- Level Selector Modal -->', premium_modal + '\n    <!-- Level Selector Modal -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Injected Telegram SDK and Premium Modal")
