class Calculator:
    """
    A simple calculator class that provides methods for addition,
    subtraction, multiplication, and division.
    """
    
    """Adds two numbers and returns the result."""
    def add(self, x, y):
        return x + y
    
    """Subtracts two numbers and returns the result."""
    def subtract(self, x, y):
        return x - y
    
    """Multiplies two numbers and returns the result."""
    def multiply(self, x, y):
        return x * y
    """Divide two numbers and returns the result."""
    def divide(self, x, y):
        """  Handles division by zero error. """
        if y == 0:
            return "Error: Division by zero is not allowed."
        return x / y

# Create an instance of the Calculator class
calc = Calculator()

print(calc.add(10, 5))        # 15
print(calc.subtract(10, 5))   # 5
print(calc.multiply(10, 5))   # 50
print(calc.divide(10, 5))     # 2.0

a = int(input('Enter the value of a : '))
b = int(input('Enter the value of b : '))

print(calc.add(a, b))        
print(calc.subtract(a, b))   
print(calc.multiply(a, b))   
print(calc.divide(a, b))   
