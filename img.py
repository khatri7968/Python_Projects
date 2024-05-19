# Import the required modules
import cv2
import pytesseract
from pdf2docx import Converter

# Specify the path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# Read the image file
img = cv2.imread('img.jpg')

# Convert the image to PDF using Tesseract
pdf = pytesseract.image_to_pdf_or_hocr(img, extension='pdf')

# Write the PDF to a file
with open(f'temp.pdf', 'w+b') as f:
    f.write(pdf)

c = Converter('temp.pdf')
c.convert('output.docx')
c.close()