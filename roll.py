import random

def roll(rangeMax): 
	return str(random.randint(1, rangeMax))

diceSize = input('Die size: ')
output = 'You rolled a ' + roll(int(diceSize)) + ' out of ' + str(diceSize)

print(output)