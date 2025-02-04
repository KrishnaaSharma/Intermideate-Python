class Car:
    wheel = 4  # class variable

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

Car.wheel= 6 # chanage Variable


car1 =Car("tesla", "2020")

print(car1.wheel)# output: 4

print(car1.wheel) # 6

    

