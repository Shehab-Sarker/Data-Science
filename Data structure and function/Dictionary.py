#  Dictionary
#  A dictionary in Python is an unordered collection of key-value pairs.
#  1. Each key is unique and is associated with a value.
#  2. Dictionaries are defined using curly braces {} with the key-value pairs separated by
#  a colon :.
#  3. Mutable – You can change, add, or remove items.
#  4. Keys are Unique – No two keys can be the same.

# Basic Dictionary
student = {
    "name": "John",
    "age": 20,
    "course": "Computer Science"
}
print(student)  
print(student["name"])
print(student["age"])
print(student["course"])
print()

# Dictionary with Different Data Types
person = {
    "name": "Alice",
    "age": 25,
    "is_student": True,
    "marks": [80, 90, 85]
}
print(person) 
print(person["marks"]) 
print(person["is_student"]) 
print()

# items() – Get all key-value pairs
student={"name":"john","age":20}
print(student.items())
print(student.keys())
print(student.values())
print()

# get() – Access values safely
# Returns value for key, or default if not found
student = {"name": "John", "age": 20, "course": "Python"}
print(student.get("course"))  # Output: Python
print(student.get("address", "Not Available"))  # Output: Not Available
print()

#Add/Update Elements
person ={
    "name":"Alice",
    "age":"25"
}
print(person)
person.update({"city":"Dhaka"})
print(person)
new_info={
    "course": "python",
    "age1": 21,
    "Dept": "CSE"
}
student.update(new_info)
print(student)
print()

#If key exists: returns its value.
#If not: adds key with the given default value and returns it

student.setdefault("grade","A")
print(student) 
student.setdefault('name', 'New Name')
print()

#Removing elements
#clear() - Remove all items
# student.clear()
student.pop("grade")
print(student)
print()

#popitem() – Remove an arbitrary item
# Removes and returns the last inserted key-value pair 
remove_item=student.popitem()
print(remove_item)
print(student)
print()

# Suppose you're designing a system where every user must have some default field
# but they haven't filled in anything yet. 
# You can create a base template like this:
# Define the required profile fields

fields=['name','email','phone','address']

# Set a default placeholder for all fields
user_profile=dict.fromkeys(fields,"Not provided")
print(user_profile) 

user_profile=dict.fromkeys(fields,)
print(user_profile) 
print()

#Nested Dictionaries
students={
    "john":{"age":20,"Dept":"CSE"},
    "Alice":{"age":23,"Dept":"EEE"}
}

print(students["john"])
print(students["Alice"])