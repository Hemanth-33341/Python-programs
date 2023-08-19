class movie:
	def __init__(self,name,hero,budget,collection,result='N/A'):
		self.name=name
		self.hero=hero
		self.bud=budget
		self.c=collection
		self.res=result
		print(self.name,self.hero,self.bud,self.c,self.res)

	def mv_rslt(self):
		if self.c<self.bud:
			print("flop")
		elif self.c>self.bud and self.c<2*self.bud:
			print("hit")
		else:
			print("blockbuster hit")

class series(movie):
	def __init__(self):
		super().__init__(self.name,hero,budget,collection,result='N/A')

	def rerelease(self,amount):
		self.c=self.c+amount
		print(self.c)



ssr=movie('rrr','charan',550,1250)
ssr.mv_rslt()

rampradha=movie('radheshyam','prabash',450,125)
rampradha.mv_rslt()

a=series()
a.rerelease('rrr','charan',550,1250)