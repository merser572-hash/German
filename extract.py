import re
import json

html_content = open('prompt_html.txt', 'r', encoding='utf-8').read()

match = re.search(r'const GRAMMAR_DATA = (\[.*?\]);', html_content, re.DOTALL)
if match:
    data = match.group(1)
    with open('extracted_grammar.json', 'w', encoding='utf-8') as f:
        f.write(data)
    print("Extracted successfully.")
else:
    print("Not found.")
