for i in range(1,5):
	for j in range(1,8):
		if i+j==5 or j-i==3 or i==4:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()


for row in range(0,5):
	for col in range(0,5):
		if row+col==2 or col-row==2 or row-col==2:
			print("*",end=" ")
		elif row==3 and col==3:
			print("*")
		else:
			print(" ",end=" ")			

	print()
