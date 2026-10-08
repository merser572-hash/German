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
    document.getElementById('lang-select').value = appState.settings.language;
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
        showMascot(`${wrongMsg} "${appState.dddWord.article} ${appState.dddWord.word}".<br><span style="font-size:14px; opacity:0.9; margin-top:5px; display:block; font-weight:normal;">${explanation}</span>`, 4500);
        
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
    window.mascotTimeout = setTimeout(() => { mascot.classList.remove('show'); }, duration);
}

function triggerVibrate(pattern) {
    if (appState.settings.vibration && 'vibrate' in navigator) navigator.vibrate(pattern);
}

function playSound(type) {
    if (!appState.settings.sound) return;
    
    if (window.Sfx) {
        if (type === 'success') { window.Sfx.playSuccessChime(); return; }
        if (type === 'error') { window.Sfx.playSlipperBonk(); return; }
    }

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
    appState.satzSelectedWords = [];
    
    renderSatzbau();
}

function renderSatzbau() {
    const tilesContainer = document.getElementById('satz-tiles');
    const dropzone = document.getElementById('satz-dropzone');
    const checkBtn = document.getElementById('satz-check-btn');
    
    tilesContainer.innerHTML = '';
    dropzone.innerHTML = '';
    
    appState.satzAvailableWords.forEach((word, idx) => {
        const btn = document.createElement('button');
        btn.className = 'satz-tile';
        btn.textContent = word;
        if(word === null) {
            btn.classList.add('hidden');
        } else {
            btn.onclick = () => {
                if(window.Sfx) window.Sfx.playTap();
                appState.satzSelectedWords.push({word: word, origIdx: idx});
                appState.satzAvailableWords[idx] = null;
                renderSatzbau();
            };
        }
        tilesContainer.appendChild(btn);
    });
    
    appState.satzSelectedWords.forEach((item, selIdx) => {
        const btn = document.createElement('button');
        btn.className = 'satz-tile';
        btn.textContent = item.word;
        btn.onclick = () => {
            if(window.Sfx) window.Sfx.playTap();
            appState.satzAvailableWords[item.origIdx] = item.word;
            appState.satzSelectedWords.splice(selIdx, 1);
            renderSatzbau();
        };
        dropzone.appendChild(btn);
    });
    
    if(appState.satzSelectedWords.length > 0) {
        checkBtn.style.display = 'block';
    } else {
        checkBtn.style.display = 'none';
    }
}

function checkSatzbau() {
    const target = appState.currentSentence.de.replace(/[.!?]/g, '').toLowerCase().trim();
    const current = appState.satzSelectedWords.map(w => w.word).join(' ').toLowerCase().trim();
    
    const dropzone = document.getElementById('satz-dropzone');
    
    if (current === target) {
        if(window.Sfx) window.Sfx.playSuccessChime();
        appState.xp += 15;
        updateStats();
        dropzone.style.borderColor = 'var(--green-btn)';
        dropzone.style.backgroundColor = '#e8fce8';
        
        setTimeout(() => {
            dropzone.style.borderColor = '#ccc';
            dropzone.style.backgroundColor = 'var(--bg-card)';
            startSatzbauRound();
        }, 1500);
    } else {
        if(window.Sfx) window.Sfx.playSlipperBonk();
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
