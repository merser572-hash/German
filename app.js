// WunderDeutsch Core Logic

const appState = {
    streak: 3,
    xp: 120,
    lives: 5,
    words: [],
    currentWotd: null,
    dddWord: null,
    settings: {
        sound: true,
        vibration: true
    }
};

// Auth Credentials
const AUTH_EMAIL = 'merser572@gmail.com';
const AUTH_PASS = 'Hasanboy0412';

// UI Elements
const els = {
    streak: document.getElementById('streak'),
    xp: document.getElementById('xp'),
    lives: document.getElementById('lives'),
    dddLives: document.getElementById('ddd-lives'),
    homeWotdTitle: document.getElementById('home-wotd-title'),
    homeWotdSub: document.getElementById('home-wotd-sub'),
    homeTtsBtn: document.getElementById('home-tts-btn'),
    dddWord: document.getElementById('ddd-word'),
    dddTrans: document.getElementById('ddd-translation'),
    dddSearch: document.getElementById('dict-search-input'),
    dddTtsBtn: document.getElementById('ddd-tts-btn')
};

// Initialize App
async function initApp() {
    loadSettings();
    setupAuth();
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
    }
    document.getElementById('toggle-sound').checked = appState.settings.sound;
    document.getElementById('toggle-vibration').checked = appState.settings.vibration;
}

function toggleSetting(key) {
    appState.settings[key] = !appState.settings[key];
    localStorage.setItem('wunderdeutsch_settings', JSON.stringify(appState.settings));
    if (appState.settings.sound && key === 'sound') playPopSound();
    if (appState.settings.vibration && key === 'vibration') triggerVibrate(50);
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
        const email = document.getElementById('login-email').value;
        const pass = document.getElementById('login-password').value;
        if (email === AUTH_EMAIL && pass === AUTH_PASS) {
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

async function loadVocabulary() {
    try {
        const response = await fetch('words.json');
        appState.words = await response.json();
        setWordOfTheMoment();
    } catch (e) {
        console.error("Failed to load vocabulary:", e);
    }
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

// ---- VIEW ROUTER ----
function switchView(viewId) {
    triggerVibrate(30);
    document.querySelectorAll('.view').forEach(v => v.style.display = 'none');
    document.getElementById('view-' + viewId).style.display = 'block';
    
    document.querySelectorAll('.nav-item').forEach(btn => btn.classList.remove('active'));
    const iconMap = { 'home': 0, 'derdiedas': 1, 'satzbau': 2, 'dictionary': 3, 'grammar': 4 };
    if (iconMap[viewId] !== undefined) {
        document.querySelectorAll('.nav-item')[iconMap[viewId]].classList.add('active');
    }

    if (viewId === 'derdiedas') initDerDieDas();
    if (viewId === 'dictionary') renderDictionary();
}

// ---- DER DIE DAS GAME ----
function initDerDieDas() {
    const nouns = appState.words.filter(w => w.article && ['der', 'die', 'das'].includes(w.article.toLowerCase()));
    if(nouns.length === 0) return;
    appState.dddWord = nouns[Math.floor(Math.random() * nouns.length)];
    
    els.dddWord.textContent = appState.dddWord.word;
    els.dddTrans.textContent = appState.dddWord.translation;
}

function checkArticle(guess) {
    triggerVibrate(40);
    if(!appState.dddWord) return;
    if(guess === appState.dddWord.article.toLowerCase()) {
        appState.xp += 10;
        updateStats();
        playPopSound();
        showMascot("Richtig! Super gemacht! 🎉");
        setTimeout(initDerDieDas, 1500);
    } else {
        triggerVibrate([100, 50, 100]); // Error vibration pattern
        appState.lives = Math.max(0, appState.lives - 1);
        updateStats();
        showMascot(`Oh nein! Es heißt "${appState.dddWord.article} ${appState.dddWord.word}".`);
    }
}

// ---- DICTIONARY ----
function renderDictionary() {
    const query = els.dddSearch.value.toLowerCase();
    const list = document.getElementById('dict-list');
    list.innerHTML = '';
    
    const filtered = appState.words.filter(w => 
        w.word.toLowerCase().includes(query) || 
        w.translation.toLowerCase().includes(query)
    );
    
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
            <button class="icon-btn small-btn" onclick="speakText('${w.article ? w.article + ' ' : ''}${w.word}')">
                <i data-lucide="volume-2"></i>
            </button>
        `;
        list.appendChild(div);
    });
    lucide.createIcons();
}

// ---- MASCOT NOTIFICATIONS ----
function showMascot(text) {
    document.getElementById('mascot-msg').textContent = text;
    const mascot = document.getElementById('global-mascot');
    mascot.classList.add('show');
    setTimeout(() => { mascot.classList.remove('show'); }, 3500);
}

function triggerMascotGreeting() {
    triggerVibrate(30);
    playPopSound();
    speakText("Hallo, ich bin Fritz!");
    showMascot("Lass uns lernen! 🦊");
}

// ---- AUDIO & HAPTICS ----
function triggerVibrate(pattern) {
    if (appState.settings.vibration && 'vibrate' in navigator) {
        navigator.vibrate(pattern);
    }
}

function playPopSound() {
    if (!appState.settings.sound) return;
    try {
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain); gain.connect(ctx.destination);
        osc.type = 'sine';
        osc.frequency.setValueAtTime(800, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(1200, ctx.currentTime + 0.1);
        gain.gain.setValueAtTime(0.5, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.1);
        osc.start(); osc.stop(ctx.currentTime + 0.1);
    } catch(e) {}
}

function speakText(text) {
    if (!appState.settings.sound) return;
    if ('speechSynthesis' in window) {
        // Fix: Cancel any queued speech so it doesn't spam infinitely
        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'de-DE';
        window.speechSynthesis.speak(utterance);
    }
}

window.addEventListener('DOMContentLoaded', initApp);
