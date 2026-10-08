// WunderDeutsch Core Logic & i18n Engine

const TRANSLATIONS = {
    en: {
        "title_home": "Home", "title_ddd": "Der Die Das", "title_dict": "Dictionary", "title_settings": "Settings",
        "subtitle_ddd": "Gender Trainer", "subtitle_dict": "Your Vocabulary", "title_satzbau": "Sentence Puzzle", "subtitle_satzbau": "Sentence Puzzle",
        "title_grammar": "Grammar", "subtitle_grammar": "Rules", "daily_goal": "Daily Goal", "wotd": "WORD OF THE MOMENT",
        "listen": "Listen", "search": "Search word...", "settings_pref": "Preferences", "settings_sound": "Sound",
        "settings_vib": "Vibration", "settings_lang": "Language", "about_title": "About WunderDeutsch",
        "about_text": "WunderDeutsch is an interactive learning app specifically designed to master German playfully. Learn vocabulary, train articles, and build sentences!",
        "contact_title": "Contact", "game_prompt": "Which article is correct?", 
        "leave_guard_title": "Are you sure?", "leave_guard": "Are you sure you want to leave your homework? Progress might be lost.",
        "btn_stay": "Stay", "btn_leave": "Leave",
        "coming_soon": "Coming soon!", "coming_desc1": "I am preparing this feature!", "coming_desc2": "Grammar rules will be here soon!",
        "private_access": "Private Access Only", "btn_login": "Login", "msg_wrong": "Incorrect credentials.",
        "mascot_hello": "<strong>Hello! I'm Fritz.</strong>", "mascot_sub": "Let's learn with your own vocabulary!",
        "msg_correct": "Correct! Great job! 🎉", "msg_ohno": "Oh no! It is", "check": "Check"
    },
    de: {
        "title_home": "Home", "title_ddd": "Der Die Das", "title_dict": "Wörterbuch", "title_settings": "Einstellungen",
        "subtitle_ddd": "Artikel Trainer", "subtitle_dict": "Deine Vokabeln", "title_satzbau": "Satzbau", "subtitle_satzbau": "Satz-Puzzle",
        "title_grammar": "Grammatik", "subtitle_grammar": "Regeln", "daily_goal": "Tagesziel", "wotd": "WORT DES MOMENTS",
        "listen": "Aussprache hören", "search": "Wort suchen...", "settings_pref": "Präferenzen", "settings_sound": "Ton",
        "settings_vib": "Vibration", "settings_lang": "Sprache", "about_title": "Über WunderDeutsch",
        "about_text": "WunderDeutsch ist eine interaktive Lern-App, die speziell entwickelt wurde, um Deutsch auf spielerische Weise zu meistern. Lerne Vokabeln, trainiere Artikel und baue Sätze!",
        "contact_title": "Kontakt", "game_prompt": "Welcher Artikel ist richtig?", 
        "leave_guard_title": "Bist du sicher?", "leave_guard": "Bist du sicher, dass du deine Hausaufgaben verlassen möchtest?",
        "btn_stay": "Bleiben", "btn_leave": "Verlassen",
        "coming_soon": "Kommt bald!", "coming_desc1": "Ich bereite diese Funktion noch vor!", "coming_desc2": "Hier kommen bald Grammatikregeln hin!",
        "private_access": "Nur privater Zugang", "btn_login": "Einloggen", "msg_wrong": "Falsche Zugangsdaten.",
        "mascot_hello": "<strong>Hallo! Ich bin Fritz.</strong>", "mascot_sub": "Lass uns mit deinen eigenen Vokabeln lernen!",
        "msg_correct": "Richtig! Super gemacht! 🎉", "msg_ohno": "Oh nein! Es heißt", "check": "Prüfen"
    },
    uz: {
        "title_home": "Asosiy", "title_ddd": "Der Die Das", "title_dict": "Lug'at", "title_settings": "Sozlamalar",
        "subtitle_ddd": "Artikl Mashqi", "subtitle_dict": "Sizning so'zlaringiz", "title_satzbau": "Gap tuzish", "subtitle_satzbau": "Gap Pazzli",
        "title_grammar": "Grammatika", "subtitle_grammar": "Qoidalar", "daily_goal": "Kunlik maqsad", "wotd": "KUN SO'ZI",
        "listen": "Talaffuzni eshitish", "search": "So'z qidirish...", "settings_pref": "Afzalliklar", "settings_sound": "Ovoz",
        "settings_vib": "Vibratsiya", "settings_lang": "Til", "about_title": "WunderDeutsch haqida",
        "about_text": "WunderDeutsch - nemis tilini o'yin orqali o'rganish uchun maxsus ishlab chiqilgan interaktiv ilova. So'zlarni yodlang, artikllarni mashq qiling va gaplar tuzing!",
        "contact_title": "Aloqa", "game_prompt": "Qaysi artikl to'g'ri?", 
        "leave_guard_title": "Ishonchingiz komilmi?", "leave_guard": "Haqiqatan ham vazifani tark etmoqchimisiz?",
        "btn_stay": "Qolish", "btn_leave": "Chiqish",
        "coming_soon": "Tez orada!", "coming_desc1": "Men ushbu xususiyatni tayyorlayapman!", "coming_desc2": "Grammatika qoidalari tez orada bu yerda bo'ladi!",
        "private_access": "Faqat shaxsiy kirish", "btn_login": "Kirish", "msg_wrong": "Parol noto'g'ri.",
        "mascot_hello": "<strong>Salom! Men Fritsman.</strong>", "mascot_sub": "Keling, o'zingizning so'zlaringiz bilan o'rganamiz!",
        "msg_correct": "To'g'ri! Barakalla! 🎉", "msg_ohno": "Afsus! To'g'risi:", "check": "Tekshirish"
    }
};

const appState = {
    streak: 3, xp: 120, lives: 5, words: [], currentWotd: null, dddWord: null, currentView: 'home',
    settings: { sound: true, vibration: true, language: 'en' }
};

