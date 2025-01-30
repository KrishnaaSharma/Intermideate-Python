# class Vehical:
#     def __init__(self):
#         print("This is a vehicle class Constructor")

#     def car_info(self):
#         print("Jaquar F-type  2020 edititon")


# class Car(Vehical):
#     def __init__(self):
#         super().__init__()
#         print("This is Car class Constructor")

#     def serch_engin(self):
#         print("Press Start Button to start the car")

# c= Car()
# c.serch_engin()

#-------------------------------------------------------------------------------------------------

class Vehical:
    # def __init__(self):
    #     print("This is a vehicle class Constructor")

    def __init__(self, model):
        self.model= model
        print("This is a vehicle class Constructor")
        print("price is car:", self.model)


    def car_info(self):
        print("Jaquar F-type  2020 edititon")


class Car(Vehical):
    # def __init__(self):
    #     super().__init__()
    #     print("This is Car class Constructor")

    def __init__(self, model, price):
        self.price = price
        super().__init__(model)
        print("This is Car class Constructor")
        print("price is car:", self.price)
        print("model is car:", self.model)

    def serch_engin(self):
        print("Press Start Button to start the car")


c= Car("tesla", 49)

c.car_info()


