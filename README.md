

OOP's(object oriented programming) (07/06/2024).

#Classes :is Like a blueprint that stores object .
#Objects:are variables that contain data and functions that can be used to manipulate the data.

#example:
#1)
class Chair:
    def __init__(self, color="grey", price=1700, type="wooden"):
        self.color = color
        self.price = price
        self.type = type
    def setdata(self, color, price, type):
        self.color = color
        self.price = price
        self.type = type
    def showdata(self):
        print(self.color, self.price, self.type)


chair1 = Chair()
chair2 = Chair()
chair3 = Chair()
chair1.setdata("Red", 1200, "Plastic")
chair2.setdata("Blue", 1000, "Aluminium")
chair1.showdata()  # Output: Red 1200 Plastic
chair2.showdata()  # Output: Blue 1000 Aluminium
chair3.showdata()  # Output: grey 1700 wooden

#2)
class Bike:
    def __init__(self, color=None, model=1999, company_name="Royal Enfield", price=150000):
        if color is None:
            color = ["Black", "Blue", "Red", "Brown"]
        self.color = color
        self.model = model
        self.company_name = company_name
        self.price = price
    def setdata(self, color, model, company_name, price):
        self.color = color
        self.model = model
        self.company_name = company_name
        self.price = price
    def showdata(self, choice):
        self.choice = choice
        if self.choice in self.color:
            print("Yes, this color is available for this model")
        else:
            print("No, this color is not available for this model")
        print(self.color, self.model, self.company_name, self.price, self.choice)


bike1 = Bike()
bike2 = Bike()
bike3 = Bike()
bike1.setdata(["Black", "Blue"], 2005, "Bajaj", 100000)
bike3.setdata(["Blue-Black"], 2011, "Hero Honda", 80000)
choice = input("Enter color of bike:")

bike1.showdata(choice)  # Output depends on the user's input
bike2.showdata(choice)  # Output depends on the user's input
bike3.showdata(choice)  # Output depends on the user's input

Enter color of bike: Red
No, this color is not available for this model
['Black', 'Blue'] 2005 Bajaj 100000 Red
Yes, this color is available for this model
['Black', 'Blue', 'Red', 'Brown'] 1999 Royal Enfield 150000 Red
No, this color is not available for this model
['Blue-Black'] 2011 Hero Honda 80000 Red

#__init__ : method in Python is a special method used to initialize newly created objects. It's called a constructor in object-oriented programming. 

#Example:
class Chair:
    def __init__(self, color="grey", price=1700, type="wooden"):
        self.color = color
        self.price = price
        self.type = type
    def setdata(self, color, price, type):
        self.color = color
        self.price = price
        self.type = type
    def showdata(self):
        print(self.color, self.price, self.type)


chair1 = Chair()
chair2 = Chair()
chair3 = Chair()
chair1.setdata("Red", 1200, "Plastic")
chair2.setdata("Blue", 1000, "Aluminium")
chair1.showdata()  # Output: Red 1200 Plastic
chair2.showdata()  # Output: Blue 1000 Aluminium
chair3.showdata()  # Output: grey 1700 wooden

#__new__: method in Python is a special method used for creating a new instance of a class. It is called before __init__ and is responsible for returning a new instance of the class.
#Example:
class Chair:
    def __new__(cls, *args, **kwargs):
        print(f"Creating a new Chair instance: {cls}")
        instance = super(Chair, cls).__new__(cls)
        return instance
    def __init__(self, color="grey", price=1700, type="wooden"):
        self.color = color
        self.price = price
        self.type = type
    def setdata(self, color, price, type):
        self.color = color
        self.price = price
        self.type = type
    def showdata(self):
        print(self.color, self.price, self.type)
# Create instances of Chair
chair1 = Chair()
chair2 = Chair()
chair3 = Chair()

# Set data for chairs
chair1.setdata("Red", 1200, "Plastic")
chair2.setdata("Blue", 1000, "Aluminium")

# Show data for chairs
chair1.showdata()  # Output: Red 1200 Plastic
chair2.showdata()  # Output: Blue 1000 Aluminium
chair3.showdata()  # Output: grey 1700 wooden