const AUTH_EMAIL = 'merser572@gmail.com';
const AUTH_PASS = 'Hasanboy0412';
let pendingView = null;

const els = {
    streak: document.getElementById('streak'), xp: document.getElementById('xp'),
    lives: document.getElementById('lives'), dddLives: document.getElementById('ddd-lives'),
    homeWotdTitle: document.getElementById('home-wotd-title'), homeWotdSub: document.getElementById('home-wotd-sub'),
    homeTtsBtn: document.getElementById('home-tts-btn'), dddWord: document.getElementById('ddd-word'),
    dddTrans: document.getElementById('ddd-translation'), dddSearch: document.getElementById('dict-search-input'),
    dddTtsBtn: document.getElementById('ddd-tts-btn')
};

async function initApp() {
    loadSettings();
    applyLanguage();
    setupAuth();
    setupModals();
    updateStats();
    await loadVocabulary();
    lucide.createIcons();
    
    els.homeTtsBtn.addEventListener('click', () => {
        triggerVibrate(50);
        if(appState.currentWotd) {
            const t = appState.currentWotd.article ? `${appState.currentWotd.article} ${appState.currentWotd.word}` : appState.currentWotd.word;
            speakText(t);
        }
    });

    els.dddTtsBtn.addEventListener('click', () => {
        if(appState.dddWord) speakText(appState.dddWord.word);
    });

    els.dddSearch.addEventListener('input', renderDictionary);
}

function loadSettings() {
    const saved = localStorage.getItem('wunderdeutsch_settings');
    if (saved) {
        appState.settings = JSON.parse(saved);
        if(!appState.settings.language) appState.settings.language = 'en';
    }
    document.getElementById('toggle-sound').checked = appState.settings.sound;
    document.getElementById('toggle-vibration').checked = appState.settings.vibration;
    
    document.querySelectorAll('.lang-btn').forEach(btn => {
        if(btn.getAttribute('data-lang') === appState.settings.language) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });
}

function toggleSetting(key) {
    appState.settings[key] = !appState.settings[key];
    saveSettings();
    if (appState.settings.sound && key === 'sound') playSound('success');
    if (appState.settings.vibration && key === 'vibration') triggerVibrate(50);
}

function changeLanguage(lang) {
    appState.settings.language = lang;
    saveSettings();
    applyLanguage();
    
    document.querySelectorAll('.lang-btn').forEach(btn => {
        if(btn.getAttribute('data-lang') === lang) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });
    
    if (appState.currentView === 'grammar') {
        renderGrammar();
    }
}

function saveSettings() {
    localStorage.setItem('wunderdeutsch_settings', JSON.stringify(appState.settings));
}

function applyLanguage() {
    const lang = appState.settings.language;
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (TRANSLATIONS[lang] && TRANSLATIONS[lang][key]) {
            if (el.tagName === 'INPUT' && el.hasAttribute('placeholder')) {
                el.setAttribute('placeholder', TRANSLATIONS[lang][key]);
            } else {
                el.innerHTML = TRANSLATIONS[lang][key];
            }
        }
    });
}

function setupAuth() {
    if (localStorage.getItem('wunderdeutsch_auth') === 'true') {
        document.getElementById('login-overlay').style.display = 'none';
        document.getElementById('app-container').style.display = 'block';
    } else {
        document.getElementById('login-overlay').style.display = 'flex';
        document.getElementById('app-container').style.display = 'none';
    }

    document.getElementById('login-btn').addEventListener('click', () => {
        if (document.getElementById('login-email').value === AUTH_EMAIL && document.getElementById('login-password').value === AUTH_PASS) {
            localStorage.setItem('wunderdeutsch_auth', 'true');
            document.getElementById('login-overlay').style.display = 'none';
            document.getElementById('app-container').style.display = 'block';
            lucide.createIcons();
        } else {
            document.getElementById('login-error').style.display = 'block';
            setTimeout(() => { document.getElementById('login-error').style.display = 'none'; }, 3000);
        }
    });
}

function setupModals() {
    document.getElementById('modal-cancel-btn').addEventListener('click', () => {
        document.getElementById('custom-modal-overlay').style.display = 'none';
        pendingView = null;
    });

    document.getElementById('modal-confirm-btn').addEventListener('click', () => {
        document.getElementById('custom-modal-overlay').style.display = 'none';
        if (pendingView) {
            executeSwitchView(pendingView);
            pendingView = null;
        }
    });
}

async function loadVocabulary() {
    try {
        const response = await fetch('words.json');
        appState.words = await response.json();
        setWordOfTheMoment();
        
        const resSentences = await fetch('sentences.json');
        appState.satzSentences = await resSentences.json();
    } catch (e) { console.error("Failed to load vocabulary or sentences:", e); }
}

function setWordOfTheMoment() {
    if(appState.words.length === 0) return;
    const nouns = appState.words.filter(w => w.article);
    if(nouns.length === 0) return;
    const rw = nouns[Math.floor(Math.random() * nouns.length)];
    appState.currentWotd = rw;
    els.homeWotdTitle.textContent = `${rw.article} ${rw.word}`;
    let sub = rw.translation;
    if(rw.plural) sub += ` (${rw.plural})`;
    els.homeWotdSub.textContent = sub;
}

function updateStats() {
    els.streak.textContent = appState.streak;
    els.xp.textContent = appState.xp;
    els.lives.textContent = appState.lives;
    els.dddLives.textContent = appState.lives;
}

function switchView(viewId) {
    // Custom Navigation Guard
    if (appState.currentView === 'derdiedas' && viewId !== 'derdiedas') {
        pendingView = viewId;
        document.getElementById('custom-modal-overlay').style.display = 'flex';
        return; // Wait for modal response
    }
    executeSwitchView(viewId);
}

