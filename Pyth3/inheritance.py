class a:
	def __init__(self):
		print("this is from class A")

class b:
	def __init__(self):
		print("this is from class B")

class c(a,b):
	def __init__(self):
		super().__init__()
		print("this is from class C")

#aa=a()
#bb=b()
cc=c()
