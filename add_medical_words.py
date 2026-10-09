import json

with open('words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

max_id = max([int(w.get('id', 0)) for w in words] + [0])
id_counter = max_id + 1

medical_words = [
    # Anatomie
    {"word": "Magen", "article": "der", "plural": "die Mägen", "translation": "oshqozon", "category": "Medizin B2 - 1. Anatomie & Organe"},
    {"word": "Leber", "article": "die", "plural": "die Lebern", "translation": "jigar", "category": "Medizin B2 - 1. Anatomie & Organe"},
    {"word": "Niere", "article": "die", "plural": "die Nieren", "translation": "buyrak", "category": "Medizin B2 - 1. Anatomie & Organe"},
    {"word": "Herz", "article": "das", "plural": "die Herzen", "translation": "yurak", "category": "Medizin B2 - 1. Anatomie & Organe"},
    {"word": "Lunge", "article": "die", "plural": "die Lungen", "translation": "o'pka", "category": "Medizin B2 - 1. Anatomie & Organe"},
    {"word": "Blinddarm", "article": "der", "plural": "die Blinddärme", "translation": "ko'richak", "category": "Medizin B2 - 1. Anatomie & Organe"},
    {"word": "Blut", "article": "das", "plural": "die Blute", "translation": "qon", "category": "Medizin B2 - 1. Anatomie & Organe"},
    {"word": "Gehirn", "article": "das", "plural": "die Gehirne", "translation": "miya", "category": "Medizin B2 - 1. Anatomie & Organe"},
    {"word": "Knochen", "article": "der", "plural": "die Knochen", "translation": "suyak", "category": "Medizin B2 - 1. Anatomie & Organe"},
    {"word": "Muskel", "article": "der", "plural": "die Muskeln", "translation": "mushak", "category": "Medizin B2 - 1. Anatomie & Organe"},
    
    # Symptome
    {"word": "Gastritis", "article": "die", "plural": "die Gastritiden", "translation": "gastrit (oshqozon yallig'lanishi)", "category": "Medizin B2 - 2. Symptome & Diagnosen"},
    {"word": "Appendizitis", "article": "die", "plural": "die Appendizitiden", "translation": "appenditsit (ko'richak yallig'lanishi)", "category": "Medizin B2 - 2. Symptome & Diagnosen"},
    {"word": "Bluthochdruck", "article": "der", "plural": "die Bluthochdrücke", "translation": "qon bosimi oshishi (gipertoniya)", "category": "Medizin B2 - 2. Symptome & Diagnosen"},
    {"word": "Sodbrennen", "article": "das", "plural": "", "translation": "jig'ildon qaynashi", "category": "Medizin B2 - 2. Symptome & Diagnosen"},
    {"word": "Übelkeit", "article": "die", "plural": "die Übelkeiten", "translation": "ko'ngil aynishi", "category": "Medizin B2 - 2. Symptome & Diagnosen"},
    {"word": "Schwindel", "article": "der", "plural": "die Schwindel", "translation": "bosh aylanishi", "category": "Medizin B2 - 2. Symptome & Diagnosen"},
    {"word": "Schmerz", "article": "der", "plural": "die Schmerzen", "translation": "og'riq", "category": "Medizin B2 - 2. Symptome & Diagnosen"},
    {"word": "Fieber", "article": "das", "plural": "die Fieber", "translation": "isitma", "category": "Medizin B2 - 2. Symptome & Diagnosen"},
    {"word": "Husten", "article": "der", "plural": "die Husten", "translation": "yo'tal", "category": "Medizin B2 - 2. Symptome & Diagnosen"},
    {"word": "Entzündung", "article": "die", "plural": "die Entzündungen", "translation": "yallig'lanish", "category": "Medizin B2 - 2. Symptome & Diagnosen"},
    
    # Fachbegriff
    {"word": "Hypertonie", "article": "die", "plural": "die Hypertonien", "translation": "gipertoniya (baland qon bosimi)", "category": "Medizin B2 - 3. Fachbegriff vs Umgangssprache"},
    {"word": "Abdomen", "article": "das", "plural": "die Abdomina", "translation": "qorin bo'shlig'i", "category": "Medizin B2 - 3. Fachbegriff vs Umgangssprache"},
    {"word": "Emesis", "article": "die", "plural": "die Emesen", "translation": "qayt qilish (qusish)", "category": "Medizin B2 - 3. Fachbegriff vs Umgangssprache"},
    {"word": "Cephalgie", "article": "die", "plural": "die Cephalgien", "translation": "bosh og'rig'i", "category": "Medizin B2 - 3. Fachbegriff vs Umgangssprache"},
    {"word": "Insomnie", "article": "die", "plural": "die Insomnien", "translation": "uyqusizlik", "category": "Medizin B2 - 3. Fachbegriff vs Umgangssprache"},
    {"word": "Diarrhö", "article": "die", "plural": "die Diarrhöen", "translation": "diareya (ich ketishi)", "category": "Medizin B2 - 3. Fachbegriff vs Umgangssprache"}
]

for w in medical_words:
    w['id'] = str(id_counter)
    words.append(w)
    id_counter += 1

with open('words.json', 'w', encoding='utf-8') as f:
    json.dump(words, f, ensure_ascii=False, indent=4)

print(f"Added {len(medical_words)} medical words. Total: {len(words)}")
