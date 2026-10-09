import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the single Click button with the 3 tiers
new_buttons = '''
            <div style="display:flex; flex-direction:column; gap:8px; margin-bottom:24px;">
                <button class="action-btn" onclick="buyPro('click_1mo')" style="width:100%; background:#00AEEF; color:white; box-shadow: 0 4px 0 #007BB5;">
                    1 Oylik — 15,000 so'm (Click)
                </button>
                <button class="action-btn" onclick="buyPro('click_3mo')" style="width:100%; background:#00AEEF; color:white; border: 2px solid #FDCB6E; box-shadow: 0 4px 0 #007BB5; position:relative;">
                    <div style="position:absolute; top:-10px; right:-10px; background:#FDCB6E; color:var(--text-dark); font-size:10px; font-weight:800; padding:2px 8px; border-radius:8px;">TAVSIYA</div>
                    90 kunlik Challenge — 50,000 so'm
                </button>
                <button class="action-btn" onclick="buyPro('click_lifetime')" style="width:100%; background:#00AEEF; color:white; box-shadow: 0 4px 0 #007BB5;">
                    To'liq Yo'l (Lifetime) — 200,000 so'm
                </button>
            </div>
'''
html = re.sub(r'<button class="action-btn" onclick="buyPro\(\'click\'\)".*?</button>', new_buttons, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated pricing matrix in index.html")
