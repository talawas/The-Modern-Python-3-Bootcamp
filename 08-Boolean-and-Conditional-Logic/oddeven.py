from random import randint
num = randint(1, 1000)
print (f"Your random number is {num}")

if num % 2 != 0:
	print ("Odd")
else :
	print ("Even") 