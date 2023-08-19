# n=6
# for i in range (n):
# 	for j in range(i):
# 		print(" ",end="")
# 	for j in range(n-i):
# 		print("*",end=" ")
# 	print()
# for i in range(n):
# 	for j in range(n-i):
# 		print(" ",end="")
# 	for j in range (i):
# 		print("*",end=" ")
# 	print()



a=6
for i in range(a):
	for j in range(i):
		print(" ",end=" ")
	print("*")
	for j in range(a-i):
		print(" ",end="")
	print("*")
	print()



for i in range(3):
	for j in range(i):
		print("hai")
	for j in range(i):
		print("Hello")
print()