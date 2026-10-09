import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Include srs-engine.js
if 'srs-engine.js' not in html:
    html = html.replace('<!-- App Scripts -->', '<!-- App Scripts -->\n    <script src="srs-engine.js?v=37"></script>')

# 2. Add Start Flashcards button to Home Screen
start_btn = '''
            <section class="card" style="margin-bottom: 20px; text-align:center;">
                <h3 style="margin-bottom:8px;">Daily Flashcards</h3>
                <p style="font-size:14px; color:var(--text-muted); margin-bottom:16px;">Learn and review your vocabulary using spaced repetition.</p>
                <button class="action-btn primary-btn" onclick="startFlashcards()" style="display:flex; justify-content:center; align-items:center; gap:8px;">
                    <i data-lucide="play" style="width:20px;"></i> Start Review
                </button>
            </section>
'''
if 'Daily Flashcards' not in html:
    html = html.replace('<section class="main-grid">', start_btn + '\n            <section class="main-grid">')

# 3. Add view-flashcards HTML
flashcards_view = '''
        <!-- ================= FLASHCARDS VIEW ================= -->
        <div id="view-flashcards" class="view" style="display: none;">
            <header class="top-bar">
                <button class="icon-btn" onclick="switchView('home')"><i data-lucide="arrow-left"></i></button>
                <h3 style="font-weight: 800;">Flashcards</h3>
                <div class="stat star"><i data-lucide="star"></i> <span id="fc-xp">120</span></div>
            </header>
            
            <div style="padding: 0 16px;">
                <button class="category-select-btn" onclick="openCategoryModal()">
                    <div style="display:flex; align-items:center; gap:10px;">
                        <i data-lucide="layers"></i>
                        <span id="fc-category-label">Barcha bo'limlar</span>
                    </div>
                    <i data-lucide="chevron-down"></i>
                </button>
            </div>
            
            <div style="padding: 0 16px; margin-bottom:12px; text-align:center; font-size:14px; font-weight:700; color:var(--text-muted);">
                Qolgan kartalar: <span id="fc-queue-count">0</span>
            </div>

            <div class="game-container" style="display:flex; flex-direction:column; align-items:center;">
                
                <!-- The Card -->
                <div id="fc-card" class="flashcard-ui" onclick="flipFlashcard()">
                    <div class="fc-front">
                        <h2 id="fc-word" style="font-size: 32px; margin-bottom:8px;">Word</h2>
                        <p style="font-size:14px; color:#888;">(Tap to flip)</p>
                    </div>
                    <div class="fc-back" style="display:none;">
                        <h2 id="fc-word-back" style="font-size: 28px; margin-bottom:8px; color:var(--blue-btn);">der Word</h2>
                        <p id="fc-plural" style="font-size: 16px; color:#555; margin-bottom:16px;">(Pl: die Words)</p>
                        <h3 id="fc-translation" style="font-size: 20px; color:#333; margin-bottom:24px;">Tarjimasi</h3>
                        
                        <button class="icon-btn" onclick="event.stopPropagation(); speakText(document.getElementById('fc-word-back').textContent)" style="margin: 0 auto;">
                            <i data-lucide="volume-2"></i>
                        </button>
                    </div>
                </div>
                
                <!-- Rating Buttons -->
                <div id="fc-rating-buttons" style="display:none; width:100%; grid-template-columns: 1fr 1fr; gap:12px; margin-top:24px;">
                    <button class="action-btn" style="background:#FF7675; box-shadow: 0 4px 0 #D63031; color:white; padding:12px;" onclick="rateCard(1)">
                        <div style="font-weight:800; font-size:16px;">Again</div>
                        <div style="font-size:12px; opacity:0.9;">(1 min)</div>
                    </button>
                    <button class="action-btn" style="background:#FDCB6E; box-shadow: 0 4px 0 #E1B12C; color:#2D3436; padding:12px;" onclick="rateCard(2)">
                        <div style="font-weight:800; font-size:16px;">Hard</div>
                        <div style="font-size:12px; opacity:0.8;">(1.2x)</div>
                    </button>
                    <button class="action-btn" style="background:#74B9FF; box-shadow: 0 4px 0 #0984E3; color:white; padding:12px;" onclick="rateCard(3)">
                        <div style="font-weight:800; font-size:16px;">Good</div>
                        <div style="font-size:12px; opacity:0.9;">(2.5x)</div>
                    </button>
                    <button class="action-btn" style="background:#55EFC4; box-shadow: 0 4px 0 #00B894; color:#2D3436; padding:12px;" onclick="rateCard(4)">
                        <div style="font-weight:800; font-size:16px;">Easy</div>
                        <div style="font-size:12px; opacity:0.8;">(3.3x)</div>
                    </button>
                </div>

                <div id="fc-done-msg" style="display:none; text-align:center; padding: 40px 20px;">
                    <div style="font-size:60px; margin-bottom:16px;">🎉</div>
                    <h2 style="margin-bottom:12px;">Barcha kartalar o'qildi!</h2>
                    <p style="color:var(--text-muted);">Bugun uchun boshqa karta qolmadi. Ajoyib natija!</p>
                </div>

            </div>
        </div>
'''

if 'id="view-flashcards"' not in html:
    html = html.replace('<!-- ================= SETTINGS VIEW ================= -->', flashcards_view + '\n        <!-- ================= SETTINGS VIEW ================= -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html with flashcards view")
