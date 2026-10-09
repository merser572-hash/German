import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Dictionary categories container
old_dict_cat = '<div id="dict-categories" class="horizontal-scroll" style="padding-bottom:10px; margin-bottom:8px;"></div>'
new_dict_cat = '''<button class="category-select-btn" onclick="openCategoryModal()">
                <div style="display:flex; align-items:center; gap:10px;">
                    <i data-lucide="layers"></i>
                    <span id="dict-category-label">Barcha bo'limlar</span>
                </div>
                <i data-lucide="chevron-down"></i>
            </button>'''
html = html.replace(old_dict_cat, new_dict_cat)

# Replace Der Die Das categories container
old_ddd_cat = '<div id="ddd-categories" class="horizontal-scroll" style="padding: 0 16px; margin-bottom: 16px;"></div>'
new_ddd_cat = '''<div style="padding: 0 16px;">
                <button class="category-select-btn" onclick="openCategoryModal()">
                    <div style="display:flex; align-items:center; gap:10px;">
                        <i data-lucide="layers"></i>
                        <span id="ddd-category-label">Barcha bo'limlar</span>
                    </div>
                    <i data-lucide="chevron-down"></i>
                </button>
            </div>'''
html = html.replace(old_ddd_cat, new_ddd_cat)

# Inject Modal at the end of body
modal_html = '''
    <!-- Category Modal -->
    <div id="category-modal" class="modal-overlay" style="display: none;" onclick="if(event.target===this) closeCategoryModal()">
        <div class="modal-content">
            <div class="modal-header">
                <h3>Bo'limni tanlang</h3>
                <button class="icon-btn" onclick="closeCategoryModal()"><i data-lucide="x"></i></button>
            </div>
            <div id="category-modal-list" class="category-list">
                <!-- Dynamically populated -->
            </div>
        </div>
    </div>
'''

if 'id="category-modal"' not in html:
    html = html.replace('</body>', modal_html + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("index.html updated with modals")
