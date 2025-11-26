import math

class Circle:
    """Parameterized Constructor for circle."""
    def __init__(self, radius):
        self.radius = radius

    """Calculate the area of the circle."""
    def area(self):
         return math.pi * self.radius ** 2
    """Calculate the perimeter i.e circumference of the circle."""
    def perimeter(self):
        return 2 * math.pi * self.radius

# Create a object of Circle class
c = Circle(5)
# Display 
print("Radius:", c.radius)
print("Area:", c.area())
print("Perimeter:", c.perimeter())

# output formatted to 2 decimal places
print(f"Radius: {c.radius}")
print(f"Area: {c.area():.2f}")  
print(f"Perimeter: {c.perimeter():.2f}")

r = float(input("Enter Radius of Circle : "))
c1 = Circle(r)

# output formatted to 2 decimal places
print(f"Radius: {c1.radius}")
print(f"Area: {c1.area():.2f}")  
print(f"Perimeter: {c1.perimeter():.2f}")