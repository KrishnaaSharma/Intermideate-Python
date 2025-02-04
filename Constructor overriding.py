class Vehical:

    def __init__(self):
        print("This is a vehicle class Constructor")

    def car_info(self):
        print("Jaquar F-type  2020 edititon")


class Car(Vehical):

    #def __inti__(self):
        #print("This is Car class Constructor")

    def start_engin(self):
        print("f'Press Start Button to start the car")

c= Car()
c.start_engin()
#c.car_info()


#ch = Vehical()
#c.car_info()

# 1. If we define class constructor in parent class and create a Instance of child class, class constructor of 
#    PARENT class get called automatically.

# 2. If define class constructor in  both parent class and child class and create a Instance of child class,
#    class constructor of CHILD class get called automatically.

# 3. First preference will be always  child class constructor