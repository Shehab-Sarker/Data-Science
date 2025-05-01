# Inheritance and Advanced OOP Features
# Create a base class Animal and a derived class Dog that inherits from Animal.
# Output: 
# Animals make different sounds. # From Animal class
# Dog barks! # From Dog Class

class Animal:
    def sound(self):
        print("Animals make different sounds.")
class dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks!")
        
d=dog()
d.sound()