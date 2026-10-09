import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

firebase_scripts = '''
    <!-- Firebase SDKs -->
    <script src="https://www.gstatic.com/firebasejs/10.13.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.13.0/firebase-auth-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.13.0/firebase-firestore-compat.js"></script>
    
    <script src="https://unpkg.com/lucide@latest"></script>
'''

html = html.replace('<script src="https://unpkg.com/lucide@latest"></script>', firebase_scripts)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added Firebase CDNs properly")
