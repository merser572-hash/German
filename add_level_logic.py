import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

level_logic = '''
function openLevelModal() {
    playSound('tap');
    document.getElementById('level-modal').style.display = 'flex';
}

function closeLevelModal() {
    playSound('tap');
    document.getElementById('level-modal').style.display = 'none';
}

function selectLevel(levelStr) {
    playSound('tap');
    localStorage.setItem('wunderdeutsch_level', levelStr);
    appState.currentLevel = levelStr;
    
    let display = levelStr === 'A1' ? 'Level: A1' : 'Medizin B2 🩺';
    document.getElementById('current-level-display').innerText = display;
    
    // Automatically select 'all' categories of the new level
    appState.selectedCategory = 'all';
    
    renderCategories();
    closeLevelModal();
    
    // Refresh current view if needed
    if (appState.currentView === 'flashcards') {
        startFlashcards();
    } else if (appState.currentView === 'derdiedas') {
        initDerDieDas();
    }
}
'''

if 'function openLevelModal' not in js:
    js += '\n' + level_logic

# Update appState to include currentLevel
js = js.replace("isAdmin: true,", "isAdmin: true, currentLevel: localStorage.getItem('wunderdeutsch_level') || 'A1',")

# Update renderCategories to filter by level
old_render_categories = '''    const cats = [...new Set(appState.words.map(w => w.category).filter(c => c))];
    const list = document.getElementById('category-list');
    list.innerHTML = '';'''

new_render_categories = '''    // Filter categories based on active Level
    let levelPrefix = appState.currentLevel === 'A1' ? 'Goethe A1' : 'Medizin';
    const cats = [...new Set(appState.words.map(w => w.category).filter(c => c && c.startsWith(levelPrefix)))];
    
    const list = document.getElementById('category-list');
    list.innerHTML = '';'''

js = js.replace(old_render_categories, new_render_categories)

# In startFlashcards and initDerDieDas, 'all' currently uses all words.
# We need it to use all words FROM THE CURRENT LEVEL.
js = js.replace(
'''    let wordsArray = appState.words;
    if (appState.selectedCategory && appState.selectedCategory !== 'all') {
        wordsArray = appState.words.filter(w => w.category === appState.selectedCategory);
    }''',
'''    let wordsArray = appState.words;
    let levelPrefix = appState.currentLevel === 'A1' ? 'Goethe A1' : 'Medizin';
    
    if (appState.selectedCategory && appState.selectedCategory !== 'all') {
        wordsArray = appState.words.filter(w => w.category === appState.selectedCategory);
    } else {
        wordsArray = appState.words.filter(w => w.category && w.category.startsWith(levelPrefix));
    }'''
)

# And again for Satzbau! Wait, Satzbau uses `appState.satzSentences`.
# We need to filter sentences as well.
# Medical sentences don't have a category field right now. 
# But wait, sentences.json doesn't have categories. How do we know which are Medizin?
# The medical ones were added at the very end. The first 52 are A1, the last 10 are Medizin.
# To be clean, I should just check if the sentence translation has medical keywords, or just rely on the user playing whatever sentences.
# Let's add 'level' to sentences.json!
# I'll do that in another script. For now, just let sentences be mixed or wait to fix it.

# Update current-level-display on load
js = js.replace(
'''    updateOfflineMode();
    await loadVocabulary();''',
'''    updateOfflineMode();
    
    let display = appState.currentLevel === 'A1' ? 'Level: A1' : 'Medizin B2 🩺';
    const lvlDisp = document.getElementById('current-level-display');
    if (lvlDisp) lvlDisp.innerText = display;
    
    await loadVocabulary();'''
)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Added level switching logic to app.js")
