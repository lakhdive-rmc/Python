class Point:                         # new class -> Array of Object
    count = 0
    def __init__(self, x = 10, y = 15):
        self.x = x
        self.y = y
        Point.count = Point.count + 1
    def show(self):
        print("(x =", self.x, ",", "y =",self.y,")")
        print(self.y)

# Create a list to hold Point objects
aobj = []

# Append Point objects to the list

aobj.append(Point())
aobj.append(Point(12))
aobj.append(Point(24,34))

# Show all points
for obj in aobj:
    print("Point : ") 
    obj.show()
