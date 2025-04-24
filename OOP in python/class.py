# OOP
# OOP is a way of writing code by grouping data and functions into reusable structures called
# classes. It mimics real-world objects.
# OOP Core Concepts:
# 1. Class – A blueprint for creating objects.
# 2. Object – A real instance based on the class.
# 3. Method – Function inside a class.
# 4. Constructor – A special method used to initialize objects.
# 5. Inheritance – One class can inherit features from another.

#Object

class Student:
    pass

s1=Student()
print(type(s1))
print(type(3))
print()
print(dir())
print(__name__)
print()

def greet():
    """This function says hello."""
    print("Hello!")
    
print(greet.__doc__)
print()
print(dir("Hello"))  

