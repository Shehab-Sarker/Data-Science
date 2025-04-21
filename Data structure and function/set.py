# Set
#  A set is an unordered collection of unique elements.
#  1. Sets are mutable (can be modified), but they do not allow duplicate values.
#  2. Sets are defined using curly braces {} or the set() constructor.

#basic Set
fruits={"apple","banana","cherry"}
print(fruits)

# Set with Duplicates (Duplicates will be removed)
fruits = {"apple", "banana", "cherry", "apple", "banana"}
print(fruits)  
print()

#Creating a Set from a list
numbers = set([1,2,3,4,5])
print(numbers)
print(list(numbers))
print()

#add() -Add an element
fruits={"apple","banana"}
fruits.add("cherry")
print(fruits)
print()

#clear() -remove all elements
fruits = {"apple","banana","cherry"}
fruits.clear()
print()

#Copy -copy a set
fruits={"apple","banana","cherry"}
fruits_copy=fruits.copy()
print(fruits_copy)
print()

# discard() – Remove an element (if exists)
fruits.discard("apple")
print(fruits)
print()

 # remove() – Remove an element (raises error if element doesn't exist)
 
fruits={"apple","banana","cherry"}
fruits.remove("cherry")
print(fruits)
# fruits.remove("orange")
print(fruits)
print()

# union() – Combine two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Set1|set2:",set1|set2)
union_set = set1.union(set2)
print("union_set:",union_set)
print()

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("set1 & set2 :",set1 &set2)
intersection_set = set1.intersection(set2)
print("Inheritance set:",intersection_set) 
print()

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Set1 -set2:",set1-set2)
difference_set = set1.difference(set2)
print("difference_set:",difference_set)
print("Symmetric_Difference_set:",set1.symmetric_difference(set2))
print("set1^set2:",set1^set2)
print()

#issubset -Check if the set is a subset of another
set1 = {1,2}
set2 = {1,2,3,4}
print(set1.issubset(set2))
print(set1.issuperset(set2))
print()

set1 = {1,2,3,4}
set2 = {1,2}
print(set1.issubset(set2))
print(set1.issuperset(set2))




