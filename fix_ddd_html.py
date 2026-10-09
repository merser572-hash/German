import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add categories container to Der Die Das view
html = html.replace(
    '''<div class="game-container">
                <div class="game-prompt" data-i18n="game_prompt">Which article is correct?</div>''',
    '''<div id="ddd-categories" class="horizontal-scroll" style="padding: 0 16px; margin-bottom: 16px;"></div>
            
            <div class="game-container">
                <div class="game-prompt" data-i18n="game_prompt">Qaysi artikl to'g'ri?</div>'''
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Categories added to DerDieDas view')
