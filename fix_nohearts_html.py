import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

modal_html = '''
    <!-- No Hearts Modal -->
    <div id="no-hearts-modal" class="modal-overlay" style="display: none;">
        <div class="modal-content" style="align-items:center; text-align:center;">
            <div style="font-size:60px; margin-bottom:16px;">💔</div>
            <h2 style="margin-bottom:12px; color:var(--text-dark);">Yuraklar tugadi!</h2>
            <p style="color:var(--text-muted); margin-bottom:24px;">Xatoliklar tufayli barcha yuraklarni yo'qotdingiz. Yangi yurak paydo bo'lishi uchun 30 daqiqa kuting.</p>
            <button class="action-btn primary-btn" onclick="closeNoHeartsModal()" style="width:100%;">Tushundim</button>
        </div>
    </div>
'''

if 'id="no-hearts-modal"' not in html:
    html = html.replace('</body>', modal_html + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("No Hearts modal added")
