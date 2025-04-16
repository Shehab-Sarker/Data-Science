# 0.0.6 Dictionary
#  A dictionary in Python is an unordered collection of key-value pairs.
#  Each key is unique and is associated with a value.
#  Dictionaries are defined using curly braces {} with the key-value pairs separated by a colon :.
#  Mutable– You can change, add, or remove items.
#  Keys are Unique– No two keys can be the same.

#basic dictionary
student = {
    "name":"John",
    "age" :20,
    "course":"computer Science"
}
print(student)

#Dictionary with different data types
person ={
    "name":"alice",
    "age": 25,
    "is_student":True,
    "marks":[80,90,85]
}
print()
print(person)
print()

# Nested Dictionaries
students = {
"John": {"age": 20, "course": "Python"},
"Alice": {"age": 22, "course": "Java"}
}
print(students)
print(students["John"]) 