function executeSwitchView(viewId) {
    triggerVibrate(30);
    document.querySelectorAll('.view').forEach(v => v.style.display = 'none');
    document.getElementById('view-' + viewId).style.display = 'block';
    
    document.querySelectorAll('.nav-item').forEach(btn => btn.classList.remove('active'));
    const iconMap = { 'home': 0, 'derdiedas': 1, 'satzbau': 2, 'dictionary': 3, 'grammar': 4 };
    if (iconMap[viewId] !== undefined) {
        document.querySelectorAll('.nav-item')[iconMap[viewId]].classList.add('active');
    }

    appState.currentView = viewId;
    if (viewId === 'derdiedas') initDerDieDas();
    if (viewId === 'dictionary') renderDictionary();
    if (viewId === 'satzbau') loadSatzbau();
    if (viewId === 'grammar') renderGrammar();
}

function initDerDieDas() {
    appState.failedCurrentWord = false; // Reset failure state for the new word

    // Re-enable and restore button colors
    document.querySelectorAll('.ddd-controls .btn-3d').forEach(b => {
        b.disabled = false;
        b.classList.remove('btn-disabled');
    });

    const nouns = appState.words.filter(w => w.article && ['der', 'die', 'das'].includes(w.article.toLowerCase()));
    if(nouns.length === 0) return;
    appState.dddWord = nouns[Math.floor(Math.random() * nouns.length)];
    els.dddWord.textContent = appState.dddWord.word;
    els.dddTrans.textContent = appState.dddWord.translation;
}

function checkArticle(guess) {
    if(!appState.dddWord) return;
    
    const correctArticle = appState.dddWord.article.toLowerCase();
    const correctMsg = TRANSLATIONS[appState.settings.language]['msg_correct'];
    const wrongMsg = TRANSLATIONS[appState.settings.language]['msg_ohno'];

    if(guess === correctArticle) {
        // Correct answer! Disable all buttons to prevent double tap
        document.querySelectorAll('.ddd-controls .btn-3d').forEach(b => {
            b.disabled = true;
            b.classList.add('btn-disabled');
        });
        // Keep the correct button highlighted
        const correctBtn = document.querySelector(`.btn-${correctArticle}`);
        if(correctBtn) correctBtn.classList.remove('btn-disabled');

        // Only award XP if they got it right on the first try!
        if (!appState.failedCurrentWord) {
            appState.xp += 10;
            updateStats();
        }

        playSound('success');
        triggerVibrate(40);
        showMascot(correctMsg, 1200); 
        setTimeout(initDerDieDas, 700); 
    } else {
        // Wrong answer!
        appState.failedCurrentWord = true;
        appState.lives = Math.max(0, appState.lives - 1);
        updateStats();
        
        const explanation = typeof getGrammarExplanation === 'function' ? getGrammarExplanation(appState.dddWord, appState.settings.language) : '';
        
        playSound('error');
        triggerVibrate([100, 50, 100]);
        showMascot(`${wrongMsg} "${appState.dddWord.article} ${appState.dddWord.word}".<br><span style="font-size:14px; opacity:0.9; margin-top:5px; display:block; font-weight:normal;">${explanation}</span>`, 0);
        
        // Disable ONLY the button they just incorrectly tapped
        const wrongBtn = document.querySelector(`.btn-${guess}`);
        if (wrongBtn) {
            wrongBtn.disabled = true;
            wrongBtn.classList.add('btn-disabled');
        }
        
        // Notice: No setTimeout here! The app now waits for them to pick the right one.
    }
}

function renderDictionary() {
    const query = els.dddSearch.value.toLowerCase();
    const list = document.getElementById('dict-list');
    list.innerHTML = '';
    const filtered = appState.words.filter(w => w.word.toLowerCase().includes(query) || w.translation.toLowerCase().includes(query));
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
    lucide.createIcons();
}

function showMascot(text, duration = 3500) {
    document.getElementById('mascot-msg').innerHTML = text;
    const mascot = document.getElementById('global-mascot');
    mascot.classList.add('show');
    if(window.mascotTimeout) clearTimeout(window.mascotTimeout);
    if(duration > 0) {
        window.mascotTimeout = setTimeout(() => { mascot.classList.remove('show'); }, duration);
    }
}

function triggerVibrate(pattern) {
    if (appState.settings.vibration && 'vibrate' in navigator) navigator.vibrate(pattern);
}

function playSound(type) {
    if (!appState.settings.sound) return;

    try {
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain); gain.connect(ctx.destination);
        if (type === 'success') {
            osc.type = 'sine';
            osc.frequency.setValueAtTime(800, ctx.currentTime);
            osc.frequency.exponentialRampToValueAtTime(1200, ctx.currentTime + 0.1);
            gain.gain.setValueAtTime(0.5, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.1);
            osc.start(); osc.stop(ctx.currentTime + 0.1);
        } else if (type === 'error') {
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(150, ctx.currentTime);
            osc.frequency.exponentialRampToValueAtTime(80, ctx.currentTime + 0.3);
            gain.gain.setValueAtTime(0.5, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.3);
            osc.start(); osc.stop(ctx.currentTime + 0.3);
        } else if (type === 'tap') {
            osc.type = 'sine';
            osc.frequency.setValueAtTime(600, ctx.currentTime);
            gain.gain.setValueAtTime(0.05, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.05);
            osc.start(); osc.stop(ctx.currentTime + 0.05);
        }
    } catch(e) {}
}

function speakText(text) {
    if (!appState.settings.sound) return;
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'de-DE';
        window.speechSynthesis.speak(utterance);
    }
}

window.addEventListener('DOMContentLoaded', initApp);

// --- SATZBAU LOGIC ---
function loadSatzbau() {
    if (!appState.satzSentences || appState.satzSentences.length === 0) return;
    
    // Reset state
    appState.satzLives = 5;
    document.getElementById('satz-lives').textContent = appState.satzLives;
    
    startSatzbauRound();
}

let satzSortableDropzone, satzSortableTiles;

