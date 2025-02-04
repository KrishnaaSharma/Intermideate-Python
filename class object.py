
# create Class

class Student:
    name = "roger"

# create object 

s1 = Student()
print(s1.name)# roger

s2 = Student()
print(s2.name)# roger

#-----------------------------------

#create Class

class Car:
    color = "blue"
    Brand = "mercedes"

# create object 

car1 = Car()
print(car1.color)
print(car1.Brand)


# Constructor: __init__Function --------------------------------------------------------------------


class Student:
     
    # Default Constructor
    def __init__(self):
        pass
    
     # parameterrized Constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new Student in Database")

s1 = Student("Krishna", 89)
print(s1.name, s1.marks)# krisna 89



#Class & Instance Attributes---------------------------------------------------------------------

class Student:
    collage_name = "abc collage"
    name = " anonymous" # class attr.
     
    def __init__(self, name, marks):
        self.name = name    # object attr.> class attr
        self.marks = marks
        print("Adding new Student in Database")

s1 = Student("Krishna", 89)
print(s1.name, s1.marks)# krishna 89

print(Student.collage_name)# abc collage

print(s1.name)# krishna


#Mathod -----------------------------------------------------------------------------------------------


class Student:
    collage_name = "abc collage"
  
     
    def __init__(self, name, marks):
        self.name = name    
        self.marks = marks
    
    def Welcome(self):
        print("welcome student,", self.name, self.marks)

    def get_marks(self):
        return self.marks
    

s1 = Student('karan', 56)
s1.Welcome()# welcome student, karan 56
print(s1.get_marks())# 56





