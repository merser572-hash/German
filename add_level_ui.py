import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

level_btn_html = '''
            <div style="padding: 16px 16px 0 16px;">
                <button onclick="openLevelModal()" class="action-btn" style="background:var(--card-bg); border:2px solid #DFE6E9; box-shadow:0 4px 0 #DFE6E9; border-radius:16px; padding:8px 16px; display:inline-flex; align-items:center; gap:8px; font-weight:800; font-size:16px; color:var(--text-dark);">
                    <i data-lucide="graduation-cap" style="color:var(--primary-btn);"></i>
                    <span id="current-level-display">Level: A1</span>
                    <i data-lucide="chevron-down" style="width:16px; color:var(--text-muted);"></i>
                </button>
            </div>
'''

if 'id="current-level-display"' not in html:
    html = html.replace('<section class="mascot-section">', level_btn_html + '\n            <section class="mascot-section">')

level_modal_html = '''
    <!-- Level Selector Modal -->
    <div id="level-modal" class="modal-overlay" style="display: none;">
        <div class="modal-content" style="padding:24px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
                <h3 style="font-size:20px; font-weight:800;">Choose Level</h3>
                <button class="icon-btn" onclick="closeLevelModal()"><i data-lucide="x"></i></button>
            </div>
            
            <div style="display:flex; flex-direction:column; gap:12px;">
                <button class="action-btn primary-btn" onclick="selectLevel('A1')" style="text-align:left; padding:16px;">
                    <div style="font-weight:800; font-size:18px;">Level A1</div>
                    <div style="font-size:14px; opacity:0.9;">Beginner German</div>
                </button>
                <button class="action-btn" onclick="selectLevel('Medizin')" style="background:var(--blue-btn); box-shadow: 0 4px 0 var(--blue-shadow); color:white; text-align:left; padding:16px;">
                    <div style="font-weight:800; font-size:18px;">Medizin B2 🩺</div>
                    <div style="font-size:14px; opacity:0.9;">Medical German</div>
                </button>
                <button class="action-btn" style="background:#DFE6E9; box-shadow: 0 4px 0 #B2BEC3; color:#636E72; text-align:left; padding:16px;" onclick="alert('Coming soon!')">
                    <div style="font-weight:800; font-size:18px;">Level A2 (Soon)</div>
                </button>
                <button class="action-btn" style="background:#DFE6E9; box-shadow: 0 4px 0 #B2BEC3; color:#636E72; text-align:left; padding:16px;" onclick="alert('Coming soon!')">
                    <div style="font-weight:800; font-size:18px;">Level B1 (Soon)</div>
                </button>
                <button class="action-btn" style="background:#DFE6E9; box-shadow: 0 4px 0 #B2BEC3; color:#636E72; text-align:left; padding:16px;" onclick="alert('Coming soon!')">
                    <div style="font-weight:800; font-size:18px;">Level B2 (Soon)</div>
                </button>
            </div>
        </div>
    </div>
'''

if 'id="level-modal"' not in html:
    html = html.replace('</body>', level_modal_html + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added Level button and modal")
