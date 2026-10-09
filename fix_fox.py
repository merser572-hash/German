import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

local_fox_html = '''
                <!-- LOCAL FOX FOR ERRORS -->
                <div id="ddd-local-fox" style="display:none; background:#FFEAA7; border:3px solid #2D3436; border-radius:16px; padding:12px 16px; margin-top:16px; align-items:center; gap:12px; animation: shake 0.4s ease-in-out;">
                    <div style="font-size:32px; filter: drop-shadow(0 4px 0 rgba(0,0,0,0.2));">🦊</div>
                    <div id="ddd-local-fox-msg" style="font-weight:900; font-size:14px; color:#2D3436; line-height:1.4;">Fritzning onasi xatoni ko'rib qoldi! Qoidalarni takrorla!</div>
                </div>
'''

if 'ddd-local-fox' not in html:
    html = html.replace(
        '<div class="game-word-box">',
        local_fox_html + '\n                <div class="game-word-box">'
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Index HTML local fox added!")
