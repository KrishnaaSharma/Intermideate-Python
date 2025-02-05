class Car:
    def __init__(self, make, brand):
        self.__make = make                     #  Private Method 
        self.__brand = brand

    def start(self):
        print(f"Make {self.__make}, brand {self.__brand}")

    def __info(self):                                 # Private method
        print(f"brand {self.__brand}, make{self.__make}")

    def display(self):
        return self.__info()
    
c = Car(make="toyota", brand="tesla")

c.start() # Make toyota, brand tesla

c.__info()  # error

# Accessing Private Method and Private Variable using Public Method
c.display()  # brand tesla, maketoyota

# -----------------------------
print(dir(c))

c._Car__info()


        
        