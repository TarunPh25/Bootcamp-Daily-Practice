# Bootcamp-Daily-Practice
This is my first Day for python practice(06/06/2024):
<br>
Starting with python Basics
# Python Basic and functions :
#starting with input and output:
#Take a variable name as input 
name = input("Enter the name:")
#then print the name of input person
print(name)

# Data Types in python
int_num = 11
float_num = 3.14
complex_num = 2 + 3j
string = "Hello, World!"
boolean = True,False
list_example = [1, 2, 3, 4, 5]
tuple_example = (1, 2, 3, 4, 5)
dict_example = {"name": "aman", "age": 30}
set_example = {1, 2, 3, 4, 5}

# Expression and Operators in python:
# Expressions and Operators
a = 10
b = 3

# Arithmetic Operators
print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.3333333333333335
print(a // b) # Floor Division: 3
print(a % b)  # Modulus: 1
print(a ** b) # Exponentiation: 1000

# Comparison Operators
print(a == b) # Equal to: False
print(a != b) # Not equal to: True
print(a > b)  # Greater than: True
print(a < b)  # Less than: False
print(a >= b) # Greater than or equal to: True
print(a <= b) # Less than or equal to: False

# Logical Operators
print(a > 5 and b < 5)  # and: True
print(a > 5 or b < 1)   # or: True
print(not(a > 5 and b < 5)) # not: False

#Type casting:
# Type Casting
int_from_float = int(3.14)
float_from_int = float(10)
string_from_int = str(100)
list_from_string = list("Hello")
tuple_from_list = tuple([1, 2, 3, 4, 5])
set_from_list = set([1, 2, 3, 4, 5])

print(int_from_float)
print(float_from_int)
print(string_from_int)
print(list_from_string)
print(tuple_from_list)
print(set_from_list)

#conditional statements:
#Example: make a program in python for grading students marks.

score = 85

if score >= 90:
    print("You got an A grade.")
elif score >= 80:
    print("You got a B grade.")
elif score >= 70:
    print("You got a C grade.")
elif score >= 40:
    print("You got a D grade.")
else:
    print("You failed the test.")


# Looping Statements
# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
    
#Jumping Statements:
# break statement
for i in range(10):
    if i == 5:
        break
    print(i)

# continue statement
for i in range(10):
    if i == 5:
        continue
    print(i)


# Some special type of functions
# Special Functions
fruits = ["apple", "banana", "cherry"]

# len()
print(len(fruits))  # Output: 3

# id()
print(id(fruits))  # Output: Unique ID of the list object

# type()
print(type(fruits))  # Output: <class 'list'>

# range()
for i in range(5):
    print(i)  # Output: 0 1 2 3 4
    
#Functions in python:
# def: is a keyword that start of a function definiton.
#function: after def keyword function name is required.
#Parantheses: These enclose any parameters(arguments) the function.
#Example:
def greet(name): #Function definition with parameter 'name'
    """This function prints a greeting message."""
    print("Hello", name + "!")

# Function call with argument 'Alice'
greet("Aman")

#Parameters in functions:
#1) Positional Arguments:positional arguments in programming refer to the arguments passed to a function in the order they are defined.
#Example:
def greet(name, greeting):
    print(f"{greeting}, {name}!")

# Calling the function with positional arguments
greet("Alice", "Hello")  # Output: Hello, Alice!

#2) Keyword Arguments: Keyword arguments allow you to pass arguments to a function by specifying the parameter name explicitly.
#Example:
def greet(name, greeting):
    print(f"{greeting}, {name}!")

# Calling the function with keyword arguments
greet(greeting="Hello", name="Alice")  # Output: Hello, Alice!

#3)Default Arguments:Default arguments in a function are parameters that assume a default value if no value is provided when the function is called. 
#Example:

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Calling the function without providing a value for the 'greeting' parameter
greet("Alice")  # Output: Hello, Alice!

# Calling the function and providing a value for the 'greeting' parameter
greet("Bob", "Hi")  # Output: Hi, Bob!

#write a program ion python to find the factorial of a number:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calling the function
result = factorial(5)
print("Factorial of 5 is:", result)  # Output: Factorial of 5 is: 120

#Lambda Function: Lambda functions are anonymous functions in Python, meaning they are functions without a name. 
#Example:
# List of tuples
students = [('Alice', 22), ('Bob', 20), ('Charlie', 21)]

# Sorting the list of tuples based on the second element using a lambda function
sorted_students = sorted(students, key=lambda x: x[1])

print("Sorted students by age:", sorted_students)
# Output: Sorted students by age: [('Bob', 20), ('Charlie', 21), ('Alice', 22)]

#Square of given number by lambda function?
x = lambda n : n*n*n
y= x(12)
print(y)
#add two numbers:
x = lambda  n,m: n+m
y = x(12,8)
print(y)
#len of a string
x = lambda n : len(n)
y = x("Tarun")
print(y)

#given a name we have to print that name according to their length.
x= lambda n: (n+"\n")*len(n) 
y = x("Tarun")
print(y)

x= lambda n: n*len(n)
y = x("Anu\n")
print(y)

#we have given two numbers how to find greater number from them.
x = lambda n,m: n if n>m else m
y = x(12,80)
print(y)


#Some function of Lambda Functions:
#1) map function(): he map() function in Python applies a given function to all the items in an iterable (like a list, tuple, etc.) and returns a map object (an iterator) that yields the results.
#Example of map() function:
# Define a function to square a number
def square(x):
    return x * x

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using map() to apply the square function to each element in the list
squared_numbers = map(square, numbers)

# Converting the map object to a list to see the result
squared_numbers_list = list(squared_numbers)

print("Squared numbers:", squared_numbers_list)
# Output: Squared numbers: [1, 4, 9, 16, 25]

#Filter function: The filter() function in Python is used to filter elements from an iterable (such as a list, tuple, etc.) based on a function that returns either True or False for each element.
#Example:
# Example list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Define a function to filter even numbers
def is_even(n):
    return n % 2 == 0

# Use filter with the named function
even_numbers = list(filter(is_even, numbers))

print(even_numbers)  # Output: [2, 4, 6, 8, 10]

#reduce function: The reduce() function in Python, which is part of the functools module, is used to apply a function of two arguments cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single value.
#Example:
from functools import reduce

# Example list of numbers
numbers = [1, 2, 3, 4, 5]

# Use reduce with a lambda function to multiply the list of numbers
product = reduce(lambda x, y: x * y, numbers)

print(product)  # Output: 120


# local variable and global variable functions:
'''Local Variable: Exists only within the function or block where it is defined.
Global Variable: Exists throughout the entire program, accessible from any function or block'''
#example:
# Global variable
x = 10

def example_function():
    # Local variable
    y = 5
    print("Inside function, local y:", y)
    print("Inside function, global x:", x)

example_function()

print("Outside function, global x:", x)
# The following line would cause an error if uncommented because y is not accessible outside the function
# print("Outside function, local y:", y)

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


