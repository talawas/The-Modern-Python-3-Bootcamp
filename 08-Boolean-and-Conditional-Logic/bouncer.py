# ask for age
print("How old are you ? ")
age = input()
if age != "":
	age = int(age)
	#18-21 wristband
	if (age) >=18 and (age) <21:
		print ("You can go in but wear wristband") 
	#21+ drink, normal entry
	elif (age) >= 21:
		print ("You can go in w/o wristband")
	#otherwise too yound
	else:
		print ("You are not allowed in")

else:
	print ("Please enter an age!")