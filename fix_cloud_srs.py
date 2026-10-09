import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add progress to sync and save
js = js.replace('if (data.flashcardQueue) appState.flashcardQueue = data.flashcardQueue;', 'if (data.progress !== undefined) appState.progress = data.progress;\n            if (data.flashcardQueue) appState.flashcardQueue = data.flashcardQueue;')

js = js.replace('flashcardQueue: appState.flashcardQueue,', 'progress: appState.progress,\n            flashcardQueue: appState.flashcardQueue,')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

with open('srs-engine.js', 'r', encoding='utf-8') as f:
    srs = f.read()

srs_save = '''    save: function() {
        localStorage.setItem('wunder_srs_data', JSON.stringify(appState.progress.words));
        if (typeof saveUserDataToCloud === 'function') {
            saveUserDataToCloud();
        }
    },'''

srs = re.sub(r'save:\s*function\(\)\s*\{.*?\},', srs_save, srs, flags=re.DOTALL)

with open('srs-engine.js', 'w', encoding='utf-8') as f:
    f.write(srs)

print("Fixed cloud save to include SRS progress")
