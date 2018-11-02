#Computer chooses random number from 1-10 , user guess the number, option to stop

import random
random_number = random.randint(1,10) #numbers 1-10
guess = None

print ("Computer has chosen a random number between 1 and 10")

while True :
	guess =  int(input ("Guess a number between 1 and 10: "))
	if guess < random_number:
		print ("Too low, guess again")
	elif guess > random_number:
		print ("Too high, guess again")
	else:
		print ("You guessed it! You won !")
		choice = input ("Do you want to keep playing? y/n: ") 
		if choice == "y":
			random_number = random.randint(1,10)
			guess = None
		else:
			print ("Thanh you for playing")
			break
		
