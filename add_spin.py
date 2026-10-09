import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css += '''
.lucide-spin {
    animation: spin 1s linear infinite;
}
@keyframes spin {
    100% { transform: rotate(360deg); }
}
'''
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Added lucide-spin")
