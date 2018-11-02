import random
random_number = random.randint(1,10)
print ("Computer has chosen a number from 1-10")
guess = None

while True:
	guess = input ("What is your guess: ")
	guess = int(guess)
	if guess < random_number:
		print ("Too low !")
	elif guess > random_number:
		print ("Too high!")
	else:
		print ("You WON!!")
		choice = input ("Do you want to play again? y/  ")
		if choice == "y":
			random_number = random.randint(1,10)
			guess = None
		else:
			print ("Thank you for playing, see you again")
			break

