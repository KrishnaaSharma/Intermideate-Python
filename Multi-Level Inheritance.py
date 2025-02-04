class Perent:
    def perent_property(self):
        print("perent property")

class Child(Perent):

    def child_property(self):
        print("Child property")

class Grandchild(Child):

    def grand_child(self):
        print("grand Child Property")

g = Grandchild()
g.grand_child()
g.child_property()
g.perent_property()


c = Child()
c.child_property()
c.perent_property()
# grand_child()

p = Perent()
p.perent_property()
#p.child_property()
#p.grand_property()