import abc

#StrategyPattern for Canine noise
class MakeNoiseStrategyAbstract(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def makeNoise(self):
		"""REQUIRED METHOD"""

class dogNoiseStrategy(MakeNoiseStrategyAbstract):
	def makeNoise(self):
		print ("WOOF WOOF")

class wolfNoiseStrategy(MakeNoiseStrategyAbstract):
	def makeNoise(self):
		print ("AWOOOOOOO")