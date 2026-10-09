import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add isCloudSynced flag
js = js.replace('let currentUser = null;', 'let currentUser = null;\nlet isCloudSynced = false;')

# Block saveUserDataToCloud if not synced
save_logic = '''
async function saveUserDataToCloud() {
    if (!currentUser || !isCloudSynced) return;
'''
js = js.replace('async function saveUserDataToCloud() {\n    if (!currentUser) return;', save_logic)

# Set isCloudSynced = true inside onSnapshot
snapshot_logic = '''
            if (data.currentLevel) appState.currentLevel = data.currentLevel;
            
            isCloudSynced = true;
            
            // Save to local storage just in case they go offline
'''
js = js.replace('if (data.currentLevel) appState.currentLevel = data.currentLevel;\n            \n            // Save to local storage', snapshot_logic)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Added isCloudSynced flag to prevent stale overwrites")
