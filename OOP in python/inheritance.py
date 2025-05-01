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
    def sklills(self):
        print("Mother : Painting, Gardening")
        
class child(Father,Mother):
    pass

c1=child()
c1.skills()
print()


# . Child class inherits from both Father and Mother.
#  2. But since both have a method called skills(), Python uses the one from the first parent
#  listed (Father) — this is due to the MRO (Method Resolution Order).
