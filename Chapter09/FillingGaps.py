#! python3
"""Write a program that finds all files with a given prefix, such as spam001.txt,
spam002.txt, and so on, in a single folder and locates any gaps in the num-
bering (such as if there is a spam001.txt and spam003.txt but no spam002.txt).
Have the program rename all the later files to close this gap.
As an added challenge, write another program that can insert gaps
into numbered files so that a new file can be added."""

# Note: to solve the problem, as it is described, I assume the following:
# everyfile has prefix + number and same extension
# Rename's first number is 1 if <10 matching files, 001 if < 1000...


import shutil, os, sys, re

if len(sys.argv) != 3 or not os.path.exists(sys.argv[2]):
    print("Help: prefix - path (that exists)")
    exit()

prefix = sys.argv[1]
path = sys.argv[2]

prefixRegex = re.compile(r"(^)" + prefix + "(\d*)(\..*)" )

def number_digits(n):
    return len(str(n))

matchfiles = []
extension = ""

for foldername, subfolders, filenames in os.walk(path):
    for filename in filenames:
        currentfile = prefixRegex.search(filename)

        if currentfile == None:
            continue

        extension = prefixRegex.search(filename).group(3)
        abspath = os.path.join(foldername, filename)
        matchfiles.append(abspath)


matchfiles.sort()
nfiles = len(matchfiles)
ndigits = number_digits(nfiles)
index = 0

print("Renaming files...")
for file in matchfiles:
    index += 1
    numberOfZeros = ndigits - number_digits(index)
    name = prefix
    for i in range(numberOfZeros):
        name += "0"
    name += str(index)
    name += extension
    newpath = os.path.dirname(file) + "/" + name
    os.rename(file,newpath)

print("Done.")
