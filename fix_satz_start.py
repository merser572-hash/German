import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_startSatz = '''function startSatzbauRound() {
    const eb = document.getElementById('satzbau-error-box');
    if(eb) eb.style.display = 'none';
    
    const sentence = appState.satzSentences[Math.floor(Math.random() * appState.satzSentences.length)];'''

js = js.replace('''function startSatzbauRound() {
    const sentence = appState.satzSentences[Math.floor(Math.random() * appState.satzSentences.length)];''', new_startSatz)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated startSatzbauRound")
