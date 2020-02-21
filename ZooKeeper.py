from zoo import *

#This is the zookeeper class as well as the observable
class ZooKeeper(object):
	def __init__(self, name, animalList, emptyList):
		self.name = name
		self.animalList = animalList
		self.observers = emptyList

	def register(self, observer):
		if not observer in self.observers:
			self.observers.append(observer)

	def unregister(self, observer):
		if observer in self.observers:
			self.observers.remove(observer)

	def updateZoo(self, status):
		for observer in self.observers:
			observer.update(status)

	def getName(self):
		return self.name

	def wakeAnimalsUp(self):
		for animal in self.animalList:
			animal.wakeup()
		
	def shutZooDown(self):
		for animal in self.animalList:
			animal.sleep()
	def rollCall(self):
		for animal in self.animalList:
			animal.makeNoise()
	def exercise(self):
		for animal in self.animalList:
			animal.roam()
	def feed(self):
		for animal in self.animalList:
			animal.eat()
