import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Update renderCategories
js = js.replace(
    '''const dddLabel = document.getElementById('ddd-category-label');''',
    '''const dddLabel = document.getElementById('ddd-category-label');
    const fcLabel = document.getElementById('fc-category-label');'''
)
js = js.replace(
    '''if (dddLabel) dddLabel.textContent = displayTxt;''',
    '''if (dddLabel) dddLabel.textContent = displayTxt;
    if (fcLabel) fcLabel.textContent = displayTxt;'''
)

# Update openCategoryModal filtering logic to NOT filter for flashcards unless we want to.
# Actually flashcards works for ALL categories, verbs included! So we only filter for 'derdiedas'
# Which is already correct: `if (appState.currentView === 'derdiedas')`

# Update selectCategory to handle flashcards reload
js = js.replace(
    '''} else if (appState.currentView === 'derdiedas') {
        initDerDieDas();
    }''',
    '''} else if (appState.currentView === 'derdiedas') {
        initDerDieDas();
    } else if (appState.currentView === 'flashcards') {
        startFlashcards();
    }'''
)

# Add flashcard logic
fc_logic = '''
// --- FLASHCARDS LOGIC ---

function startFlashcards() {
    switchView('flashcards');
    
    // Build Queue based on selected category
    let wordsArray = appState.words;
    if (appState.selectedCategory && appState.selectedCategory !== 'all') {
        wordsArray = appState.words.filter(w => w.category === appState.selectedCategory);
    }
    
    if (window.SRS) {
        appState.fcQueue = window.SRS.buildQueue(wordsArray, 15);
    } else {
        // Fallback if srs-engine didn't load
        appState.fcQueue = [...wordsArray].slice(0, 15);
    }
    
    loadNextFlashcard();
}

function loadNextFlashcard() {
    document.getElementById('fc-queue-count').textContent = appState.fcQueue.length;
    
    const cardEl = document.getElementById('fc-card');
    const frontEl = cardEl.querySelector('.fc-front');
    const backEl = cardEl.querySelector('.fc-back');
    const btnsEl = document.getElementById('fc-rating-buttons');
    const msgEl = document.getElementById('fc-done-msg');
    
    if (appState.fcQueue.length === 0) {
        cardEl.style.display = 'none';
        btnsEl.style.display = 'none';
        msgEl.style.display = 'block';
        return;
    }
    
    msgEl.style.display = 'none';
    cardEl.style.display = 'flex';
    frontEl.style.display = 'block';
    backEl.style.display = 'none';
    btnsEl.style.display = 'none';
    
    // Get next word (first in queue)
    appState.currentFcWord = appState.fcQueue[0];
    
    document.getElementById('fc-word').textContent = appState.currentFcWord.word;
    
    let artHtml = appState.currentFcWord.article ? appState.currentFcWord.article + ' ' : '';
    document.getElementById('fc-word-back').textContent = artHtml + appState.currentFcWord.word;
    
    if (appState.currentFcWord.plural) {
        document.getElementById('fc-plural').textContent = `(Pl: ${appState.currentFcWord.plural})`;
        document.getElementById('fc-plural').style.display = 'block';
    } else {
        document.getElementById('fc-plural').style.display = 'none';
    }
    
    document.getElementById('fc-translation').textContent = appState.currentFcWord.translation;
}

function flipFlashcard() {
    const cardEl = document.getElementById('fc-card');
    const frontEl = cardEl.querySelector('.fc-front');
    const backEl = cardEl.querySelector('.fc-back');
    const btnsEl = document.getElementById('fc-rating-buttons');
    
    if (frontEl.style.display !== 'none') {
        playSound('tap');
        frontEl.style.display = 'none';
        backEl.style.display = 'block';
        btnsEl.style.display = 'grid';
        
        speakText(document.getElementById('fc-word-back').textContent);
    }
}

function rateCard(quality) {
    if (!appState.currentFcWord) return;
    
    playSound('tap');
    
    if (window.SRS) {
        window.SRS.reviewCard(appState.currentFcWord.id, quality);
    }
    
    // Remove from front of queue
    appState.fcQueue.shift();
    
    // If it was a 'fail' (quality 1), maybe we push it to the back of the queue so they see it again today?
    if (quality === 1) {
        appState.fcQueue.push(appState.currentFcWord);
    }
    
    // XP reward
    appState.xp += 5;
    updateStats();
    
    loadNextFlashcard();
}
'''

if 'function startFlashcards' not in js:
    js += '\n' + fc_logic

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Flashcards logic added to app.js")
