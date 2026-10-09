import json

with open('words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

goethe_words = [w for w in words if w.get('category', '').startswith('Goethe A1')]

with open('parsed_682.json', 'r', encoding='utf-8') as f:
    parsed_words = json.load(f)

print(f"Goethe words in words.json: {len(goethe_words)}")
print(f"Parsed words in parsed_682.json: {len(parsed_words)}")

# Compare first 5
for i in range(5):
    print(f"[{i}] words.json: {goethe_words[i]['word']}")
    print(f"[{i}] parsed_682: {parsed_words[i]['word']}")
