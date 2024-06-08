#class inheritance: Inheritance provides code reusability to the program because we can use an existing class to create a new class instead of creating it from scratch.

#Syntax:

class ParentClass:
    #parent class methods and attributes
    def prent_nethod(self):
        print("This parent method")

class ChildClass(ParentClass):
    #child class attributes and methods and parent class attributes and functions
    def child_method(self):
        print("This is child method")

#Types of in-heritance:
#Single_inheritance= when one class is parent and other one is derived.
class Person:
    def Person_info(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def show_Person_info(self):
        print(self.name,self.age,self.gender,end='')
class Employe(Person):
    def Employe_info(self,name,age,gender,e_id,salery):
        self.Person_info(name,age,gender)
        self.e_id = e_id
        self.salery = salery
    def show_Employe_info(self):
        self.show_Person_info()
        print(self.e_id,self.salery)
e1 = Employe()
e1.Employe_info("Tarun",18,"Male",123,200000)
e1.show_Employe_info()

#Multilevel_inheritance: when one is grand-parent,one is parent and other one child.
class Student:
    def Student_info(self,S_name,roll_no):
        self.S_name = S_name
        self.roll_no = roll_no
    def show_Student_info(self):
        print(self.S_name,self.roll_no,end='')
class Teacher(Student):
    def Teacher_info(self,S_name,roll_no,T_name,T_id):
        self.Student_info(S_name,roll_no)
        self.T_name = T_name
        self.T_id = T_id
    def show_Teacher_info(self):
        self.show_Student_info()
        print(self.T_name,self.T_id,end='')
class Course(Teacher):
    def Course_info(self,S_name,roll_no,T_name,T_id,Class,C_name):
        self.Teacher_info(S_name,roll_no,T_name,T_id)
        self.Class = Class
        self.C_name = C_name
    def show_Course_info(self):
        self.show_Teacher_info()
        print(self.Class,self.C_name)
c1 = Course()
c1.Course_info("Tarun",29,"Rahul",123,12,"Maths")
c1.show_Course_info()

#Multiple:two parent one child
class Student:
    def Student_info(self,S_name,roll_no):
        self.S_name = S_name
        self.roll_no = roll_no
    def show_Student_info(self):
        print(self.S_name,self.roll_no,end='')
class Teacher:
    def Teacher_info(self,T_name,T_id):
        self.T_name = T_name
        self.T_id = T_id
    def show_Teacher_info(self):
        print(self.T_name,self.T_id,end='')
class Course(Student,Teacher):
    def Course_info(self,S_name,roll_no,T_name,T_id,Class,C_name):
        self.Student_info(S_name,roll_no)
        self.Teacher_info(T_name,T_id)
        self.Class = Class
        self.C_name = C_name
    def show_Course_info(self):
        self.show_Student_info()
        self.show_Teacher_info()
        print(self.Class,self.C_name)
c1 = Course()
c1.Course_info("Tarun",29,"Rahul",123,12,"Maths")
c1.show_Course_info()

#Super():
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def show(self):
        print(self.name,self.age,self.gender,end='')
class Employe(Person):
    def __init__(self,name,age,gender,e_id,salery):
        super().__init__(name,age,gender)
        self.e_id = e_id
        self.salery = salery
    def show(self):
        super().show()
        print(self.e_id,self.salery)
e1 = Employe("Tarun",18,"Male",123,200000)
e1.show()
#multi-valued
class Student:
    def _init__(self,S_name,roll_no):
        self.S_name = S_name
        self.roll_no = roll_no
    def show(self):
        print(self.S_name,self.roll_no)
class Teacher(Student):
    def __init__(self,S_name,roll_no,T_name,T_id):
        super()._init__(S_name,roll_no)
        self.T_name = T_name
        self.T_id = T_id
    def show(self):
        super().show()
        print(self.T_name,self.T_id)
class Course(Teacher):
    def __init__(self,S_name,roll_no,T_name,T_id,C_name,C_id):
        super().__init__(S_name,roll_no,T_name,T_id)
        self.C_name = C_name
        self.C_id = C_id
    def show(self):
        super().show()
        print(self.C_name,self.C_id)
C1 = Course("Tarun",29,"Rahul",123,"Python",132)
C1.show()
    
#EXCEPTION HANDLING: In Python, an exception is an error that disrupts the normal flow of a program's execution. Error in Python can be of two types i.e. Syntax errors and Exceptions. Errors are problems in a program due to which the program will stop the execution. On the other hand, exceptions are raised when some internal events occur which change the normal flow of the program.

#Common Built-in Exceptions:
#i)Syntax Error : A SyntaxError is raised when Python encounters code that violates the language's syntax rules. This can happen due to mistakes such as incorrect indentation, invalid syntax, or missing colons or parentheses.
#For example:

try:
    # Code that causes a SyntaxError
    if x == 5:
        print("x is equal to 5")
        # Missing colon after the if statement
except SyntaxError:
    print("SyntaxError occurred")
     
#ii)IndentationError : An IndentationError occurs when there is an incorrect indentation in the code. Python uses indentation to define code blocks, so proper indentation is crucial.

#For example:

try:
    # Code with incorrect indentation
    def my_function():
        print("Inside function")
         print("This line is incorrectly indented")  # Extra space
except IndentationError:
    print("IndentationError occurred")
     
#iii) NameError : A NameError is raised when Python encounters an undefined or unassigned variable or function name.

#For example:

try:
    # Code that references an undefined name
    print(x)  # x is not defined
except NameError:
    print("NameError occurred")
     
#iv)TypeError : A TypeError is raised when an operation or function is applied to an object of an inappropriate type.

#For example:

try:
    # Code that performs an operation on incompatible types
    x = "hello"
    y = 5
    print(x + y)  # Cannot concatenate a string and an integer
except TypeError:
    print("TypeError occurred")
     
#v)ValueError : A ValueError is raised when a function receives an argument of the correct type but an inappropriate value.

try:
    # Code that passes an invalid value to a function
    int("hello")  # The string "hello" cannot be converted to an integer
except ValueError:
    print("ValueError occurred")
     
#vi)ZeroDivisionError : A ZeroDivisionError is raised when an attempt is made to divide a number by zero.

#For example:

try:
    # Code that attempts to divide by zero
    x = 10
    y = 0
    result = x / y  # Division by zero is not allowed
except ZeroDivisionError:
    print("ZeroDivisionError occurred")
     
#vii) Custom Exceptions (Brief Introduction) : In addition to the built-in exceptions, Python allows you to define your own custom exceptions by creating new exception classes. Custom exceptions can be useful when you need to handle specific error conditions in your code that are not covered by the built-in exceptions.

#Syntax:

"""
class CustomExceptionName(Exception):
    '''Docstring describing the exception'''
    pass

try:
    # Code that raises the custom exception
except CustomExceptionName:
    # Handle the custom exception
"""
     

#Example:

class InvalidAgeError(Exception):
    """Raised when the input age is invalid"""
    pass

def validate_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    elif age > 120:
        raise InvalidAgeError("Age cannot be greater than 120")
    else:
        print("Valid age")

try:
    validate_age(-5)
except InvalidAgeError:
    print("Invalid age provided")

#Questions:

#try and except:

L = [12,13,14,15,16]
try:
    for i in range(0,len(P)):
        if(L[i] == i ):
            pass
except IndexError:
    print("Please check the length of the List  ")
except NameError:
    print("Please check the name of the List")
else:
    print("All Code is OK")
finally:
    print("Finish")

#custom except :
a = int(input("Enter value of a:"));
b = int(input("Enter value of b:"));
if(a == b):
    raise Exception("number must not be same")

username = str(input("Enter username:"))
Password = str(input("Enter password:"))
if(Password in username):
    raise Exception ("Password must not cantain username")

