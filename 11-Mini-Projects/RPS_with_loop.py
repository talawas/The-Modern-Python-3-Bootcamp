# from random import choice
from random import randint
num_round = int (input("How many rounds of Rock-Paper-Scissors do you want to play? "))
best_of_round = num_round // 2 + 1
player_wins = 0
comp_wins = 0


while player_wins < best_of_round and comp_wins < best_of_round:
	print (".....ROCK.....")
	print (".....PAPER.....")
	print (".....SCISSORS.....")
	print (f"Current Score: Player {player_wins} - Computer {comp_wins}")
	

	player = input ("What do you choose: (rock/paper/scissors/quit)  ").lower()
	if player == "quit":
		break
	
	random_num = randint(1,3)
	if random_num == 1:
		computer = "rock"
	elif random_num == 2:
		computer = "paper"
	else :
		computer = "scissors"

	# computer = choice(["rock","paper","scissors"])

	print (f"Computer plays {computer}")
	if computer != player:
		if computer == "rock" and player == "scissors":
			print ("Computer Wins !")
			comp_wins += 1
		elif computer == "scissors" and player == "paper":
			print ("Computer Wins !")
			comp_wins += 1
		elif computer == "paper" and player == "rock":
			print ("Computer Wins !")
			comp_wins += 1
		else:
			print ("Player Wins !")
			player_wins +=1

	else:
		print ("It's a TIE!")

if comp_wins > player_wins :
	print (f"COMPUTER WON THE BEST OF {num_round} SERIES")
else :
	print (f"PLAYER WON THE BEST OF {num_round} SERIES")

