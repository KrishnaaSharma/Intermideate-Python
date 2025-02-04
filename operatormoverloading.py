class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x , self.y + other.y
    
p1 = Point(4 , 6)
p2 = Point(2 , 4)

print(p1+p2)

