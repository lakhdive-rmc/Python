class Point:     # new class 
                # No default constructor : use parameter with default value
    """Initializes a new Point object with given x and y coordinates.
        parameterised constructor 
    """
    #def __init__(self):
    #    self.x = 10
    #    self.y = 20
    def __init__(self, x = 10, y = 20):
        self.x = 10
        self.y = 20
    """Setter and Getter method    """
    def setX(self, a):    
        self.x = a
    def setY(self, b):   
        self.y = b
    def getX(self):
        return self.x
    def getY(self):
        return self.y
       
    def show(self):
        print("X and Y coordinate of Point")
        print(self.x)
        print(self.y)
Obj = Point()
Obj.show()
Obj.setX(100)
Obj.setY(200)
#Obj.show()
print(Obj.getX())
print(Obj.getY())
Obj.x = 15
print("new value of x = ", Obj.getX())
