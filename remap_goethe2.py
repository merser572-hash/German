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

unit_ranges = []
for i, line in enumerate(lines):
    if line in units:
        unit_ranges.append((i, f"Goethe A1 - Unit {units.index(line) + 1} ({line})"))

# For each word in parsed_682.json, find its line index in pdf_dump.txt
with open('parsed_682.json', 'r', encoding='utf-8') as f:
    parsed_words = json.load(f)

word_unit_mapping = {}

search_start_idx = 0
for w in parsed_words:
    target = w['word']
    found_idx = -1
    for i in range(search_start_idx, len(lines)):
        # Match word exactly or if target starts with line
        if lines[i] == target or (len(lines[i]) > 2 and target.startswith(lines[i])):
            found_idx = i
            search_start_idx = i + 1 # optimization, move forward
            break
            
    if found_idx != -1:
        # Determine which unit this index falls into
        assigned_unit = "Goethe A1 - Unit 1 (Shaxs va tanishuv)" # default
        for j in range(len(unit_ranges)):
            if found_idx >= unit_ranges[j][0]:
                assigned_unit = unit_ranges[j][1]
            else:
                break
        
        key = f"{w['article'].lower()} {w['word'].lower()}".strip()
        word_unit_mapping[key] = assigned_unit

with open('words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

mapped_count = 0
for w in words:
    if w.get('category', '').startswith('Goethe A1'):
        key = f"{w.get('article', '').lower()} {w.get('word', '').lower()}".strip()
        if key in word_unit_mapping:
            w['category'] = word_unit_mapping[key]
            mapped_count += 1
        elif w.get('word') in [pw['word'] for pw in parsed_words]:
             # fallback by just word name
             word_name = w.get('word')
             for pk, pu in word_unit_mapping.items():
                 if pk.endswith(word_name.lower()):
                     w['category'] = pu
                     mapped_count += 1
                     break

with open('words.json', 'w', encoding='utf-8') as f:
    json.dump(words, f, ensure_ascii=False, indent=4)

print(f"Successfully mapped {mapped_count} words to their real units!")
