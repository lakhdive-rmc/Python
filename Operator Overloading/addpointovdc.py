from dataclasses import dataclass

@dataclass
class Point:
    x: int = 10
    y: int = 15

    def show(self):
        print("x =", self.x, " ", "y =", self.y)

    def __add__(self, p2):
        return Point(self.x + p2.x, self.y + p2.y)

# Main Program
p1 = Point()
p1.show()

p2 = Point(12)
p2.show()

p3 = Point(0, 0)
p3.show()

p3 = p1 + p2
print("After Addition of two points:")
p3.show()
