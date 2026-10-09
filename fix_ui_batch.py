import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix flashcard buttons
html = html.replace(
    '''<button class="action-btn" style="flex:1; background:#fff; color:#2D3436; box-shadow:0 4px 0 #2D3436;" onclick="prevFlashcard()"><- Oldingi</button>
                <button class="action-btn" style="flex:1; background:#55EFC4; color:#2D3436; box-shadow:0 4px 0 #00B894;" onclick="nextFlashcard()">Keyingi -></button>''',
    '''<button class="action-btn" style="flex:1; padding: 12px 8px; font-size: 14px; background:#fff; color:#2D3436; box-shadow:0 4px 0 #2D3436;" onclick="prevFlashcard()"><i data-lucide="arrow-left" style="width:16px; margin-right:4px;"></i> Oldingi</button>
                <button class="action-btn" style="flex:1; padding: 12px 8px; font-size: 14px; background:#55EFC4; color:#2D3436; box-shadow:0 4px 0 #00B894;" onclick="nextFlashcard()">Keyingi <i data-lucide="arrow-right" style="width:16px; margin-left:4px;"></i></button>'''
)

# And re-init lucide icons on flip
html = html.replace(
    'flipFlashcard()',
    "flipFlashcard(); setTimeout(()=>lucide.createIcons(), 10)"
)

# And add Satzbau Error box properly (it failed to inject earlier)
if 'id="satzbau-error-box"' not in html:
    satz_error = '''
                <div id="satzbau-error-box" style="display:none; border: 3px solid #D63031; background: #FF767520; border-radius: 16px; padding: 16px; margin-top: 24px; text-align:left; animation: shake 0.4s ease-in-out;">
                    <div style="font-weight:900; color:#D63031; margin-bottom:12px; display:flex; align-items:center; gap:8px;"><i data-lucide="info" style="width:20px;"></i> Fritzning eslatmasi</div>
                    <div style="font-size:15px; margin-bottom:10px; color:#2D3436;"><b>To'g'ri tartib:</b> <span id="satzbau-correct-text" style="font-style:italic; font-weight:700;"></span></div>
                    <div style="font-size:14px; color:#2D3436; line-height:1.4; margin-bottom:16px;"><b>Qoida:</b> <span id="satzbau-explanation">Gapdagi fe'l doimo 2-o'rinda kelishi kerak (darak gaplarda).</span></div>
                    <button class="action-btn" style="width:100%; background:#FFEAA7; color:#2D3436; box-shadow:0 4px 0 #FDCB6E; border:2px solid #2D3436;" onclick="startSatzbauRound()">Tushundim, keyingisi &#8594;</button>
                </div>
    '''
    html = html.replace(
        '''<button class="action-btn primary-btn" id="satz-check-btn" onclick="checkSatzbau()" style="margin-top: 30px; display: none;" data-i18n="check">Tekshirish</button>''',
        '''<button class="action-btn primary-btn" id="satz-check-btn" onclick="checkSatzbau()" style="margin-top: 30px; display: none;" data-i18n="check">Tekshirish</button>''' + satz_error
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Flashcard and Satzbau HTML injected')
