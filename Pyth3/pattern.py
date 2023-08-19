for i in range(5):
	for j in range(5):
		if j==0 or i==4 or i==j:
			print("*",end="")
		else:
			print(end=" ")
	print()



for row in range(5):
	for column in range(5):
		if row==0 or column==4 or row==column:
			print("*",end="")
		else:
			print(end=" ")
	print()


for row in range(5):
	for column in range(9):
		if row==column or row+column==8:
			print("*")
		else:
			print(end=" ")
	print()
