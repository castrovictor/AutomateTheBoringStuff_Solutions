"""Using the os.walk() function from Chapter 9, write a script that will go
through every PDF in a folder (and its subfolders) and encrypt the PDFs
using a password provided on the command line. Save each encrypted
PDF with an _encrypted.pdf suffix added to the original filename. Before
deleting the original file, have the program attempt to read and decrypt
the file to ensure that it was encrypted correctly.
Then, write a program that finds all encrypted PDFs in a folder (and its
subfolders) and creates a decrypted copy of the PDF using a provided pass-
word. If the password is incorrect, the program should print a message to
the user and continue to the next PDF."""

import PyPDF2, os, sys

password = sys.argv[1]

for foldername, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith(".pdf"):
            path = os.path.join(foldername, filename)
            pdfFile = open(path, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            if pdfReader.isEncrypted is False:
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))

                # Encrypt pdf and save with _encrypted.pdf suffix
                pdfWriter.encrypt(password)
                encryptedPath = path[:-4] + "_encrypted.pdf"
                resultPdf = open(encryptedPath, 'wb')
                pdfWriter.write(resultPdf)
                resultPdf.close()

                #Check it was encrypted properly and remove original pdf
                pdfFile = open(encryptedPath, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                if (pdfReader.isEncrypted is True
                    and pdfReader.decrypt(password) == 1):
                        os.remove(path)
                else:
                    os.remove(encryptedPath)
                    print(path + " encryption failed")
