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
const A1_GRAMMAR = {
    en: [
        { title: "Articles (Der, Die, Das)", content: "In German, nouns have three genders...<br><b>der</b> (masculine)<br><b>die</b> (feminine)<br><b>das</b> (neuter).<br><br>Rules:<br>Words ending in <b>-ung, -heit, -keit, -schaft, -tion</b> are almost always <b>die</b>.<br>Words ending in <b>-chen, -lein, -ment</b> are almost always <b>das</b>.<br>Words ending in <b>-ismus, -or, -ling</b> are almost always <b>der</b>." },
        { title: "Plurals", content: "There are 5 main ways to form plurals:<br>1. <b>-e</b> (der Tag -> die Tage)<br>2. <b>-er</b> (das Kind -> die Kinder)<br>3. <b>-(e)n</b> (die Frau -> die Frauen)<br>4. <b>-s</b> (das Auto -> die Autos)<br>5. <b>No change</b> (der Lehrer -> die Lehrer)" },
        { title: "Personal Pronouns", content: "<b>ich</b> = I<br><b>du</b> = you (informal)<br><b>er/sie/es</b> = he/she/it<br><b>wir</b> = we<br><b>ihr</b> = you all<br><b>sie/Sie</b> = they / you (formal)" },
        { title: "Regular Verb Conjugation", content: "Example: <b>machen</b> (to do/make)<br>ich mach<b>e</b><br>du mach<b>st</b><br>er/sie/es mach<b>t</b><br>wir mach<b>en</b><br>ihr mach<b>t</b><br>sie/Sie mach<b>en</b>" },
        { title: "Special Verb Endings", content: "<b>heißen (to be called):</b> Verbs ending in -s, -ß, -z drop the extra 's' for 'du'.<br>ich heiße, du <b>heißt</b>, er heißt.<br><br><b>arbeiten (to work):</b> Verbs ending in -t or -d add an extra 'e' for pronunciation.<br>ich arbeite, du arbeit<b>e</b>st, er arbeit<b>e</b>t." },
        { title: "Modal Verbs", content: "For modal verbs, 'ich' and 'er/sie/es' are exactly the same and take NO ending!<br><br><b>können (can/be able to):</b><br>ich kann, du kannst, er kann, wir können, ihr könnt, sie können.<br><br><b>müssen (must):</b><br>ich muss, du musst, er muss, wir müssen, ihr müsst, sie müssen.<br><br><b>wollen (want to):</b><br>ich will, du willst, er will, wir wollen, ihr wollt, sie wollen.<br><br><b>möchten (would like to):</b><br>ich möchte, du möchtest, er möchte, wir möchten, ihr möchtet, sie möchten." },
        { title: "Irregular Verbs (Vowel Change)", content: "Some verbs change their stem vowel for <b>du</b> and <b>er/sie/es</b>.<br><br><b>e -> i/ie (sprechen, lesen, sehen, essen):</b><br>sprechen: ich spreche, du <b>sprichst</b>, er <b>spricht</b><br>lesen: ich lese, du <b>liest</b>, er <b>liest</b><br><br><b>a -> ä (fahren, schlafen):</b><br>fahren: ich fahre, du <b>fährst</b>, er <b>fährt</b>" },
        { title: "Important Irregular Verbs", content: "<b>sein (to be):</b><br>ich bin, du bist, er ist, wir sind, ihr seid, sie sind.<br><br><b>haben (to have):</b><br>ich habe, du hast, er hat, wir haben, ihr habt, sie haben." },
        { title: "Sentence Structure (Satzbau)", content: "<b>Rule 1:</b> The conjugated verb is always in position 2 in a normal sentence.<br>Example: Ich <b>gehe</b> heute ins Kino.<br><br><b>Rule 2:</b> If you start with time, the verb stays in position 2, and the subject moves to position 3.<br>Example: Heute <b>gehe</b> ich ins Kino." },
        { title: "Accusative Case", content: "The accusative case is used for the direct object. Only masculine (der) changes!<br><b>der -> den / ein -> einen / kein -> keinen</b><br>die -> die / eine -> eine / keine -> keine<br>das -> das / ein -> ein / kein -> kein<br><br>Example: Ich habe <b>einen</b> Hund (der Hund)." }
    ],
    de: [
        { title: "Artikel (Der, Die, Das)", content: "Im Deutschen haben Nomen drei Geschlechter...<br><b>der</b> (männlich)<br><b>die</b> (weiblich)<br><b>das</b> (sächlich).<br><br>Regeln:<br>Wörter auf <b>-ung, -heit, -keit, -schaft, -tion</b> sind fast immer <b>die</b>.<br>Wörter auf <b>-chen, -lein, -ment</b> sind fast immer <b>das</b>.<br>Wörter auf <b>-ismus, -or, -ling</b> sind fast immer <b>der</b>." },
        { title: "Pluralbildung", content: "Es gibt 5 Hauptwege, den Plural zu bilden:<br>1. <b>-e</b> (der Tag -> die Tage)<br>2. <b>-er</b> (das Kind -> die Kinder)<br>3. <b>-(e)n</b> (die Frau -> die Frauen)<br>4. <b>-s</b> (das Auto -> die Autos)<br>5. <b>Keine Änderung</b> (der Lehrer -> die Lehrer)" },
        { title: "Personalpronomen", content: "<b>ich</b> = ich<br><b>du</b> = du<br><b>er/sie/es</b> = er/sie/es<br><b>wir</b> = wir<br><b>ihr</b> = ihr<br><b>sie/Sie</b> = sie/Sie (Höflichkeitsform)" },
        { title: "Regelmäßige Verben", content: "Beispiel: <b>machen</b><br>ich mach<b>e</b><br>du mach<b>st</b><br>er/sie/es mach<b>t</b><br>wir mach<b>en</b><br>ihr mach<b>t</b><br>sie/Sie mach<b>en</b>" },
        { title: "Besondere Verben (heißen, arbeiten)", content: "<b>heißen:</b> Bei Verben auf -s, -ß, -z entfällt das 's' bei 'du'.<br>ich heiße, du <b>heißt</b>, er heißt.<br><br><b>arbeiten:</b> Bei Verben auf -t, -d wird ein 'e' eingeschoben.<br>ich arbeite, du arbeit<b>e</b>st, er arbeit<b>e</b>t." },
        { title: "Modalverben", content: "Bei Modalverben sind 'ich' und 'er/sie/es' identisch und haben KEINE Endung!<br><br><b>können:</b><br>ich kann, du kannst, er kann, wir können, ihr könnt, sie können.<br><br><b>müssen:</b><br>ich muss, du musst, er muss, wir müssen, ihr müsst, sie müssen.<br><br><b>wollen:</b><br>ich will, du willst, er will, wir wollen, ihr wollt, sie wollen.<br><br><b>möchten:</b><br>ich möchte, du möchtest, er möchte, wir möchten, ihr möchtet, sie möchten." },
        { title: "Unregelmäßige Verben (Vokalwechsel)", content: "Einige Verben wechseln den Stammvokal bei <b>du</b> und <b>er/sie/es</b>.<br><br><b>e -> i/ie (sprechen, lesen, sehen, essen):</b><br>sprechen: ich spreche, du <b>sprichst</b>, er <b>spricht</b><br>lesen: ich lese, du <b>liest</b>, er <b>liest</b><br><br><b>a -> ä (fahren, schlafen):</b><br>fahren: ich fahre, du <b>fährst</b>, er <b>fährt</b>" },
        { title: "Wichtige unregelmäßige Verben", content: "<b>sein:</b><br>ich bin, du bist, er ist, wir sind, ihr seid, sie sind.<br><br><b>haben:</b><br>ich habe, du hast, er hat, wir haben, ihr habt, sie haben." },
        { title: "Satzbau", content: "<b>Regel 1:</b> Das konjugierte Verb steht im Hauptsatz immer an Position 2.<br>Beispiel: Ich <b>gehe</b> heute ins Kino.<br><br><b>Regel 2:</b> Wenn der Satz mit einer Zeitangabe beginnt, bleibt das Verb auf Position 2, und das Subjekt rückt auf Position 3.<br>Beispiel: Heute <b>gehe</b> ich ins Kino." },
        { title: "Akkusativ", content: "Der Akkusativ wird für das direkte Objekt verwendet. Nur maskulin (der) ändert sich!<br><b>der -> den / ein -> einen / kein -> keinen</b><br>die -> die / eine -> eine / keine -> keine<br>das -> das / ein -> ein / kein -> kein<br><br>Beispiel: Ich habe <b>einen</b> Hund (der Hund)." }
    ],
    uz: [
        { title: "Artikllar (Der, Die, Das)", content: "Nemis tilida otlar uchta jinsga ega...<br><b>der</b> (muzskoy)<br><b>die</b> (jenskiy)<br><b>das</b> (sredniy).<br><br>Qoidalar:<br><b>-ung, -heit, -keit, -schaft, -tion</b> bilan tugaydigan so'zlar deyarli har doim <b>die</b> bo'ladi.<br><b>-chen, -lein, -ment</b> bilan tugaydigan so'zlar deyarli har doim <b>das</b> bo'ladi.<br><b>-ismus, -or, -ling</b> bilan tugaydigan so'zlar deyarli har doim <b>der</b> bo'ladi." },
        { title: "Ko'plik shakli (Plural)", content: "Ko'plikni hosil qilishning 5 ta asosiy usuli bor:<br>1. <b>-e</b> (der Tag -> die Tage)<br>2. <b>-er</b> (das Kind -> die Kinder)<br>3. <b>-(e)n</b> (die Frau -> die Frauen)<br>4. <b>-s</b> (das Auto -> die Autos)<br>5. <b>O'zgarmas</b> (der Lehrer -> die Lehrer)" },
        { title: "Kishilik olmoshlari", content: "<b>ich</b> = men<br><b>du</b> = sen<br><b>er/sie/es</b> = u<br><b>wir</b> = biz<br><b>ihr</b> = sizlar<br><b>sie/Sie</b> = ular / Siz (hurmat uchun)" },
        { title: "To'g'ri fe'llar tuslanishi", content: "Misol: <b>machen</b> (qilmoq)<br>ich mach<b>e</b><br>du mach<b>st</b><br>er/sie/es mach<b>t</b><br>wir mach<b>en</b><br>ihr mach<b>t</b><br>sie/Sie mach<b>en</b>" },
        { title: "Maxsus fe'llar (heißen, arbeiten)", content: "<b>heißen (ismi bo'lmoq):</b> -s, -ß, -z bilan tugagan fe'llarda 'du' shaxsida qo'shimcha 's' tushib qoladi.<br>ich heiße, du <b>heißt</b>, er heißt.<br><br><b>arbeiten (ishlamoq):</b> -t, -d bilan tugagan fe'llarga talaffuz oson bo'lishi uchun 'e' qo'shiladi.<br>ich arbeite, du arbeit<b>e</b>st, er arbeit<b>e</b>t." },
        { title: "Modal fe'llar", content: "Modal fe'llarda 'ich' va 'er/sie/es' (I va III shaxs) bir xil bo'ladi va ularga HECH QANDAY qo'shimcha qo'shilmaydi!<br><br><b>können (qila olmoq):</b><br>ich kann, du kannst, er kann, wir können, ihr könnt, sie können.<br><br><b>müssen (shart/majbur):</b><br>ich muss, du musst, er muss, wir müssen, ihr müsst, sie müssen.<br><br><b>wollen (xohlamoq):</b><br>ich will, du willst, er will, wir wollen, ihr wollt, sie wollen.<br><br><b>möchten (xohlardim):</b><br>ich möchte, du möchtest, er möchte, wir möchten, ihr möchtet, sie möchten." },
        { title: "Noto'g'ri fe'llar (O'zak o'zgarishi)", content: "Ba'zi fe'llarda <b>du</b> va <b>er/sie/es</b> shaxslarida o'zak unlisi o'zgaradi.<br><br><b>e -> i/ie (sprechen, lesen, sehen, essen):</b><br>sprechen: ich spreche, du <b>sprichst</b>, er <b>spricht</b><br>lesen: ich lese, du <b>liest</b>, er <b>liest</b><br><br><b>a -> ä (fahren, schlafen):</b><br>fahren: ich fahre, du <b>fährst</b>, er <b>fährt</b>" },
        { title: "Muhim noto'g'ri fe'llar", content: "<b>sein (bo'lmoq):</b><br>ich bin, du bist, er ist, wir sind, ihr seid, sie sind.<br><br><b>haben (ega bo'lmoq):</b><br>ich habe, du hast, er hat, wir haben, ihr habt, sie haben." },
        { title: "Gap qurilishi (Satzbau)", content: "<b>1-Qoida:</b> Oddiy gapda tuslangan fe'l doim 2-o'rinda keladi.<br>Misol: Ich <b>gehe</b> heute ins Kino.<br><br><b>2-Qoida:</b> Agar gap vaqt bilan boshlansa, fe'l baribir 2-o'rinda qoladi, eganing o'zi 3-o'ringa o'tadi.<br>Misol: Heute <b>gehe</b> ich ins Kino." },
        { title: "Tushum kelishigi (Akkusativ)", content: "Akkusativ ob'yekt uchun ishlatiladi. Faqat muzskoy (der) jins o'zgaradi!<br><b>der -> den / ein -> einen / kein -> keinen</b><br>die -> die / eine -> eine / keine -> keine<br>das -> das / ein -> ein / kein -> kein<br><br>Misol: Ich habe <b>einen</b> Hund (der Hund)." }
    ]
};

function renderGrammar() {
    const container = document.getElementById('grammar-content');
    if (!container) return;
    
    container.innerHTML = '';
    const rules = A1_GRAMMAR[appState.settings.language] || A1_GRAMMAR['en'];
    
    rules.forEach(rule => {
        const item = document.createElement('div');
        item.className = 'grammar-item';
        
        const header = document.createElement('div');
        header.className = 'grammar-header';
        header.innerHTML = `<h3>${rule.title}</h3><i data-lucide="chevron-down"></i>`;
        
        const body = document.createElement('div');
        body.className = 'grammar-body';
        body.innerHTML = `<p>${rule.content}</p>`;
        
        header.onclick = () => {
            playSound('tap');
            const isActive = item.classList.contains('active');
            document.querySelectorAll('.grammar-item').forEach(i => i.classList.remove('active'));
            if (!isActive) item.classList.add('active');
        };
        
        item.appendChild(header);
        item.appendChild(body);
        container.appendChild(item);
    });
    
    if (window.lucide) {
        lucide.createIcons();
    }
}
