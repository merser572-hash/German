import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Fix "all_categories" -> "All"
js = js.replace(
    '''let html = `<button class="category-chip ${appState.selectedCategory === 'all' ? 'active' : ''}" onclick="selectCategory('all')">all_categories</button>`;''',
    '''let html = `<button class="category-chip ${appState.selectedCategory === 'all' ? 'active' : ''}" onclick="selectCategory('all')">All</button>`;'''
)

# 2. Fix selectCategory duplicates
js = js.replace('''function selectCategory(cat) {
    playSound('tap');
    appState.selectedCategory = cat;
    renderCategories();
    renderCategories();
        renderDictionary();
}''', '''function selectCategory(cat) {
    playSound('tap');
    appState.selectedCategory = cat;
    renderCategories();
    renderDictionary();
}''')

# 3. Add filtering logic to renderDictionary
old_renderDict = '''function renderDictionary() {
    const searchEl = document.getElementById("dict-search"); const q = searchEl ? searchEl.value.toLowerCase() : "";
    const list = document.getElementById('dict-list');
    list.innerHTML = '';
    const filtered = appState.words.filter(w => w.word.toLowerCase().includes(q) || w.translation.toLowerCase().includes(q));'''

new_renderDict = '''function renderDictionary() {
    const searchEl = document.getElementById("dict-search"); const q = searchEl ? searchEl.value.toLowerCase() : "";
    const list = document.getElementById('dict-list');
    list.innerHTML = '';
    
    // FIRST filter by category
    let categoryFiltered = appState.words;
    if (appState.selectedCategory && appState.selectedCategory !== 'all') {
        categoryFiltered = appState.words.filter(w => w.category === appState.selectedCategory);
    }
    
    // THEN filter by search query
    const filtered = categoryFiltered.filter(w => w.word.toLowerCase().includes(q) || w.translation.toLowerCase().includes(q));'''

js = js.replace(old_renderDict, new_renderDict)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('Dictionary fixes applied')
