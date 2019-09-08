# have a random num 1~100
# let people guess num
# if right ,get 'you got it'
#if wrong,tell him or her bigger or smaller

import random
r = random.randint(1,100)

while True:
	num = input ('guess a number ')
	num = int (num)
	if num == r:
		print('you got it')
		break
	if num > r:
		print('your number is  bigger')
	if num < r:
		print ('your number is smaller')