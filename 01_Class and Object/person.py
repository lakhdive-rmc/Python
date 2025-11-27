class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def display(self):
        print("Name:", self.name)
        print("Country:", self.country)
        print("Date of Birth:", self.dob)

# Create a Object and Display
p1 = Person("Rohit Sharma", "India", "30-04-1987")
p1.display()

# Accept Input from User
name = input("Enter your name: ")
country = input("Enter your country: ")
dob = input("Enter your date of birth (DD-MM-YYYY): ")

p2 = Person(name, country, dob)
p2.display()
