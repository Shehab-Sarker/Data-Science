# Touple
#  A tuple is a collection of ordered, immutable (unchangeable), and heterogeneous (different data
#  types) elements.
#  Tuples are faster than lists because they are immutable.
#  Tuples are defined using parentheses ().
# Empty tuple
empty_tuple = ()
# Tuple with elements
numbers = (1, 2, 3, 4)
# Tuple with different data types
mixed_tuple = (1, "hello", 3.14, True)
# Tuple with one element (comma is required!)
single_element_tuple = (5,)
# Tuple Slicing
numbers = (0, 1, 2, 3, 4, 5)
print(numbers[1:4]) # Output: (1, 2, 3)
print()

#Tuple Concatenation
tuple1 = (1,2,3)
tuple2 = (4,5,6)
result =tuple1+tuple2
print(result) # Output: (1, 2, 3, 4, 5, 6)
print()

#Tuple Unpacking
person=("john",25,"Engineer")
print(person)
name,age,job=person
print(name)
print(age)
print(job)


# Use a Tuple (tuple) When: 1. Immutability is needed (data should not change). 2. Performance
#  is important (tuples are faster than lists). 3. Memory optimization is required (tuples use less
#  memory). 4. Tuples represent fixed structures like coordinates, database records, or settings. 5.
#  Tuples can be used as dictionary keys, unlike lists.