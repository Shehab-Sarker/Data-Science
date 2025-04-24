# Create a class Person with attributes name and age. Create an object and display its details.
# Input: Person("Alice", 25)
# Output: Name: Alice, Age: 25


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
p1=Person("Alice",25)
print(f"Name: {p1.name} ,Age: {p1.age}")