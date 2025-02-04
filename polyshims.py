class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"

# Objects
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    print(animal.speak())  # Output alag-alag classes ke hisaab se hoga
