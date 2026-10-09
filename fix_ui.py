import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the broken button tags caused by emoji corruption
html = html.replace('Next Word ?/button>', 'Next Word -> </button>')
html = html.replace('Keyingi gap ?/button>', 'Keyingi gap -> </button>')
html = html.replace('Next Word ?/button>', 'Next Word -> </button>')
html = html.replace('Keyingi gap ?/button>', 'Keyingi gap -> </button>')
html = html.replace('?/button>', '</button>')
html = html.replace('?/button>', '</button>')

# 2. Add Flashcard Modal right before </body> if not present
flashcard_modal = '''
    <!-- MODAL: FLASHCARDS -->
    <div class="login-overlay" id="modal-flashcard" style="display:none; z-index:9999; justify-content:center; align-items:center;">
        <div class="login-card" style="width:90%; max-width:400px; min-height:300px; text-align:center; position:relative; perspective: 1000px; padding:24px;">
            <button class="action-btn" style="position:absolute; top:12px; right:12px; padding:4px 12px; width:auto;" onclick="closeFlashcards()">X</button>
            <div style="font-size:14px; font-weight:900; color:var(--text-muted); margin-bottom:16px; background:#f1f2f6; display:inline-block; padding:4px 16px; border-radius:16px;" id="fc-counter">1 / 20</div>
            
            <div id="fc-card-inner" style="transition: transform 0.5s cubic-bezier(0.4, 0.2, 0.2, 1); transform-style: preserve-3d; position:relative; width:100%; height:220px; cursor:pointer;" onclick="flipFlashcard()">
                <!-- FRONT -->
                <div id="fc-front" style="position:absolute; width:100%; height:100%; backface-visibility:hidden; background:#fff; border:3px solid #2D3436; border-radius:24px; display:flex; flex-direction:column; justify-content:center; align-items:center; box-shadow:0 8px 0 #2D3436;">
                    <div style="font-size:11px; font-weight:900; color:#B2BEC3; margin-bottom:16px; text-transform:uppercase;">Old tomoni (Nemischa)</div>
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
                <button class="action-btn" style="flex:1; background:#fff; color:#2D3436; box-shadow:0 4px 0 #2D3436;" onclick="prevFlashcard()"><- Oldingi</button>
                <button class="action-btn" style="flex:1; background:#55EFC4; color:#2D3436; box-shadow:0 4px 0 #00B894;" onclick="nextFlashcard()">Keyingi -></button>
            </div>
        </div>
    </div>
'''
if 'modal-flashcard' not in html:
    html = html.replace('</body>', flashcard_modal + '\n</body>')

# 3. Add Flashcard trigger button and Categories in Dictionary view
if 'openFlashcards()' not in html:
    dict_header_replacement = '''<div class="card" style="margin-bottom:12px; display:flex; gap:8px;">
                <div style="flex:1; position:relative;">
                    <i data-lucide="search" style="position:absolute; left:12px; top:50%; transform:translateY(-50%); color:#B2BEC3; width:20px;"></i>
                    <input type="text" id="dict-search" data-i18n="search" placeholder="Search word..." style="width:100%; padding:12px 12px 12px 40px; border:2px solid #DFE6E9; border-radius:12px; font-family:'Nunito', sans-serif; font-size:16px; font-weight:700; outline:none;" oninput="renderDictionary()">
                </div>
                <button class="action-btn" style="background:#FFEAA7; color:#2D3436; box-shadow:0 4px 0 #FDCB6E; padding:0 16px; width:auto;" onclick="openFlashcards()">
                    <i data-lucide="layers" style="width:24px;"></i>
                </button>
            </div>
            
            <div id="dict-categories" style="display:flex; overflow-x:auto; gap:8px; padding-bottom:8px; margin-bottom:8px; scrollbar-width:none;">
                <!-- Dynamically populated -->
            </div>
'''
    html = re.sub(r'<div class=\"card\" style=\"margin-bottom:12px; position:relative;\">.*?</div>', dict_header_replacement, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Index fixed!')
