from random import choice
computer = choice(["rock","paper","scissors"])

print ("What is your move , player ?")
player = input().lower()

print (f"Computer plays {computer} ")

if player == computer:
	print ("it's a tie")
elif player == "rock" and computer == "paper":
		print ("computer wins")
elif player == "paper" and computer == "scissorrs":
		print ("computer wins")
elif player == "scissorrs"and computer == "rock":
		print ("computer wins")
else:
	print ("player wins")
