import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add lastHeartRegen to syncUserData
js = js.replace('if (data.lastHeartUpdate) appState.lastHeartUpdate = data.lastHeartUpdate;', 
                'if (data.lastHeartUpdate) appState.lastHeartUpdate = data.lastHeartUpdate;\n            if (data.lastHeartRegen) appState.lastHeartRegen = data.lastHeartRegen;')

# Add lastHeartRegen to saveUserDataToCloud
js = js.replace('lastHeartUpdate: appState.lastHeartUpdate,', 
                'lastHeartUpdate: appState.lastHeartUpdate,\n            lastHeartRegen: appState.lastHeartRegen,')


with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Added lastHeartRegen to Firebase sync")
