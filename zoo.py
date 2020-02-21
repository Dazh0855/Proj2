from strategy import dogNoiseStrategy
from strategy import wolfNoiseStrategy

dogNoise = dogNoiseStrategy()
wolfNoise = wolfNoiseStrategy()

class Animal(object):
	def __init__(self, name):
		self.name = name

	def wakeup(self):
		print (self.name + " has woken up")
	def sleep(self):
		print (self.name + " has gone to sleep")

#ChildClass
class Canine(Animal):
	#Strategy Pattern for noise
	def __init__(self, name, noiseStrategy):
		super().__init__(name)
		self.noise_strategy = noiseStrategy

	def makeNoise(self):
		self.noise_strategy.makeNoise()

	def roam(self):
		print (self.name + " is pacing")
	def eat(self):
		print (self.name + " is eating meat")

class Feline(Animal):
	def roam(self):
		print (self.name + " is exploring")
	def eat(self):
		print (self.name + " is eating feline food")

class Pachyderm(Animal):
	def roam(self):
		print (self.name + " is roaming")
	def eat(self):
		print (self.name + " is eating grass")

#GrandChildClass
#StrategyPattern for noise
class Dog(Canine):
	def __init__(self, name):
		super(Dog, self).__init__(name, dogNoise)
#Strategy Pattern for noise
class Wolf(Canine):
	def __init__(self, name):
		super(Wolf, self).__init__(name, wolfNoise)

class Cat(Feline):
	def makeNoise(self):
		print ("MEOWWWW")

class Tiger(Feline):
	def makeNoise(self):
		print ("RAWWWWR")

class Hippo(Pachyderm):
	def makeNoise(self):
		print ("BLOOP BLOOP")

class Elephant(Pachyderm):
	def makeNoise(self):
		print ("TRUUUUNK")







