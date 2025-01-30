# class Perent():

#     def perent_proprty(self):
#         print("perent proprty")

# class Brother():

#     def brother_property(self):
#         print("brother property")

# class Sister():

#     def sister_property(self):
#         print("Siter Property")

# b= Brother()
# b.brother_property()
# b.perent_proprty()
# b.sister_roperty()

# p= Perent()
# .brother_property()
# .perent_proprty()
# .sister_roperty()

# s= Sister()
# s.brother_property()
# s.perent_proprty()
# s.sister_roperty()

class Parent:                                # Parent class or Base Class or Super Class
    
    def parent_property(self):
        print('parent''s property')

class Brother(Parent):                          # Child class or Derived class or Sub Class
    
    def brother_property(self):
        print('Child''s property')

class Sister(Parent):                          # Child class or Derived class or Sub Class
    
    def sister_property(self):
        print('GrandChild''s property')

# Creating an instance of the Brother class (Child Class)
b = Brother()     
b.brother_property()
# b.sister_property()     # Brother cannot access sister property and vise versa
b.parent_property()

# Creating an instance of the Sister class (Child Class)
s=Sister()
s.sister_property()
# s.brother_property()  
s.parent_property()


# Creating an instance of the parent class (Parent Class)
p=Parent()
p.parent_property()
# p.brother_property()    # Parent class cannot access child property

print()
