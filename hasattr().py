# class Person:
#     def __init__(self, name ):
#         self.name = name
     

# person = Person("Krishna")

# print(hasattr(person, 'name'))
# print(hasattr(person, 'age'))

#--------------------------------------------------------------------------------

class Car:
    def start(self):
        print("Car Start")

c = Car()

print(hasattr(c, "Start"))
print(hasattr(c, "End"))