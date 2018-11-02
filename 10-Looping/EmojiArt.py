# n = 0
# while n < 10:
# 	n += 1
# 	for x in range (0,n):
# 		print("\U0001f600",end="")
# 


# for n in range (1,11):
# 	print ("\U0001f600" * n)

# t = 1
# while t <11:
# 	print ("\U0001f600" * t)
# 	t += 1
	

#MAKE EMOJI PYRAMID WITH N ROWS !
n = int(input("Choose number of rows: "))
l = 1
while l <= n :
	space = n - l 
	print ("\U0001f4a9" * space,end="")
	number = (l*2) - 1
	print ("\U0001f600" * number,end="")
	print ("\U0001f4a9" * space)
	l += 1