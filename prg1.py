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
# print("Outside function, local y:", y)
