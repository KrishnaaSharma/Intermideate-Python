from abc import ABC, abstractmethod

class Vehical(ABC):

    @abstractmethod
    def Start(self):
        pass

    @abstractmethod
    def Stop(self):
        pass

class Car(Vehical):
    
    def Start(self):
        print("Car Start ho rahi ....")

    def Stop(self):
        print("Car stop ho gayi....")


car = Car()
car.Start()
car.Stop()


#But we cannot create object of abstract class

v = Vehical()
v.Start()
v.Stop()