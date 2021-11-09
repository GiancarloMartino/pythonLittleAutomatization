#a simple countdown: enter the seconds
#and the program starts the countdown.

import time

def countdown(t):
	while t :
		mins, secs = divmod(t,60)
		timer = '{:02d}:{:02d}'.format(mins,secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1
	print('Countdown completato!')

t = input('Inserisci i secondi da mandare in countdown: ')
countdown(int(t))