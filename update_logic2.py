import re

with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# 1. Update executeSwitchView to clear mascot
mascot_fix = '''
    const mascot = document.getElementById('global-mascot');
    if (mascot) mascot.style.display = 'none';
    
    // reset fox state
    const fox = document.getElementById('ddd-mascot-inner');
    if (fox) {
        fox.classList.remove('fail');
        document.getElementById('mascot-mouth').style.borderRadius = '0 0 10px 10px';
    }
'''
app_js = app_js.replace(
    "document.querySelectorAll('.view').forEach(v => v.style.display = 'none');",
    mascot_fix + "\n    document.querySelectorAll('.view').forEach(v => v.style.display = 'none');"
)

# 2. Add Dictionary Categories and Flashcards logic
flashcard_logic = '''
let flashcardWords = [];
let currentFlashcardIndex = 0;

function openFlashcards() {
    playSound('tap');
    const cat = appState.selectedCategory || 'all';
    let wordsToPick = cat === 'all' ? appState.words : appState.words.filter(w => w.category === cat);
    
    // shuffle and pick 20
    flashcardWords = wordsToPick.sort(() => 0.5 - Math.random()).slice(0, 20);
    if(flashcardWords.length === 0) return;
    
    currentFlashcardIndex = 0;
    document.getElementById('modal-flashcard').style.display = 'flex';
    updateFlashcardUI();
}

function closeFlashcards() {
    playSound('tap');
    document.getElementById('modal-flashcard').style.display = 'none';
}

function updateFlashcardUI() {
    const w = flashcardWords[currentFlashcardIndex];
    document.getElementById('fc-counter').innerText = `${currentFlashcardIndex + 1} / ${flashcardWords.length}`;
    document.getElementById('fc-word').innerText = w.word;
    document.getElementById('fc-category').innerText = w.category || 'Vocab';
    document.getElementById('fc-translation').innerText = w.translation;
    
    const inner = document.getElementById('fc-card-inner');
    inner.style.transform = 'rotateY(0deg)'; // reset flip
}

function flipFlashcard() {
    playSound('tap');
    const inner = document.getElementById('fc-card-inner');
    if (inner.style.transform === 'rotateY(180deg)') {
        inner.style.transform = 'rotateY(0deg)';
    } else {
        inner.style.transform = 'rotateY(180deg)';
    }
}

function nextFlashcard() {
    playSound('tap');
    if (currentFlashcardIndex < flashcardWords.length - 1) {
        currentFlashcardIndex++;
        updateFlashcardUI();
    } else {
        closeFlashcards();
    }
}

function prevFlashcard() {
    playSound('tap');
    if (currentFlashcardIndex > 0) {
        currentFlashcardIndex--;
        updateFlashcardUI();
    }
}

appState.selectedCategory = 'all';

function renderCategories() {
    const catContainer = document.getElementById('dict-categories');
    if (!catContainer) return;
    
    const cats = [...new Set(appState.words.map(w => w.category).filter(Boolean))];
    
    let html = `<button class="category-chip ${appState.selectedCategory === 'all' ? 'active' : ''}" onclick="selectCategory('all')">all_categories</button>`;
    cats.forEach(c => {
        html += `<button class="category-chip ${appState.selectedCategory === c ? 'active' : ''}" onclick="selectCategory('${c.replace(/'/g, "\\'")}')">${c}</button>`;
    });
    catContainer.innerHTML = html;
}

function selectCategory(cat) {
    playSound('tap');
    appState.selectedCategory = cat;
    renderCategories();
    renderDictionary();
}

// Intercept renderDictionary to filter by category
'''

app_js = app_js.replace(
    'function renderDictionary() {',
    flashcard_logic + '\nfunction renderDictionary() {'
)

# Insert renderCategories in loadVocabulary()
app_js = app_js.replace(
    'renderDictionary();',
    'renderCategories();\n        renderDictionary();'
)

# update renderDictionary filtering
app_js = app_js.replace(
    "const q = els.dictSearch.value.toLowerCase();",
    "const q = els.dictSearch.value.toLowerCase();\n    const cat = appState.selectedCategory || 'all';"
)
app_js = app_js.replace(
    "const match = w.word.toLowerCase().includes(q) || w.translation.toLowerCase().includes(q);",
    "const match = (w.word.toLowerCase().includes(q) || w.translation.toLowerCase().includes(q)) && (cat === 'all' || w.category === cat);"
)
# Add example sentence to dictionary item if we want, but let's just use existing template and add a generic example if none exists.
# We will inject a dynamic example if it doesn't exist
dict_template_replace = '''
        // generate a dynamic example
        let exDe = w.example || `Ich lerne das Wort "${w.word}".`;
        let exUz = w.example_uz || `Men "${w.word}" so'zini o'rganyapman.`;
        if(w.article === 'der') { exDe = `Der ${w.word} ist hier.`; exUz = `${w.word} shu yerda.`; }
        else if(w.article === 'die') { exDe = `Die ${w.word} ist schön.`; exUz = `${w.word} chiroyli.`; }
        else if(w.article === 'das') { exDe = `Das ${w.word} ist neu.`; exUz = `${w.word} yangi.`; }

        const div = document.createElement('div');
        div.className = 'dict-item';
        div.innerHTML = `
            <div style="flex:1;">
                <div class="dict-word">${w.article ? w.article + ' ' : ''}${w.word}</div>
                <div class="dict-trans">${w.plural ? '(Pl: ' + w.plural + ') ' : ''}${w.translation}</div>
                <div style="font-style:italic; font-size:13px; color:var(--blue-btn); margin-top:4px;">"${exDe}"</div>
            </div>
'''
app_js = re.sub(
    r'const div = document\.createElement\(\'div\'\);\s*div\.className = \'dict-item\';\s*div\.innerHTML = `.*?</div>\s*`;',
    dict_template_replace + '            <button class="icon-btn" onclick="speak(\\\'' + "${w.word}" + '\\\')"><i data-lucide="volume-2"></i></button>\n        `;',
    app_js,
    flags=re.DOTALL
)

