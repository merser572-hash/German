import json

with open('sentences.json', 'r', encoding='utf-8') as f:
    sentences = json.load(f)

medical_sentences = [
    {
        "uz": "Qachondan beri oshqozoningiz og'riyapti?", 
        "de": "Seit wann haben Sie diese Magenschmerzen?",
        "explanation": "Tibbiy anamnezda 'Seit wann' (Qachondan beri) so'roq so'zi kasallik tarixini bilish uchun ishlatiladi."
    },
    {
        "uz": "Bemor o'tkir gastritdan aziyat chekmoqda.", 
        "de": "Der Patient leidet an akuter Gastritis.",
        "explanation": "'leiden an' (+ Dativ) - biror kasallikdan aziyat chekmoq."
    },
    {
        "uz": "Biz gastroskopiya o'tkazishimiz kerak.", 
        "de": "Wir müssen eine Magenspiegelung durchführen.",
        "explanation": "Modal fe'l 'müssen' 2-o'rinda, asosiy fe'l 'durchführen' gap oxirida keladi."
    },
    {
        "uz": "Og'riq orqaga tarqalyaptimi?", 
        "de": "Strahlen die Schmerzen in den Rücken aus?",
        "explanation": "'ausstrahlen' (tarqalmoq) ajraladigan fe'l, shuning uchun 'aus' gap oxiriga o'tadi."
    },
    {
        "uz": "Iltimos, chuqur nafas oling va chiqaring.", 
        "de": "Bitte atmen Sie tief ein und aus.",
        "explanation": "'einatmen' (nafas olmoq) va 'ausatmen' (nafas chiqarmoq) tibbiy ko'rikda juda ko'p ishlatiladigan ajraladigan fe'llardir."
    },
    {
        "uz": "Men sizning qon bosimingizni o'lchashim kerak.", 
        "de": "Ich muss Ihren Blutdruck messen.",
        "explanation": "Modal fe'l 'muss' bilan 'messen' fe'li gapning oxiriga tushadi."
    },
    {
        "uz": "Ushbu dori kuniga uch marta olinishi kerak.", 
        "de": "Dieses Medikament muss dreimal täglich eingenommen werden.",
        "explanation": "Passiv nisbat va modal fe'l birgalikda: 'muss ... eingenommen werden'."
    },
    {
        "uz": "Sizda qanday simptomlar bor?", 
        "de": "Welche Symptome haben Sie?",
        "explanation": "Bemorga savol berish: 'Welche' (qanday/qaysi) + ot."
    },
    {
        "uz": "Operatsiya muvaffaqiyatli o'tdi.", 
        "de": "Die Operation ist erfolgreich verlaufen.",
        "explanation": "Perfekt zamoni: 'ist ... verlaufen' (o'tdi)."
    },
    {
        "uz": "Bemorning isitmasi baland va boshi aylanmoqda.", 
        "de": "Der Patient hat hohes Fieber und Schwindel.",
        "explanation": "'hohes Fieber' (baland isitma) kuchli sifat turlanishi."
    }
]

sentences.extend(medical_sentences)

with open('sentences.json', 'w', encoding='utf-8') as f:
    json.dump(sentences, f, ensure_ascii=False, indent=4)

print(f"Added {len(medical_sentences)} medical sentences. Total: {len(sentences)}")
