import pymupdf
import json

pdf_path = 'C:/Users/Хасанбой-Хусанбой/.gemini/antigravity/brain/99032e89-b1b4-4d7a-b502-8770623576ac/.user_uploaded/media_1791455255227.pdf'
doc = pymupdf.open(pdf_path)

full_text = []
for i in range(doc.page_count):
    text = doc[i].get_text('text')
    # Just split and extend
    full_text.extend([t.strip() for t in text.split('\n') if t.strip()])

with open('full_pdf_dump.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(full_text))

print("Dumped full PDF text!")
