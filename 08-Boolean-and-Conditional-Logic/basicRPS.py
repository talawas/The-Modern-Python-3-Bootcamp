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


if p1choice== p2choice:
	print ("it's a tie")
elif p1choice == "rock":	
	if p2choice == "paper":
		print ("Player 2 wins")
	if p2choice == "scissors":
		print ("Player 1 wins")
elif p1choice == "paper":
	if p2choice == "rock":
		print ("Player 1 wins")	
	if p2choice == "scissors":
		print ("Player 2 wins")
elif p1choice == "scissors" :
	if p2choice == "rock":
		print ("Player 2 wins")
	if p2choice == "paper":
		print ("Player 1 wins")	
else:
	print ("Something went wrong")