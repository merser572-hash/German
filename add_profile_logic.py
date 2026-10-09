import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

profile_logic = '''
            // Check if admin
            appState.isAdmin = (user.email === 'merser572@gmail.com');
            
            // Update Settings Profile
            let displayName = user.displayName || "Student";
            const settingsName = document.getElementById('settings-name');
            const settingsEmail = document.getElementById('settings-email');
            const settingsAvatar = document.getElementById('settings-avatar');
            
            if (settingsName) settingsName.innerText = displayName;
            if (settingsEmail) settingsEmail.innerText = user.email || "";
            if (settingsAvatar) settingsAvatar.innerText = displayName.charAt(0).toUpperCase();
            
            // Sync data with Firestore
'''

js = js.replace('// Check if admin\n            appState.isAdmin = (user.email === \'merser572@gmail.com\');\n            \n            // Sync data with Firestore', profile_logic)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Added profile logic to app.js")
