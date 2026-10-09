import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace crypto.subtle with a simple custom hash (djb2) to avoid browser API issues
new_hash_func = '''
const AUTH_EMAIL = 'merser572@gmail.com';
const AUTH_HASH = '1776510484'; // custom hash for Hasanboy0412

async function hashPassword(str) {
    let hash = 5381;
    for (let i = 0; i < str.length; i++) {
        hash = ((hash << 5) + hash) + str.charCodeAt(i); /* hash * 33 + c */
    }
    return Math.abs(hash).toString();
}
'''

js = re.sub(r"const AUTH_EMAIL = 'merser572@gmail.com';\s*const AUTH_HASH = '.*?';\s*async function hashPassword\(.*?\) \{.*?(?=\n\nfunction setupAuth)", new_hash_func, js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Replaced crypto.subtle with simple hash")
