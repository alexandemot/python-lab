
from random import randrange

def is_even():
	if ((randrange(0, 9)) % 2 == 0):
		result = True
	else:
		result = False
		
	return result


def aleatorycamelcase(stringinputed):

	newstring = ''
	
	for x in range(len(stringinputed)):
		
		flipcoin = is_even()
		
		if flipcoin == True:
			newstring = newstring + stringinputed[x].upper()
		elif flipcoin == False:
			newstring = newstring + stringinputed[x]
	return newstring
	

def main():

	string = 'AnOtHEr'
	
	x = aleatorycamelcase(string)
	print('\n'+ x)

main()
	
	

	
	
	
	