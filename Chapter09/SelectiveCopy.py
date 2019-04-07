#! python3
# SelectiveCopy.py - Write a program that walks through a folder
# tree and searches for files with a certain file extension
# (such as .pdf or .jpg). Copy these files from whatever
# location they are in to a new folder.

import shutil, os, re, sys

extension = sys.argv[1]
source = sys.argv[2]
destiny = sys.argv[3]

#If arguments are not correct, we stop the program
if len(sys.argv) != 4 or not os.path.exists(source) or not os.path.exists(destiny):
    print("Wrong arguments or paths incorrect: extension source path destiny path")
    exit()

#Create a regex that match files with the extension
extensionPattern = re.compile(r"." + extension + "$")
copiedFiles = False
# Walk the entire folder in tree and copy files in to new location
for foldername, subfolders, filenames in os.walk(source):
    for filename in filenames:
        currentfile = extensionPattern.search(filename)

        if currentfile == None:
            continue


        basepath = os.path.basename(filename)
        abspath = os.path.join(foldername, filename)

        print("Copying " + basepath)
        shutil.copy(abspath, destiny)
        copiedFiles = True

if not copiedFiles:
    print("No files with " + extension + " extension found")
