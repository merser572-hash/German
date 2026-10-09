import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add to appState
js = js.replace(
    "currentView: 'home',",
    "currentView: 'home',\n    dddQueue: [],\n    satzQueue: [],"
)

# Fix initDerDieDas shuffle
old_ddd_logic = '''if(nouns.length === 0) return;
    
    // reset extra info
    document.getElementById('ddd-extra-info').style.display = 'none';
    document.getElementById('ddd-buttons-container').style.display = 'grid';

    appState.dddWord = nouns[Math.floor(Math.random() * nouns.length)];
    els.dddWord.textContent = appState.dddWord.word;
    els.dddTrans.textContent = appState.dddWord.translation;'''

new_ddd_logic = '''if(nouns.length === 0) return;
    
    // reset extra info
    document.getElementById('ddd-extra-info').style.display = 'none';
    document.getElementById('ddd-buttons-container').style.display = 'grid';

    // Shuffling algorithm: Deck/Bag system to prevent repeats
    if (!appState.dddQueue || appState.dddQueue.length === 0) {
        appState.dddQueue = [...nouns];
        for (let i = appState.dddQueue.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [appState.dddQueue[i], appState.dddQueue[j]] = [appState.dddQueue[j], appState.dddQueue[i]];
        }
    }
    appState.dddWord = appState.dddQueue.pop();
    
    els.dddWord.textContent = appState.dddWord.word;
    els.dddTrans.textContent = appState.dddWord.translation;'''

js = js.replace(old_ddd_logic, new_ddd_logic)

# Wait, we need to reset the queue when the user changes the category!
# Let's add that to selectCategory!
old_select_cat = '''function selectCategory(cat) {
    playSound('tap');
    appState.selectedCategory = cat;
    renderCategories();'''

new_select_cat = '''function selectCategory(cat) {
    playSound('tap');
    appState.selectedCategory = cat;
    appState.dddQueue = []; // Reset queue on category change
    renderCategories();'''

js = js.replace(old_select_cat, new_select_cat)

# Now fix Satzbau shuffle
old_satz_logic = '''function startSatzbauRound() {
    const eb = document.getElementById('satzbau-error-box');
    if(eb) eb.style.display = 'none';
    
    const sentence = appState.satzSentences[Math.floor(Math.random() * appState.satzSentences.length)];'''

new_satz_logic = '''function startSatzbauRound() {
    const eb = document.getElementById('satzbau-error-box');
    if(eb) eb.style.display = 'none';
    
    // Shuffling algorithm: Deck/Bag system to prevent repeats
    if (!appState.satzQueue || appState.satzQueue.length === 0) {
        appState.satzQueue = [...appState.satzSentences];
        for (let i = appState.satzQueue.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [appState.satzQueue[i], appState.satzQueue[j]] = [appState.satzQueue[j], appState.satzQueue[i]];
        }
    }
    const sentence = appState.satzQueue.pop();'''

js = js.replace(old_satz_logic, new_satz_logic)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
    
print("Shuffling algorithms fixed!")
