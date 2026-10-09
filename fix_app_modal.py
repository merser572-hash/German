import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_render_cats = '''
function renderCategories() {
    // Update labels
    const dLabel = document.getElementById('dict-category-label');
    const dddLabel = document.getElementById('ddd-category-label');
    
    let displayTxt = appState.selectedCategory === 'all' ? "Barcha bo'limlar" : appState.selectedCategory;
    if (dLabel) dLabel.textContent = displayTxt;
    if (dddLabel) dddLabel.textContent = displayTxt;
}

function openCategoryModal() {
    const listContainer = document.getElementById('category-modal-list');
    listContainer.innerHTML = '';
    
    let cats = [...new Set(appState.words.map(w => w.category).filter(Boolean))];
    
    // If in Der Die Das, filter out categories that have NO nouns
    if (appState.currentView === 'derdiedas') {
        cats = cats.filter(c => {
            return appState.words.some(w => w.category === c && w.article && ['der', 'die', 'das'].includes(w.article.toLowerCase()));
        });
    }
    
    // Natural sort
    cats.sort((a, b) => {
        return a.localeCompare(b, undefined, {numeric: true, sensitivity: 'base'});
    });
    
    let html = `<button class="category-list-item ${appState.selectedCategory === 'all' ? 'active' : ''}" onclick="selectCategory('all')">Barcha bo'limlar</button>`;
    cats.forEach(c => {
        html += `<button class="category-list-item ${appState.selectedCategory === c ? 'active' : ''}" onclick="selectCategory('${c.replace(/'/g, "\\'")}')">${c}</button>`;
    });
    
    listContainer.innerHTML = html;
    document.getElementById('category-modal').style.display = 'flex';
}

function closeCategoryModal() {
    document.getElementById('category-modal').style.display = 'none';
}

function selectCategory(cat) {
    playSound('tap');
    appState.selectedCategory = cat;
    appState.dddQueue = []; // Reset queue
    renderCategories();
    closeCategoryModal();
    
    if (appState.currentView === 'dictionary') {
        renderDictionary();
    } else if (appState.currentView === 'derdiedas') {
        initDerDieDas();
    }
}
'''

# We need to replace the old renderCategories and selectCategory
js = re.sub(r'function renderCategories\(\) \{.*?(?=\/\/ Intercept renderDictionary|\/\/ FIRST filter by category|function renderDictionary)', new_render_cats + '\n\n', js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated app.js with modal logic")
