import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

firebase_scripts = '''
    <!-- Firebase SDKs -->
    <script src="https://www.gstatic.com/firebasejs/10.13.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.13.0/firebase-auth-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.13.0/firebase-firestore-compat.js"></script>
    
    <!-- Lucide Icons -->
'''

html = html.replace('<!-- Lucide Icons -->', firebase_scripts)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added Firebase CDN scripts to index.html")
