const GRAMMAR_EXPLANATIONS = {
    uz: {
        suffix_die: "💡 Qoida: -<b>{suffix}</b> bilan tugaydigan so'zlar deyarli har doim <b>die</b> bo'ladi.",
        suffix_das: "💡 Qoida: -<b>{suffix}</b> bilan tugaydigan so'zlar deyarli har doim <b>das</b> bo'ladi.",
        suffix_der: "💡 Qoida: -<b>{suffix}</b> bilan tugaydigan so'zlar deyarli har doim <b>der</b> bo'ladi.",
        ends_in_e: "💡 Maslahat: <b>-e</b> bilan tugaydigan ko'pchilik so'zlar <b>die</b> bo'ladi (ayrim istisnolardan tashqari).",
        compound: "💡 Qoida: Qo'shma so'zlar doim oxirgi so'zning artiklini oladi! Bu yerda asosiy so'z: <b>{article} {baseWord}</b>.",
        default: "💡 Maslahat: Bu asosiy so'z. Uning artiklini xuddi shunday yodlab olishingiz kerak!"
    },
    en: {
        suffix_die: "💡 Rule: Words ending in -<b>{suffix}</b> are almost always <b>die</b>.",
        suffix_das: "💡 Rule: Words ending in -<b>{suffix}</b> are almost always <b>das</b>.",
        suffix_der: "💡 Rule: Words ending in -<b>{suffix}</b> are almost always <b>der</b>.",
        ends_in_e: "💡 Hint: Most words ending in <b>-e</b> are <b>die</b> (with some exceptions).",
        compound: "💡 Rule: Compound nouns take the article of the last word! The root here is: <b>{article} {baseWord}</b>.",
        default: "💡 Hint: This is a root word. You just have to memorize its article!"
    },
    de: {
        suffix_die: "💡 Regel: Wörter auf -<b>{suffix}</b> sind fast immer <b>die</b>.",
        suffix_das: "💡 Regel: Wörter auf -<b>{suffix}</b> sind fast immer <b>das</b>.",
        suffix_der: "💡 Regel: Wörter auf -<b>{suffix}</b> sind fast immer <b>der</b>.",
        ends_in_e: "💡 Tipp: Sehr viele Wörter, die auf <b>-e</b> enden, sind <b>die</b>.",
        compound: "💡 Regel: Komposita bekommen den Artikel des letzten Wortes! Das Grundwort ist: <b>{article} {baseWord}</b>.",
        default: "💡 Tipp: Diesen Artikel musst du dir einfach merken!"
    }
};

function getGrammarExplanation(wordObj, lang = 'uz') {
    const word = wordObj.word;
    const article = (wordObj.article || '').toLowerCase();
    const lowerWord = word.toLowerCase();
    
    // 1. Suffix Rules
    const dieSuffixes = ['ung', 'heit', 'keit', 'schaft', 'tion', 'tät', 'ik', 'ur', 'ie', 'enz'];
    const dasSuffixes = ['chen', 'lein', 'ment', 'um', 'ma'];
    const derSuffixes = ['ismus', 'ist', 'or', 'ling', 'ig', 'ich'];

    if (article === 'die') {
        for (let suf of dieSuffixes) {
            if (lowerWord.endsWith(suf)) return GRAMMAR_EXPLANATIONS[lang].suffix_die.replace('{suffix}', suf);
        }
        if (lowerWord.endsWith('e') && word.length > 3) {
            return GRAMMAR_EXPLANATIONS[lang].ends_in_e;
        }
    }
    
    if (article === 'das') {
        for (let suf of dasSuffixes) {
            if (lowerWord.endsWith(suf)) return GRAMMAR_EXPLANATIONS[lang].suffix_das.replace('{suffix}', suf);
        }
    }
    
    if (article === 'der') {
        for (let suf of derSuffixes) {
            if (lowerWord.endsWith(suf)) return GRAMMAR_EXPLANATIONS[lang].suffix_der.replace('{suffix}', suf);
        }
    }

    // 2. Compound Noun Rule (Search existing words dictionary)
    // Find if the word ends with another known noun.
    if (window.appState && window.appState.words) {
        // Nouns only
        const nouns = window.appState.words.filter(w => w.article && ['der','die','das'].includes(w.article.toLowerCase()));
        
        // Sort by length descending to match the longest possible root word first 
        // e.g. "Krankenhaus" should match "Haus" (or "Krankenhaus" itself shouldn't match, length check handles that)
        nouns.sort((a,b) => b.word.length - a.word.length);
        
        for (let root of nouns) {
            // Ignore if it's the exact same word
            if (root.word.toLowerCase() === lowerWord) continue;
            
            // If the word ends with the root word and root word is at least 3 chars
            if (lowerWord.endsWith(root.word.toLowerCase()) && root.word.length >= 3) {
                // Make sure the article matches! Compound nouns take the article of the LAST word.
                if (root.article.toLowerCase() === article) {
                    return GRAMMAR_EXPLANATIONS[lang].compound
                        .replace('{article}', root.article)
                        .replace('{baseWord}', root.word);
                }
            }
        }
    }

    // 3. Fallback
    return GRAMMAR_EXPLANATIONS[lang].default;
}
