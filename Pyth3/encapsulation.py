#private encapsulation
class A:
	def __init__(self,a,b):
		self.__a=a 
		self.__b=b
	def show(self):
		print(self.__a)
		print(self.__b)

obj1=A(10,20)
obj1.show()
