#this app generate a string with a randomizzation on a set of chars


import random

print('Benvenuto in Generatore di Password')

chars = '123456789ABCDEFGHILMNOPQRSTUVZabcdefghilmnopqrstuvz!£$%&/()=?^_.,:;' 
#you can personalize this part with a list with your personal data and favourite keywords

number = input('Quante password vuoi generare? ')
number = int(number)

length = input ('la lunghezza della tua password di quanto deve essere? ')
length = int(length)

print('\nqueste sono delle password consigliate: ')

for pwd in range(number):
	passwords = ''
	for c in range(length):
		passwords += random.choice(chars)
	print(passwords)