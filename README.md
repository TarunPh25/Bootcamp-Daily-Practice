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



