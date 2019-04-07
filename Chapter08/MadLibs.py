# Create a Mad Libs program that reads in text files and lets the user add
# their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
# appears in the text file

#I have used str.replace() method instead of regex

adj = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
oth_noun = input("Enter a noun: ")

inputText = open('inputText.txt')
content = inputText.read()

content = content.replace('ADJECTIVE', adj, 1)
content = content.replace('NOUN', noun, 1)
content = content.replace('VERB', verb, 1)
content = content.replace('NOUN', oth_noun, 1)

outText = open('outText.txt' , 'w')
outText.write(content)
print(content)
inputText.close()
outText.close()
