print ("...rock...")
print ("...paper...")
print ("...scissors...")

print ("Player one choose: ")
p1choice = input()

print ("* * * * * NO CHEATING * * * * *")
print ("* * * * * NO CHEATING * * * * *")
print ("* * * * * NO CHEATING * * * * *")
print ("* * * * * NO CHEATING * * * * *")
print ("* * * * * NO CHEATING * * * * *")
print ("* * * * * NO CHEATING * * * * *")
print ("* * * * * NO CHEATING * * * * *")
print ("* * * * * NO CHEATING * * * * *")
print ("* * * * * NO CHEATING * * * * *")
print ("* * * * * NO CHEATING * * * * *")
print ("* * * * * NO CHEATING * * * * *")
print ("* * * * * NO CHEATING * * * * *")
print ("* * * * * NO CHEATING * * * * *")
print ("* * * * * NO CHEATING * * * * *")


print ("Player two choose: ")
p2choice = input()


if p1choice == "rock" and p2choice == "paper":
	print ("player 2 wins")
elif p1choice == "rock" and p2choice == "scissors":
	print ("player 1 wins")
elif p1choice == "paper" and p2choice == "rock":
	print ("player 1 wins")
elif p1choice == "paper" and p2choice == "scissors":
	print ("player 2 wins")
elif p1choice == "scissors" and p2choice == "rock":
	print ("player 2 wins")
elif p1choice == "scissors" and p2choice == "paper":
	print ("player 1 wins")
elif p1choice == p2choice:
	print ("it's a draw")
else:
	print ("Something went wrong")
