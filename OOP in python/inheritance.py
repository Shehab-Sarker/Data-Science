# Why is OOP Important?
#  1. OOP groups data and functions together inside classes.
#  2. Code is cleaner and easier to understand.
#  3. Once you build a class, you don't need to rewrite it.
#  4. New classes can inherit from old ones and add new features.
#  5. Increases security and prevents accidental changes.
#  6. Code feels more natural and logical.
#  OOP makes your code organized, reusable, safe, and close to real life.

#self
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def greet(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old.")
        
        
s1=Student("Alice",22)
s2=Student("Bob",18)

s1.greet()
s2.greet()
print()

# These are the instance variables — they belong to the object being created.
#  1. self.name stores the name inside the object
#  2. self.age stores the age inside the object
#  # Python does not require the first parameter of a method to be called self. It's j
#  # self is the standard naming convention in Python.

class Car:
    def __init__(this,brand):
        this.brand=brand
        
    def show_brand(this):
        print(f"Brand is {this.brand}")
        
c=Car("Toyota")
c.show_brand()
print()

# 1. Single Inheritance 
# One child class inherits from one parent class.

class Animal:
    def sound(self):
        print("Animal makes a different sound")
        
        
class Dog(Animal):
    def bark(self):
        print("Dogs barks.")
        
d=Dog()
d.sound()
d.bark()
print()

#  2. Hierarchical Inheritance
#  One parent class, multiple child classes.

class Cat(Animal):
    def meow(self):
        print("Cat meows.")
        
c=Cat()
c.sound()
c.meow()
print()

# 3. Multilevel Inheritance
#  A child inherits from a parent, and another child inherits from that child.

class Puppy(Dog):
    def weep(self):
        print("Puppy weeps.")
        
p=Puppy()
p.sound()
p.bark()
p.weep()
print()


# 4. Multiple Inheritance
#  Multiple Inheritance means a class can inherit from more than one parent class.
#  class ChildClass(Parent1, Parent2): # class body

class Father:
    def skills(self):
        print("Father : Cooking, Driving")
        
        
class Mother:
    def skills(self):
        print("Mother : Painting, Gardening")
        
class child(Father,Mother):
    pass

c1=child()
c1.skills()
print()


# . Child class inherits from both Father and Mother.
#  2. But since both have a method called skills(), Python uses the one from the first parent
#  listed (Father) — this is due to the MRO (Method Resolution Order).
#diffent method uses parent classes

class Engine:
    def start(self):
        print("Engine Started.")
        
class Bettery:
    def charge(self):
        print("Bettery Charging.")
        
class Electric_car(Engine,Bettery):
    pass

Ec=Electric_car()
Ec.start()
Ec.charge()
print()

#same method uses from different parent class for showing all output print

class Father1:
    def skills1(self):
        print("Father : Programming")
        
class Mother1:
    def skills1(self):
        print("Mother : painting")
        
class Child1(Father1,Mother1):
    def skills1(self):
        Father1.skills1(self)
        Mother1.skills1(self)
        print("Child : Playing")
        
c1=Child1()
c1.skills1()
print()


#  Methods without self
# If you're accessing or modifying object-specific data (attributes), then self is 
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):  # needs self!
        print("Hello.")
 # Python automatically passes the object as the first argument, so if there's no self
 
class WrongExample:
    @staticmethod
    def say_hello():
        print("Hello.")
        
obj=WrongExample()
obj.say_hello()
# TypeError: say_hello() takes 0 positional arguments but 1 was given  
# Without Self
print()

# Typically used when the method works with or modifies the object’s attributes.
#  Static Method → No self required

class Mathtools:
    @staticmethod
    def add(a,b):
        return a+b
    
sum_=Mathtools()
print(f"Sum : {sum_.add(2,3)}")
print()
# Use @staticmethod when:
#  1. You don’t need self or cls
#  2. You just want to group utility functions inside a class


 # Class Method → Uses cls instead of self
#  Use @classmethod when:
#  1. You want to work with class variables
#  2. You don’t need access to individual object (self)

class Myclass:
    count=6
    @classmethod
    def show_count(cls):
        print(f"Count is : {cls.count}")
        
my=Myclass()
my.show_count()
# my.show_count(8)
# TypeError: Myclass.show_count() takes 1 positional argument but 2 were given
print()

#  Decorator
#  They are used to wrap or decorate a function with additional functionality. For example, a
#  decorator could add logging, timing, or access control to a function.

# A simple decorator that prints a message before a function is called
def my_decorator(func):
    def wrapper():
        print("Before function Execution.")
        func()
        print("After function Execution.")
        
    return wrapper

@my_decorator   # Applying the decorator to the function
def greet():
    print("Hello!")
    
greet()
print()


#  Built-in Decorators in Python
#  Python has several built-in decorators that serve common purposes, like:
#  1. @staticmethod: Used for defining static methods (doesn't access self or cls).
#  2. @classmethod: Used for defining class methods (accesses the class with cls).
#  3. @property: Used to make a method behave like an attribute (no need to call it with (),
#  just use it like a normal attribute).

# @property
#  you can access it like an attribute instead of calling it like a method. It allows you to define behavior for getting (and optionally setting) a value, without having to explicitly use method calls

class Circle:
    def __init__(self,radius):
        self._radius=radius #Private attribute
        
    @property
    def radius(self): #Getter method
        return self._radius
    
    @property
    def area(self): #Another Property method
        return 3.14159*(self._radius**2)
    
    @radius.setter
    def radius(self,value):
        if value<0:
            raise ValueError("Radius cannot be negetive.")
        self._radius=value
        
cle=Circle(5)
print(f"Radius : {cle.radius}")
print(f"Area : {cle.area}") 
cle.radius=10    
print(f"Update Radius : {cle.radius}")
print(f"Update Area : {cle.area}")  
print()

#Method Overloading
class Mathh:
    def multiply(self,*args):
        result=1
        if not args:
            return 0
        for num in args:
            result*=num
        return result
    
mt=Mathh()
print(mt.multiply(3))
print(mt.multiply(2,3))
print(mt.multiply(2,3,4))
print(mt.multiply())
print()

class Greeter:
    def greett(self,name=None):
        self.name=name
        if name:
            print(f"Hello {self.name}!")
        else:
            print("Hello, there!")
            
g = Greeter()
g.greett("Shehab")
g.greett()
