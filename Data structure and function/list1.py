# Data Structure
#  Data structures are ways to organize and store data in a computer so that we can use it
#  efficiently.
#  Common data structures in Python:
#  1. List – an ordered collection (like a shopping list)
#  2. Dictionary – a collection of key-value pairs (like a contact list)
#  3. Set – an unordered collection of unique items
#  4. Tuple – an ordered, unchangeable collection

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
my_list = ["a", "b", "c", "d"] # List
print(my_list[0])  # Output: 'a'
print(my_list[-1]) # Output: 'd' (Last element
print()

#Adding Elements
#numbers=[1,2,3]
numbers.append(4)
numbers.append([7,8])
print(numbers)
print()

#extend() -Merge two lists
list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1)
print()

list3=[1,2,3]
list4=[4,5,6]
a=list3.extend(list4)
print(a)

#insert() - insert at a specific index
fruits = ["apple","banana"]
fruits.insert(1,"Orange")
print(fruits)
print()

#Remove() - remove first occurance of the item
numbers = [1,2,3,3,5,3]
numbers.remove(3)
print(numbers)
print()

# pop() – Remove and returns item at index i (or last item if index not provided)
numbers=[1,2,3,4,5]
remove_item=numbers.pop()
# remove_item=numbers.pop(2)
print(remove_item)
print(numbers)
print()

# clear() – Remove all elements
numbers = [1, 2, 3]
numbers.clear()
print(numbers)  # Output: []
print()

#Searching and Counting
#index()- Find the Position of an item
fruits=["apple","banana","cherry"]
print(fruits.index("banana"))
print()

#count() - Count occurrences
numbers = [1,2,2,3,2,2,2,2,4]
print(numbers.count(2)) 
print()

#Reordering
#sort() - Sort a list
numbers = [3,1,4,2]
print(numbers)
print(numbers)
print()

#reverse - Reverse the list
numbers=[3,1,4,2]
numbers.sort(reverse=True)
num=[3,1,9,3]
num.reverse()
print(numbers)
print(num)

#Copy()-Copy a list
num1=[1,4,2]
new_lsit=num1.copy()
print(new_lsit)