class Dad:
    def __init__(self):
        super().__init__()
        print("Dad class Constructor")

class Mom:
    def __init__(self):
        super().__init__()
        print('Mom Class Constructor')

class Child(Dad,Mom):
    def __init__(self):
        super().__init__()
        print('Child class Constructor')

ch = Child()
# Output: Mom Class Constructor
# Dad class Constructor  
# Child class Constructo

#-----------------------------------------------------------------

class Dad:
    def __init__(self):
        #super().__init__()
        print("Dad class Constructor")

class Mom:
    def __init__(self):
        super().__init__()
        print('Mom Class Constructor')

class Child(Dad,Mom):
    def __init__(self):
        super().__init__()
        print('Child class Constructor')

ch = Child()
# Output: Dad class Constructor
# Child class Constructor