# Import the required modules
import cv2
import pytesseract
from PyPDF4 import PdfFileMerger

# Specify the path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Create a PdfFileMerger object
merger = PdfFileMerger()

# Add your image file names here
image_files = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg',
               '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg', '17.jpg', '18.jpg', '19.jpg',
               '20.jpg', '21.jpg', '22.jpg', '23.jpg', '24.jpg', '25.jpg', '26.jpg', '27.jpg', '28.jpg',
               '29.jpg', '30.jpg']

# Loop through the image files
for image_file in image_files:
    # Read the image file
    img = cv2.imread(image_file)
    # Convert the image to PDF using Tesseract
    pdf = pytesseract.image_to_pdf_or_hocr(img, extension='pdf')
    # Append the PDF to the merger object
    merger.append(pdf)


# Write the merged PDF to a file
with open('output.pdf', 'w+b') as f:
    merger.write(f)
