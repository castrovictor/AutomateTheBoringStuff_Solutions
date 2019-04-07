"Decrypt a pdf using brute-force"

import PyPDF2, sys

filename = sys.argv[1]
openFile = open(sys.argv[2])
passwords = openFile.readlines()

pdfFile = open(filename, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)

found = False

if pdfReader.isEncrypted is True:
    for line in range(len(passwords)):
        if (pdfReader.decrypt(passwords[line].lower()) == 1):
            print("The passwords is: " + passwords[line].lower())
            found = True
            break;
        elif (pdfReader.decrypt(passwords[line].upper()) == 1):
            print("The passwords is: " + passwords[line].upper())
            found = True
            break;

if found is False:
    print("Password not found")
