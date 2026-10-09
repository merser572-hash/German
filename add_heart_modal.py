import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add heart modal
heart_modal = '''
    <!-- Heart Modal -->
    <div id="heart-modal" class="modal-overlay" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:9999; justify-content:center; align-items:center; padding:20px;">
        <div style="background:var(--card-bg); padding:32px; border-radius:24px; text-align:center; max-width:400px; width:100%; box-shadow:0 8px 0 rgba(0,0,0,0.1);">
            <i data-lucide="heart" style="color:var(--red-btn); width:64px; height:64px; margin-bottom:16px;"></i>
            <h2 style="font-size:24px; font-weight:800; margin-bottom:8px;">Your Hearts</h2>
            <p style="color:var(--text-muted); margin-bottom:24px;">You have <span id="heart-modal-count" style="font-weight:800; color:var(--red-btn);">20</span> hearts remaining.</p>
            
            <div style="background:var(--bg-color); padding:16px; border-radius:16px; margin-bottom:24px;">
                <p style="font-weight:700; margin-bottom:4px; color:var(--text-muted);">Next heart refills in:</p>
                <p style="font-size:36px; font-weight:800; color:var(--primary-btn); font-variant-numeric: tabular-nums;" id="heart-countdown">30:00</p>
            </div>
            
            <button class="action-btn" onclick="closeHeartModal()" style="width:100%; background:#DFE6E9; color:var(--text-dark); box-shadow: 0 4px 0 #B0BEC5;">Close</button>
        </div>
    </div>
'''

if 'id="heart-modal"' not in html:
    html = html.replace('<!-- Level Selector Modal -->', heart_modal + '\n    <!-- Level Selector Modal -->')

# Make the heart in top bar clickable
html = html.replace('<div class="stat heart"><i data-lucide="heart"></i> <span id="lives">5</span></div>',
                    '<div class="stat heart" onclick="openHeartModal()" style="cursor:pointer;"><i data-lucide="heart"></i> <span id="lives">20</span></div>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html with heart modal")
