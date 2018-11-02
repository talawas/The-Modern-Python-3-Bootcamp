# for num in range (1,21):
# 	if num == 4 or num == 13:
# 		print (f"{num} is UNLUCKY !")
# 	elif num % 2 == 0:
# 		print (f"{num} is EVEN")
# 	else:
# 		print (f"{num} is ODD")


for num in range (1,21):
	if num == 4 or num == 13:
		state = "UNLUCKY"
	elif num % 2 == 0:
		state = "EVEN"
	else:
		state = "ODD"
	print (f"{num} is {state}")
