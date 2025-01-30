class perent:
    def perent_property(self):
        print("perent Property")

class Child(perent):
    def child_property(self):
        print("child property")

c = Child()
c.child_property()
c.perent_propery()