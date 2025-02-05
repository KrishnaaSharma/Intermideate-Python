
print(2+3)  #5
print("hell0" + " world")  #concatenate
print([1,2,3] + [4,5,6])   # merge


class Animal():
    def feed(self):
        pass
    
class Dog(Animal):
    def feed(self):
        print("dog")

class Lion(Animal):
    def feed(self):
        print("Lion")

class Elephant(Animal):
    def feed(self):
        print("Elephant")

def Perform_feeding(self):
    self.feed()


do = Dog()
lion = Lion()
elephant = Elephant()


Perform_feeding(do)
Perform_feeding(lion)
Perform_feeding(elephant)