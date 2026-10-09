import json

with open('sentences.json', 'r', encoding='utf-8') as f:
    sentences = json.load(f)

for s in sentences:
    if 'category' not in s and 'level' not in s:
        # A simple check to separate the medical sentences from A1
        if "oshqozon" in s['uz'] or "gastrit" in s['uz'] or "bemor" in s['uz'].lower() or "simptom" in s['uz'] or "qon" in s['uz'] or "isitma" in s['uz'] or "operatsiya" in s['uz'] or "Operatsiya" in s['uz']:
            s['level'] = 'Medizin'
        else:
            s['level'] = 'A1'

with open('sentences.json', 'w', encoding='utf-8') as f:
    json.dump(sentences, f, ensure_ascii=False, indent=4)
print("Added levels to sentences")
