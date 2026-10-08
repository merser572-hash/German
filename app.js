// WunderDeutsch Core Logic

const appState = {
    streak: 3,
    xp: 120,
    lives: 5,
    dailyGoal: { current: 14, total: 20 },
    words: [],
    currentWord: null
};

// UI Elements
const els = {
    streak: document.getElementById('streak'),
    xp: document.getElementById('xp'),
    lives: document.getElementById('lives'),
    mascot: document.querySelector('.mascot'),
    wotdSection: document.querySelector('.wotd-section'),
    wotdTitle: document.querySelector('.wotd-section h2'),
    wotdSubtitle: document.querySelector('.wotd-section .subtitle'),
    ttsButtons: document.querySelectorAll('.action-btn, .icon-btn')
};

// Initialize App
async function initApp() {
    updateStats();
    attachListeners();
    await loadVocabulary();
    console.log("WunderDeutsch Initialized!");
}

async function loadVocabulary() {
    try {
        const response = await fetch('words.json');
        appState.words = await response.json();
        console.log(`Loaded ${appState.words.length} words!`);
        setWordOfTheMoment();
    } catch (e) {
        console.error("Failed to load vocabulary:", e);
    }
}

function setWordOfTheMoment() {
    if(appState.words.length === 0) return;
    // Pick a random word that has an article
    const nouns = appState.words.filter(w => w.article);
    if(nouns.length === 0) return;
    
    const randomWord = nouns[Math.floor(Math.random() * nouns.length)];
    appState.currentWord = randomWord;
    
    els.wotdTitle.textContent = `${randomWord.article} ${randomWord.word}`;
    
    // Construct subtitle: translation + (plural)
    let subtitleText = randomWord.translation;
    if(randomWord.plural) subtitleText += ` (${randomWord.plural})`;
    els.wotdSubtitle.textContent = subtitleText;
}

function updateStats() {
    els.streak.textContent = appState.streak;
    els.xp.textContent = appState.xp;
    els.lives.textContent = appState.lives;
}

function attachListeners() {
    // Add simple bouncy animation to mascot on click
    els.mascot.addEventListener('click', () => {
        els.mascot.style.transform = 'scale(1.2)';
        setTimeout(() => els.mascot.style.transform = 'scale(1)', 150);
        playPopSound();
        speakText("Hallo, ich bin Fritz!");
    });

    // Handle dummy TTS
    els.ttsButtons.forEach(btn => {
        if(btn.textContent.includes('🔊')) {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                if(appState.currentWord) {
                    const textToSpeak = appState.currentWord.article ? `${appState.currentWord.article} ${appState.currentWord.word}` : appState.currentWord.word;
                    speakText(textToSpeak);
                }
            });
        }
    });
}

function playPopSound() {
    // Simple Web Audio API pop sound for feedback
    try {
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.type = 'sine';
        osc.frequency.setValueAtTime(600, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(100, ctx.currentTime + 0.1);
        gain.gain.setValueAtTime(0.5, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.1);
        osc.start();
        osc.stop(ctx.currentTime + 0.1);
    } catch(e) {
        console.log("Audio not supported");
    }
}

function speakText(text) {
    if ('speechSynthesis' in window) {
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'de-DE';
        utterance.rate = 0.9;
        window.speechSynthesis.speak(utterance);
    }
}

// Start app
window.addEventListener('DOMContentLoaded', initApp);
