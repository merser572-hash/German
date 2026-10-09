import json

with open('words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

# Collect all Goethe A1 words
goethe_words = [w for w in words if w.get('category') == 'Goethe A1']
other_words = [w for w in words if w.get('category') != 'Goethe A1']

# Split goethe_words into 17 chunks
import math
chunk_size = math.ceil(len(goethe_words) / 17)

for i, w in enumerate(goethe_words):
    unit_num = (i // chunk_size) + 1
    # clamp to 17 just in case
    if unit_num > 17: unit_num = 17
    w['category'] = f'Goethe A1 - Unit {unit_num}'

words = other_words + goethe_words

# Sort words by id maybe? Or keep them as is.
words.sort(key=lambda x: int(x['id']) if x.get('id', '').isdigit() else 999999)

with open('words.json', 'w', encoding='utf-8') as f:
    json.dump(words, f, indent=4, ensure_ascii=False)

print("Split Goethe A1 into 17 units!")
