class Vehical:
    def __init__(self, brand, color):
        self._brand  = brand             # protect value
        self._color  = color

class Car(Vehical):
    def __init__(self, brand, color, year):
        super().__init__(brand, color)
        self._year = year

    def _display_info(self):
            print(f"brand{self._brand}, color {self._color}, year{self._year}")

#Creating Object
car = Car("tesla", "blue", 2021)

car._display_info()   #brandtesla, color blue, year2021
              



