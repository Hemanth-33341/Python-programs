for i in range(5000,10000):
	for j in range(2,i):
		if (i%j==0):
			break
	else:
		print(i)





string="hey my name is hemanth i am studying btech"
lis1=string.split()
lis2=[]
for i in lis1:
	lis2.append(i.capitalize())
answer=" ".join(lis2)
print(answer)





string="hello world hai"
a,b,c=map(str,string.split())
print(a[0].upper(),a[1:],b[0].upper(),b[1:],c[0].upper(),c[1:])

