# # Import the PyPDF4 library
# from PyPDF4 import PdfFileMerger
#
# # Create a PdfFileMerger object
# merger = PdfFileMerger()
#
# # Loop through the PDF files
# pdf_files = ['1.pdf', '2.pdf', '3.pdf', '4.pdf', '5.pdf', '6.pdf', '7.pdf', '8.pdf', '9.pdf', '10.pdf',
#              '11.pdf', '12.pdf', '13.pdf', '14.pdf', '15.pdf', '16.pdf', '17.pdf', '18.pdf', '19.pdf',
#              '20.pdf', '21.pdf', '22.pdf', '23.pdf', '24.pdf', '25.pdf', '26.pdf', '27.pdf', '28.pdf',
#              '29.pdf', '30.pdf'] # Add your PDF file names here
# for pdf_file in pdf_files:
#     # Append the PDF file to the merger object
#     merger.append(pdf_file)
#
# # Write the merged PDF file to a new file
# merger.write('output.pdf')
#
# # Close the merger object
# merger.close()

from PyPDF2 import PdfMerger
pdfs = ['1.pdf', '2.pdf', '3.pdf', '4.pdf', '5.pdf', '6.pdf', '7.pdf', '8.pdf', '9.pdf', '10.pdf',
         '11.pdf', '12.pdf', '13.pdf', '14.pdf', '15.pdf', '16.pdf', '17.pdf', '18.pdf', '19.pdf',
         '20.pdf', '21.pdf', '22.pdf', '23.pdf', '24.pdf', '25.pdf', '26.pdf', '27.pdf', '28.pdf',
         '29.pdf', '30.pdf']
merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()