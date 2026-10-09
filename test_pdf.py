import pymupdf

doc = pymupdf.open(r'C:\Users\Хасанбой-Хусанбой\.gemini\antigravity\brain\99032e89-b1b4-4d7a-b502-8770623576ac\.user_uploaded\media_1791455255227.pdf')

with open('font_dump.txt', 'w', encoding='utf-8') as f:
    page = doc[3]
    blocks = page.get_text('dict')['blocks']
    for b in blocks[:50]:
        if 'lines' in b:
            for l in b['lines']:
                for s in l['spans']:
                    f.write(f"Text: {s['text'][:30]:<30} Font: {s['font']:<20} Color: {hex(s['color'])}\n")
