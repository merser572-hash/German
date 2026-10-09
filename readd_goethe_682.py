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

# Keep only NON-Goethe words
clean_words = [w for w in words if not w.get('category', '').startswith('Goethe A1')]

max_id = max([int(w.get('id', 0)) for w in clean_words] + [0])
id_counter = max_id + 1

# Helper for plural
def apply_umlaut(word):
    if "Haus" in word: return word.replace("Haus", "Häus")
    if "Buch" in word: return word.replace("Buch", "Büch")
    if "Stuhl" in word: return word.replace("Stuhl", "Stühl")
    if "Schrank" in word: return word.replace("Schrank", "Schränk")
    if "Vater" in word: return word.replace("Vater", "Väter")
    if "Mutter" in word: return word.replace("Mutter", "Mütter")
    if "Tochter" in word: return word.replace("Tochter", "Töchter")
    if "Bruder" in word: return word.replace("Bruder", "Brüder")
    if "Sohn" in word: return word.replace("Sohn", "Söhn")
    if "Arzt" in word: return word.replace("Arzt", "Ärzt")
    if "Land" in word: return word.replace("Land", "Länd")
    if "Mann" in word: return word.replace("Mann", "Männ")
    if "Hand" in word: return word.replace("Hand", "Händ")
    if "Wort" in word: return word.replace("Wort", "Wört")
    if "Glas" in word: return word.replace("Glas", "Gläs")
    if "Tierarzt" in word: return word.replace("Tierarzt", "Tierärzt")
    if "Großvater" in word: return word.replace("Großvater", "Großväter")
    if "Großmutter" in word: return word.replace("Großmutter", "Großmütter")
    if "Ehemann" in word: return word.replace("Ehemann", "Ehemänn")
    if "Satz" in word: return word.replace("Satz", "Sätz")
    if "Tuch" in word: return word.replace("Tuch", "Tüch")
    if "Holz" in word: return word.replace("Holz", "Hölz")
    if "Gott" in word: return word.replace("Gott", "Gött")
    if "Traum" in word: return word.replace("Traum", "Träum")
    if "Saft" in word: return word.replace("Saft", "Säft")
    if "Apfel" in word: return word.replace("Apfel", "Äpfel")
    if "Gruß" in word: return word.replace("Gruß", "Grüß")
    if "Nacht" in word: return word.replace("Nacht", "Nächt")
    if "Huhn" in word: return word.replace("Huhn", "Hühn")
    if "Flug" in word: return word.replace("Flug", "Flüg")
    if "Zug" in word: return word.replace("Zug", "Züg")
    if "Sack" in word: return word.replace("Sack", "Säck")
    if "Ausgang" in word: return word.replace("Ausgang", "Ausgäng")
    if "Hof" in word: return word.replace("Hof", "Höf")
    if "Maus" in word: return word.replace("Maus", "Mäus")
    if "Platz" in word: return word.replace("Platz", "Plätz")
    if "Bad" in word: return word.replace("Bad", "Bäd")
    if "Vorschlag" in word: return word.replace("Vorschlag", "Vorschläg")
    if "Spaziergang" in word: return word.replace("Spaziergang", "Spaziergäng")
    if "Wald" in word: return word.replace("Wald", "Wäld")
    if "Vogel" in word: return word.replace("Vogel", "Vögel")
    if "Kuss" in word: return word.replace("Kuss", "Küss")
    if "Laden" in word: return word.replace("Laden", "Läden")
    if "Zahn" in word: return word.replace("Zahn", "Zähn")
    if "Chor" in word: return word.replace("Chor", "Chör")
    if "Anfang" in word: return word.replace("Anfang", "Anfäng")
    if "Schloss" in word: return word.replace("Schloss", "Schlöss")
    if "Garten" in word: return word.replace("Garten", "Gärten")
    if "Anwalt" in word: return word.replace("Anwalt", "Anwält")
    if "Aufzug" in word: return word.replace("Aufzug", "Aufzüg")
    if "Schrank" in word: return word.replace("Schrank", "Schränk")
    if "Plan" in word: return word.replace("Plan", "Plän")
    if "Rad" in word: return word.replace("Rad", "Räd")
    if "Koch" in word: return word.replace("Koch", "Köch")
    if "Schlag" in word: return word.replace("Schlag", "Schläg")
    if "Bauch" in word: return word.replace("Bauch", "Bäuch")
    if "Fall" in word: return word.replace("Fall", "Fäll")
    if "Grund" in word: return word.replace("Grund", "Gründ")
    if "Boden" in word: return word.replace("Boden", "Böden")
    if "Bart" in word: return word.replace("Bart", "Bärt")
    if "Wand" in word: return word.replace("Wand", "Wänd")
    if "Hut" in word: return word.replace("Hut", "Hüt")
    if "Anzug" in word: return word.replace("Anzug", "Anzüg")
    if "Strumpf" in word: return word.replace("Strumpf", "Strümpf")
    if "Wunsch" in word: return word.replace("Wunsch", "Wünsch")
    if "Gast" in word: return word.replace("Gast", "Gäst")
    if "Stadt" in word: return word.replace("Stadt", "Städt")
    if "Baum" in word: return word.replace("Baum", "Bäum")
    return word

for w in parsed_words:
    target = w['word']
    assigned_unit = parsed_word_to_unit.get(target, "Goethe A1 - 17. Grammatik so'zlar")
    
    # Process plural
    plural_suffix = w['plural_suffix'].strip()
    plural = ""
    clean_word = target.split('(')[0].strip()
    article = w['article'].strip()
    
    if article and article.lower() in ['der', 'die', 'das']:
        if plural_suffix == "--" or plural_suffix == "-":
            plural = f"die {clean_word}"
        elif plural_suffix == "¨-":
            plural = f"die {apply_umlaut(clean_word)}"
        elif plural_suffix.startswith("¨-") or plural_suffix.startswith('"e') or plural_suffix.startswith('"-'):
            ending = "e" if ("e" in plural_suffix or '"e' in plural_suffix) else plural_suffix[-2:]
            if ending.startswith('-'): ending = ending[1:]
            plural = f"die {apply_umlaut(clean_word)}{ending}"
        elif plural_suffix.startswith("-"):
            ending = plural_suffix[1:]
            if ending.startswith("¨"): 
                ending = ending[1:]
                plural = f"die {apply_umlaut(clean_word)}{ending}"
            else:
                plural = f"die {clean_word}{ending}"
        elif plural_suffix == "(Pl.)":
            plural = f"die {clean_word}"
            plural_suffix = ""
        elif plural_suffix == "(Sg.)":
            plural = ""
            plural_suffix = ""
        elif not plural_suffix.startswith("-") and plural_suffix != "":
            plural = f"die {plural_suffix}"
            
    new_entry = {
        "id": str(id_counter),
        "word": target,
        "article": article if article.lower() in ['der', 'die', 'das'] else "",
        "plural": plural,
        "translation": w['translation'],
        "category": assigned_unit
    }
    clean_words.append(new_entry)
    id_counter += 1

with open('words.json', 'w', encoding='utf-8') as f:
    json.dump(clean_words, f, ensure_ascii=False, indent=4)

print(f"Successfully re-added all 682 Goethe words! Total words: {len(clean_words)}")
