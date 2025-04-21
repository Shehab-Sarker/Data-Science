# Touple
#  1. A tuple is a collection of ordered, immutable (unchangeable), and heterogeneous
#  (different data types) elements.
#  2. Tuples are faster than lists because they are immutable.
#  3. Tuples are defined using parentheses ().
# Tuples in Python are immutable, which means you can't change, add, or remove items once the tuple is created. Because of this,
#  tuple methods are very limited compared to lists.
# Tuples are compared element by element, from left to right.
#empty tuple
empuy_tuple=()
print(empuy_tuple)
# Tuple with elements
numbers = (1, 2, 3, 4)
print(numbers)
# Tuple with different data types
mixed_tuple = (1, "hello", 3.14, True)
print(mixed_tuple)
# count() – Count occurrences of a value
numbers = (1,2,3,2,2,4)
print(numbers.count(2))
fruits = ("apple", "banana", "cherry", "banana")
print(fruits.index("banana")) 
print()

#Tuple Concatenation
tuple1 = (1,2,3)
tuple2 = (4,5,6)
result =tuple1+tuple2
print(result)
print()

# If we ever need to modify a tuple, you have to convert it to a list first:
t = (1,2,3)
temp =list(t)
temp.append(4)
print(tuple(temp))
print()

# Tuple Unpacking (Very useful and common!)
t = (10,20,30)
a,b,c=t
print(a)
print(b)
print(c)
print()

# If you want to unpack a part of a tuple and collect the rest
t = (1,2,3,4,5)
a,*b,c=t
print(a)
print(b)
print(c)


print()

# Tuples are compared element by element, from left to right.
t1 = (1, 2, 3)
t2 = (1, 2, 4)
print(t1 == t2) 
print(t1 < t2)
print()

#Class Assignment :02
#  Objective: Use tuple unpacking and comparison to manage and compare student data. Problem: You are given a list of students
#  where each student is represented as a tuple:


# Write a program that:
# 1. Unpacks and prints each student's name and CGPA.
# 2. Finds the student with the highest CGPA using tuple comparison.
# 3. Sorts the list based on CGPA in descending order.

students=[
    ("alice",3.75),
    ("bob",3.60),
    ("charlie",3.90),
    
]


# 1. Unpacks and prints each student's name and CGPA.
for name, cgpa in students:
    print(f"Name: {name}, CGPA: {cgpa}")
    
# 2. Finds the student with the highest CGPA using tuple comparison.
Top_student =max(students, key=lambda x:x[1])
print(f"\nTop student: {Top_student[0]} with CGPA {Top_student[1]}")

# 3. Sorts the list based on CGPA in descending order.
sorted_students =sorted(students, key=lambda x:x[1],reverse=True)
print(sorted_students)
