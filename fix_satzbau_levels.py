import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace(
'''    let cleanWords = appState.currentSentence.de.replace(/[.!?]/g, '').split(' ');''',
'''    
    // Filter sentences by level
    let levelPrefix = appState.currentLevel === 'A1' ? 'A1' : 'Medizin';
    let availableSentences = appState.satzSentences.filter(s => s.level === levelPrefix);
    if(availableSentences.length === 0) availableSentences = appState.satzSentences; // Fallback
    
    // Pick random sentence from filtered pool
    appState.currentSentence = availableSentences[Math.floor(Math.random() * availableSentences.length)];
    
    let cleanWords = appState.currentSentence.de.replace(/[.!?]/g, '').split(' ');'''
)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated Satzbau to respect levels")