# 3. DerDieDas Mnemonic & Example Box
ddd_init_reset = '''
    // reset extra info
    document.getElementById('ddd-extra-info').style.display = 'none';
    document.getElementById('ddd-buttons-container').style.display = 'flex';
'''
app_js = app_js.replace(
    'appState.dddWord = nouns[Math.floor(Math.random() * nouns.length)];',
    ddd_init_reset + '\n    appState.dddWord = nouns[Math.floor(Math.random() * nouns.length)];'
)

ddd_answer_logic = '''
function getMnemonicForArticle(w) {
    if (w.article === 'der') return "Fritz Tip: Picture masculine words as active, bold characters or in vibrant blue. (Muzskoy so'zlarni ko'k rangda tasavvur qiling).";
    if (w.article === 'die') return "Fritz Tip: Feminine words often end in -e, -ung, -heit. Picture them in soft red. (Jenskiy so'zlarni qizil rangda tasavvur qiling).";
    if (w.article === 'das') return "Fritz Tip: Neuter words are solid and balanced. Picture them in natural green. (Sredniy so'zlarni yashil rangda tasavvur qiling).";
    return "";
}

function showDDDExtra() {
    const w = appState.dddWord;
    document.getElementById('ddd-buttons-container').style.display = 'none';
    document.getElementById('ddd-extra-info').style.display = 'block';
    
    document.getElementById('ddd-mnemonic-title').innerText = `${w.article.toUpperCase()} ${w.word}`;
    document.getElementById('ddd-mnemonic-badge').innerText = w.article.toUpperCase();
    document.getElementById('ddd-mnemonic-badge').style.color = w.article === 'der' ? '#0984E3' : (w.article === 'die' ? '#D63031' : '#00B894');
    document.getElementById('ddd-mnemonic-text').innerText = w.mnemonic || getMnemonicForArticle(w);
    
    let exDe = w.example || `Ich lerne das Wort "${w.word}".`;
    let exUz = w.example_uz || `Men "${w.word}" so'zini o'rganyapman.`;
    if(w.article === 'der') { exDe = `Der ${w.word} ist hier.`; exUz = `${w.word} shu yerda.`; }
    else if(w.article === 'die') { exDe = `Die ${w.word} ist schön.`; exUz = `${w.word} chiroyli.`; }
    else if(w.article === 'das') { exDe = `Das ${w.word} ist neu.`; exUz = `${w.word} yangi.`; }
    
    document.getElementById('ddd-example-de').innerText = exDe;
    document.getElementById('ddd-example-uz').innerText = exUz;
}
'''
app_js = app_js.replace(
    'function checkArticle(guess) {',
    ddd_answer_logic + '\nfunction checkArticle(guess) {'
)
# Inject showDDDExtra() in checkArticle success block
app_js = app_js.replace(
    "els.dddTrans.textContent = '✅ Richtig!';",
    "els.dddTrans.textContent = '✅ Richtig!';\n        showDDDExtra();"
)

# 4. Satzbau Error Box
satzbau_init_reset = '''
    document.getElementById('satzbau-error-box').style.display = 'none';
    document.getElementById('satzbau-btn-row').style.display = 'flex';
'''
app_js = app_js.replace(
    "els.dropzone.innerHTML = '';",
    satzbau_init_reset + "\n    els.dropzone.innerHTML = '';"
)

satzbau_fail_logic = '''
        document.getElementById('satzbau-btn-row').style.display = 'none';
        document.getElementById('satzbau-error-box').style.display = 'block';
        document.getElementById('satzbau-correct-text').innerText = appState.satzbauSentence.de;
        document.getElementById('satzbau-explanation').innerText = appState.satzbauSentence.explanation || "In standard German declarative sentences, the conjugated verb MUST always be in the 2nd position. (Nemis tilida darak gaplarda fe'l DOIM 2-o'rinda kelishi shart!).";
'''
app_js = app_js.replace(
    "els.dropzone.innerHTML = '❌ Xato! Qaytadan urinib ko\\'ring.';",
    "els.dropzone.innerHTML = '❌ Xato!';\n" + satzbau_fail_logic
)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("App JS updated!")
