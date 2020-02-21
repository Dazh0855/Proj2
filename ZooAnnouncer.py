from abc import *

#Creates an Observer to update subscribers
class Observer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, status):
        pass

class ZooAnnouncer(Observer):
    def update(self, status):
        if (status == "Opening"):
            print ("Hello, this is the ZooAnnouncer, the zoo is opening")
        elif (status == "RollCall"):
            print ("The ZooKeeper is introducing our animals")
        elif (status == "Feeding"):
            print ("The ZooKeeper is feeding our animals")
        elif (status == "Roaming"):
            print ("The ZooKeeper is letting our animals out for the day")
        else:
            print ("The Zoo is now shutting down, please make your way to the exit")
