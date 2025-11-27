class Point:                         # new class -> Addition of two point => operator overloading
    def __init__(self, x = 10, y = 15):
        self.x = x
        self.y = y
        
    def show(self):
        print("x=",self.x, " ", "y =", self.y)
    
    #def add(self, p1, p2):
    #    self.x = p1.x + p2.x
    #    self.y = p1.y + p2.y
    
    def __add__(self, p2):
        p3 = Point()
        p3.x = self.x + p2.x
        p3.y = self.y + p2.y
        return p3
        
p1 = Point()
p1.show()
p2 = Point(12)
p2.show()
p3 = Point(0,0)
p3.show()
#p3.add(p1,p2)
p3 = p1 + p2
print("After Addition of two point : ")
p3.show()