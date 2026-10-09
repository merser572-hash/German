import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<button class="icon-btn" onclick="clearAllCaches()"><i data-lucide="refresh-cw"></i></button>',
                    '<button class="icon-btn" onclick="forceCloudSync()" id="sync-btn" style="color:var(--primary-btn);"><i data-lucide="refresh-ccw"></i></button>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated refresh button to Cloud Sync")
