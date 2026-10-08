import json
import re

raw_data = """
**Lektion 1**
wie | qanday
heißen (heißt) | nomlanadi / ataladi (atalmoq)
ich | men
du | sen
er / es / sie | u (erkak) / u (narsa) / u (ayol)
sein (bist) | san (bo‘lmoq)
sein (bin) | man (bo‘lmoq)
Wer | kim
kommen (kommst) | kelasan (kelmoq)
lernen (lernt) | o‘rganadi (o‘rganmoq)
gehen (geht's) | boradi (bormoq)
Hallo | salom
Guten Tag | hayrli kun
Guten Morgen | hayrli tong
Guten Abend | hayrli kech
Gute Nacht | hayrli tun
Tschüs | xayr
Auf Wiedersehen | ko‘rishguncha
das Alphabet, -e | alifbo
Entschuldigung | kechirasiz
Wie bitte? | nima dedingiz?
Danke | rahmat
mein / dein | mening / sening
der Name, -n | nom
der Vorname, -n | ism
der Familienname, -n | familiya
der Herr, -en | janob
die Frau, -en | xonim / ayol
Super! | zo‘r!
Sehr gut | juda yaxshi
Gut | yaxshi
Es geht | bo‘ladi
Nicht so gut | unchalik yaxshi emas
Und dir? | Sendachi?
Woher | qayerdan
aus | dan / -dan
das Land, ¨-er | mamlakat
Deutschland | Germaniya
die Schweiz | Shveytsariya
Eritrea | Eritreya
die Türkei | Turkiya
Spanien | Ispaniya
Frankreich | Fransiya
Österreich | Avstriya
die USA (Pl.) | AQSh
die Musik (Sg.) | musiqa
die Information, -en | ma’lumot
das Gespräch, -e | suhbat

**Lektion 2**
Jahre alt | yoshda
das Jahr, -e | yil
alt | eski, yoshda
verheiratet | uylangan
haben | ega bo‘lmoq
du hast | sen egasan
das Kind, -er | bola
keine Kinder | bolasi yo‘q
kein | hech qanday, yo‘q
wohnen | yashamoq
in | ichida, da
das Interview, -s | suhbat, intervyu
der Partner, - | sherik (erkak)
die Partnerin, -nen | sherik (ayol)
Wie alt seid ihr? | Sizlar necha yoshdasizlar?
ich bin 28 Jahre alt | men 28 yoshdaman
ich bin auch 28 | men ham 28 yoshdaman
sein | bo‘lmoq
ich bin | menman
du bist | sensan
er / es / sie ist | u
wir sind | biz
ihr | sizlar
sie | ular
Wie alt | necha yosh
Lebt ihr zusammen? | Sizlar birga yashaysizlarmi?
ja | ha
zusammen | birga
leben | yashamoq / hayot kechirmoq
aber | lekin
wo | qayerda
sie (Pl.) | ular
der Satz, ¨-e | gap, ibora
richtig | to‘g‘ri
der Punkt, -e | nuqta
die Zahl, -en | son
das Rätsel | jumboq, topishmoq
falsch | noto‘g‘ri
minus | minus
plus | plus
geschieden sein | ajrashgan bo‘lmoq
der Single, -s | yolg‘iz, juftsiz odam
allein | yolg‘iz
machen | qilmoq
beruflich | kasbiy
der Paketzusteller, - | posilka yetkazuvchi (erkak)
die Paketzustellerin, -nen | posilka yetkazuvchi (ayol)
arbeiten | ishlamoq
als | sifatida / kabi / bo‘lib
bei | da
die Firma, Firmen | firma, kompaniya
der Job, -s | ish, kasb
der Friseur, -e | sartarosh (erkak)
die Friseurin, -nen | sartarosh (ayol)
der Kellner, - | ofitsiant (erkak)
die Kellnerin, -nen | ofitsiantka (ayol)
vielen Dank für das Interview! | suhbat uchun katta rahmat
der Beruf, -e | kasb
die Berufe | kasblar
der Ingenieur, -e | muhandis (erkak)
die Ingenieurin, -nen | muhandis (ayol)
der Kfz-Mechatroniker, - | avtomobil mexanigi (erkak)
die Kfz-Mechatronikerin, -nen | avtomobil mexanigi (ayol)
der Student, -en | talaba (erkak)
die Studentin, -nen | talaba (ayol)
der Journalist, -en | jurnalist (erkak)
die Journalistin, -nen | jurnalist (ayol)
der Architekt, -en | arxitektor (erkak)
die Architektin, -nen | arxitektor (ayol)
der Arzt, ¨-e | shifokor (erkak)
die Ärztin, -nen | shifokor (ayol)
der Lehrer, - | o‘qituvchi (erkak)
die Lehrerin, -nen | o‘qituvchi (ayol)
der Verkäufer, - | sotuvchi (erkak)
die Verkäuferin, -nen | sotuvchi (ayol)
sammeln | yig‘moq
von Beruf | kasbi bo‘yicha
die Stelle, -n | ish o‘rni
studieren | o‘qimoq (universitetda)
der Schüler, - | o‘quvchi (o‘g‘il)
die Schülerin, -nen | o‘quvchi (qiz)
der Rentner, - | nafaqaxo‘r (erkak)
die Rentnerin, -nen | nafaqaxo‘r (ayol)
die Ausbildung, -en | kasbiy ta’lim
das Praktikum, Praktika | amaliyot
der Moment, -e | lahza
jetzt | hozir
die Herkunft | kelib chiqish
der Wohnort, -e | yashash joyi
das Alter | yosh
der Familienstand | oilaviy holat
das Studium | o‘qish
die Krankenschwester, -n | hamshira
das Tier, -e | hayvon
der Tierarzt, ¨-e | veterinar (erkak)
die Tierärztin, -nen | veterinar (ayol)
der Schauspieler, - | aktyor
die Schauspielerin, -nen | aktrisa
der Sänger, - | qo‘shiqchi (erkak)
die Sängerin, -nen | qo‘shiqchi (ayol)

**Lektion 3**
die Familie, -n | oila
die Mutter, ¨- | ona
der Vater, ¨- | ota
die Schwester, -n | opa, singil
glauben | ishonmoq, o‘ylamoq
der Onkel, - | tog‘a, amaki
die Oma, -s | buvi
dein | sening
das Enkelkind, -er | nevara, nabira
der Papa, -s | dada
die Mama, -s | ona (Mama)
die Eltern (Pl.) | ota-ona, ota-onalar
der Sohn, ¨-e | o‘g‘il farzand
die Tochter, ¨- | qiz farzand
der Bruder, ¨- | aka, uka
die Geschwister (Pl.) | aka-ukalar, opa-singillar
der Großvater, ¨- | bobo
der Opa, -s | bobo (Opa)
die Großmutter, ¨- | buvi
die Oma, -s | buvi (Oma)
die Großeltern (Pl.) | bobo-buvi
der Enkel, - | nevara (o‘g‘il bola)
die Enkelin, -nen | nevara (qiz bola)
der Ehemann, ¨-er | er
die Ehefrau, -en | xotin
der Verwandte, -n | qarindosh (erkak)
die Verwandte, -n | qarindosh (ayol)
die Tante, -n | xola, amma
das Fest, -e | bayram, tadbir
die Liste, -n | ro‘yxat
nein | yo‘q
doch | ha (inkor javobiga qarshi)
Polen | Polsha
der Mann, ¨-er | erkak, o‘g‘il
die Frau, -en | ayol, xotin
das Mitglied, -er | a’zo
Spanisch | ispan tili
Englisch | ingliz tili
Russisch | rus tili
Chinesisch | xitoy tili
Polnisch | polyak tili
Französisch | fransuz tili
Italienisch | italyan tili
Türkisch | turk tili
Deutsch | nemis tili
Welche Sprachen sprichst du? | Qaysi tillarda gapirasan?
sehr gut | juda yaxshi
und | va
welche | qaysi
die Sprache, -n | til
sprechen | gapirmoq
ein bisschen | biroz, ozgina
gar nicht | umuman emas

**Lektion 4**
das Bett, -en | karavot / to‘shak
das Bild, -er | rasm / surat
der Stuhl, ¨-e | stul
die Lampe, -n | lampa / chiroq
der Sessel, -- | kreslo
das Sofa, -s | divan
der Tisch, -e | stol
der Schrank, ¨-e | shkaf
der Teppich, -e | gilam
das Regal, -e | javon
zu Hause | uyda
das Geschäft, -e | do‘kon / magazin
die Möbel, -- | mebellar
groß | katta
schön | chiroyli
teuer | qimmat
hässlich | xunuk
günstig | arzon
Ich finde, … | Menimcha, …
finden | topmoq / deb hisoblamoq
du findest | sen topasan / seningcha
er/sie/es findet | u topadi / uning fikricha
oh | voy / o‘h
Oh ja! | Ha, albatta!
Schau doch mal, da! | Qara-chi, u yoqda!
schau | qara
schauen | qaramoq
mal | bir
da | u yerda /
kennen | bilmoq / tanimoq
der Spiegel, -- | ko‘zgu
die Million, -en | million
der Preis, -e | narx
der Cent, -s | sent
das Zimmer, - | xona
das Hotel, -s | mehmonxona
der Stern, -e | yulduz
modern | zamonaviy
praktisch | qulay / amaliy
zu | juda / ortiqcha
klein | kichik
wie viel | qancha / nechta
kosten | turmoq
das Glück, -- | omad / baxt
nur | faqat
der Euro, -s | yevro
das Sonderangebot, -e | maxsus taklif / chegirma
wirklich | rostdan / haqiqatdan

**Lektion 5**
die Uhr, -en | soat
das Auto, -s | mashina
das Handy, -s | telefon / qo‘l telefoni
zeichnen | chizmoq
der Bleistift, -e | qalam
die Brille, -n | ko‘zoynak
das Buch, ¨-er | kitob
die Flasche, -n | shisha / flakon / butilka
die Kamera, -s | kamera / fotokamera
die Kette, -n | zanjir / taqinchoq
der Kugelschreiber, -- | ruchka
der Schlüssel, -- | kalit
die Tasche, -n | sumka
das Material, -ien | material
das Holz, - | yog‘och
das Papier, -e | qog‘oz
das Metall, -e | metall
das Plastik, -- | plastik
das Glas, ¨-er | oyna / shisha
die Farbe, -n | rang
weiß | oq
gelb | sariq
orange | to‘q sariq
rot | qizil
grün | yashil
blau | ko‘k
braun | jigarrang
schwarz | qora
sehen | ko‘rmoq
etwas | nimadir / biror narsa
viele | ko‘p
das Ding, -e | narsa
und so weiter | va hokazo
sagen | aytmoq
fragen | so‘ramoq
antworten | javob bermoq
weiter | davom etmoq / keyin
das Feuerzeug, -e | zajigalka
der Geldbeutel, -- | hamyon / pulxalta
das Taschentuch, ¨-er | ro‘molcha / salfetka
der Regen, -- | yomg‘ir
auf Deutsch | nemis tilida
das Wort, -e | so‘z
bitten | so‘ramoq / iltimos qilmoq
bitte | iltimos / marhamat
Noch einmal, bitte | Yana bir marta, iltimos
Wie schreibt man ...? | Qanday yoziladi ...?
schreiben | yozmoq
man | odam / kimdir
sich bedanken | minnatdorchilik bildirmoq
danke schön | katta rahmat
das Problem, -e | muammo / masala
Bitte schön | Marhamat / iltimos
Kein Problem | Muammo emas / Hech gap yo‘q
das Online-Wörterbuch, ¨-er | (onlayn) lug‘at
die Jacke, -n | kurtka / jomper
das Streichholz, ¨-er | gugurt
die Bürste, -n | cho‘tka / taroq
die Seife, -n | sovun
das Handtuch, ¨-er | sochiq
der Föhn, -e | soch quritgich / fen
Ich weiß nicht | Bilmayman
online | onlayn
bestellen | buyurtma bermoq / zakaz qilmoq
die Sonne, -n | quyosh
die Sonnenbrille, -n | quyosh ko‘zoynagi
dunkel- | to‘q
hell- | och
die Nummer, -n | raqam
der Kunststoff, -e | sintetik / plastmassa
das Produkt, -e | mahsulot
der Produktname, -n | mahsulot nomi
die Menge, -n | miqdor / son
das Formular, -e | anketa / forma
die Anrede, -n | murojaat shakli
die E-Mail, -s | elektron pochta
das Telefon, -e | telefon
das Haus, ¨-er | uy
die Adresse, -n | manzil
der Unterstrich, -e | pastki chiziq (_)
ät | @ belgisi / kuchukcha
der Name, -n | ism
die Hausnummer, -n | uy raqami
die Straße, -n | ko‘cha
der Ort, -e | joy / aholi punkti
die Postleitzahl, -en | pochta indeksi
die Telefonnummer, -n | telefon raqami
die E-Mail-Adresse, -n | elektron pochta manzili
nennen | atamoq
"""

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
    return word

