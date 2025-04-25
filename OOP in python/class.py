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
print()

print(help(list.append))
print()

#Methods
#Methods define behaviors/actions the object can perform. Always use self as the first parameter.

#Methods (Functions inside class)
class Myclass:
    def __init__(self):
        self.name="Shehab"
        
    def greet(self):
        return "Hello"
    
print(dir(Myclass))
print()

#introducing Methods
class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
        
    def start_engine(self):
        print(f"{self.brand} engine started!")
        
my_car = Car("Supra","black")
my_car.start_engine() 
print()

#Default Constructor(No Parameters)
class Bike:
    def __init__(self):
        self.brand="Gixzar"
        self.color="black"
        
    def show_info(self):
        print(f"{self.brand} is my favourite bike and this color should {self.color}")
        
my_bike=Bike()
my_bike.show_info()
print()


#Parametrized Constructor
class Laptop:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        
    def show_spection(self):
        print(f"Brand: {self.brand} and price : {self.price}")
        
my_laptop=Laptop("Apple Macbook","1 Lakh")
my_laptop.show_spection()
print()

#Inheritance
class Animal:
    def __init__(self):
        print("Animal is created")
        
    def sound(self):
        print("Animal make a sound")
        
    def move(self):
        print("Animal were move")
        
#Child Class just inherits evrything from Animal

class Dog(Animal):
    pass

#Create a object of dog
d=Dog()
d.sound()
d.move()
print()

#Intro to Inheritance
#Base Class

class Animal1:
    def __init__(self,name):
        self.name=name
        
    def speak(self):
        print(f"{self.name} makes a sound")
        
#Derived Class
class Dog1(Animal1):
    def speak(self):
        print(f"{self.name} barks")
        
dog1=Dog1("Buddy")
dog1.speak()

# Dog inherits from Animal.
# It overrides the speak method.
# Promotes code reuse and extension.
print()

# Variables assigned using self.variable = value inside the parent class constructor (init) are not automatically inherited — but they are available if the constructor is called using super()

class A:
    def __init__(self):
        self.name="Shehab"
        
class B(A):
    def __init__(self):
        super().__init__() 
        
b=B()
print(b.name)  # ✅name is accessible after calling super().__init__()
print()

#super() let us call the parent class constructor or method. 
class Person:
    def __init__(self,name):
        self.name=name
        
    def show(self):
        print(f"Name: {self.name}")
        
class Employee(Person):
    def __init__(self, name,salary):
        super().__init__(name) #call base constructor
        self.salary=salary
        
    def show(self):
        super().show()
        print(self.name)
        print(f"Salary: {self.salary}")
        
e1=Employee("Shehab","200000")
e1.show()
print()

class Employee1:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def details(self):
        print(f"Name: {self.name} id : {self.id}")
        
class Manager(Employee1):
    def __init__(self, name, id,department):
        super().__init__(name, id)
        self.department=department
        
    def details(self):
        super().details()
        print(f"Department: {self.department}")
        
m1=Manager("Shehab","2103046","Computer Science")
m1.details()
        
         
        
        
    


        