function startSatzbauRound() {
    const sentence = appState.satzSentences[Math.floor(Math.random() * appState.satzSentences.length)];
    appState.currentSentence = sentence;
    
    document.getElementById('satz-translation').textContent = sentence.uz;
    
    const words = sentence.de.replace(/[.!?]/g, '').split(' ');
    const cleanWords = words.filter(w => w.trim().length > 0);
    
    for(let i = cleanWords.length - 1; i > 0; i--){
        const j = Math.floor(Math.random() * (i + 1));
        [cleanWords[i], cleanWords[j]] = [cleanWords[j], cleanWords[i]];
    }
    
    appState.satzAvailableWords = cleanWords;
    renderSatzbau();
}

function renderSatzbau() {
    const tilesContainer = document.getElementById('satz-tiles');
    const dropzone = document.getElementById('satz-dropzone');
    const checkBtn = document.getElementById('satz-check-btn');
    
    tilesContainer.innerHTML = '';
    dropzone.innerHTML = '';
    checkBtn.style.display = 'block'; // Always show button, or check dynamically
    
    appState.satzAvailableWords.forEach((word) => {
        const btn = document.createElement('button');
        btn.className = 'satz-tile';
        btn.textContent = word;
        btn.onclick = () => {
            playSound('tap');
            if (btn.parentElement === tilesContainer) {
                dropzone.appendChild(btn);
            } else {
                tilesContainer.appendChild(btn);
            }
        };
        tilesContainer.appendChild(btn);
    });
    
    // Initialize SortableJS
    if (window.Sortable) {
        if (satzSortableDropzone) satzSortableDropzone.destroy();
        if (satzSortableTiles) satzSortableTiles.destroy();
        
        satzSortableDropzone = new Sortable(dropzone, {
            group: 'satzbau',
            animation: 150,
            onEnd: () => playSound('tap')
        });
        
        satzSortableTiles = new Sortable(tilesContainer, {
            group: 'satzbau',
            animation: 150,
            onEnd: () => playSound('tap')
        });
    }
}

function checkSatzbau() {
    const target = appState.currentSentence.de.replace(/[.!?]/g, '').toLowerCase().trim();
    
    const dropzone = document.getElementById('satz-dropzone');
    const currentWords = [];
    dropzone.querySelectorAll('.satz-tile').forEach(btn => {
        currentWords.push(btn.textContent);
    });
    const current = currentWords.join(' ').toLowerCase().trim();
    
    if (current === target) {
        playSound('success');
        appState.xp += 15;
        updateStats();
        dropzone.style.borderColor = 'var(--green-btn)';
        dropzone.style.backgroundColor = '#e8fce8';
        
        setTimeout(() => {
            dropzone.style.borderColor = '#ccc';
            dropzone.style.backgroundColor = '#f7f7f7';
            startSatzbauRound();
        }, 1500);
    } else {
        playSound('error');
        appState.satzLives = Math.max(0, appState.satzLives - 1);
        document.getElementById('satz-lives').textContent = appState.satzLives;
        
        dropzone.style.borderColor = 'var(--red-btn)';
        
        // Shake animation
        dropzone.style.transition = 'transform 0.05s';
        dropzone.style.transform = 'translateX(5px)';
        setTimeout(() => dropzone.style.transform = 'translateX(-5px)', 50);
        setTimeout(() => dropzone.style.transform = 'translateX(5px)', 100);
        setTimeout(() => dropzone.style.transform = 'translateX(-5px)', 150);
        setTimeout(() => dropzone.style.transform = 'translateX(0)', 200);
        
        setTimeout(() => {
            dropzone.style.transition = '';
            dropzone.style.borderColor = '#ccc';
        }, 1000);
    }
}

// --- GRAMMAR TAB LOGIC ---