#__str__: method in Python is a special method that defines the string representation of an object. It is called by the built-in str() function and by the print() function to provide a human-readable representation of an object
class Chair:
    def __init__(self, color="grey", price=1700, type="wooden"):
        self.color = color
        self.price = price
        self.type = type
    def setdata(self, color, price, type):
        self.color = color
        self.price = price
        self.type = type
    def __str__(self):
        return f"Chair(color={self.color}, price={self.price}, type={self.type})"
    def showdata(self):
        print(self)
# Create instances of Chair
chair1 = Chair()
chair2 = Chair()
chair3 = Chair()

# Set data for chairs
chair1.setdata("Red", 1200, "Plastic")
chair2.setdata("Blue", 1000, "Aluminium")

# Show data for chairs
chair1.showdata()  # Output: Chair(color=Red, price=1200, type=Plastic)
chair2.showdata()  # Output: Chair(color=Blue, price=1000, type=Aluminium)
chair3.showdata()  # Output: Chair(color=grey, price=1700, type=wooden)

#Data encapsulation :is an important concept in object-oriented programming (OOP) that involves restricting direct access to some of an object's components, which means internal object details are hidden from the outside world.
#Example:
class Person:
    def __init__(self, name, age, email):
        self.__name = name
        self.__age = age
        self.__email = email
    # Getter methods
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_email(self):
        return self.__email
    # Setter methods
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        if age > 0:  # Basic validation for age
            self.__age = age
        else:
            print("Please enter a valid age.")
    def set_email(self, email):
        self.__email = email
    # String representation method
    def __str__(self):
        return f"Person(name={self.__name}, age={self.__age}, email={self.__email})"


# Create a Person instance
person1 = Person("John Doe", 30, "john.doe@example.com")

# Accessing data using getter methods
print("Initial data:")
print("Name:", person1.get_name())
print("Age:", person1.get_age())
print("Email:", person1.get_email())

# Modifying data using setter methods
person1.set_name("Jane Doe")
person1.set_age(25)
person1.set_email("jane.doe@example.com")

# Accessing modified data using getter methods
print("\nModified data:")
print("Name:", person1.get_name())
print("Age:", person1.get_age())
print("Email:", person1.get_email())

# Printing the string representation of the person
print("\nString representation of the person:")
print(person1)

#output:

Initial data:
Name: John Doe
Age: 30
Email: john.doe@example.com

Modified data:
Name: Jane Doe
Age: 25
Email: jane.doe@example.com

String representation of the person:
Person(name=Jane Doe, age=25, email=jane.doe@example.com)

#Data Hiding :is a technique used to prevent direct access to an object's internal data from outside the class


class MyClass:
    def __init__(self):
        # The __hidden_var is a private instance variable (hidden from outside the class)
        self.__hidden_var = 0  # Hidden variable, initialized with 0
    def get_hidden_var(self):
        # This method is a getter to retrieve the value of the __hidden_var
        return self.__hidden_var  # Returns the value of the hidden variable
    def set_hidden_var(self, value):
        # This method is a setter to update the value of the __hidden_var
        self.__hidden_var = value  # Updates the hidden variable with the provided value

# Creating an instance of the MyClass
obj = MyClass()

# Calling the set_hidden_var method to update the hidden variable
obj.set_hidden_var(10)  # Sets the hidden variable to 10

# Calling the get_hidden_var method to retrieve the value of the hidden variable
print(obj.get_hidden_var())  # Output: 10

# Data Abstraction: Abstraction is the principle of exposing only the essential features of an object to the outside world while hiding the unnecessary implementation details.


class Employee:
    def __init__(self, name, age, salary):
        # Public attributes
        self.name = name
        self.age = age
        # Private attribute
        self.__salary = salary
    def get_salary(self):
        # Method to retrieve the salary
        return self.__salary
    def set_salary(self, new_salary):
        # Method to update the salary
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary")

# Create an instance of the Employee class
employee = Employee("John", 30, 5000)

# Retrieve the salary using the get_salary method
print(employee.get_salary())  # Output: 5000

# Update the salary using the set_salary method
employee.set_salary(6000)

# Retrieve the updated salary
print(employee.get_salary())  # Output: 6000

#output:

5000
6000


