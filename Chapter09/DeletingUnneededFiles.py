#! python3
""" DeletingUnneededFiles.py - Write a program that walks through a folder tree and searches
for exceptionally large files or folders—say, ones that have a file size of more than
100MB. (Remember, to get a file’s size, you can use os.path.getsize() from
the os module.) Print these files with their absolute path to the screen."""

import shutil, os, sys

MAXSIZE = 100
# Convert bytes to megabytes
def mb (size):
    return size / (1024 * 1024)



if len(sys.argv) != 2 or not os.path.exists(sys.argv[1]):
    print("Incorrect path, existing program")
    exit()

path = sys.argv[1]

print("Files with a size bigger than " + str(MAXSIZE) + " mb:")

for foldername, subfolders, filenames, in os.walk(path):
    for filename in filenames:
        size = os.path.getsize(os.path.join(foldername, filename))
        size = mb (size)
        if size >= MAXSIZE:
            print(os.path.join(foldername, filename))
