class Car:

    def __init__(self,brand , model, year):
        self.brand = brand                      # Instance Attribute of a class
        self.model = model
        self.year = year
    
    def start(self):                    # instance Method of a class
        print(f"{self.brand} {self.model} {self.year} ")


    def display_info(self):
        print(f"\nCar Information:\n"
              f"Make: {self.brand}\n"
              f"Model: {self.model}\n"
              f"Year: {self.year}\n")

toyota = Car(brand= "toyota", model = "corola", year= 2023)
tesla= Car(brand= "tesla", model = "corola", year= 2023)

toyota.start()


tesla.display_info()
