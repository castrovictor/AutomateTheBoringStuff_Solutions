# Strong Password Detection
''' Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is at
least eight characters long, contains both uppercase and lowercase charac-
ters, and has at least one digit. You may need to test the string against mul-
tiple regex patterns to validate its strength. '''

import sys, re

password = input('Write your password: ')
weakMes = 'Ups! Your pass should contain both upper and lowercase characters, one digit and 8 characters long'

# Regex contain upper and lower case
UpperCaseRegex = re.compile(r'[A-Z]+')
LowerCaseRegex = re.compile(r'[a-z]+')
DigitRegex = re.compile(r'\d+')


if len(password) < 8:
    print(weakMes)
else:
    if (UpperCaseRegex.search(password) != None and LowerCaseRegex.search(password) != None and DigitRegex.search(password) != None):
        print('Nice! Your password is strong')
    else:
        print(weakMes)
