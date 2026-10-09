import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Flashcard modal
flashcard_modal = '''
    <!-- MODAL: FLASHCARDS -->
    <div class="modal-backdrop" id="modal-flashcard" style="display:none; z-index:9999; justify-content:center; align-items:center;">
        <div class="modal-card" style="width:90%; min-height:300px; text-align:center; position:relative; perspective: 1000px;">
            <button class="modal-close-btn" onclick="closeFlashcards()">✕</button>
            <div style="font-size:14px; font-weight:900; color:var(--text-muted); margin-bottom:16px; background:#f1f2f6; display:inline-block; padding:4px 16px; border-radius:16px;" id="fc-counter">1 / 20</div>
            
            <div id="fc-card-inner" style="transition: transform 0.5s cubic-bezier(0.4, 0.2, 0.2, 1); transform-style: preserve-3d; position:relative; width:100%; height:220px; cursor:pointer;" onclick="flipFlashcard()">
                <!-- FRONT -->
                <div id="fc-front" style="position:absolute; width:100%; height:100%; backface-visibility:hidden; background:#fff; border:3px solid #2D3436; border-radius:24px; display:flex; flex-direction:column; justify-content:center; align-items:center; box-shadow:0 8px 0 #2D3436;">
                    <div style="font-size:11px; font-weight:900; color:#B2BEC3; margin-bottom:16px; text-transform:uppercase;">Old tomoni (Nemischa) - O'girish uchun bosing</div>
                    <h2 id="fc-word" style="font-size:36px; font-weight:900; color:#2D3436; margin:0;">kommen</h2>
                    <div id="fc-category" style="color:var(--blue-btn); font-weight:800; margin-top:12px; font-size:14px;">Verbs</div>
                </div>
                <!-- BACK -->
                <div id="fc-back" style="position:absolute; width:100%; height:100%; backface-visibility:hidden; background:#E8F8F5; border:3px solid #16A085; border-radius:24px; display:flex; flex-direction:column; justify-content:center; align-items:center; transform: rotateY(180deg); box-shadow:0 8px 0 #16A085;">
                     <div style="font-size:11px; font-weight:900; color:#16A085; margin-bottom:16px; text-transform:uppercase;">Orqa tomoni (O'zbekcha)</div>
                     <h2 id="fc-translation" style="font-size:28px; font-weight:900; color:#2D3436; margin:0; padding:0 12px;">kelmoq</h2>
                </div>
            </div>

            <div style="display:flex; gap:12px; margin-top:32px;">
                <button class="action-btn" style="flex:1; background:#fff; color:#2D3436; box-shadow:0 4px 0 #2D3436;" onclick="prevFlashcard()">⬅ Oldingi</button>
                <button class="action-btn" style="flex:1; background:#55EFC4; color:#2D3436; box-shadow:0 4px 0 #00B894;" onclick="nextFlashcard()">Keyingi ➡</button>
            </div>
        </div>
    </div>
'''

html = html.replace('<!-- MODAL: Grammar Detail -->', flashcard_modal + '\n    <!-- MODAL: Grammar Detail -->')

# 2. Add Flashcard trigger button and Categories in Dictionary view
dict_header_replacement = '''<div class="card" style="margin-bottom:12px; display:flex; gap:8px;">
                <div style="flex:1; position:relative;">
                    <i data-lucide="search" style="position:absolute; left:12px; top:50%; transform:translateY(-50%); color:#B2BEC3; width:20px;"></i>
                    <input type="text" id="dict-search" data-i18n="search" placeholder="Search word..." style="width:100%; padding:12px 12px 12px 40px; border:2px solid #DFE6E9; border-radius:12px; font-family:'Nunito', sans-serif; font-size:16px; font-weight:700; outline:none;" oninput="renderDictionary()">
                </div>
                <button class="action-btn" style="background:#FFEAA7; color:#2D3436; box-shadow:0 4px 0 #FDCB6E; padding:0 16px;" onclick="openFlashcards()">
                    <i data-lucide="layers" style="width:24px;"></i>
                </button>
            </div>
            
            <div id="dict-categories" style="display:flex; overflow-x:auto; gap:8px; padding-bottom:8px; margin-bottom:8px; scrollbar-width:none;">
                <!-- Dynamically populated -->
            </div>
'''
html = re.sub(r'<div class=\"card\" style=\"margin-bottom:12px; position:relative;\">.*?</div>', dict_header_replacement, html, flags=re.DOTALL)

