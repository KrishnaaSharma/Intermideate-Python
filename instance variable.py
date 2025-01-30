# class Car:
#     def __init__(self, make, model):
#         self.make = make       # Istance Variable
#         self.model = model     # Istance Variable

# # create istance (object)
# car1 =Car("toyota", "corola")

# print(car1.make)  #toyota
# print(car1.model) # corola



class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"{self.model} {self.brand}"

car2 =Car("toyota", "corola")

print(car2.display_info())



