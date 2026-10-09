with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix old ID reference
js = js.replace('dict-search-input', 'dict-search')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('Done')
