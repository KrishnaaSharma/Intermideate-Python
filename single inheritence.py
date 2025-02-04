class perent:
    def perent_property(self):
        print("perent Property")    # # Parent class or Base Class or Super Class

class Child(perent):
    def child_property(self):
        print("child property")         # Child class or Derived class or Sub Class



c = Child()
c.child_property()
c.perent_property()

print()


p = perent()
p.perent_property()
# p.child_property() # Parent class cannot access child class method