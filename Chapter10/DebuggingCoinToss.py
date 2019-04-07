import random
import logging

# The problem with tthe original code was that it was comparing a string with an
# integer, so toss == gess was always false.
# It is easy to identify just looking at the code, but I used logging module
# to know how this module works. To disable it, uncomment line 10 of the code

logging.basicConfig(filename="test.log", level=logging.DEBUG)
# logging.disable(logging.DEBUG)

def gessToInt(guess):
	if guess == 'heads':
		return 1
	return 0



guess = ''
while guess not in ('heads', 'tails'):
	print('Guess the coin toss! Enter heads or tails:')
	guess = input()

toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug("Toss is: " + str(toss))

guess = gessToInt(guess)
logging.debug("Gess is: " + str(guess))

if toss == guess:
	print('You got it!')
else:
	print('Nope! Guess again!')
	guess = input()
	guess = gessToInt(guess)
	logging.debug("New gess is: " + str(guess))
	if toss == guess:
		print('You got it!')
	else:
		print('Nope. You are really bad at this game.')
