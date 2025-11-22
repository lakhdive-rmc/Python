class Point:                         # new class
    """Initializes a new Point object with given x and y coordinates.
        parameterised constructor
    """
    def __init__(self):
        self.x = 10
        self.y = 20
    """Setter and Getter method    """
    def setX(self, a):    
        self.x = a
    def setY(self, b):   
        self.y = b
    def show(self):
        print("X and Y coordinate of Point")
        print(self.x)
        print(self.y)
Obj = Point()
Obj.show()
Obj.setX(100)
Obj.setY(200)
Obj.show()
