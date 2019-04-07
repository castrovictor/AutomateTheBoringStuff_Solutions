# Write a program that opens all .txt files in a folder and searches for any
# line that matches a user-supplied regular expression. The results should
# be printed to the screen
import re, os
usRegex = input ("Enter your regular expression:" )
usRegex = re.compile(usRegex)

for filename in os.listdir('./aux/'):
    openFile = open('./aux/' + filename)
    content = openFile.readlines()
    for line in range(len(content)):
        if usRegex.search(content[line]):
            print(content[line])
