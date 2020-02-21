from zoo import *
from abc import *
from strategy import *
from ZooKeeper import *
from ZooAnnouncer import *

#instantiate animals
Wolf = Wolf("Winston the Wolf")
Dog = Dog("Dennis the Dog")
Cat = Cat("Cathy the Cat")
Tiger = Tiger("Tony the Tiger")
Hippo = Hippo("Henry the Hippo")
Elephant = Elephant("Earl the Elephant")
animalList = [Wolf, Dog, Cat, Tiger, Hippo, Elephant]
emptyList = []
#Instantiate Zookeepr
ZooKeeper = ZooKeeper("Zack the ZooKeeper", animalList, emptyList)
ZooAnnouncer = ZooAnnouncer()
#Register Observer
ZooKeeper.register(ZooAnnouncer)


#Observer reacts to events and announces them
print ("Day in Zoo Begins")
print (ZooKeeper.getName() + " is opening up the zoo ------- ")

ZooKeeper.updateZoo("Opening")
ZooKeeper.wakeAnimalsUp()

print (ZooKeeper.getName() + " is checking if all animals are accounted for --------")
ZooKeeper.updateZoo("RollCall")
ZooKeeper.rollCall()

print (ZooKeeper.getName() + " is feeding all the animals --------")
ZooKeeper.updateZoo("Feeding")
ZooKeeper.feed()

print (ZooKeeper.getName() + " is taking the animals out of their cage -------")
ZooKeeper.updateZoo("Roaming")
ZooKeeper.exercise()

print (ZooKeeper.getName() + " is closing the zoo -------")
ZooKeeper.updateZoo("Closing")
ZooKeeper.unregister(ZooAnnouncer)
ZooKeeper.shutZooDown()