const GRAMMAR_DATA = [{"id": "gender_articles", "title": "1. Der, Die, Das & Gender Clues", "tag": "Articles", "summary": "German nouns have three genders: Masculine (der), Feminine (die), and Neuter (das). Plural nouns always use 'die'.", "color": "#74B9FF", "rules": [{"label": "Der (Masculine)", "tip": "Male people/animals, days, months, seasons, and nouns ending in -er, -ling, -or, -ismus (der Sommer, der Montag, der Lehrer)."}, {"label": "Die (Feminine)", "tip": "Female people/animals, and nouns ending in -ung, -heit, -keit, -schaft, -tion, -tät, -ei (die Zeitung, die Freiheit, die Bäckerei)."}, {"label": "Das (Neuter)", "tip": "Diminutives ending in -chen, -lein, infinitive nouns, and endings in -ment, -um, -tum (das Mädchen, das Brötchen, das Essen, das Museum)."}, {"label": "Die (Plural)", "tip": "All plural nouns use 'die' in the nominative case regardless of their original singular gender!"}], "table": {"headers": ["Gender", "Definite (The)", "Indefinite (A/An)", "Negative (No/None)"], "rows": [["Masculine", "der Tisch", "ein Tisch", "kein Tisch"], ["Feminine", "die Katze", "eine Katze", "keine Katze"], ["Neuter", "das Buch", "ein Buch", "kein Buch"], ["Plural", "die Kinder", "(kein Plural-ein)", "keine Kinder"]]}, "fritz_tip": "Look at the ending of the word! 99% of words ending in -ung, -heit, -keit, and -schaft are DIE. Words ending in -chen or -lein are always DAS (even das Mädchen)! 🦊💡", "quiz": [{"q": "What is the article for 'Zeitung' (newspaper)?", "options": ["der", "die", "das"], "answer": 1, "hint": "Words ending in -ung are always feminine!"}, {"q": "What is the article for 'Mädchen' (girl)?", "options": ["der", "die", "das"], "answer": 2, "hint": "The diminutive ending -chen always makes a noun neuter!"}, {"q": "Which article do all plural nouns take in Nominative?", "options": ["der", "die", "das"], "answer": 1, "hint": "Plural always takes 'die' in Nominative."}]}, {"id": "cases_nom_akk", "title": "2. Cases: Nominative vs. Accusative", "tag": "Cases", "summary": "The Nominative case marks the SUBJECT (who does the action). The Accusative case marks the DIRECT OBJECT (who/what receives the action).", "color": "#FF7675", "rules": [{"label": "The Magic Shift", "tip": "ONLY the masculine gender changes in Accusative: der -> den, ein -> einen, kein -> keinen. Feminine, Neuter, and Plural do not change!"}, {"label": "Subject (Wer/Was?)", "tip": "Der Mann trinkt einen Kaffee. -> 'Der Mann' is the subject (Nominative)."}, {"label": "Direct Object (Wen/Was?)", "tip": "Er trinkt den Kaffee. -> 'den Kaffee' is the direct object (Accusative)."}, {"label": "Fixed Accusative Prepositions", "tip": "bis, durch, für, gegen, ohne, um (Mnemonic: DOGFU / BDFGOU). These prepositions ALWAYS require Accusative!"}], "table": {"headers": ["Case", "Masculine", "Feminine", "Neuter", "Plural"], "rows": [["Nominative", "der / ein / kein", "die / eine / keine", "das / ein / kein", "die / - / keine"], ["Accusative", "den / einen / keinen", "die / eine / keine", "das / ein / kein", "die / - / keine"]]}, "fritz_tip": "Remember: Only the masculine gets the 'N' in Accusative! 'Ich habe EINEN Hund (m), EINE Katze (f), EIN Auto (n)'. 🦊🐶", "quiz": [{"q": "Fill in the blank: 'Ich kaufe _____ Apfel (m)'.", "options": ["ein", "einen", "eine"], "answer": 1, "hint": "Apfel is masculine and is the direct object: ein -> einen."}, {"q": "Which preposition ALWAYS takes the Accusative case?", "options": ["mit", "nach", "für"], "answer": 2, "hint": "'für' is always accusative (Das ist für dich!)."}, {"q": "What happens to feminine nouns ('die Tasche') in Accusative?", "options": ["Changes to 'den'", "Changes to 'der'", "Stays 'die'"], "answer": 2, "hint": "Feminine and Neuter never change between Nominative and Accusative."}]}, {"id": "cases_dative", "title": "3. Dative Case Basics", "tag": "Cases", "summary": "The Dative case marks the INDIRECT OBJECT (to whom / for whom) and is required after key everyday prepositions.", "color": "#55EFC4", "rules": [{"label": "Dative Article Shifts", "tip": "der -> dem, das -> dem, die -> der, die (pl) -> den + n on the noun!"}, {"label": "Fixed Dative Prepositions", "tip": "aus, bei, mit, nach, seit, von, zu (Sing to the melody of Blue Danube: aus-bei-mit, nach-seit-von-zu!)."}, {"label": "Common Dative Verbs", "tip": "helfen (hilf mir!), danken (ich danke dir), gefallen (das gefällt mir), schmecken (das schmeckt mir)."}], "table": {"headers": ["Gender", "Nominative", "Accusative", "Dative"], "rows": [["Masculine", "der / ein", "den / einen", "dem / einem"], ["Feminine", "die / eine", "die / eine", "der / einer"], ["Neuter", "das / ein", "das / ein", "dem / einem"], ["Plural", "die / -", "die / -", "den / - (+n)"]]}, "fritz_tip": "Sing the magic rhyme: 'Aus, bei, mit, nach, seit, von, zu — immer mit dem Dativ, du!' 🎶🦊", "quiz": [{"q": "Fill in: 'Ich fahre mit _____ Bus (m)'.", "options": ["den", "dem", "der"], "answer": 1, "hint": "'mit' requires Dative, so 'der' becomes 'dem'."}, {"q": "What does feminine 'die' turn into in Dative?", "options": ["dem", "der", "den"], "answer": 1, "hint": "Feminine 'die' flips to 'der' in the Dative case."}, {"q": "Which verb always takes a Dative object?", "options": ["helfen", "kaufen", "sehen"], "answer": 0, "hint": "'helfen' takes Dative: 'Ich helfe dir'."}]}, {"id": "verb_conjugation", "title": "4. Present Tense Verb Conjugation", "tag": "Verbs", "summary": "German verbs change their endings based on the subject pronoun: -e, -st, -t, -en, -t, -en.", "color": "#FFEAA7", "rules": [{"label": "Regular Endings", "tip": "ich -e | du -st | er/sie/es -t | wir -en | ihr -t | sie/Sie -en."}, {"label": "Vowel Changers (du / er)", "tip": "e -> i/ie (sprechen -> du sprichst, lesen -> er liest); a -> ä (fahren -> du fährst, schlafen -> er schläft)."}, {"label": "Verbs ending in -t / -d", "tip": "Add an extra 'e' for pronunciation: arbeiten -> du arbeitest, er arbeitet."}], "table": {"headers": ["Pronoun", "lernen (regular)", "fahren (a->ä)", "sprechen (e->i)"], "rows": [["ich", "lerne", "fahre", "spreche"], ["du", "lernst", "fährst", "sprichst"], ["er / sie / es", "lernt", "fährt", "spricht"], ["wir", "lernen", "fahren", "sprechen"], ["ihr", "lernt", "fahrt", "sprecht"], ["sie / Sie", "lernen", "fahren", "sprechen"]]}, "fritz_tip": "Remember the formula: 'E - ST - T - EN - T - EN'. Just drop the -en from the infinitive and snap on the matching ending! 🦊✨", "quiz": [{"q": "Conjugate: 'Du _____ (sprechen) sehr gut Deutsch.'", "options": ["sprechtest", "sprechst", "sprichst"], "answer": 2, "hint": "'sprechen' has an e -> i vowel change for 'du' and 'er/sie/es'."}, {"q": "Conjugate: 'Er _____ (fahren) mit dem Zug.'", "options": ["fahrt", "fährst", "fährt"], "answer": 2, "hint": "'fahren' takes an umlaut (ä) in the 3rd person singular."}, {"q": "What is the ending for 'wir' (we)?", "options": ["-e", "-t", "-en"], "answer": 2, "hint": "'wir' always takes the '-en' ending (identical to the infinitive)."}]}, {"id": "sein_haben", "title": "5. The Big Three: Sein, Haben & Werden", "tag": "Verbs", "summary": "These three irregular auxiliary verbs are the absolute backbone of German conversation and future/past tenses.", "color": "#A29BFE", "rules": [{"label": "sein (to be)", "tip": "Essential for identity, adjectives, professions, and location: 'Ich bin glücklich'."}, {"label": "haben (to have)", "tip": "Expresses possession and many idioms: 'Ich habe Hunger/Durst/Zeit'."}, {"label": "werden (to become)", "tip": "Used for changes of state and future tense: 'Es wird kalt'."}], "table": {"headers": ["Pronoun", "sein (to be)", "haben (to have)", "werden (to become)"], "rows": [["ich", "bin", "habe", "werde"], ["du", "bist", "hast", "wirst"], ["er / sie / es", "ist", "hat", "wird"], ["wir", "sind", "haben", "werden"], ["ihr", "seid", "habt", "werdet"], ["sie / Sie", "sind", "haben", "werden"]]}, "fritz_tip": "Watch out for 'ihr seid' (you all are) vs. 'sie sind' (they are). They are easy to mix up! 🦊", "quiz": [{"q": "Fill in: 'Wir _____ zwei Brüder.'", "options": ["sind", "haben", "werdet"], "answer": 1, "hint": "Having family members uses 'haben'."}, {"q": "Fill in: 'Wie alt _____ du?'", "options": ["hast", "bist", "wirst"], "answer": 1, "hint": "In German, you 'are' your age (sein), you don't 'have' it."}, {"q": "What is 'ihr' for the verb 'sein'?", "options": ["sind", "seid", "bist"], "answer": 1, "hint": "'ihr seid' is the 2nd person plural form."}]}, {"id": "modal_verbs", "title": "6. Modal Verbs & The Sentence Bracket", "tag": "Modal Verbs", "summary": "Modal verbs express ability, necessity, or desire. They send the main infinitive verb to the end of the sentence!", "color": "#FDCB6E", "rules": [{"label": "können (can / able)", "tip": "ich kann, du kannst, er kann, wir können"}, {"label": "müssen (must / have to)", "tip": "ich muss, du musst, er muss, wir müssen"}, {"label": "wollen (want to)", "tip": "ich will, du willst, er will, wir wollen"}, {"label": "möchten (would like)", "tip": "ich möchte, du möchtest, er möchte, wir möchten"}, {"label": "dürfen (may / allowed)", "tip": "ich darf, du darfst, er darf, wir dürfen"}, {"label": "sollen (should / ought)", "tip": "ich soll, du sollst, er soll, wir sollen"}], "table": {"headers": ["Position 1", "Position 2 (Modal)", "Middle (Time/Place/Object)", "End (Infinitive)"], "rows": [["Ich", "kann", "gut Deutsch", "sprechen."], ["Wir", "müssen", "heute die Hausaufgaben", "machen."], ["Er", "möchte", "einen Kaffee", "trinken."]]}, "fritz_tip": "Notice that 'ich' and 'er/sie/es' have the EXACT same form with all modal verbs: 'ich kann' = 'er kann'! 🦊🎉", "quiz": [{"q": "Where does the second verb go when using a modal verb?", "options": ["Right after the modal verb", "At the very end of the sentence", "Before the subject"], "answer": 1, "hint": "The main verb in infinitive form closes the bracket at the very end."}, {"q": "Conjugate: 'Er _____ (können) sehr schnell laufen.'", "options": ["kann", "könnt", "kannst"], "answer": 0, "hint": "3rd person singular of können is 'kann' (no -t ending!)."}, {"q": "Which modal verb expresses 'permission'?", "options": ["müssen", "wollen", "dürfen"], "answer": 2, "hint": "'dürfen' means to be allowed / permitted."}]}, {"id": "word_order", "title": "7. Word Order & The V2 Golden Rule", "tag": "Syntax", "summary": "In main clauses, the conjugated verb ALWAYS occupies the 2nd position. Even if you start with time or place!", "color": "#00B894", "rules": [{"label": "Standard SVO", "tip": "[Position 1: Subject] + [Position 2: VERB] + [Rest]. Example: 'Ich lerne heute Deutsch.'"}, {"label": "Inversion (Time first)", "tip": "[Position 1: Time/Place] + [Position 2: VERB] + [Position 3: Subject]. Example: 'Heute lerne ich Deutsch.'"}, {"label": "Questions", "tip": "Yes/No questions put Verb in Position 1: 'Lernst du Deutsch?' W-questions put W-word in Pos 1, Verb in Pos 2: 'Wo lernst du Deutsch?'"}], "table": {"headers": ["Type", "Pos 1", "Pos 2 (VERB)", "Pos 3", "End"], "rows": [["Subject First", "Ich", "trinke", "morgens Kaffee", "-"], ["Time First", "Morgens", "trinke", "ich", "Kaffee"], ["Yes/No Question", "Trinkst", "du", "morgens Kaffee", "?"], ["W-Question", "Wann", "trinkst", "du Kaffee", "?"]]}, "fritz_tip": "Position 2 does NOT mean the second word — it means the second grammatical block! 'Meine liebe Oma [1] kocht [2] die Suppe.' 🦊🍲", "quiz": [{"q": "What happens if a sentence starts with 'Gestern' (Yesterday)?", "options": ["Subject comes next", "Verb comes next", "Object comes next"], "answer": 1, "hint": "The verb MUST stay in Position 2: 'Gestern ging ich...'."}, {"q": "Which sentence has correct word order?", "options": ["Heute ich fahre nach Berlin.", "Heute fahre ich nach Berlin.", "Fahre heute ich nach Berlin."], "answer": 1, "hint": "Pos 1: Heute, Pos 2: fahre, Pos 3: ich."}, {"q": "Where does the verb sit in a Yes/No question?", "options": ["Position 1", "Position 2", "At the end"], "answer": 0, "hint": "'Kommst du morgen?' -> Verb is in Position 1."}]}, {"id": "negation", "title": "8. Negation: Nicht vs. Kein", "tag": "Grammar", "summary": "Never mix them up: use 'kein' for nouns with indefinite or zero articles, and 'nicht' for verbs, adjectives, and specific nouns.", "color": "#E17055", "rules": [{"label": "When to use KEIN", "tip": "Replaces 'ein' or zero-article nouns: 'Ich habe EIN Auto' -> 'Ich habe KEIN Auto'. 'Ich habe Zeit' -> 'Ich habe KEINE Zeit'."}, {"label": "When to use NICHT", "tip": "Negates verbs, adjectives, adverbs, pronouns, and nouns with definite articles ('der/die/das'): 'Ich schlafe NICHT', 'Das ist NICHT gut', 'Ich kenne DEN Mann NICHT'."}, {"label": "Doch!", "tip": "If someone asks a negative question ('Kommst du nicht?') and you want to say yes, use 'DOCH!' instead of 'Ja'."}], "table": {"headers": ["Item to Negate", "Use", "Affirmative Example", "Negative Example"], "rows": [["Noun with 'ein'", "kein", "Ich habe ein Buch.", "Ich habe kein Buch."], ["Noun with no article", "keine", "Ich trinke Milch.", "Ich trinke keine Milch."], ["Verb / Entire action", "nicht", "Ich schwimme gern.", "Ich schwimme nicht gern."], ["Adjective", "nicht", "Das Hotel ist teuer.", "Das Hotel ist nicht teuer."], ["Specific noun (der/die/das)", "nicht", "Ich suche den Schlüssel.", "Ich suche den Schlüssel nicht."]]}, "fritz_tip": "If you could say 'no/not any' in English, use 'kein'. For everything else, use 'nicht'! 🦊⛔", "quiz": [{"q": "Fill in: 'Ich habe _____ Zeit.' (Zeit is feminine, zero article)", "options": ["nicht", "keine", "keinen"], "answer": 1, "hint": "Negating a zero-article feminine noun takes 'keine'."}, {"q": "Fill in: 'Das Essen ist _____ teuer.'", "options": ["nicht", "kein", "keine"], "answer": 0, "hint": "Negating an adjective ('teuer') takes 'nicht'."}, {"q": "Someone asks: 'Hast du keinen Hunger?' You are very hungry. You answer:", "options": ["Ja!", "Doch!", "Nein!"], "answer": 1, "hint": "'Doch' contradicts a negative question."}]}, {"id": "prepositions", "title": "9. Common Prepositions & Cases", "tag": "Prepositions", "summary": "Prepositions dictate the case of the noun that follows them. Master the essential A1 prepositions!", "color": "#0984E3", "rules": [{"label": "Dative Prepositions", "tip": "aus (from), bei (at/with), mit (with), nach (after/to), seit (since), von (from/of), zu (to). ALWAYS Dative!"}, {"label": "Accusative Prepositions", "tip": "bis (until), durch (through), für (for), gegen (against/around), ohne (without), um (at/around). ALWAYS Accusative!"}, {"label": "Contractions", "tip": "in + dem = im | an + dem = am | zu + dem = zum | zu + der = zur | bei + dem = beim | für + das = fürs."}], "table": {"headers": ["Preposition", "Case", "Meaning", "Example"], "rows": [["mit", "Dativ", "with / by (transit)", "Ich fahre mit dem Bus."], ["für", "Akkusativ", "for", "Das Geschenk ist für dich."], ["zu", "Dativ", "to", "Ich gehe zum Arzt."], ["ohne", "Akkusativ", "without", "Kaffee ohne Zucker bitte."], ["bei", "Dativ", "at / with", "Ich wohne bei meinen Eltern."], ["nach", "Dativ", "after / to (city/country)", "Nach dem Essen schlafe ich."]]}, "fritz_tip": "Remember: 'zum' = zu dem (masc/neut), 'zur' = zu der (fem). 'Ich gehe zum Arzt, aber zur Bank!' 🦊🏦", "quiz": [{"q": "Fill in: 'Ein Kaffee _____ (without) Milch bitte.'", "options": ["mit", "ohne", "für"], "answer": 1, "hint": "'ohne' means without."}, {"q": "What is the contraction for 'in dem'?", "options": ["im", "am", "ans"], "answer": 0, "hint": "'in + dem' contracts to 'im'."}, {"q": "Which preposition means 'since' and takes Dative?", "options": ["nach", "seit", "von"], "answer": 1, "hint": "'seit' means since / for a period of time: 'seit einem Jahr'."}]}, {"id": "plurals", "title": "10. Plural Patterns & Noun Endings", "tag": "Nouns", "summary": "Unlike English (-s), German has 5 main plural patterns: -e, -(e)n, -er, -s, and no ending (often with umlauts).", "color": "#6C5CE7", "rules": [{"label": "Pattern 1: -e (often with Umlaut)", "tip": "Common for masculine & neuter nouns: der Tisch -> die Tische, der Baum -> die Bäume."}, {"label": "Pattern 2: -(e)n", "tip": "Standard for ~90% of feminine nouns: die Frau -> die Frauen, die Lampe -> die Lampen."}, {"label": "Pattern 3: -er (usually with Umlaut)", "tip": "Mostly short neuter nouns: das Kind -> die Kinder, das Buch -> die Bücher, das Bild -> die Bilder."}, {"label": "Pattern 4: -s", "tip": "Foreign loanwords and abbreviations: das Auto -> die Autos, das Sofa -> die Sofas, das Handy -> die Handys."}, {"label": "Pattern 5: No ending (or just Umlaut)", "tip": "Nouns ending in -el, -en, -er: der Lehrer -> die Lehrer, der Apfel -> die Äpfel, der Computer -> die Computer."}], "table": {"headers": ["Singular", "Plural", "Pattern", "English"], "rows": [["der Tag", "die Tage", "+e", "day -> days"], ["die Zeitung", "die Zeitungen", "+en", "newspaper -> newspapers"], ["das Kind", "die Kinder", "+er", "child -> children"], ["das Auto", "die Autos", "+s", "car -> cars"], ["der Apfel", "die Äpfel", "Umlaut only", "apple -> apples"]]}, "fritz_tip": "Whenever you learn a German noun, always learn it with its article AND its plural: 'der Tisch, die Tische'! 🦊📚", "quiz": [{"q": "What is the plural of 'das Buch'?", "options": ["die Buche", "die Büchen", "die Bücher"], "answer": 2, "hint": "Das Buch takes an umlaut and -er: die Bücher."}, {"q": "What is the plural ending for most feminine nouns ending in -ung?", "options": ["-e", "-en", "-s"], "answer": 1, "hint": "die Zeitung -> die Zeitungen."}, {"q": "What is the plural of 'das Auto'?", "options": ["die Autos", "die Auton", "die Autoe"], "answer": 0, "hint": "Loanwords usually take -s."}]}];