words = []
current_category = "Lektion 1"
id_counter = 1

for line in raw_data.strip().split('\n'):
    line = line.strip()
    if not line: continue
    if line.startswith("**"):
        current_category = line.replace("**", "").strip()
        continue
        
    parts = line.split(" | ")
    if len(parts) != 2: continue
    
    german = parts[0].strip()
    uzbek = parts[1].strip()
    
    article = ""
    word = german
    plural_suffix = ""
    plural = ""
    
    # Check for noun with article
    match = re.match(r"^(der|die|das)\s+([^,]+)(?:,\s*(.+))?$", german)
    if match:
        article = match.group(1)
        word = match.group(2).strip()
        if match.group(3):
            plural_suffix = match.group(3).strip()
            
        if plural_suffix == "--":
            plural = f"die {word}"
        elif plural_suffix == "¨-":
            plural = f"die {apply_umlaut(word)}"
        elif plural_suffix.startswith("¨-"):
            ending = plural_suffix[2:]
            plural = f"die {apply_umlaut(word)}{ending}"
        elif plural_suffix.startswith("-"):
            ending = plural_suffix[1:]
            plural = f"die {word}{ending}"
        elif plural_suffix == "(Pl.)":
            plural = f"die {word}"
            plural_suffix = ""
        elif plural_suffix == "(Sg.)":
            plural = ""
            plural_suffix = ""
        elif plural_suffix in ["Firmen", "Praktika"]:
            plural = f"die {plural_suffix}"
        else:
            plural = plural_suffix 
            
    else:
        # Check for verbs with parenthesis "heißen (heißt)"
        v_match = re.match(r"^([^\(]+)\s*\((.+)\)$", german)
        if v_match:
            word = v_match.group(1).strip()
        
    words.append({
        "id": str(id_counter),
        "word": word,
        "article": article,
        "plural": plural,
        "plural_suffix": plural_suffix,
        "translation": uzbek,
        "category": current_category
    })
    id_counter += 1

with open('words.json', 'w', encoding='utf-8') as f:
    json.dump(words, f, ensure_ascii=False, indent=4)

print(f"Generated {len(words)} words in words.json")
