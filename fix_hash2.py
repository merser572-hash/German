import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_hash_func = '''
const AUTH_EMAIL = 'merser572@gmail.com';
const AUTH_HASH = 'SGFzYW5ib3kwNDEy'; // Base64 encoding

async function hashPassword(str) {
    return btoa(str);
}
'''

js = re.sub(r"const AUTH_EMAIL = 'merser572@gmail.com';\s*const AUTH_HASH = '.*?';\s*async function hashPassword\(.*?\) \{.*?(?=\n\nfunction setupAuth)", new_hash_func, js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Replaced hash with base64")