function renderGrammar() {
    const container = document.getElementById('grammar-cards-container');
    if (!container) return;
    container.innerHTML = '';

    GRAMMAR_DATA.forEach((chap, idx) => {
        const card = document.createElement('div');
        card.className = 'grammar-item';
        card.style.marginBottom = '12px';
        card.style.cursor = 'pointer';
        
        card.innerHTML = `
            <div class="grammar-header" style="background: #fff;">
                <span style="font-size: 16px; font-weight: 800; color: #2D3436;">${chap.title}</span>
                <span style="font-size: 11px; font-weight: 800; padding: 2px 8px; border-radius: 12px; background: #E8F8F5; color: #16A085; border: 1px solid #16A085;">${chap.tag}</span>
            </div>
            <div class="grammar-body" style="display: block; max-height: none; padding: 0 20px 15px 20px; background: #fff; border-bottom: 2px solid transparent;">
                <p style="font-size:13px; color:var(--text-muted); line-height:1.4;">${chap.summary}</p>
            </div>
        `;
        
        card.onclick = () => openGrammarChapter(idx);
        container.appendChild(card);
    });
}

let activeGrammarChap = null;

function openGrammarChapter(idx) {
    playSound('tap');
    activeGrammarChap = GRAMMAR_DATA[idx];
    document.getElementById('gm-title').innerText = activeGrammarChap.title;
    document.getElementById('gm-summary').innerText = activeGrammarChap.summary;
    document.getElementById('gm-fritz-tip').innerText = activeGrammarChap.fritz_tip;

    const rulesBox = document.getElementById('gm-rules-list');
    rulesBox.innerHTML = '';
    activeGrammarChap.rules.forEach(r => {
        const div = document.createElement('div');
        div.style.marginBottom = '10px';
        div.innerHTML = `<span style="font-weight:800; font-size:16px; color:#0984E3;">• ${r.label}:</span> <span style="font-size:15px; color:#2D3436; line-height:1.5;">${r.tip}</span>`;
        rulesBox.appendChild(div);
    });

    const tableBox = document.getElementById('gm-table-container');
    tableBox.innerHTML = '';
    if (activeGrammarChap.table) {
        let ths = activeGrammarChap.table.headers.map(h => `<th>${h}</th>`).join('');
        let trs = activeGrammarChap.table.rows.map(row => `<tr>${row.map(c => `<td>${c}</td>`).join('')}</tr>`).join('');
        tableBox.innerHTML = `<div style="width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch; margin-bottom: 16px;"><table class="rule-table" style="min-width: 450px;"><thead><tr>${ths}</tr></thead><tbody>${trs}</tbody></table></div>`;
    }

    const quizBox = document.getElementById('gm-quiz-container');
    quizBox.innerHTML = '';
    activeGrammarChap.quiz.forEach((qObj, qIdx) => {
        const qDiv = document.createElement('div');
        qDiv.style.margin = '14px 0';
        qDiv.style.background = '#F8F9FA';
        qDiv.style.border = '2px solid var(--border-color)';
        qDiv.style.borderRadius = '14px';
        qDiv.style.padding = '14px 16px';
        
        let opts = qObj.options.map((opt, oIdx) => `
            <button style="margin-top:8px; font-size:15px; font-weight:800; color:#2D3436; background:#fff; border:2px solid var(--border-color); border-radius:12px; padding:12px 16px; width: 100%; text-align:left; cursor:pointer; box-shadow: 0 4px 0 var(--border-color);" onclick="answerGrammarQuiz(${qIdx}, ${oIdx}, this)">
                ${opt}
            </button>
        `).join('');

        qDiv.innerHTML = `
            <div style="font-weight:800; font-size:16px; margin-bottom:8px; color:#2D3436;">Frage ${qIdx + 1}: ${qObj.q}</div>
            <div class="opts-group" id="quiz-opts-${qIdx}">${opts}</div>
            <div id="quiz-feedback-${qIdx}" style="font-size:14px; font-weight:700; margin-top:10px; display:none; line-height:1.5;"></div>
        `;
        quizBox.appendChild(qDiv);
    });

    const modal = document.getElementById('modal-grammar-detail');
    modal.style.display = 'flex';
}

function answerGrammarQuiz(qIdx, oIdx, btn) {
    if (!activeGrammarChap) return;
    const qObj = activeGrammarChap.quiz[qIdx];
    const feed = document.getElementById(`quiz-feedback-${qIdx}`);
    const parent = document.getElementById(`quiz-opts-${qIdx}`);
    
    parent.querySelectorAll('button').forEach(b => b.disabled = true);
    
    feed.style.display = 'block';
    if (oIdx === qObj.answer) {
        playSound('success');
        btn.style.background = '#55EFC4';
        feed.style.color = '#00B894';
        feed.innerText = '✅ Richtig! ' + qObj.hint;
        appState.xp += 10;
        updateStats();
    } else {
        playSound('error');
        btn.style.background = '#FF7675';
        feed.style.color = '#D63031';
        feed.innerText = '❌ Nicht ganz: ' + qObj.hint;
    }
}

function closeGrammarModal() {
    playSound('tap');
    document.getElementById('modal-grammar-detail').style.display = 'none';
}
