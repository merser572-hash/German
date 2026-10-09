import json

units = [
    "Shaxs va tanishuv", "Oila va munosabatlar", "Muloqot iboralari", "Vaqt",
    "Uy-joy", "Ovqat va ichimlik", "Xarid, pul, kiyim", "Sayohat va transport",
    "Xizmatlar", "Tana va sog'liq", "Ish va kasb", "Ta'lim va imtihon",
    "Bo'sh vaqt", "Tabiat va ob-havo", "Umumiy fe'llar", "Sifatlar", "Grammatik so'zlar"
]

with open('full_pdf_dump.txt', 'r', encoding='utf-8') as f:
    lines = [l.strip() for l in f if l.strip()]

unit_ranges = []
for i, line in enumerate(lines):
    if line in units:
        unit_ranges.append((i, f"Goethe A1 - {units.index(line) + 1}. {line}"))

with open('parsed_682.json', 'r', encoding='utf-8') as f:
    parsed_words = json.load(f)

parsed_word_to_unit = {}
last_found_idx = 0

for w in parsed_words:
    target = w['word']
    best_idx = -1
    for i in range(last_found_idx, len(lines)):
        if lines[i] == target or (len(lines[i]) > 2 and target.startswith(lines[i])):
            best_idx = i
            last_found_idx = i
            break
            
    if best_idx == -1:
        best_idx = last_found_idx
        
    assigned_unit = f"Goethe A1 - 1. {units[0]}"
    for j in range(len(unit_ranges)):
        if best_idx >= unit_ranges[j][0]:
            assigned_unit = unit_ranges[j][1]
        else:
            break
            
    parsed_word_to_unit[target] = assigned_unit

with open('words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

mapped_count = 0
for w in words:
    if w.get('category', '').startswith('Goethe'):
        w_target = w['word']
        if w_target in parsed_word_to_unit:
            w['category'] = parsed_word_to_unit[w_target]
            mapped_count += 1
        else:
            # Try to match word name directly without strict equal if it has plural suffix
            found = False
            for pw in parsed_words:
                if pw['word'].startswith(w_target):
                    w['category'] = parsed_word_to_unit[pw['word']]
                    mapped_count += 1
                    found = True
                    break
            if not found:
                w['category'] = "Goethe A1 - 17. Grammatik so'zlar"

with open('words.json', 'w', encoding='utf-8') as f:
    json.dump(words, f, ensure_ascii=False, indent=4)

print(f"Properly mapped {mapped_count} Goethe words!")
