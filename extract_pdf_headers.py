import pymupdf

pdf_path = 'C:/Users/Хасанбой-Хусанбой/.gemini/antigravity/brain/99032e89-b1b4-4d7a-b502-8770623576ac/.user_uploaded/media_1791455255227.pdf'
doc = pymupdf.open(pdf_path)

with open('pdf_headers.txt', 'w', encoding='utf-8') as f:
    for page_num in range(doc.page_count):
        page = doc[page_num]
        
        # Get blocks to see font sizes
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:
                for l in b["lines"]:
                    for s in l["spans"]:
                        text = s["text"].strip()
                        size = s["size"]
                        if size > 11 and text and text != "Sanjar Quchqorov" and not text.isdigit():
                            f.write(f"Page {page_num+1}: [{size}] {text}\n")