# 3. Add DerDieDas Extra Info panel
ddd_extra_html = '''<div id="ddd-extra-info" style="display:none; margin-top: 24px; text-align:left; animation: scaleIn 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);">
                <div style="border: 2px dashed #B2BEC3; border-radius: 16px; padding: 16px; position:relative; background:#fff;">
                    <span id="ddd-mnemonic-badge" style="font-size:11px; font-weight:900; background:#FFEAA7; color:#2D3436; padding:4px 10px; border-radius:12px; position:absolute; top:-14px; left:16px;">Mnemonic Hook</span>
                    <div id="ddd-mnemonic-title" style="font-weight:900; font-size:18px; margin-bottom:6px; margin-top:4px;">DER Hals</div>
                    <div id="ddd-mnemonic-text" style="font-size:14px; color:var(--text-muted); line-height:1.4; margin-bottom:16px;">Fritz Tip: Picture masculine words as active, bold characters or in vibrant blue.</div>
                    <button class="action-btn" style="width:100%; background:var(--green-btn); color:white; padding:12px; box-shadow:0 4px 0 var(--green-shadow);" onclick="initDerDieDas()">Next Word ➡</button>
                </div>
                
                <div style="background:#f1f2f6; border-radius:16px; padding:16px; margin-top:16px; border:2px solid #DFE6E9;">
                    <div style="font-weight:900; font-size:12px; color:#636E72; margin-bottom:6px; text-transform:uppercase;">Misol jumla:</div>
                    <div id="ddd-example-de" style="font-weight:800; font-size:16px; color:#2D3436; margin-bottom:4px;">Ich habe Halsschmerzen und Husten.</div>
                    <div id="ddd-example-uz" style="font-style:italic; font-size:14px; color:var(--text-muted);">I have a sore throat and cough.</div>
                </div>
            </div>'''
html = html.replace('<div class="ddd-controls">', ddd_extra_html + '\n            <div class="ddd-controls" id="ddd-buttons-container">')

# 4. Add Satzbau Error Box
satzbau_error_html = '''<div id="satzbau-error-box" style="display:none; border: 3px solid #D63031; background: #FF767520; border-radius: 16px; padding: 16px; margin-top: 24px; text-align:left; animation: shake 0.4s ease-in-out;">
                <div style="font-weight:900; color:#D63031; margin-bottom:12px; display:flex; align-items:center; gap:8px;"><i data-lucide="search" style="width:20px;"></i> Nicht ganz richtig</div>
                <div style="font-size:15px; margin-bottom:10px; color:#2D3436;"><b>Richtige Reihenfolge:</b> <span id="satzbau-correct-text" style="font-style:italic; font-weight:700;"></span></div>
                <div style="font-size:14px; color:#2D3436; line-height:1.4; margin-bottom:16px;"><b>Warum?</b> <span id="satzbau-explanation">In standard German declarative sentences, the conjugated verb ('trinke') MUST always be in the 2nd position.</span></div>
                <button class="action-btn" style="width:100%; background:#FFEAA7; color:#2D3436; box-shadow:0 4px 0 #FDCB6E; border:2px solid #2D3436;" onclick="initSatzbau()">Keyingi gap ➡</button>
            </div>'''

html = html.replace('<div class="btn-row" style="margin-top:16px;">', satzbau_error_html + '\n            <div class="btn-row" id="satzbau-btn-row" style="margin-top:16px;">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Index HTML updated!')
