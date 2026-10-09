/**
 * SuperMemo-2 (SM-2) Implementation for WunderDeutsch
 */

const SRS = {
    // Save to localStorage
    save: function() {
        localStorage.setItem('wunder_srs_data', JSON.stringify(appState.progress.words));
    },
    
    // Initialize or get a card
    getCard: function(wordId) {
        if (!appState.progress.words) appState.progress.words = {};
        if (!appState.progress.words[wordId]) {
            appState.progress.words[wordId] = {
                state: "new",       // 'new', 'learning', 'review', 'relearning'
                stepIndex: 0,       // index in learning steps
                interval: 0,        // days
                easeFactor: 2.50,
                reps: 0,
                lapses: 0,
                dueDate: Date.now()
            };
        }
        return appState.progress.words[wordId];
    },

    // Process a review
    // quality: 1 (Again), 2 (Hard), 3 (Good), 4 (Easy)
    reviewCard: function(wordId, quality) {
        let card = this.getCard(wordId);
        
        // SM-2 logic
        if (quality === 1) {
            // Again / Fail
            card.lapses += 1;
            card.easeFactor = Math.max(1.30, card.easeFactor - 0.20);
            card.interval = 0;
            card.state = "relearning";
            card.dueDate = Date.now() + 1 * 60 * 1000; // 1 minute
        } else if (quality === 2) {
            // Hard
            card.easeFactor = Math.max(1.30, card.easeFactor - 0.15);
            card.interval = Math.max(1, card.interval * 1.2);
            card.state = "review";
            card.dueDate = Date.now() + card.interval * 24 * 60 * 60 * 1000;
        } else if (quality === 3) {
            // Good
            if (card.state === "new" || card.state === "learning" || card.state === "relearning") {
                card.interval = 1;
            } else {
                card.interval = Math.max(1, (card.interval * card.easeFactor));
            }
            card.state = "review";
            card.dueDate = Date.now() + card.interval * 24 * 60 * 60 * 1000;
        } else if (quality === 4) {
            // Easy
            card.easeFactor += 0.15;
            if (card.state === "new" || card.state === "learning" || card.state === "relearning") {
                card.interval = 4;
            } else {
                card.interval = Math.max(1, (card.interval * card.easeFactor * 1.3));
            }
            card.state = "review";
            card.dueDate = Date.now() + card.interval * 24 * 60 * 60 * 1000;
        }
        
        if (quality > 1) {
            card.reps += 1;
        } else {
            card.reps = 0;
        }
        
        this.save();
        return card;
    },
    
    // Build the daily queue from a specific category or 'all'
    buildQueue: function(wordsArray, dailyNewLimit = 15) {
        let queue = [];
        let newCount = 0;
        const now = Date.now();
        
        // Shuffle words array to add randomness to the queue order
        let shuffled = [...wordsArray];
        for (let i = shuffled.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
        }
        
        for (let w of shuffled) {
            let card = this.getCard(w.id);
            if (card.state === "new") {
                if (newCount < dailyNewLimit) {
                    queue.push(w);
                    newCount++;
                }
            } else if (card.dueDate <= now) {
                // Due for review or learning
                queue.push(w);
            }
        }
        
        // Sort queue: put learning/relearning cards first, then review, then new
        queue.sort((a, b) => {
            let cA = this.getCard(a.id);
            let cB = this.getCard(b.id);
            return cA.dueDate - cB.dueDate;
        });
        
        return queue;
    }
};

window.SRS = SRS;
