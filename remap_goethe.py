import json

units = [
    "Shaxs va tanishuv",
    "Oila va munosabatlar",
    "Muloqot iboralari",
    "Vaqt",
    "Uy-joy",
    "Ovqat va ichimlik",
    "Xarid, pul, kiyim",
    "Sayohat va transport",
    "Xizmatlar",
    "Tana va sog'liq",
    "Ish va kasb",
    "Ta'lim va imtihon",
    "Bo'sh vaqt",
    "Tabiat va ob-havo",
    "Umumiy fe'llar",
    "Sifatlar",
    "Grammatik so'zlar"
]

with open('pdf_dump.txt', 'r', encoding='utf-8') as f:
    lines = [l.strip() for l in f if l.strip()]

with open('parsed_682.json', 'r', encoding='utf-8') as f:
    parsed_words = json.load(f)

current_unit_name = "Goethe A1 - Unit 1 (Shaxs va tanishuv)"
word_unit_mapping = {}

parsed_idx = 0

for line in lines:
    if line in units:
        current_unit_name = f"Goethe A1 - Unit {units.index(line) + 1} ({line})"
    
    if parsed_idx < len(parsed_words):
        expected_word = parsed_words[parsed_idx]['word']
        # If the line exactly matches the expected word, we map it
        # Sometimes PDF words have "(sich)" etc, so check if line starts with expected word or vice versa
        if line == expected_word or expected_word.startswith(line) or line.startswith(expected_word):
            key = f"{parsed_words[parsed_idx]['article'].lower()} {expected_word.lower()}".strip()
            word_unit_mapping[key] = current_unit_name
            parsed_idx += 1

# Now apply this mapping to words.json
with open('words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

for w in words:
    if w.get('category', '').startswith('Goethe A1'):
        # construct key
        key = f"{w.get('article', '').lower()} {w.get('word', '').lower()}".strip()
        # Fallback to Unit 1 if not mapped (e.g. if skipped by regex somehow)
        w['category'] = word_unit_mapping.get(key, w['category']) # leave as is if not found

with open('words.json', 'w', encoding='utf-8') as f:
    json.dump(words, f, ensure_ascii=False, indent=4)

print(f"Successfully mapped {len(word_unit_mapping)} words to their real units!")
