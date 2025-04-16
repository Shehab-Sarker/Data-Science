# List
#  A list in Python is a mutable, ordered collection that can store multiple data types, including
#  numbers, strings, and even other lists. Lists are defined using square brackets [].
 # Empty List
empty_list = []
# List with integers
numbers = [1, 2, 3, 4, 5]
# List with mixed data types
mixed = [10, "Python", 3.14, True]
# List containing another list (Nested List)
nested = [[1, 2], [3, 4], [5, 6]]
# List with duplicate values
duplicates = [1, 2, 2, 3, 4, 4, 5]

mylist=["a",'b',"c","d"]
print(mylist[0]) #output: "a"
print(mylist[-1]) #output: "d" this is last element

print(mylist[1:3])
print(mylist[::-1]) #reversed list
print(mylist[::1])

num1=[1,2,3]
num2=num1
num2.append(4)
print(num1)
