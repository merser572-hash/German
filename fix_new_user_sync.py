import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace('// New user, save initial local state to cloud\n            saveUserDataToCloud();', '// New user, save initial local state to cloud\n            isCloudSynced = true;\n            saveUserDataToCloud();')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Fixed new user cloud sync block")
