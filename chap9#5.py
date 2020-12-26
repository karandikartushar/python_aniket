Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
>>> num=random.randint(1,100)
>>> while True:
	print('Guess a number between 1 and 100')
	guess=input()
	i=int(guess)
	if i ==num:
		print('you guessed right!')
		break
	elif i <num:
		print('try higher')
		break
	elif i > num:
		print('try lower')
