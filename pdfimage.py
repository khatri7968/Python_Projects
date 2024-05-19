import pytesseract
from pdf2image import convert_from_path

# Convert PDF pages to images
pages = convert_from_path('Okta _project .pdf')
extracted_text = ''
for page in pages:
    text = pytesseract.image_to_string(page)
    extracted_text += text
with open('output.docx', 'w', encoding='utf-8') as file:
    file.write(extracted_text)
