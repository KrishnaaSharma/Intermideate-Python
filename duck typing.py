class Cat:
    def sound(self):
        return "Meao"
    
class Dog:
    def sound(self):
        return "Bark Bark"

def make_sound(animal):
    print(animal.sound())

cat = Cat()
dog = Dog()

make_sound(cat)      # "Meao"
make_sound(dog)  # "Bark Bark"
