import pymupdf
import json
import re

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

with open('parsed_682.json', 'r', encoding='utf-8') as f:
    entries = json.load(f)

with open('words.json', 'r', encoding='utf-8') as f:
    existing_words = json.load(f)

max_id = max([int(w['id']) for w in existing_words])

existing_set = set()
for w in existing_words:
    article = w.get('article', '').strip().lower()
    word = w.get('word', '').strip().lower().split('(')[0].strip()
    existing_set.add(f"{article} {word}".strip())

new_unique_words = []
id_counter = max_id + 1

for entry in entries:
    article = entry['article'].lower()
    word = entry['word']
    word_lower = word.lower().split('(')[0].strip()
    key = f"{article} {word_lower}".strip()
    
    # Deduplicate
    is_duplicate = False
    if '/' in key:
        parts = [p.strip() for p in article.split('/')]
        for p in parts:
            if f"{p} {word_lower}" in existing_set:
                is_duplicate = True
    elif key in existing_set:
        is_duplicate = True
        
    if is_duplicate:
        continue

    # Process plural
    plural_suffix = entry['plural_suffix'].strip()
    plural = ""
    clean_word = word.split('(')[0].strip()
    
    if article:
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
    
    # Add category from the book title
    new_entry = {
        "id": str(id_counter),
        "word": word,
        "article": article,
        "plural": plural,
        "plural_suffix": plural_suffix,
        "translation": entry['translation'],
        "category": "Goethe A1"
    }
    new_unique_words.append(new_entry)
    id_counter += 1

existing_words.extend(new_unique_words)

with open('words.json', 'w', encoding='utf-8') as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=4)

print(f"Added {len(new_unique_words)} entirely new words! Total is now {len(existing_words)}")
