import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 4. Add Satzbau Error Box (if missing)
if 'satzbau-error-box' not in html:
    satzbau_error_html = '''<div id="satzbau-error-box" style="display:none; border: 3px solid #D63031; background: #FF767520; border-radius: 16px; padding: 16px; margin-top: 24px; text-align:left; animation: shake 0.4s ease-in-out;">
                <div style="font-weight:900; color:#D63031; margin-bottom:12px; display:flex; align-items:center; gap:8px;"><i data-lucide="search" style="width:20px;"></i> Nicht ganz richtig</div>
                <div style="font-size:15px; margin-bottom:10px; color:#2D3436;"><b>Richtige Reihenfolge:</b> <span id="satzbau-correct-text" style="font-style:italic; font-weight:700;"></span></div>
                <div style="font-size:14px; color:#2D3436; line-height:1.4; margin-bottom:16px;"><b>Warum?</b> <span id="satzbau-explanation">In standard German declarative sentences, the conjugated verb MUST always be in the 2nd position.</span></div>
                <button class="action-btn" style="width:100%; background:#FFEAA7; color:#2D3436; box-shadow:0 4px 0 #FDCB6E; border:2px solid #2D3436;" onclick="initSatzbau()">Keyingi gap -></button>
            </div>'''
    # inject before btn-row in satzbau view
    html = html.replace('<div class="btn-row" style="margin-top:16px;">', satzbau_error_html + '\n            <div class="btn-row" id="satzbau-btn-row" style="margin-top:16px;">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
