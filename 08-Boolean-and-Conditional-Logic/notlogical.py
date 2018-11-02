#2-8 = 2$ ticket
#65 and over = 2$ ticket
#everyone else = 5$ ticket

print ("What is your age")
age = int(input ())


if not ((age >= 2 and age <= 8) or age >= 65):
	print ("Your ticket price is 5$")
else:
	print ("Your ticket price is 2$")
