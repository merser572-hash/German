import re
import json

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix renderCategories with natural sort and apply to both views
new_renderCats = '''function renderCategories() {
    const dictCatContainer = document.getElementById('dict-categories');
    const dddCatContainer = document.getElementById('ddd-categories');
    if (!dictCatContainer && !dddCatContainer) return;
    
    let cats = [...new Set(appState.words.map(w => w.category).filter(Boolean))];
    // Natural sort: Lektion 2 comes before Lektion 10
    cats.sort((a, b) => {
        return a.localeCompare(b, undefined, {numeric: true, sensitivity: 'base'});
    });
    
    let html = `<button class="category-chip ${appState.selectedCategory === 'all' ? 'active' : ''}" onclick="selectCategory('all')">All</button>`;
    cats.forEach(c => {
        html += `<button class="category-chip ${appState.selectedCategory === c ? 'active' : ''}" onclick="selectCategory('${c.replace(/'/g, "\\'")}')">${c}</button>`;
    });
    
    if (dictCatContainer) dictCatContainer.innerHTML = html;
    if (dddCatContainer) dddCatContainer.innerHTML = html;
}'''

js = re.sub(r'function renderCategories\(\) \{.*?(?=function selectCategory)', new_renderCats + '\n\n', js, flags=re.DOTALL)

# Fix selectCategory to update both views
new_selectCat = '''function selectCategory(cat) {
    playSound('tap');
    appState.selectedCategory = cat;
    renderCategories();
    if (appState.currentView === 'dictionary') {
        renderDictionary();
    } else if (appState.currentView === 'derdiedas') {
        initDerDieDas();
    }
}'''

js = re.sub(r'function selectCategory\(cat\) \{.*?(?=// Intercept renderDictionary)', new_selectCat + '\n\n', js, flags=re.DOTALL)

# Fix renderDictionary to actually filter
new_renderDict = '''function renderDictionary() {
    const query = (els.dddSearch && els.dddSearch.value) ? els.dddSearch.value.toLowerCase() : "";
    const list = document.getElementById('dict-list');
    list.innerHTML = '';
    
    // FIRST filter by category
    let categoryFiltered = appState.words;
    if (appState.selectedCategory && appState.selectedCategory !== 'all') {
        categoryFiltered = appState.words.filter(w => w.category === appState.selectedCategory);
    }
    
    // THEN filter by search query
    const filtered = categoryFiltered.filter(w => w.word.toLowerCase().includes(query) || (w.translation && w.translation.toLowerCase().includes(query)));
    
    filtered.forEach(w => {
        const div = document.createElement('div');
        div.className = 'dict-item';
        let artHtml = w.article ? `<span class="artikel">${w.article}</span> ` : '';
        let pluralHtml = w.plural ? ` (Pl: ${w.plural})` : '';
        div.innerHTML = `
            <div>
                <h4>${artHtml}${w.word}</h4>
                <p>${w.translation}${pluralHtml}</p>
            </div>
            <button class="icon-btn small-btn" onclick="speakText('${w.article ? w.article + ' ' : ''}${w.word}')"><i data-lucide="volume-2"></i></button>
        `;
        list.appendChild(div);
    });
    if(typeof lucide !== 'undefined') lucide.createIcons();
}'''

js = re.sub(r'function renderDictionary\(\) \{.*?lucide\.createIcons\(\);\s*\}', new_renderDict, js, flags=re.DOTALL)

# Fix initDerDieDas to filter by category
js = js.replace(
    '''const nouns = appState.words.filter(w => w.article && ['der', 'die', 'das'].includes(w.article.toLowerCase()));''',
    '''let categoryFiltered = appState.words;
    if (appState.selectedCategory && appState.selectedCategory !== 'all') {
        categoryFiltered = appState.words.filter(w => w.category === appState.selectedCategory);
    }
    const nouns = categoryFiltered.filter(w => w.article && ['der', 'die', 'das'].includes(w.article.toLowerCase()));
    
    if (nouns.length === 0) {
        // fallback if no nouns in this category
        document.getElementById('ddd-word').innerText = "Hech qanday so'z yo'q";
        document.getElementById('ddd-translation').innerText = "Boshqa bo'limni tanlang";
        appState.dddWord = null;
        return;
    }'''
)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('Dictionary and DerDieDas filtering updated')
