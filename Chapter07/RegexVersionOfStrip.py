# Regex Version of strip()
''' Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to
strip, then whitespace characters will be removed from the beginning and
end of the string. Otherwise, the characters specified in the second argu-
ment to the function will be removed from the string. '''

import re

def RegexString(string, rm_str = None):
    if rm_str == None:
        splitRegex = re.compile('(^\s+)|(\s+$)')
        string = splitRegex.sub('',string)
    else:
        splitRegexRemove = re.compile(rm_str)
        string = splitRegexRemove.sub('',string)
    return string

text = input("Write your text: ")
string = input("String to remove: ")

text_no_whitespace = RegexString(text)
text_no_str = RegexString(text,string)

print('Text without whitespace characters: ')
print(text_no_whitespace)
print('Text without your string: ')
print(text_no_str)
